from ascentDb.app.database import Base, engine
from ascentDb.app.models import *

def init_db():
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully!")

if __name__ == "__main__":
    init_db()
