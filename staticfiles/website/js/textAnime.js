// Wrap every letter in a span
var textWrapper = document.querySelector('.anime3');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

window.onscroll(anime.timeline({loop: true})
    .add({
        targets: '.anime3 .letter',
        opacity: [0,1],
        easing: "easeInOutQuad",
        duration: 2250,
        dealy: (el, i) => 1000 * (i+1)
    }).add({
        targets: '.anime3',
        opacity: 0,
        duration: 1000,
        easing: "easeInOutExpo",
        delay: 1000
    })
)
