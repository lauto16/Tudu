// Obtener elementos del DOM
const modal = document.getElementById('myModal');
const addNoteBtn = document.getElementById('boton-add');
const closeBtn = document.getElementsByClassName('close')[0];
const saveNoteBtn = document.getElementById('saveNoteBtn');

addNoteBtn.onclick = function() {
  modal.style.display = 'block';
}

closeBtn.onclick = function() {
  modal.style.display = 'none';
}

window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
}

saveNoteBtn.onclick = function() {
  modal.style.display = 'none';
}