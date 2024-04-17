document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const items = document.querySelectorAll('.carousel-item');
    const itemCount = items.length;

    document.querySelector('.prev').addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : itemCount - 1;
        updateCarousel();
    });

    document.querySelector('.next').addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % itemCount;
        updateCarousel();
    });

    function updateCarousel() {
        const newTransform = `translateX(-${currentIndex * 100}%)`;
        document.querySelector('.carousel-items').style.transform = newTransform;
    }
});
