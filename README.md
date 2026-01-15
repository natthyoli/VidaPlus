# 🏥 VidaPlus - Sistema de Agendamento Hospitalar

O **VidaPlus** é uma aplicação Backend desenvolvida para modernizar a gestão de agendamentos hospitalares. O sistema permite o controle centralizado de cadastros de médicos, pacientes e consultas, garantindo que os dados sejam organizados e acessíveis via API.

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python
* **Framework:** FastAPI
* **Documentação:** Swagger UI
* **Versionamento:** Git e GitHub
* **Modelagem:** UML (Diagramas de Classe e Casos de Uso)

## 📋 Funcionalidades
- [x] Cadastro e listagem de Médicos.
- [x] Gerenciamento de prontuários de Pacientes.
- [x] Agendamento de consultas hospitalares.
- [x] Documentação interativa de todos os endpoints.

## 🛠️ Como executar o projeto

Siga os passos abaixo para rodar a aplicação em sua máquina local:

### 1. Pré-requisitos
Certifique-se de ter instalado:
* **Git**
* **Python 3.10+**
* **Pip** (Gerenciador de pacotes do Python)

### 2. Clonagem do Repositório
```bash
git clone [https://github.com/natthyoli/VidaPlus.git](https://github.com/natthyoli/VidaPlus.git)
cd VidaPlus
### 3. Configuração do Ambiente
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
### 4.instalação de Dependências
### 5. Execução do Servidor
uvicorn main:app --reload
### 6. Acesso à Documentação (Swagger UI)
Após o servidor iniciar, acesse no seu navegador para testar os endpoints: 👉 http://127.0.0.1:8000/docs
