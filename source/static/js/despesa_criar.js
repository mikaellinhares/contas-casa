function alteraOpcaoPagamento() {
    var iconePagamento = document.querySelector('#icone-pagamento');
    var bgIconePagamento = document.querySelector('#bg-icone-pagamento');
    var descricaoPagamento = document.querySelector('#descricao-pagamento');
    var inputPagamento = document.querySelector('#input-pagamento');
    var btnAddPessoa = document.querySelector('#btn-add-pessoa');
    
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

    btnAddPessoa.style.display = elementsDisplay;
}

function validarCampo(element) {
    let isValid = false;

    if (element.value) {
        isValid = true;

        if (element.id == 'input-vencimento') {
            const inputDate   = new Date(element.value);
            const currentDate = new Date();

            inputDate.setDate(inputDate.getDate() + 1);
            inputDate.setHours(0, 0, 0, 0);
            currentDate.setHours(0, 0, 0, 0);
            
            if (inputDate < currentDate) {
                isValid = false;
            }
        }
    }

    if (isValid) {
        element.classList.remove('is-invalid');
        element.classList.add('is-valid');
    } else {
        element.classList.remove('is-valid');
        element.classList.add('is-invalid');
    }    

    return isValid
}


function validarFormulario() {
    let elementsIds = ['input-nome', 'select-categoria', 'input-valor', 'input-vencimento'];
    if (document.querySelector('#input-pagamento').value == 'true') {
        elementsIds.push('select-pessoa');
        elementsIds.push('select-forma-pagamento');
    }

    let element;
    let validated = true;
    
    elementsIds.forEach((elementId) => {
        element = document.querySelector(`#${elementId}`);
        if (validarCampo(element) === false) {
            validated = false;
        }
    });

    return validated;
}

// Envio Formulário
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona validação do formulário ao enviar
    const form = document.querySelector('#form-criar-despesa');
    form.addEventListener('submit', function(event) {
        if (validarFormulario() === false) {
            event.preventDefault();
        }
    });

    // Adiciona validação de campos ao digitar
    var elementsIds = [
        'input-nome',
        'select-categoria',
        'input-valor',
        'input-vencimento',
        'select-pessoa',
        'select-forma-pagamento'
    ];

    elementsIds.forEach((elementId) => {
        let element = document.querySelector(`#${elementId}`);
        element.addEventListener('input', function() {
            validarCampo(element);   
        });
    });

    //
});
