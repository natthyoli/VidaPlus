from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base

class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    mes_nascimento = Column(Integer)
    ano_nascimento = Column(Integer)
    telefone = Column(String)
    email = Column(String, unique=True)

class Medico(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especialidade = Column(String)
    crm = Column(String, unique=True)

class Agendamento(Base):
    __tablename__ = "agendamentos"
    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))
    status = Column(String, default="Agendado")