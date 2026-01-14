from sqlalchemy.orm import Session
from models import Paciente, Medico, Agendamento
from fastapi import HTTPException


def criar_paciente(db: Session, paciente_schema):
    novo = Paciente(**paciente_schema.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def criar_medico(db: Session, medico_schema):
    novo = Medico(**medico_schema.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def criar_agendamento(db: Session, agendamento_schema):
    dt = agendamento_schema.data_hora

    # 1️⃣ Regra: Clínica não atende fim de semana
    if dt.weekday() >= 5:
        raise HTTPException(
            status_code=400,
            detail="A clínica não atende aos sábados e domingos."
        )

    # 2️⃣ Regra: Horário comercial
    if dt.hour < 8 or dt.hour >= 18:
        raise HTTPException(
            status_code=400,
            detail="Horário inválido. Atendimento das 08:00 às 18:00."
        )

    # 3️⃣ Regra: Médico não pode ter dois pacientes no mesmo horário
    conflito_medico = db.query(Agendamento).filter(
        Agendamento.medico_id == agendamento_schema.medico_id,
        Agendamento.data_hora == agendamento_schema.data_hora
    ).first()

    if conflito_medico:
        raise HTTPException(
            status_code=400,
            detail="O médico já possui consulta neste horário."
        )

    # 4️⃣ Regra NOVA: Paciente não pode ter dois agendamentos no mesmo horário
    conflito_paciente = db.query(Agendamento).filter(
        Agendamento.paciente_id == agendamento_schema.paciente_id,
        Agendamento.data_hora == agendamento_schema.data_hora
    ).first()

    if conflito_paciente:
        raise HTTPException(
            status_code=400,
            detail="O paciente já possui um agendamento neste horário."
        )

    novo = Agendamento(**agendamento_schema.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
