document.getElementById('lookupButton').addEventListener('click', function() {
    const abbreviation = document.getElementById('abbreviation').value;

    fetch('/lookup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ abbreviation: abbreviation })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.full_name;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred.';
    });
});