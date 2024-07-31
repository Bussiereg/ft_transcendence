import { gameState } from "./game-state.js";

export async function registerMatches() {
    console.log('Match Result:', gameState.matchResult);

    const matches = gameState.matchResult.map(match => ({
        player1: match.player1,
        player2: match.player2,
        score1: match.score1,
        score2: match.score2,
        timestamp: match.timestamp || Date.now()
    }));

    try {
        // Send the match data to the server
        const response = await fetch('/api/register_matches/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() // Include CSRF token for security
            },
            body: JSON.stringify({ matches, tournament_id: gameState.tournamentId })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log('Server response:', result);

        if (result.success) {
            const txHash = result.tx_hash;
            const etherscanUrl = `https://sepolia.etherscan.io/tx/${txHash}`;
            alert(`Matches registered successfully! Transaction Hash: ${txHash}`);

            document.getElementById('transaction-info').innerHTML = 
                `Transaction Hash: <a href="${etherscanUrl}" target="_blank">${txHash}</a>`;
        } else {
            alert('Error registering matches: ' + result.error);
        }
    } catch (error) {
        console.error(error);
        alert('Error registering matches.');
    }
}

// Helper function to get CSRF token for security
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 10) === 'csrftoken=') {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}