import unittest

from calculadora_financeira import (
    calcular_total_com_desconto,
    classificar_nota,
    eh_cliente_premium,
    parcelar_valor,
)

class CalculosFinanceirosTests(unittest.TestCase):
    def test_calcular_total_com_desconto_sem_desconto_retorna_valor_original(self):
        resultado = calcular_total_com_desconto(100, 0)

        self.assertEqual(resultado, 100)

    def test_calcular_total_com_desconto_percentual_valido_retorna_total_com_desconto(self):
        resultado = calcular_total_com_desconto(200, 15)

        self.assertEqual(resultado, 170)

    def test_calcular_total_com_desconto_percentual_acima_do_limite_lanca_erro(self):
        with self.assertRaises(ValueError):
            calcular_total_com_desconto(100, 150)

    def test_calcular_total_com_desconto_percentual_negativo_lanca_erro(self):
        with self.assertRaises(ValueError):
            calcular_total_com_desconto(100, -1)

    def test_calcular_total_com_desconto_valor_negativo_lanca_erro(self):
        with self.assertRaises(ValueError):
            calcular_total_com_desconto(-100, 10)

    def test_parcelar_valor_com_duas_casas_decimais(self):
        resultado = parcelar_valor(100, 3)

        self.assertAlmostEqual(resultado, 33.33, places=2)

    def test_parcelar_valor_parcelas_iguais_a_zero_lanca_erro(self):
        with self.assertRaises(ValueError):
            parcelar_valor(100, 0)

    def test_parcelar_valor_valor_negativo_lanca_erro(self):
        with self.assertRaises(ValueError):
            parcelar_valor(-100, 3)

    def test_classificar_nota_multiplos_cenarios_retorna_classificacao_esperada(self):
        cenarios = [
            (4.9, "reprovado"),
            (5.0, "recuperacao"),
            (6.8, "recuperacao"),
            (7.0, "aprovado"),
            (9.5, "aprovado"),
        ]

        for nota, classificacao_esperada in cenarios:
            with self.subTest(nota=nota):
                self.assertEqual(classificar_nota(nota), classificacao_esperada)

    def test_classificar_nota_acima_do_intervalo_lanca_erro(self):
        with self.assertRaises(ValueError):
            classificar_nota(11)

    def test_classificar_nota_abaixo_do_intervalo_lanca_erro(self):
        with self.assertRaises(ValueError):
            classificar_nota(-0.1)

    def test_eh_cliente_premium_por_total_de_compras_retorna_true(self):
        self.assertTrue(eh_cliente_premium(5200, 1))

    def test_eh_cliente_premium_por_tempo_de_relacionamento_retorna_true(self):
        self.assertTrue(eh_cliente_premium(1000, 5))

    def test_eh_cliente_premium_sem_criterios_retorna_false(self):
        self.assertFalse(eh_cliente_premium(3000, 2))

    def test_eh_cliente_premium_com_dados_negativos_lanca_erro(self):
        with self.assertRaises(ValueError):
            eh_cliente_premium(-1, 2)


if __name__ == "__main__":
    unittest.main()