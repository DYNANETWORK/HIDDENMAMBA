import re
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os, sys
from HIDDENMAMBA import DB_URI, MAMBA_STAR, telethn
if MAMBA_STAR == 5038173179:
   print ("MAMBA_STAR ADDED SIR ")
else:
   print ("YOU REMOVED MAMBA STAR NOW SEE")
   os.execl(sys.executable, sys.executable, *sys.argv)
   telethn.disconnect()

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
