function submitProfile(evt) {
  evt.preventDefault();

  const data = {
    name: document.querySelector('#name-field').value,
    age: document.querySelector('#age-field').value,
    job: document.querySelector('#occupation-field').value,
    salary: document.querySelector('select[name="salary"]').value,
    edu: document.querySelector('select[name="education"]').value,
    state: document.querySelector('#state-field').value,
    cityType: document.querySelector('input[name="city"]').value,
    doesGarden: document.querySelector('input[name="garden"]').value,
    tvHours: document.querySelector('select[name="tv"]').value
  };

  // make request to server to get the data
  fetch('/api/profile', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      const info = document.createElement('div');
      for (let item in data) {
        let line = document.createElement('p');
        line.innerHTML = `${item}: ${data[item]}`;
        console.log(line)
        document.querySelector('#profiles').appendChild(line);
      }
    })
  // add the data the server returns to the document
  // (you can add it to the end of the div with ID "profiles")

}

document.querySelector('#profile-form').addEventListener('submit', submitProfile);
