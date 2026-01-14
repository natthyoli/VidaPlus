from pydantic import BaseModel, EmailStr
from datetime import datetime

class PacienteBase(BaseModel):
    nome: str
    mes_nascimento: int
    ano_nascimento: int
    telefone: str
    email: EmailStr

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id: int
    class Config:
        from_attributes = True

class MedicoCreate(BaseModel):
    nome: str
    especialidade: str
    crm: str

class MedicoResponse(MedicoCreate):
    id: int
    class Config:
        from_attributes = True

class AgendamentoCreate(BaseModel):
    data_hora: datetime
    paciente_id: int
    medico_id: int

class AgendamentoResponse(AgendamentoCreate):
    id: int
    status: str
    class Config:
        from_attributes = True