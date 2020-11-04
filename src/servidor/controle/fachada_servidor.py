from src.servidor.regras_de_negocio.usuarios import Cliente, Estabelecimento

def login(email: str, senha: str) -> tuple:
    cliente = Cliente(email, senha)
    estabelecimento = Estabelecimento(email, senha)

    if cliente.login():
        return cliente.nome, cliente.cidade, True, None
    elif estabelecimento.login():
        return estabelecimento.nome, estabelecimento.cidade, False, estabelecimento.cnpj

    return None

def salva(tabela: int, elemento: dict) -> bool:
    if tabela == 0:
        print("Entrou Estabelecimento")
        return Estabelecimento(elemento['email'], elemento['senha'], elemento['nome'],
                               elemento['cidade'], elemento['id'], elemento['cnpj']).salva()
    elif tabela == 1:
        print("Entrou cliente")
        return Cliente(elemento['email'], elemento['senha'], elemento['nome'], elemento['cidade'],
                       elemento['id'], elemento['privilegio']).salva()

    print("Não entrou")
    return False