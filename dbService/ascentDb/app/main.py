from fastapi import FastAPI
from ascentDb.app.routers import (
    profile, classes, subjects, exams,
    attendance, resources, notifications,
    progress, reports, auth
)

app = FastAPI(title="School Management API", version="1.0")

app.include_router(profile.router)
app.include_router(classes.router)
app.include_router(subjects.router)
app.include_router(exams.router)
app.include_router(attendance.router)
app.include_router(resources.router)
app.include_router(notifications.router)
app.include_router(progress.router)
app.include_router(reports.router)
app.include_router(auth.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
