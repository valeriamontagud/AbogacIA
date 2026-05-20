# RAG System for Legal Document Generation

## Descripción

Sistema de **Retrieval-Augmented Generation (RAG)** integrado con OpenAI GPT-4 y Pinecone para generar plantillas, correos y documentos legales personalizados basados en la información del bufete de abogados.

## Arquitectura

```
┌─────────────────────────────────────────┐
│   FastAPI Backend (main.py)             │
├─────────────────────────────────────────┤
│   RAG Engine (rag/rag_engine.py)        │
│   ├─ Embeddings Manager                 │
│   ├─ Pinecone Client                    │
│   └─ Document Processor                 │
├─────────────────────────────────────────┤
│   Pinecone Vector Database              │
│   (Almacenamiento de embeddings)        │
├─────────────────────────────────────────┤
│   OpenAI GPT-4 API                      │
│   (Generación de contenido)             │
└─────────────────────────────────────────┘
```

## Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

Copia `.env.template` a `.env` y rellena tus claves API:

```bash
cp .env.template .env
```

Luego edita `.env` con tus credenciales:

```
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=your-pinecone-key
PINECONE_INDEX_NAME=bufete-legal-rag
```

### 3. Prepara tus datos

Crea archivos de texto en `backend/data/`:

- `bufete_info.txt` - Información del bufete
- `email_templates.txt` - Ejemplos de correos
- `template_examples.txt` - Ejemplos de plantillas

## Uso

### 1. Iniciar la API

```bash
cd backend
uvicorn main:app --reload
```

### 2. Ingestar documentos

```bash
POST /rag/ingest
{
  "documents": [
    {
      "text": "Información del bufete...",
      "doc_type": "info",
      "doc_name": "bufete_info"
    }
  ]
}
```

### 3. Generar plantilla

```bash
POST /rag/generate/template
{
  "template_type": "aceptacion_pago",
  "cliente": "Juan García",
  "details": {
    "importe": "5000 euros",
    "fecha": "2024-01-15"
  }
}
```

### 4. Generar correo

```bash
POST /rag/generate/email
{
  "email_type": "seguimiento",
  "recipient": "cliente@example.com",
  "subject": "Seguimiento de su caso",
  "body_details": {
    "avance": "Se ha completado la etapa de pruebas",
    "proximos_pasos": "Espera de sentencia"
  }
}
```

## Estructura de Módulos

### `rag/embeddings.py`
Maneja la vectorización de documentos usando OpenAI Embeddings API.

**Clases:**
- `EmbeddingsManager`: Gestiona embeddings de documentos

### `rag/pinecone_client.py`
Cliente para interactuar con Pinecone vector database.

**Clases:**
- `PineconeManager`: Gestiona operaciones en Pinecone (upsert, query, delete)

### `rag/document_processor.py`
Procesa y chunifica documentos para ingestion.

**Clases:**
- `DocumentProcessor`: Procesa documentos, los chunifica y extrae secciones

### `rag/rag_engine.py`
Motor principal del RAG que orquesta todo el sistema.

**Clases:**
- `RAGEngine`: Orquesta embeddings, Pinecone y OpenAI para generar contenido

## API Endpoints

### `POST /rag/ingest`
Ingesta documentos en el sistema RAG.

**Request:**
```json
{
  "documents": [
    {
      "text": "contenido",
      "doc_type": "info|email|template",
      "doc_name": "nombre_documento"
    }
  ]
}
```

### `POST /rag/retrieve`
Recupera contexto relevante para una consulta.

**Request:**
```json
{
  "query": "plantilla aceptación pago",
  "top_k": 5,
  "doc_type_filter": "template"
}
```

### `POST /rag/generate/template`
Genera una plantilla legal personalizada.

**Request:**
```json
{
  "template_type": "demanda",
  "cliente": "Nombre Cliente",
  "details": {"key": "value"}
}
```

### `POST /rag/generate/email`
Genera un correo profesional personalizado.

**Request:**
```json
{
  "email_type": "confirmacion",
  "recipient": "cliente@email.com",
  "subject": "Asunto",
  "body_details": {"key": "value"}
}
```

### `GET /rag/stats`
Obtiene estadísticas del índice RAG.

## Flujo de Uso Típico

1. **Ingestion**
   - Carga información del bufete, ejemplos de plantillas y correos
   - Se vectorizan y se almacenan en Pinecone

2. **Consulta**
   - Usuario solicita generar una plantilla/correo
   - RAG recupera ejemplos relevantes de Pinecone

3. **Generación**
   - GPT-4 usa el contexto recuperado
   - Genera contenido personalizado

4. **Entrega**
   - Se retorna la plantilla/correo generada

## Mejores Prácticas

### Datos de Ingestion

- Proporciona **ejemplos de alta calidad** de correos y plantillas
- Incluye **información clara** sobre el bufete
- Mantén un **tono consistente** en todos los documentos
- Agrupa por **tipo de documento** (info, email, template)

### Generación

- Usa **descripciones claras** en `details` y `body_details`
- Proporciona **contexto suficiente** pero no excesivo
- Prueba con diferentes **valores de temperatura** según el caso

## Troubleshooting

### Error: "RAG Engine not initialized"
- Verifica que las claves API estén correctamente configuradas en `.env`
- Comprueba que `OPENAI_API_KEY` y `PINECONE_API_KEY` sean válidas

### Error: "No results found"
- Asegúrate de haber ingestion documentos primero
- Prueba con consultas más simples
- Aumenta `top_k` en las búsquedas

### Respuestas genéricas
- Proporciona más ejemplos en los datos de ingestion
- Mejora la claridad de tus consultas
- Aumenta el `chunk_size` para más contexto

## Desarrollo Futuro

- [ ] Soporte para PDFs y documentos Word
- [ ] Fine-tuning de modelos específicos
- [ ] Caché de respuestas frecuentes
- [ ] Dashboard de monitoreo
- [ ] Feedback loop para mejora continua
