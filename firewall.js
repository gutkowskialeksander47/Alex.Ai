// Alex.ai Ping Firewall
// Blokada pingów od wybranych użytkowników

const blockedUsers = [
  'ewelina lisowska',
  'bad_actor',
  'marek lewandowski'
];

function isPingBlocked(pingEvent) {
    const sender = (pingEvent.senderName || pingEvent.uid || '').toLowerCase();
    return blockedUsers.some(blocked => sender.includes(blocked));
}

// Główna funkcja obsługi pinga
function handlePing(pingEvent) {
    if (isPingBlocked(pingEvent)) {
        console.log(`[BLOCKED] Ping od zablokowanego użytkownika: ${pingEvent.senderName}`);
        return {
            status: 403,
            message: 'Ping zablokowany. Użytkownik nie posiada uprawnień do komunikacji z RCA.'
        };
    }

    // Normalne przetwarzanie pinga
    return {
        status: 200,
        message: 'Ping przyjęty.',
        data: processPing(pingEvent)
    };
}

// Przykład funkcji przetwarzającej pinga
function processPing(pingEvent) {
    return {
        received: true,
        from: pingEvent.senderName,
        timestamp: Date.now()
    };
}

module.exports = { handlePing };