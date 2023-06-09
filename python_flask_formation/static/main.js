let genreSelect = document.querySelector('#main > nav select')
genreSelect.addEventListener('change', evt => {
    window.location.href = '/genre/'+evt.target.value;
})