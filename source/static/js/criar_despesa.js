function alteraOpcaoPagamento() {
    var iconePagamento = document.querySelector('#icone-pagamento');
    var bgIconePagamento = document.querySelector('#bg-icone-pagamento');
    var descricaoPagamento = document.querySelector('#descricao-pagamento');
    var inputPagamento = document.querySelector('#input-pagamento');
    var iconTag
    var classAdd
    var classRemove
    var paymentText
    var paymentCondition
    var elementsDisplay

    if (bgIconePagamento.classList.contains('bg-success')) {
        iconTag = 'disabled_by_default';
        classRemove = 'bg-success';
        classAdd = 'bg-danger';
        paymentText = 'Sem pagamento';
        paymentCondition = false;
        elementsDisplay = 'none';
    } else {
        iconTag = 'check_box';
        classRemove = 'bg-danger';
        classAdd = 'bg-success';
        paymentText = 'Com pagamento';
        paymentCondition = true;
        elementsDisplay = 'block';
    }

    iconePagamento.innerHTML = iconTag;
    bgIconePagamento.classList.remove(classRemove);
    bgIconePagamento.classList.add(classAdd);
    descricaoPagamento.value = paymentText;
    inputPagamento.value = paymentCondition;

    ['pessoa', 'forma-pagamento'].forEach(key => {
        document.querySelector(`#label-${key}`).style.display = elementsDisplay;
        document.querySelector(`#select-${key}`).style.display = elementsDisplay;

    });
}

function selecionaCategoria() {
    var selectCategorie = document.querySelector('#select-categoria');   
    var optionSelected = selectCategorie.selectedOptions[0];
    selectCategorie.style.color = 'white';
    selectCategorie.style.backgroundColor = optionSelected.style.backgroundColor;   
}


function validarCampo(element) {
    
}


function enviarFormulario() {
    var validated = true;

    var element;

    var elementsIds = ['input-nome', 'select-categoria', 'input-valor', 'input-vencimento'];
    if (document.querySelector('#input-pagamento').value = 'true') {
        elementsIds.push('select-pessoa');
        elementsIds.push('select-forma-pagamento');
    }

    elementsIds.forEach((elementId) => {
        element = document.querySelector(`#${elementId}`);
        if (!element.value) {
            element.classList.remove('is-valid');                
            element.classList.add('is-invalid');
            validated = false;
        } else {               
            element.classList.remove('is-invalid');
            element.classList.add('is-valid');
        }
    });

    return validated;
}

// Envio Formulário
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#form-criar-despesa');
    form.addEventListener('submit', function(event) {
        if (!enviarFormulario()) {
            event.preventDefault();
        }
    });
});
