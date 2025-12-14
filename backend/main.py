from fastapi import FastAPI, UploadFile, File, HTTPException
from services.pdf_parser import extract_text_from_pdf
from services.docx_parser import extract_text_from_docx
from services.extractor import extract_info
from models.cv_result import CVResult

app = FastAPI(title="CV Extractor API")

@app.post("/api/v1/upload-cv", response_model=CVResult)
async def upload_cv(file: UploadFile = File(...)):

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)

    elif file.filename.endswith(".docx"):
        text = extract_text_from_docx(file.file)

    else:
        raise HTTPException(status_code=400, detail="Format non supporté")

    result = extract_info(text)
    return result
