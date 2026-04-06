import unittest

from calculadora_financeira import (
    calcular_total_com_desconto,
    classificar_nota,
    eh_cliente_premium,
    parcelar_valor,
)

class CalculosFinanceirosTests(unittest.TestCase):
    def test_calcula_total_sem_desconto(self):
        resultado = calcular_total_com_desconto(100, 0)

        self.assertEqual(resultado, 100)

    def test_calcula_total_com_desconto_percentual(self):
        resultado = calcular_total_com_desconto(200, 15)

        self.assertEqual(resultado, 170)

    def test_lanca_erro_quando_valor_do_desconto_e_invalido(self):
        with self.assertRaises(ValueError):
            calcular_total_com_desconto(100, 150)

    def test_parcela_valor_com_duas_casas_decimais(self):
        resultado = parcelar_valor(100, 3)

        self.assertAlmostEqual(resultado, 33.33, places=2)

    def test_lanca_erro_quando_numero_de_parcelas_e_zero(self):
        with self.assertRaises(ValueError):
            parcelar_valor(100, 0)

    def test_classifica_notas_em_multiplos_cenarios(self):
        cenarios = [
            (4.9, "reprovado"),
            (5.0, "recuperação"),
            (6.8, "recuperação"),
            (7.0, "aprovado"),
            (9.5, "aprovado"),
        ]

        for nota, classificacao_esperada in cenarios:
            with self.subTest(nota=nota):
                self.assertEqual(classificar_nota(nota), classificacao_esperada)

    def test_lanca_erro_para_nota_fora_do_intervalo(self):
        with self.assertRaises(ValueError):
            classificar_nota(11)

    def test_identifica_cliente_premium_por_total_de_compras(self):
        self.assertTrue(eh_cliente_premium(5200, 1))

    def test_identifica_cliente_premium_por_tempo_de_relacionamento(self):
        self.assertTrue(eh_cliente_premium(1000, 5))

    def test_identifica_cliente_nao_premium(self):
        self.assertFalse(eh_cliente_premium(3000, 2))

    def test_lanca_erro_para_dados_negativos_de_cliente(self):
        with self.assertRaises(ValueError):
            eh_cliente_premium(-1, 2)


if __name__ == "__main__":
    unittest.main()