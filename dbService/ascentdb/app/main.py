import uvicorn
from fastapi import FastAPI

from ascentdb.app.routers import reports, attendance, activities, users, students
from ascentdb.app.routers import marks

app = FastAPI(title="AscentDB API")

# Include routers
app.include_router(students.router)
app.include_router(attendance.router)
app.include_router(marks.router)
app.include_router(activities.router)
app.include_router(reports.router)
app.include_router(users.router)

# if __name__ == "__main__":
#     uvicorn.run(
#         "ascentdb.app.main:app",
#         host="0.0.0.0",
#         port=9900,
#         reload=True
#     )