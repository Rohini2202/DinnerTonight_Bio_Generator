async function generateBio() {
    const career = document.getElementById('career').value;
    const personality = document.getElementById('personality').value;
    const interests = document.getElementById('interests').value;

    const response = await fetch('/generate-bio', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ career, personality, interests })
    });

    const data = await response.json();
    document.getElementById('bioResult').innerText = data.bio;
}
