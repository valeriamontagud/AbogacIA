from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from docxtpl import DocxTemplate
from datetime import datetime
import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import RAG modules
from rag.rag_engine import RAGEngine
from rag.document_processor import DocumentProcessor

app = FastAPI(title="AbogacIA API", version="1.0.0")

# Initialize RAG Engine
try:
    rag_engine = RAGEngine(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        pinecone_api_key=os.getenv("PINECONE_API_KEY"),
        index_name=os.getenv("PINECONE_INDEX_NAME", "bufete-legal-rag")
    )
except ValueError as e:
    print(f"Warning: RAG Engine not fully initialized: {e}")
    rag_engine = None


# 🔹 Modelo de datos (lo que recibe la API)
class Caso(BaseModel):
    cliente: str
    fecha_siniestro: str
    importe: float


class RAGIngestRequest(BaseModel):
    """Request model for RAG document ingestion."""
    documents: List[Dict[str, Any]]


class RAGGenerateTemplateRequest(BaseModel):
    """Request model for RAG template generation."""
    template_type: str
    cliente: str
    details: Optional[Dict[str, Any]] = None


class RAGGenerateEmailRequest(BaseModel):
    """Request model for RAG email generation."""
    email_type: str
    recipient: str
    subject: Optional[str] = None
    body_details: Optional[Dict[str, Any]] = None


class RAGRetrieveRequest(BaseModel):
    """Request model for RAG context retrieval."""
    query: str
    top_k: Optional[int] = 5
    doc_type_filter: Optional[str] = None


# 🔹 Endpoint básico
@app.get("/")
def root():
    rag_status = "disponible" if rag_engine else "no inicializado"
    return {
        "status": "API funcionando correctamente",
        "rag_status": rag_status,
        "version": "1.0.0"
    }


# 🔹 Endpoint principal (generador de documento - compatible con versión anterior)
@app.post("/generar")
def generar_escrito(caso: Caso):
    template_path = os.path.join("templates", "aceptacion_pago.docx")
    doc = DocxTemplate(template_path)

    # 🧠 Cálculo de mora
    fecha_siniestro = datetime.strptime(caso.fecha_siniestro, "%Y-%m-%d")
    fecha_siniestro_formateada = fecha_siniestro.strftime("%d/%m/%Y")
    hoy = datetime.today()
    dias = (hoy - fecha_siniestro).days

    hay_mora = dias > 90

    # 📄 Datos para el Word
    context = {
        "cliente": caso.cliente,
        "fecha_siniestro": fecha_siniestro_formateada,
        "importe": caso.importe,
        "fecha_actual": datetime.today().strftime("%d/%m/%Y"),
        "hay_mora": hay_mora
    }

    # 🔄 Rellenar plantilla
    doc.render(context)

    # 💾 Guardar archivo
    nombre_archivo = f"escrito_{caso.cliente}.docx"
    doc.save(nombre_archivo)

    return {
        "mensaje": f"Documento generado: {nombre_archivo}",
        "mora": hay_mora
    }


# ============================================================================
# RAG ENDPOINTS
# ============================================================================

@app.post("/rag/ingest")
def rag_ingest_documents(request: RAGIngestRequest):
    """Ingest documents into the RAG system."""
    if not rag_engine:
        raise HTTPException(status_code=503, detail="RAG Engine not initialized")
    
    try:
        result = rag_engine.ingest_documents(request.documents)
        return {
            "status": "success",
            **result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rag/retrieve")
def rag_retrieve_context(request: RAGRetrieveRequest):
    """Retrieve context documents from the RAG system."""
    if not rag_engine:
        raise HTTPException(status_code=503, detail="RAG Engine not initialized")
    
    try:
        results = rag_engine.retrieve_context(
            query=request.query,
            top_k=request.top_k,
            doc_type_filter=request.doc_type_filter
        )
        return {
            "status": "success",
            "query": request.query,
            "results_count": len(results),
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rag/generate/template")
def rag_generate_template(request: RAGGenerateTemplateRequest):
    """Generate a legal template using RAG context."""
    if not rag_engine:
        raise HTTPException(status_code=503, detail="RAG Engine not initialized")
    
    try:
        template = rag_engine.generate_template(
            template_type=request.template_type,
            cliente=request.cliente,
            details=request.details or {}
        )
        return {
            "status": "success",
            "template_type": request.template_type,
            "cliente": request.cliente,
            "template": template
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rag/generate/email")
def rag_generate_email(request: RAGGenerateEmailRequest):
    """Generate a professional email using RAG context."""
    if not rag_engine:
        raise HTTPException(status_code=503, detail="RAG Engine not initialized")
    
    try:
        email = rag_engine.generate_email(
            email_type=request.email_type,
            recipient=request.recipient,
            subject=request.subject or "",
            body_details=request.body_details or {}
        )
        return {
            "status": "success",
            "email_type": request.email_type,
            "recipient": request.recipient,
            "email": email
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rag/stats")
def rag_get_stats():
    """Get RAG index statistics."""
    if not rag_engine:
        raise HTTPException(status_code=503, detail="RAG Engine not initialized")
    
    try:
        stats = rag_engine.get_index_stats()
        return {
            "status": "success",
            "stats": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))