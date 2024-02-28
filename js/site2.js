document.addEventListener("DOMContentLoaded", function() {
    const changeInfoBtn = document.getElementById('changeInfoBtn');
    const infos = document.querySelectorAll('.info');

    let currentIndex = 0;

    changeInfoBtn.addEventListener('click', function() {
        infos[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % infos.length;
        infos[currentIndex].classList.add('active');
    });
});
