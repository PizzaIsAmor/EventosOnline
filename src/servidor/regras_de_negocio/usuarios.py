import re

from src.servidor.regras_de_negocio.informacao import Data, Email
from src.servidor.regras_de_negocio.excessoes import NomeInvalidoError
from src.servidor.dados.dao import Dao

class Usuario:
    def __init__(self, email: str, senha: str, nome: str = None,
                 cidade: str = None, id: int = -1):
        self.__email: Email = Email(email)
        self.__senha: str = senha
        self.__cidade: str = cidade
        self.__nome: str = None
        self.__id: int = id
        self.__inicializa_nome(nome)

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
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @staticmethod
    def __eh_nome_valido(nome):
        return type(nome) is str and re.fullmatch(r'[A-Za-z]+(\s[A-Za-z]+)*', nome)

    def __inicializa_nome(self, nome):
        if nome:
            nome = nome.strip()
            if self.__eh_nome_valido(nome):
                self.__nome = nome
            else:
                raise NomeInvalidoError(classe="Nome de Usuário", nome=nome)

    def login(self, tabela: str) -> tuple:
        usuario = Dao(tabela).busca('email', self.__email.email)

        if usuario and usuario[2] == self.__senha:
            self.__cidade = usuario[4]
            self.__inicializa_nome(usuario[3])
            self.__id = usuario[0]

            return usuario
        return None

    def salva(self, tabela: str, atributos_adicionais: dict) -> bool:
        atributos_adicionais['nome'] = self.__nome
        atributos_adicionais['email'] = self.__email.email
        atributos_adicionais['senha'] = self.__senha
        atributos_adicionais['cidade'] = self.__cidade
        if self.__id != -1:
            atributos_adicionais['id'] = self.__id

        return Dao(tabela).salvar(atributos_adicionais)

class Cliente(Usuario):
    def __init__(self, email: str, senha: str = None, nome: str = None,
                 cidade: str = None, id: int = -1, privilegio: bool = False):
        super().__init__(email, senha, nome, cidade, id)
        self.__privilegio = privilegio

    @property
    def privilegio(self):
        return self.__privilegio

    def login(self) -> bool:
        usuario = super().login('cliente')

        if usuario:
            self.__privilegio = usuario[5]

            return True
        return False

    def salva(self):
        return super().salva('cliente', {'privilegio': self.__privilegio})


class Estabelecimento(Usuario):
    def __init__(self, email: str, senha: str = None, nome: str = None,
                 cidade: str = None, id: int = -1, cnpj: str = None):
        super().__init__(email, senha, nome, cidade, id)
        self.__cnpj = cnpj
        self.senha = senha

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    def login(self) -> bool:
        usuario = super().login('estabelecimento')

        if usuario:
            self.__cnpj = usuario[5]

            return True
        return False

    def salva(self):
        return super().salva('estabelecimento', {'cnpj': self.__cnpj})