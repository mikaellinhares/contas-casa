function selecionaSituacao(valorOpcao) {
    let selectSituacao = document.querySelector('#filtro-situacao');
    
    ['success', 'info', 'danger', 'warning'].forEach((classe) => {
        if (selectSituacao.classList.contains(`alert-${classe}`)) {
            selectSituacao.classList.remove(`alert-${classe}`);
        }
    });

    if (valorOpcao == 'pago') {
        selectSituacao.classList.add('alert-success');
    } else if (valorOpcao == 'vence-hoje') {
        selectSituacao.classList.add('alert-info');
    } else if (valorOpcao == 'vencido') {
        selectSituacao.classList.add('alert-danger');
    } else if (valorOpcao == 'pendente') {
        selectSituacao.classList.add('alert-warning');
    }
}

function mostrarPagamentos(despesaId) {
    fetch(`despesas/${despesaId}/pagamentos`)
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Erro na rede');
            }
            return response.json();
        })
        .then(function (data) {
            const pagamentosList = document.getElementById('modal-pagamentos');
            pagamentosList.innerHTML = data;
            pagamentosList.style.display = 'block';
        })
        .catch(error => {
            console.error('Erro ao buscar pagamentos:', error);
        });
}

function validarCampos() {
    let elemento
    let todosValidos = true;

    elemento = document.querySelector('input[name="valor"]');
    if (elemento.value <= 0) {
        elemento.classList.toggle('is-invalid', true);
        todosValidos = false;
    }

    elemento = document.querySelector('select[name="forma_pagamento"]');
    if (elemento.value == "") {
        elemento.classList.toggle('is-invalid', true);
        todosValidos = false;
    }

    elemento = document.querySelector('select[name="pessoa"]');
    if (elemento.value == "") {
        elemento.classList.toggle('is-invalid', true);
        todosValidos = false;
    }

    elemento = document.querySelector('input[name="data"]');
    if (elemento.value == "") {
        elemento.classList.toggle('is-invalid', true);
        todosValidos = false;
    }

    return todosValidos;
}

function pagarDespesa(despesaId) {
    // Validar campos
    if (!validarCampos()) { return }

    csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const data = {
        valor: document.querySelector('input[name="valor"]').value,
        forma_pagamento: document.querySelector('select[name="forma_pagamento"]').value,
        pessoa: document.querySelector('select[name="pessoa"]').value,
        data: document.querySelector('input[name="data"]').value,
        descricao: document.querySelector('input[name="descricao"]').value,
    };

    fetch(`despesas/${despesaId}/pagar`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            fecharModal();
            mostrarPagamentos(despesaId);
        } else {
            alert('Ocorreu um erro ao gerar o pagamento!');
        }
    });
}