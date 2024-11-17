
async function generateBio() {
    const career = document.getElementById('career')?.value || '';
    const personality = document.getElementById('personality')?.value || '';
    const interests = document.getElementById('interests')?.value || '';
    const relationship = document.getElementById('relationship')?.value || '';
    console.log({ career, personality, interests, relationship });
    try {
        const response = await fetch('/generate-bio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                career,
                personality,
                interests,
                relationship
            }),
        });

        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        const result = await response.json();
        document.getElementById('bioResult').innerText = result.bio;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('bioResult').innerText = 'Failed to generate bio.';
    }
