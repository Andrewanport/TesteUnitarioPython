# Testes Unitarios em Python

Este projeto contem um exemplo simples de logica Python com testes unitarios. A suite foi escrita com `unittest`, mas tambem pode ser executada com `pytest`.

## Arquivos principais

- `calculadora_financeira.py`: modulo com funcoes simples para servir de base aos testes.
- `test_calculadora_financeira.py`: suite de testes unitarios.

## Como rodar os testes

### Opcao 1: unittest

No terminal, dentro da pasta do projeto, execute:

```powershell
python -m unittest -v
```

Se estiver usando a virtualenv criada neste projeto no Windows, voce tambem pode executar:

```powershell
.venv\Scripts\python.exe -m unittest -v
```

### Opcao 2: pytest

Instale a dependencia de desenvolvimento:

```powershell
pip install -r requirements-dev.txt
```

Depois execute:

```powershell
pytest -v
```

Ou, com a virtualenv do projeto no Windows:

```powershell
.venv\Scripts\python.exe -m pytest -v
```

## Resultado esperado

Com `unittest`, o comando deve listar os testes executados e finalizar com `OK`.
<img width="1860" height="868" alt="image" src="https://github.com/user-attachments/assets/8ba6d1c0-9867-4ac2-a389-816b63cd933d" />


Com `pytest`, o comando deve mostrar a coleta dos testes e finalizar com algo como `11 passed`.
<img width="1919" height="1021" alt="image" src="https://github.com/user-attachments/assets/dee5cdf5-2ebb-4605-b5df-390ff2d9d405" />
