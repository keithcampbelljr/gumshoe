# gumshoe

# Objective
- Wrap nmap scan in a Python service that takes environment variables and performs network connectivity checks between Non Production netweorks and Production networks
- Deploy service with Docker
- Deploy temporary Azure Container Instance to a network to run connectivity tests
- Depeloy / Consume Azure Storage Account configuration to export results for security team

# Setup
- `python -m venv venv`
- `pip install -r requirements.txt`
- `python main.py`