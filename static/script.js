const candidatoBtn = document.querySelectorAll('[data-tipo="candidato"]');

candidatoBtn.forEach((btn) => {
    btn.addEventListener('click', (event) => {
        candidatoBtn.forEach((img) => {
            img.classList.remove('selecionado');
        });

        event.target.classList.add('selecionado');
        document.querySelector('input[name="candidato"]').value = event.target.getAttribute('data-candidato');
    });
});