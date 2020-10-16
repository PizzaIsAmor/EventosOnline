def construtor_de_mensagem_de_erro(tipo_erro, erro=None, adicional=None) -> str:
    mensagem: str = f' {tipo_erro.strip().lower().title()} informado é inválido.\n'

    if not (erro is None):
        mensagem = mensagem + f' {tipo_erro} digitado: {erro}\n'
    if not (adicional is None):
        mensagem = mensagem + adicional

    return mensagem


class DataInvalidaError(Exception):
    def __init__(self, mensagem='', data=None, *args):
        msg = construtor_de_mensagem_de_erro("Data", data, ' Formato da data: "dia/mes/ano"')

        super(DataInvalidaError, self).__init__(mensagem or msg, data, args)


class EmailInvalidoError(Exception):
    def __init__(self, mensagem='', email=None, *args):
        msg = construtor_de_mensagem_de_erro("Email", email, f'Exemplo de email: nome@endereco.com')

        super(EmailInvalidoError, self).__init__(mensagem or msg, email, args)


class EnderecoInvalidoError(Exception):
    def __init__(self, mensagem='', endereco=None, unidade=None, *args):
        msg = construtor_de_mensagem_de_erro("Cep", endereco, f"Unidade: {unidade}")

        super(EnderecoInvalidoError, self).__init__(mensagem or msg, endereco, args)


class NomeInvalidoError(Exception):
    def __init__(self, classe, mensagem='', nome=None, *args):
        msg = construtor_de_mensagem_de_erro(classe, nome)

        super(NomeInvalidoError, self).__init__(mensagem or msg, nome, args)
