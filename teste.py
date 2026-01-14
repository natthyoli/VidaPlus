import requests

BASE_URL = "http://127.0.0.1:8000"

def testar():
    print("--- INICIANDO TESTES DO SISTEMA ---")

    # 1. Cadastrar Médico
    medico = {"nome": "Dr. Rodrigo", "especialidade": "Geral", "crm": "999-SP"}
    res_med = requests.post(f"{BASE_URL}/medicos", json=medico)
    id_medico = res_med.json().get("id")
    print(f"1. Cadastro Médico: {'✅ OK' if res_med.status_code == 200 else '❌ ERRO'}")

    # 2. Cadastrar Paciente
    paciente = {
        "nome": "João Silva", "mes_nascimento": 1, "ano_nascimento": 1990,
        "telefone": "11988887777", "email": "joao@email.com"
    }
    res_pac = requests.post(f"{BASE_URL}/pacientes", json=paciente)
    id_paciente = res_pac.json().get("id")
    print(f"2. Cadastro Paciente: {'✅ OK' if res_pac.status_code == 200 else '❌ ERRO'}")

    # 3. Agendamento Válido (Segunda-feira às 10h)
    agenda_ok = {
        "data_hora": "2026-01-19T10:00:00", 
        "paciente_id": id_paciente, "medico_id": id_medico
    }
    res_ag_ok = requests.post(f"{BASE_URL}/agendamentos", json=agenda_ok)
    print(f"3. Agendamento Válido: {'✅ OK' if res_ag_ok.status_code == 200 else '❌ ERRO'}")

    # 4. Teste de Erro: Fim de Semana (Domingo)
    agenda_domingo = {
        "data_hora": "2026-01-18T10:00:00", 
        "paciente_id": id_paciente, "medico_id": id_medico
    }
    res_dom = requests.post(f"{BASE_URL}/agendamentos", json=agenda_domingo)
    print(f"4. Bloqueio Fim de Semana: {'✅ FUNCIONOU' if res_dom.status_code == 400 else '❌ FALHOU'}")
    print(f"   Mensagem: {res_dom.json().get('detail')}")

    # 5. Teste de Erro: Horário fora do Comercial (20:00h)
    agenda_noite = {
        "data_hora": "2026-01-19T20:00:00", 
        "paciente_id": id_paciente, "medico_id": id_medico
    }
    res_noite = requests.post(f"{BASE_URL}/agendamentos", json=agenda_noite)
    print(f"5. Bloqueio Horário Noturno: {'✅ FUNCIONOU' if res_noite.status_code == 400 else '❌ FALHOU'}")
    print(f"   Mensagem: {res_noite.json().get('detail')}")

if __name__ == "__main__":
    testar()