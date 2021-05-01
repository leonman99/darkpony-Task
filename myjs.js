function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}


var ul = document.querySelector('#quotesli');
// console.log(Object.keys(ul).length);
console.log(ul.textContent);
// for (var i = ul.children.length; i >= 0; i--) {
//     ul.appendChild(ul.children[Math.random() * i | 0]);
// }
shuffleArray(ul.textContent);
console.log(ul.textContent);