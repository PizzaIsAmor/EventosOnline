import re

from src.servidor.regras_de_negocio.dados import Data, Endereco, Email
from src.servidor.regras_de_negocio.excessoes import NomeInvalidoError


class Usuario:
    def __init__(self, nome: str, nascimento: str, email: str, cep: str, unidade: str):
        self.__nome: str = ""
        self.__inicializa_nome(nome)

        self.__endereco: Endereco = Endereco(cep, unidade)
        self.__nascimento: Data = Data(nascimento)
        self.__email: Email = Email(email)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__inicializa_nome(nome)

    @property
    def email(self):
        return self.__email.email

    @email.setter
    def email(self, novo_email):
        self.__email.email = novo_email

    @property
    def endereco(self):
        return str(self.__endereco)

    def novo_endereco(self, cep, unidade):
        self.__endereco.novo_endereco(cep, unidade)

    @property
    def nascimento(self):
        return self.__nascimento.data

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento.data = nascimento

    def __inicializa_nome(self, nome):
        nome = nome.strip()

        if self.__eh_nome_valido(nome):
            self.__nome = nome
        else:
            raise NomeInvalidoError(classe="Nome de Usuário", nome=nome)

    @staticmethod
    def __eh_nome_valido(nome):
        return type(nome) is str and re.fullmatch(r'[A-Za-z]+(\s[A-Za-z]+)*', nome)


class Adiministrador(Usuario):
    def __init__(self, nome: str, nascimento: str, email: str, cep: str, unidade: str):
        super().__init__(nome, nascimento, email, cep, unidade)


class Cliente(Usuario):
    def __init__(self, nome: str, nascimento: str, email: str, cep: str, unidade: str):
        super().__init__(nome, nascimento, email, cep, unidade)


class Estabelecimento(Usuario):
    def __init__(self, nome: str, nascimento: str, email: str, cep: str, unidade: str,
                 cnpj, comprovantes_de_seguranca, fotos):
        super().__init__(nome, nascimento, email, cep, unidade)
        self.__cnpj = cnpj
        self.__seguranca = comprovantes_de_seguranca
        self.__fotos = fotos

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def comprovante_de_seguranca(self):
        return self.__seguranca

    @comprovante_de_seguranca.setter
    def comprovante_de_seguranca(self, comprovante_de_seguranca):
        self.__seguranca = comprovante_de_seguranca

    @property
    def fotos(self):
        return self.__fotos

    @fotos.setter
    def fotos(self, fotos):
        self.__fotos = fotos
