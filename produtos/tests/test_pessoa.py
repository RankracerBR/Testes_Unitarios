import unittest
from produtos import main


class PessoaTestCase(unittest.TestCase):
    def setUp(self):
        self.pessoa = main.Pessoa("Augusto", 20, "agst@gmail.com")
    
    def test_nome(self):
        self.assertEqual(self.pessoa.nome, "Augusto")

    def test_idade(self):
        self.assertEqual(self.pessoa.idade, 20)

    def test_email(self):
        self.assertEqual(self.pessoa.email, "agst@gmail.com")

    def test_string_representation(self):
        expected_str = 'Nome: Augusto, Idade: 20, Email: agst@gmail.com'
        self.assertEqual(str(self.pessoa), expected_str)

if __name__ == "__main__":
    unittest.main()