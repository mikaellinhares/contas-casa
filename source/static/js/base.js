// Execuções
document.getElementById('open_btn').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('open-sidebar');
  });

document.querySelectorAll('.side-item').forEach(function(element) {
  element.addEventListener('click', function () { 
    window.location.href = document.querySelector(`#${element.id} a`).href; 
  })
});

// Funções
function selecionarItemSidebar(sideItemId) {
    document.getElementById(sideItemId).classList.add('active');
}