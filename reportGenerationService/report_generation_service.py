import json
import re
import requests
from typing import List, Dict
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# -------------------- FastAPI App --------------------
app = FastAPI(
    title="Student Report Generator & Chatbot",
    description="Generate structured student reports or chat with Ollama AI.",
    version="1.1.0"
)

# -------------------- Schemas --------------------
class SubjectScore(BaseModel):
    score: float
    max_score: float

class Marks(BaseModel):
    exam_type: str
    date: str
    teacher_note: str
    subject_scores: Dict[str, SubjectScore]

class Attendance(BaseModel):
    month: str
    days_present: int
    days_absent: int

class Activity(BaseModel):
    activity_type: str
    description: str
    achievement: str
    date: str

class StudentData(BaseModel):
    student_id: str
    student_name: str
    class_name: str
    parent_email: str
    marks: List[Marks]
    attendance: List[Attendance]
    activities: List[Activity]

class GeneratedReport(BaseModel):
    detailed_report: str
    summary: str

class ReportResponse(BaseModel):
    student_id: str
    student_name: str
    report_data: GeneratedReport

# ✅ New: Chat schema
class ChatRequest(BaseModel):
    message: str
    model: str = "tinyllama:latest"

class ChatResponse(BaseModel):
    reply: str

# -------------------- Ollama Config --------------------
OLLAMA_API_ENDPOINT = "http://localhost:11434/api/generate"

def call_ollama(prompt: str, model: str = "tinyllama:latest", expect_json: bool = False):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    if expect_json:
        payload["format"] = "json"

    try:
        response = requests.post(OLLAMA_API_ENDPOINT, json=payload, timeout=120)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {e}")

    return response.json().get("response", "")

def get_report_from_ollama(student_data: dict) -> GeneratedReport:
    prompt = f"""
You are an AI that generates a detailed student progress report for parents.

Student Data:
{json.dumps(student_data, indent=2)}

Requirements:
- Return only **valid JSON**.
- Keys must be:
  - "detailed_report": a string containing a textual report summarizing all marks, attendance, and activities.
  - "summary": a string containing a short textual summary for parents.
- Do NOT include nested objects inside "detailed_report" or "summary".
- Close all strings properly.
- Return JSON only; no extra text.
"""

    ai_response_text = call_ollama(prompt, expect_json=True)

    # Extract first JSON object
    match = re.search(r"\{.*\}", ai_response_text, re.DOTALL)
    if not match:
        raise HTTPException(status_code=500, detail=f"AI returned malformed JSON: {ai_response_text}")

    report_str = match.group(0)

    try:
        report_data = json.loads(report_str)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"JSON decode error: {e}. Response: {report_str}")

    # Ensure fields are strings
    for key in ["detailed_report", "summary"]:
        if key not in report_data:
            report_data[key] = ""
        elif not isinstance(report_data[key], str):
            report_data[key] = json.dumps(report_data[key])

    return GeneratedReport(**report_data)

# -------------------- API Endpoints --------------------
@app.post("/generate-reports", response_model=List[ReportResponse])
async def generate_student_reports(students: List[StudentData]):
    """
    Generate reports for multiple students by sending data to Ollama AI.
    """
    reports: List[ReportResponse] = []

    for student in students:
        student_dict = student.model_dump()

        # Format student data
        formatted_data = {
            "student_id": student_dict["student_id"],
            "student_name": student_dict["student_name"],
            "class_name": student_dict["class_name"],
            "parent_email": student_dict.get("parent_email", "N/A"),
            "marks": [
                {
                    "exam_type": m["exam_type"],
                    "date": m["date"],
                    "teacher_note": m.get("teacher_note", ""),
                    "subject_scores": m["subject_scores"],
                } for m in student_dict["marks"]
            ],
            "attendance": [
                {
                    "month": a["month"],
                    "days_present": a["days_present"],
                    "days_absent": a["days_absent"],
                } for a in student_dict["attendance"]
            ],
            "activities": [
                {
                    "activity_type": act["activity_type"],
                    "description": act["description"],
                    "achievement": act["achievement"],
                    "date": act["date"],
                } for act in student_dict["activities"]
            ]
        }

        report = get_report_from_ollama(formatted_data)
        reports.append(ReportResponse(
            student_id=student.student_id,
            student_name=student.student_name,
            report_data=report
        ))
    print(reports)
    return reports

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(chat_request: ChatRequest):

    reply = call_ollama(chat_request.message, model=chat_request.model)
    return ChatResponse(reply=reply)

# -------------------- Run Server --------------------
if __name__ == "__main__":
    uvicorn.run("report_generation_service:app", host="0.0.0.0", port=9999, reload=True)
