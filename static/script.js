async function generateBio() {
    const career = document.getElementById('career').value;
    const personality = document.getElementById('personality').value;
    const interests = document.getElementById('interests').value;
    const relationship = document.getElementById('relationship').value;

    try {
        const response = await fetch('/generate-bio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ career, personality, interests, relationship}),
        });

        const result = await response.json();
        document.getElementById('result').innerText = result.bio;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Failed to generate bio.';
    }
};

