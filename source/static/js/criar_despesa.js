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