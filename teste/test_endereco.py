import pytest

from src.servidor.regras_de_negocio.informacao import Endereco
from src.servidor.regras_de_negocio.excessoes import EnderecoInvalidoError


@pytest.fixture
def masp():
    return Endereco('01310-200', '1578')


def test_permite_trocar_endereco_com_cep_e_numero_em_formato_int_e_string(masp):
    masp.novo_endereco('01310200', '1578')
    assert str(masp) == "Bairro Bela Vista Avenida Paulista São Paulo 1578, 01310200 SP"

    masp.novo_endereco(90650002, 81)
    assert str(masp) == "Bairro Partenon Avenida Bento Gonçalves Porto Alegre 81, 90650002 RS"


def test_levanta_erro_quando_dado_tipo_invalido_de_cep_e_unidade(masp):
    with pytest.raises(EnderecoInvalidoError):
        cep_invalido = "11111111"
        masp.novo_endereco(cep_invalido, "91")

    with pytest.raises(EnderecoInvalidoError):
        masp.novo_endereco('01310-200', "7f")

    with pytest.raises(EnderecoInvalidoError):
        masp.novo_endereco('01310-200', "7#")

    with pytest.raises(EnderecoInvalidoError):
        masp.novo_endereco('013102-00', "7")

    with pytest.raises(EnderecoInvalidoError):
        masp.novo_endereco('0131-0200', "7")

    with pytest.raises(EnderecoInvalidoError):
        masp.novo_endereco('013a10-200', "7")
