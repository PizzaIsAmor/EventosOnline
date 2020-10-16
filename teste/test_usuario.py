import pytest

from src.servidor.regras_de_negocio.excessoes import EmailInvalidoError, NomeInvalidoError, \
    DataInvalidaError, EnderecoInvalidoError
from src.servidor.regras_de_negocio.usuarios import Usuario


@pytest.fixture
def pessoa() -> Usuario:
    return Usuario("Rafael Fernando Braga", "25/12/1994",
                   "rafael.braga@outlook.com", '01310-200', '1578')


def test_levantar_erro_quando_eh_email_invalido(pessoa: Usuario) -> None:
    with pytest.raises(EmailInvalidoError):
        pessoa.email = "@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail."

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.com."

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.bragahotmail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = ""

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = ".rafael.braga@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "0rafael.braga@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotm_ail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.c_o"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.co5"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.comm"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.com."

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.com.b5"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.com.b."

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.b@raga@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail@.com"

    with pytest.raises(EmailInvalidoError):
        pessoa.email = "rafael.braga@hotmail.co@m"


def test_levantar_erro_quando_o_nome_eh_invalido(pessoa: Usuario) -> None:
    with pytest.raises(NomeInvalidoError):
        pessoa.nome = "Rafael Bra0ga"

    with pytest.raises(NomeInvalidoError):
        pessoa.nome = "Raf0ael Braga"

    with pytest.raises(NomeInvalidoError):
        pessoa.nome = "Rafael Brag&a"

    with pytest.raises(NomeInvalidoError):
        pessoa.nome = "Rafa@el Braga"

    with pytest.raises(NomeInvalidoError):
        pessoa.nome = "Rafael Braga."


def test_levantar_erro_quando_eh_data_de_nascimento_invalida(pessoa: Usuario) -> None:
    with pytest.raises(DataInvalidaError):
        ano_com_5_digitos = "01/01/16667"
        pessoa.nascimento = ano_com_5_digitos

    with pytest.raises(DataInvalidaError):
        mes_maior_que_desembro = "01/13/1993"
        pessoa.nascimento = mes_maior_que_desembro

    with pytest.raises(DataInvalidaError):
        dia_maior_que_31 = "32/01/1993"
        pessoa.nascimento = dia_maior_que_31

    with pytest.raises(DataInvalidaError):
        mes_igual_a_0 = "01/00/1993"
        pessoa.nascimento = mes_igual_a_0

    with pytest.raises(DataInvalidaError):
        dia_igual_a_0 = "00/01/1993"
        pessoa.nascimento = dia_igual_a_0

    with pytest.raises(DataInvalidaError):
        data_vazia = ""
        pessoa.nascimento = data_vazia

    with pytest.raises(DataInvalidaError):
        janeiro = "32/01/2021"
        pessoa.nascimento = janeiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "29/02/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        marco = "32/03/2021"
        pessoa.nascimento = marco

    with pytest.raises(DataInvalidaError):
        fevereiro = "31/04/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "32/05/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "31/06/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "32/07/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "32/08/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "31/09/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "32/10/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "31/11/2021"
        pessoa.nascimento = fevereiro

    with pytest.raises(DataInvalidaError):
        fevereiro = "32/12/2021"
        pessoa.nascimento = fevereiro


def test_permitir_29_de_fevereiro_quando_eh_ano_bixesto(pessoa: Usuario) -> None:
    ano_bixesto = "29/02/2020"
    pessoa.nascimento = ano_bixesto

    assert pessoa.nascimento == ano_bixesto


def test_erro_quando_passar_formato_errado_de_endereco(pessoa: Usuario) -> None:
    with pytest.raises(EnderecoInvalidoError):
        cep_invalido = "11111111"
        pessoa.novo_endereco(cep_invalido, "91")

    with pytest.raises(EnderecoInvalidoError):
        pessoa.novo_endereco('01310-200', "7f")

    with pytest.raises(EnderecoInvalidoError):
        pessoa.novo_endereco('01310-200', "7#")

    with pytest.raises(EnderecoInvalidoError):
        pessoa.novo_endereco('013102-00', "7")

    with pytest.raises(EnderecoInvalidoError):
        pessoa.novo_endereco('0131-0200', "7")

    with pytest.raises(EnderecoInvalidoError):
        pessoa.novo_endereco('013a10-200', "7")
