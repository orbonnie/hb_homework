'use strict';

/** ********************
 Make an Event Handler
********************* */

document.querySelector('#popup-alert-button').addEventListener('click', () => {
  alert('Here is your popup');
})
/** ***********************
Practice Your Times Tables
************************ */


document.querySelector('#multiplying-form').addEventListener('submit', (e) => {
  e.preventDefault();

  const values = [];
  const mults = Number(document.querySelector('#mults-of').value);
  const max = Number(document.querySelector('#max').value);

  let curr = mults;

  while (curr <= max) {
    values.push(curr);
    curr += mults;
  }
  const results = document.createElement('p');
  results.innerHTML = values;
  document.querySelector('#multiplying-form').after(results)

  document.querySelector('#mults-of').selectedIndex = 0;
  document.querySelector('#max').value = '';

})

/** **************
An Agreeable Form
*************** */

// Your Code Here

/** ****************
Five colored primes
***************** */

const PRIME_COLORS = ['orange', 'midnightblue', 'darkgoldenrod', 'green', 'purple'];

// Your Code Here

/** *********
Got Puppies?
********** */

// NOTE: DO NOT CHANGE THE CODE OF THIS FUNCTION
function showPuppies(results) {
  // get the URL for the puppy photo out of the results object
  const puppyURL = results.url;
  const puppyDiv = document.querySelector('#puppies-go-here');
  // clear anything currently in the div
  puppyDiv.innerHTML = null;
  // add the img element
  puppyDiv.insertAdjacentHTML('beforeend', `<img src=${puppyURL} alt="puppy-image">`);
}

// Your Code Here
