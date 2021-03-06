import unittest
from should_dsl import should
from pessoa import Pessoa
class PessoaSpec(unittest.TestCase):

    def it_creates_a_pessoa_object(self):
        pessoa = Pessoa(10, 50, 123)
        pessoa.idade|should| equal_to(10)       
        pessoa.peso|should| equal_to(50)
        pessoa.altura|should| equal_to(123)

    def it_add_altura_a_pessoa_object(self):
        pessoa = Pessoa(10, 50, 123)
        pessoa.adicionarcm(234)
        pessoa.altura|should| equal_to(234)
        
    def it_envelhecer_pessoa_object(self):
        pessoa = Pessoa(10, 50, 123)
        pessoa.envelhecer(5)
        pessoa.idade|should| equal_to(15)
        pessoa.altura|should| equal_to(130.5)
        
            
    def it_emagrecer_pessoa_object(self):
        pessoa = Pessoa(10, 50, 123)
        pessoa.emagrecer(5)
        pessoa.peso|should| equal_to(45)

    def it_engordar_pessoa_object(self):
        pessoa = Pessoa(10, 50, 123)
        pessoa.engordar(5)
        pessoa.peso|should| equal_to(55)

