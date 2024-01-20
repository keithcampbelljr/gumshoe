# gumshoe

# Objective
- Wrap nmap scan in a Python service that takes environment variables and performs network connectivity checks between Non Production networks and Production networks
- Deploy service with Docker
- Deploy temporary Azure Container Instance to a network to run connectivity tests
    - need to look into using temporary VM instead, ACI will not work will due to requiring its own subnet on a vnet with no other resources deployed. This makes the adoption of this workflow less desirable.
- Depeloy / Consume Azure Storage Account configuration to export results for security team

# Setup
- `python -m venv venv`
- `pip install -r requirements.txt`
- `python main.py`