import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8001"

# 1. Criar um Médico (Necessário para o agendamento)
medico_data = {
    "nome": "Dra Ana",
    "especialidade": "Cardiologia",
    "crm": "12345-SP"
}
response_medico = requests.post(f"{BASE_URL}/medicos", json=medico_data)
medico_id = response_medico.json().get("id")
print(f"Médico criado: {response_medico.status_code} (ID: {medico_id})")

# 2. Criar um Paciente (Apenas com os campos que existem no seu schemas.py)
paciente_data = {
    "nome": "Pedro Silva",
    "mes_nascimento": 5,
    "ano_nascimento": 2015,
    "telefone": "11999990000",
    "email": "pedro.silva@email.com"
}
response_paciente = requests.post(f"{BASE_URL}/pacientes", json=paciente_data)
paciente_id = response_paciente.json().get("id")
print(f"Paciente criado: {response_paciente.status_code} (ID: {paciente_id})")

# 3. Criar um Agendamento (Respeitando as regras de horário comercial no crud.py)
# Data: Uma segunda-feira às 10h (Horário válido)
agendamento_data = {
    "data_hora": "2026-01-19T10:00:00", 
    "paciente_id": paciente_id,
    "medico_id": medico_id
}
response_agendamento = requests.post(f"{BASE_URL}/agendamentos", json=agendamento_data)
print(f"Agendamento: {response_agendamento.status_code}")
if response_agendamento.status_code != 200:
    print(f"Erro no agendamento: {response_agendamento.json().get('detail')}")