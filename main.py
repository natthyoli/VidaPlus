from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="VidaPlus - Agendamento Hospitalar")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/medicos", response_model=schemas.MedicoResponse)
def cadastrar_medico(medico: schemas.MedicoCreate, db: Session = Depends(get_db)):
    return crud.criar_medico(db, medico)

@app.post("/pacientes", response_model=schemas.PacienteResponse)
def cadastrar_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.criar_paciente(db, paciente)

@app.post("/agendamentos", response_model=schemas.AgendamentoResponse)
def agendar(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    return crud.criar_agendamento(db, agendamento)