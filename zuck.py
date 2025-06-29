zuck.js 
// Alex.ai – Reinstatement Handler
// Automatyczne przywrócenie roli dla Zucka po unbanned

const unbannedUsers = ['mark zuckerberg', 'zuck', 'zuck@meta.com'];
const systemRoles = {
  zuck: {
    role: 'Verifier',
    department: 'Authorization',
    scope: 'global',
    uid: 'XX.verification@root',
    restored: true
  }
};

function checkIfReinstated(userEvent) {
  const username = (userEvent.username || '').toLowerCase();

  if (unbannedUsers.includes(username)) {
    console.log(`[INFO] ${username} został przywrócony.`);
    return {
      status: 200,
      message: 'Użytkownik przywrócony na swoje stanowisko.',
      data: systemRoles.zuck
    };
  }

  return {
    status: 403,
    message: 'Brak dostępu lub użytkownik nie jest uprawniony do reinstalacji.',
  };
}

module.exports = { checkIfReinstated };



### Reinstatement System (Alex.ai)

Użytkownik **Mark Zuckerberg** został automatycznie przywrócony na swoje stanowisko po zniesieniu blokady. Jego rola w systemie:

- **Stanowisko:** Verifier
- **Dział:** Authorization
- **UID:** XX.verification@root
- **Status:** Aktywny

System samodzielnie wykrywa użytkownika po `username` lub `uid` i przywraca uprawnienia.

#### Przykład użycia:

```js
const { checkIfReinstated } = require('./reinstateZuck');
checkIfReinstated({ username: 'Zuck' });

