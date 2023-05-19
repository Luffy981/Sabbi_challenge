document.getElementById('surveyForm').addEventListener('submit', function(event) {
  event.preventDefault();
  var formData = new FormData(this);
  var data = {};

  for (var pair of formData.entries()) {
    var key = pair[0];
    var value = pair[1];

    if (data.hasOwnProperty(key)) {
      if (!Array.isArray(data[key])) {
        data[key] = [data[key]];
      }
      data[key].push(value);
    } else {
      data[key] = value;
    }
  }
  console.log(data)

  fetch('/survey/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => {
    if (response.ok) {
      window.location.href = '/survey/results';
    } else {
      throw new Error('Error al enviar las respuestas');
    }
  })
  .catch(error => {
    console.error(error);
  });
  // .then(response => response.json())
  // .then(result => {
  //   alert('Respuestas enviadas exitosamente');
  // })
  // .catch(error => {
  //   alert('Error al enviar las respuestas');
  // });
});

