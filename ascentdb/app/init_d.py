from ascentdb.app.database import Base, engine
from ascentdb.app.models import user, student, reports, activities, marks, attendance
def init_db():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")

if __name__ == "__main__":
    init_db()
