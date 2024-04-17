// Drag and Drop Functionality
const furnitureItems = document.querySelectorAll('.furniture-item');
const roomCanvas = document.getElementById('room-canvas');

furnitureItems.forEach(item => {
    item.addEventListener('dragstart', dragStart);
    item.addEventListener('dragend', dragEnd);
});

roomCanvas.addEventListener('dragover', dragOver);
roomCanvas.addEventListener('drop', drop);

function dragStart(e) {
    e.dataTransfer.setData('text/plain', null);
    setTimeout(() => {
        e.target.classList.add('dragging');
    }, 0);
}

function dragEnd(e) {
    e.target.classList.remove('dragging');
}

function dragOver(e) {
    e.preventDefault();
}

function drop(e) {
    e.preventDefault();
    const furniture = document.querySelector('.dragging');
    furniture.classList.remove('dragging');

    // Create a new copy of the furniture item
    const furnitureCopy = furniture.cloneNode(true);
    furnitureCopy.style.position = 'absolute';
    furnitureCopy.style.cursor = 'move';
    furnitureCopy.tabIndex = 0; // Make the furniture item focusable

    const furnitureRect = furnitureCopy.getBoundingClientRect();
    const canvasRect = roomCanvas.getBoundingClientRect();
    furnitureCopy.style.left = `${e.clientX - canvasRect.left - furnitureRect.width / 2}px`;
    furnitureCopy.style.top = `${e.clientY - canvasRect.top - furnitureRect.height / 2}px`;

    roomCanvas.appendChild(furnitureCopy);

    // Add event listeners to the new copy for drag and drop
    furnitureCopy.addEventListener('dragstart', dragStart);
    furnitureCopy.addEventListener('dragend', dragEnd);

    // Add keydown event listener for deleting the furniture item
    furnitureCopy.addEventListener('keydown', handleKeyDown);
}

function handleKeyDown(e) {
    if (e.key === 'd') {
        const furnitureItem = e.target;
        furnitureItem.remove();
    }
}