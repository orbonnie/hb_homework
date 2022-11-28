'use strict';

function colorChange(){
    const change_els = document.querySelectorAll('.color-change');
    // console.log(change_els)
    for (let el of change_els) {
        el.style.color = 'red';
    }
}

document.querySelector('.color-changer').addEventListener('click', colorChange)

document.querySelector('.number-form').addEventListener('submit', (e) => {
    e.preventDefault();

    let num = Number(document.querySelector('#number-input').value)
    let msg = 'You are good to go!';

    if (Number.isNaN(num) || num > 9) {
        msg = 'Please enter a smaller number';
    }

    document.querySelector('#formFeedback'). innerHTML = msg;
    document.querySelector('#number-input').value = '';
})
