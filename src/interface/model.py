from src.servidor.controle.fachada_servidor import login, salva


class Cliente:
    def __init__(self, email: str, senha: str, nome: str = None, eh_cliente: bool = None,
                 cidade: str = None, cnpj: str = None):
        self.__email = email
        self.__senha = senha
        self.__nome = nome
        self.__eh_cliente: bool = eh_cliente
        self.__cidade = cidade
        self.__cnpj = cnpj

    @property
    def email(self):
        return self.__email

    @property
    def nome(self):
        return self.__nome

    @property
    def eh_cliente(self):
        return self.__eh_cliente

    @property
    def cidade(self):
        return self.__cidade

    @property
    def cnpj(self):
        return self.__cnpj

    def login(self) -> bool:
        resposta: tuple = login(self.__email, self.__senha)

        if resposta:
            self.__nome = resposta[0]
            self.__cidade = resposta[1]
            self.__eh_cliente = resposta[2]
            self.__cnpj = resposta[3]

            return True
        else:
            return False

    def cadastrar(self) -> bool:
        conta: dict = {'nome': self.__nome, 'senha': self.__senha, 'email': self.__email,
                       'cidade': self.__cidade, 'id': -1}
        if self.__eh_cliente:
            conta['privilegio'] = False
            tabela = 1
        else:
            conta['cnpj'] = self.__cnpj
            tabela = 0
        print("model: " + str(conta))

        return salva(tabela, conta)

    def estrutura_json(self):
        return {"email": self.__email, "nome": self.__nome, "eh_cliente": self.__eh_cliente,
                "cidade": self.__cidade, "cnpj": self.__cnpj}
