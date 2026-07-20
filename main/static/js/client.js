
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.project-card');
    const prev = document.querySelector('.arrow.prev');
    const next = document.querySelector('.arrow.next');

    let current = 0;

    function showCard(index){
        cards.forEach((card,i) => {
            card.classList.remove('active');
            if(i === index) card.classList.add('active');
        });
    }

    prev.addEventListener('click', () => {
        current = (current - 1 + cards.length) % cards.length;
        showCard(current);
    });

    next.addEventListener('click', () => {
        current = (current + 1) % cards.length;
        showCard(current);
    });

    // show first card on load
    showCard(current);
});
