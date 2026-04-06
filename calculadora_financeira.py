def calcular_total_com_desconto(valor, percentual_desconto):
    if valor < 0:
        raise ValueError("O valor nao pode ser negativo.")
    if not 0 <= percentual_desconto <= 100:
        raise ValueError("O percentual de desconto deve estar entre 0 e 100.")

    return valor * (1 - percentual_desconto / 100)


def parcelar_valor(valor, parcelas):
    if valor < 0:
        raise ValueError("O valor nao pode ser negativo.")
    if parcelas <= 0:
        raise ValueError("A quantidade de parcelas deve ser maior que zero.")

    return round(valor / parcelas, 2)


def classificar_nota(nota):
    if not 0 <= nota <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")
    if nota < 5:
        return "reprovado"
    if nota < 7:
        return "recuperacao"
    return "aprovado"


def eh_cliente_premium(total_compras, anos_cliente):
    if total_compras < 0 or anos_cliente < 0:
        raise ValueError("Os valores informados nao podem ser negativos.")

    return total_compras >= 5000 or anos_cliente >= 5