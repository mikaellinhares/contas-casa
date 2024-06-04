// ===== Execuções =====
// -> Abrir side-bar
document.getElementById('open_btn').addEventListener('click', function () {
  document.getElementById('sidebar').classList.toggle('open-sidebar');
});


// -> Acessar item da side-bar
document.querySelectorAll('.side-item').forEach(function (element) {
  element.addEventListener('click', function () {
    window.location.href = document.querySelector(`#${element.id} a`).href;
  })
});

// -> Desaparecer mensagens 
document.addEventListener('DOMContentLoaded', () => {
  var timeOut
  
  const messages = document.querySelectorAll('.alert');
  messages.forEach((message, index) => {
    timeOut = (index + 1) * 3000;

    // Adiciona tempo para desaparecer
    setTimeout(() => {
      message.classList.add('hidden');
    }, timeOut);

    // Remover o elemento após a transição
    message.addEventListener('transitionend', () => { message.remove(); });
  });

  setTimeout(() => {
    document.querySelector('#display-mensagens').style.display = 'none';
  }, timeOut + 1000);

});


// ===== Funções =====
function selecionarItemSidebar(sideItemId) {
  document.getElementById(sideItemId).classList.add('active');
}