var conta = document.getElementById("cadastro_conta");
var eh_conta_cliente = document.getElementsByName("tipo-conta");
var cliente = document.getElementById("cadastro_dados");
var estabelecimento = document.getElementById("cadastro_esta");
var cancelar = document.getElementById("botao-cancelar");
var cadastro = document.getElementById("botao-cadastro");
var conta_esta = document.getElementById("conta-estabelecimento");
var conta_cliente = document.getElementById("conta-cliente");


document.getElementById("prox_pagina").addEventListener("click", function(event) {
    event.preventDefault();
    conta.classList.add("esconder");
    cancelar.classList.add("esconder");

    if (eh_conta_cliente[0].checked) {
        cliente.classList.remove("esconder");
    }
    else {
        estabelecimento.classList.remove("esconder");
    }

    cadastro.classList.remove("esconder");
});

document.getElementById("botao-voltar").addEventListener("click", function(event) {
    event.preventDefault();
    conta.classList.remove("esconder");
    cancelar.classList.remove("esconder");
    cliente.classList.add("esconder");
    estabelecimento.classList.add("esconder");
    cadastro.classList.add("esconder");
});

conta_cliente.addEventListener("click", function(event) {
    event.preventDefault();
    conta_esta.classList.remove("active");
    this.classList.add("active");
    eh_conta_cliente[0].checked = true;
});

conta_esta.addEventListener("click", function(event) {
    event.preventDefault();
    conta_cliente.classList.remove("active");
    this.classList.add("active");
    eh_conta_cliente[1].checked = true;
});