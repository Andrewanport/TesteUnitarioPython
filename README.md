# Testes Unitários em Python

Este projeto contém um exemplo simples de lógica Python (se trata de uma calculadora) com testes unitários. A suíte foi escrita com `unittest`, mas também pode ser executada com `pytest`.

## Arquivos principais

- `calculadora_financeira.py`: módulo com funções simples para servir de base aos testes.
- `test_calculadora_financeira.py`: suíte de testes unitários.

## Regras de Negócio Testadas

As regras abaixo são validadas automaticamente na suíte `test_calculadora_financeira.py`:

1. Cálculo de total com desconto:
- Aplica desconto percentual corretamente.
- Mantém o valor original quando o desconto é `0%`.
- Rejeita percentual fora do intervalo permitido (`0` a `100`) com `ValueError`.
- Rejeita valor de compra negativo com `ValueError`.

2. Parcelamento de valor:
- Calcula o valor da parcela com arredondamento para duas casas decimais.
- Rejeita número de parcelas menor ou igual a zero com `ValueError`.
- Rejeita valor total negativo com `ValueError`.

3. Classificação de nota:
- Classifica como `reprovado` para notas menores que `5`.
- Classifica como `recuperacao` para notas entre `5` (inclusive) e `7` (exclusive).
- Classifica como `aprovado` para notas maiores ou iguais a `7`.
- Rejeita notas fora do intervalo `0` a `10` com `ValueError`.

4. Identificação de cliente premium:
- Classifica como premium quando `total_compras >= 5000`.
- Classifica como premium quando `anos_cliente >= 5`.
- Classifica como não premium quando nenhum dos critérios é atendido.
- Rejeita valores negativos de entrada com `ValueError`.

## Como rodar os testes

### Opção 1: unittest

No terminal, dentro da pasta do projeto, execute:

```powershell
python -m unittest -v
```

### Opção 2: pytest

Instale a dependencia de desenvolvimento:

```powershell
pip install -r requirements-dev.txt
```

Depois execute:

```powershell
pytest -v
```

### Opcao 3: pytest com cobertura

Para gerar cobertura de linhas e ramos (branch):

```powershell
pytest --cov=calculadora_financeira --cov-branch --cov-report=term-missing -v
```

## Resultado esperado

Com `unittest`, o comando deve listar os testes executados e finalizar com `OK`.
<img width="1860" height="868" alt="image" src="https://github.com/user-attachments/assets/8ba6d1c0-9867-4ac2-a389-816b63cd933d" />


Com `pytest`, o comando deve mostrar a coleta dos testes e finalizar com algo como `15 passed`.
<img width="1919" height="1021" alt="image" src="https://github.com/user-attachments/assets/dee5cdf5-2ebb-4605-b5df-390ff2d9d405" />

## Cobertura de teste

A suite valida os fluxos de sucesso e falha das regras mais criticas do modulo de servico `calculadora_financeira.py`.

Resultado atual esperado com cobertura habilitada:

- Cobertura de linhas: `100%`
- Cobertura de ramos (branch): `100%`
- Execucao da suite: `15 passed, 5 subtests passed`
- Relatorio detalhado exportado em `coverage.xml`
