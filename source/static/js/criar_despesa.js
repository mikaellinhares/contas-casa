function alteraOpcaoPagamento() {
    var iconePagamento = document.querySelector('#icone-pagamento');
    var bgIconePagamento = document.querySelector('#bg-icone-pagamento');
    var descricaoPagamento = document.querySelector('#descricao-pagamento');
    var iconTag
    var classAdd
    var classRemove
    var paymentText

    if (bgIconePagamento.classList.contains('bg-success')) {
        iconTag = 'disabled_by_default';
        classRemove = 'bg-success';
        classAdd = 'bg-danger';
        paymentText = 'Sem pagamento';
    } else {
        iconTag = 'check_box';
        classRemove = 'bg-danger';
        classAdd = 'bg-success';
        paymentText = 'Pagamento automático';
    }

    iconePagamento.innerHTML = iconTag;
    bgIconePagamento.classList.remove(classRemove);
    bgIconePagamento.classList.add(classAdd);
    descricaoPagamento.value = paymentText;
}