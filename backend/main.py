from fastapi import FastAPI
from pydantic import BaseModel
from docxtpl import DocxTemplate
from datetime import datetime
import os

app = FastAPI()


# 🔹 Modelo de datos (lo que recibe la API)
class Caso(BaseModel):
    cliente: str
    fecha_siniestro: str
    importe: float


# 🔹 Endpoint básico
@app.get("/")
def root():
    return {"status": "API funcionando correctamente"}


# 🔹 Endpoint principal (generador de documento)
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