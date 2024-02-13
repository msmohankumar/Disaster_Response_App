document.getElementById('message-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const message = document.getElementById('message-input').value;
    const response = await fetch('/result', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();
    const resultContainer = document.getElementById('result-container');
    const classificationResults = document.getElementById('classification-results');
    resultContainer.style.display = 'block';
    classificationResults.innerHTML = '';
    for (const [category, value] of Object.entries(data)) {
      const li = document.createElement('li');
      li.innerHTML = `<span>${category}:</span> ${value}`;
      classificationResults.appendChild(li);
    }
  });