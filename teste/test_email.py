import pytest

from src.servidor.regras_de_negocio.informacao import Email
from src.servidor.regras_de_negocio.excessoes import EmailInvalidoError


@pytest.fixture
def endereco():
    return Email("rafael.braga@outlook.com")


def test_nao_permite_criar_email_vazio():
    with pytest.raises(EmailInvalidoError):
        Email("")


def test_troca_email(endereco):
    endereco.email = "brazinha.4.20@pweed.com.br"

    assert endereco.email == "brazinha.4.20@pweed.com.br"


def test_deve_levantar_erro_quando_colocado_email_invalido(endereco):
    with pytest.raises(EmailInvalidoError):
        endereco.email = "@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail."

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.com."

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.bragahotmail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = ""

    with pytest.raises(EmailInvalidoError):
        endereco.email = "@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = ".rafael.braga@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "0rafael.braga@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotm_ail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.c_o"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.co5"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.comm"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.com."

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.com.b5"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.com.b."

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.b@raga@hotmail.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail@.com"

    with pytest.raises(EmailInvalidoError):
        endereco.email = "rafael.braga@hotmail.co@m"
