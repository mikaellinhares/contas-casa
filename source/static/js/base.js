document.getElementById('open_btn').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('open-sidebar');
  });

function selecionarItemSidebar(sideItemId) {
    let sideItem = document.getElementById(sideItemId);
    sideItem.classList.add('active');
}