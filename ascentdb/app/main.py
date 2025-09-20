from fastapi import FastAPI

from ascentdb.app.routers import students, attendance, marks, activities, reports, users
import uvicorn

app = FastAPI(title="AscentDB API")

# Include routers
app.include_router(students.router)
app.include_router(attendance.router)
app.include_router(marks.router)
app.include_router(activities.router)
app.include_router(reports.router)
app.include_router(users.router)

# using vercel for the server
# if __name__ == "__main__":
#     uvicorn.run(
#         "ascentdb.app.main:app",
#         host="0.0.0.0",
#         port=9900,
#         reload=True
#     )