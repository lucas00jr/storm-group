import unittest
from entities.facts import facts
from entities.schema import schema
from service.facts_service import get_current_facts


class TestFactsService(unittest.TestCase):

    def test_get_current_facts(self):
        # Chama a função com os dados de teste
        current_facts = get_current_facts(facts, schema)

        # Resultado esperado
        expected_facts = [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True)
        ]

        # Verifica se o resultado atual é igual ao esperado
        self.assertCountEqual(current_facts, expected_facts)

    #Teste para Verificar Fatos de Diferentes Entidades
    def test_multiple_entities(self):
        additional_facts = [
            ('maria', 'endereço', 'rua das flores, 45', True),
            ('maria', 'telefone', '98765-4321', True)
        ]

        facts_with_multiple_entities = facts + additional_facts
        current_facts = get_current_facts(facts_with_multiple_entities, schema)

        expected_facts = [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('maria', 'endereço', 'rua das flores, 45', True),
            ('maria', 'telefone', '98765-4321', True)
        ]

        self.assertCountEqual(current_facts, expected_facts)


if __name__ == '__main__':
    unittest.main()
