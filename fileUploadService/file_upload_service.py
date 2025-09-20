from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import csv, io, json, os
import aiofiles
from typing import Optional, List
import uvicorn

app = FastAPI(title="File Upload & Parsing Service")

class Student(BaseModel):
    id: Optional[int]
    name: str
    class_name: Optional[str] = None
    parent_id: Optional[int] = None

class Attendance(BaseModel):
    student_id: int
    month: str
    days_present: int

class Report(BaseModel):
    student_id: int
    report_text: Optional[str] = None
    file_url: Optional[str] = None
    date: Optional[str] = None

# Helpers
def parse_csv_bytes(b: bytes) -> List[dict]:
    text = b.decode("utf-8", errors="replace")
    reader = csv.DictReader(io.StringIO(text))
    return [row for row in reader]

def parse_json_bytes(b: bytes) -> List[dict]:
    obj = json.loads(b.decode("utf-8", errors="replace"))
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for v in obj.values():
            if isinstance(v, list):
                return v
        return [obj]
    raise ValueError("Unsupported JSON structure")

async def save_bytes_to_file(content: bytes, filename: str, dest_folder: str = "uploads") -> str:
    os.makedirs(dest_folder, exist_ok=True)
    path = os.path.join(dest_folder, filename)
    async with aiofiles.open(path, "wb") as f:
        await f.write(content)
    return path

def validate_parsed(parsed: List[dict], file_type: str) -> List[dict]:
    if file_type == "students":
        Model = Student
    elif file_type == "attendance":
        Model = Attendance
    elif file_type == "reports":
        Model = Report
    else:
        raise ValueError("file_type must be one of: students, attendance, reports")

    validated_data = []
    for i, item in enumerate(parsed):
        if "class" in item and "class_name" not in item:
            item["class_name"] = item.pop("class")
        try:
            validated = Model(**item)
            validated_data.append(validated.dict())
        except ValidationError as e:
            raise ValueError(f"Validation error at row {i}: {e}")

    return validated_data

@app.get("/")
def root():
    return {"message": "Welcome to File Upload & Parsing Service"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    file_type: str = Form(...),
):
    filename = file.filename or "uploaded"
    ext = os.path.splitext(filename)[1].lower()

    if ext not in (".csv", ".json"):
        raise HTTPException(status_code=400, detail="Only CSV or JSON files are allowed")

    content = await file.read()

    # Parse based on extension
    try:
        if ext == ".csv":
            parsed = parse_csv_bytes(content)
        else:
            parsed = parse_json_bytes(content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse file: {e}")

    # Validate
    try:
        validated = validate_parsed(parsed, file_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Save raw file
    saved_path = await save_bytes_to_file(content, filename)

    return JSONResponse({
        "status": "ok",
        "filename": filename,
        "rows_received": len(parsed),
        "rows_validated": len(validated),
        "sample": validated[:5],
        "saved_path": saved_path
    })
if __name__ == "__main__":
    uvicorn.run(
        "fileUploadService.file_upload_service:app",
        host="0.0.0.0",
        port=9990,
        reload=True
    )