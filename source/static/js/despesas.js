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