import re
import requests

from datetime import date, datetime
from src.servidor.regras_de_negocio.excessoes import DataInvalidaError, EmailInvalidoError, EnderecoInvalidoError


class Data:
    def __init__(self, data=None):
        self.__data = None

        if data:
            self.__adiciona_data(data)
        else:
            self.__data = date.today()

    @property
    def data(self):
        return str(self)

    @data.setter
    def data(self, nova_data):
        self.__adiciona_data(nova_data)

    def __add__(self, other):
        return self.__data + other.__data

    def __sub__(self, other):
        return self.__data - other.__data

    def __str__(self):
        return self.__data.strftime('%d/%m/%Y')

    def __adiciona_data(self, data: str):
        try:
            data = data.strip()

            self.__data = datetime.strptime(data, '%d/%m/%Y').date()
        except ValueError:
            raise DataInvalidaError(data=data)


class Email:
    def __init__(self, email: str):
        self.__email = None

        self.__inicializa_email(email)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__inicializa_email(email)

    @staticmethod
    def __eh_email_valido(email):
        return re.fullmatch(r'^[a-zA-Z][a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}((\.[a-zA-Z]{2})?)$', email)

    def __inicializa_email(self, email):
        email = email.strip()

        if self.__eh_email_valido(email):
            self.__email = email
        else:
            raise EmailInvalidoError(email=email)


class Endereco:
    def __init__(self, cep, unidade):
        self.__cep = None
        self.__logradouro = None
        self.__complemento = None
        self.__bairro = None
        self.__localidade = None
        self.__uf = None
        self.__unidade = None
        self.__ibge = None
        self.__gia = None

        self.__adiciona_endereco(cep, unidade)

    def novo_endereco(self, cep, unidade):
        self.__adiciona_endereco(cep, unidade)

    def __str__(self):
        return f'Bairro {self.__bairro} {self.__logradouro} {self.__localidade}' + \
               f' {self.__unidade}, {self.__cep} {self.__uf}'

    def __adiciona_endereco(self, cep, unidade):
        if type(cep) is int:
            cep = str(cep)
        if type(unidade) is int:
            unidade = str(unidade)

        cep = cep.strip()
        unidade = unidade.strip()
        if self.__eh_endereco_valido(cep, unidade):
            if '-' in cep:
                self.__cep = cep[:5] + cep[6:]
            else:
                self.__cep = cep

            endereco = requests.get(f'https://viacep.com.br/ws/{self.__cep}/json/').json()

            if "erro" in endereco:
                raise EnderecoInvalidoError(endereco=cep, unidade=unidade)
            else:
                self.__logradouro = endereco['logradouro']
                self.__complemento = endereco['complemento']
                self.__bairro = endereco['bairro']
                self.__localidade = endereco['localidade']
                self.__uf = endereco['uf']
                self.__ibge = endereco['ibge']
                self.__gia = endereco['gia']
                self.__unidade = unidade
        else:
            raise EnderecoInvalidoError(endereco=cep, unidade=unidade)

    @staticmethod
    def __eh_endereco_valido(cep: str, unidade: str):
        return Endereco.__eh_cep_valido(cep) and Endereco.__eh_unidade_valida(unidade)

    @staticmethod
    def __eh_unidade_valida(unidade: str):
        return type(unidade) is str and re.fullmatch(r'[0-9]+', unidade)

    @staticmethod
    def __eh_cep_valido(cep: str):
        return type(cep) is str and re.fullmatch(r'([0-9]{5}-[0-9]{3})|([0-9]{8})', cep)
