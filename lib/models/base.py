from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///lib/flower_shop.db")
Session = sessionmaker(bind=engine)
