#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

// Poziomy zaufania
enum TrustLevel {
    GREEN,      // Wysokie zaufanie
    ORANGE,     // Średnie zaufanie
    RED         // Niskie zaufanie
};

// Struktura użytkownika
struct User {
    string username;
    TrustLevel level;
};

// Mapa użytkowników
unordered_map<string, User> users;

// Funkcja pomocnicza: konwersja poziomu zaufania na tekst
string trustLevelToString(TrustLevel level) {
    switch (level) {
        case GREEN: return "Zielony";
        case ORANGE: return "Pomarańczowy";
        case RED: return "Czerwony";
        default: return "Nieznany";
    }
}

// Dodaj użytkownika
void addUser(const string& username, TrustLevel level) {
    users[username] = User{username, level};
    cout << "Dodano użytkownika: " << username << " z poziomem zaufania: " << trustLevelToString(level) << endl;
}

// Zmień poziom zaufania
void updateTrustLevel(const string& username, TrustLevel newLevel) {
    if (users.find(username) != users.end()) {
        users[username].level = newLevel;
        cout << "Zaktualizowano poziom zaufania dla " << username << " na " << trustLevelToString(newLevel) << endl;
    } else {
        cout << "Użytkownik nie istnieje." << endl;
    }
}

// Wyświetl wszystkich użytkowników
void listUsers() {
    cout << "\nLista użytkowników:" << endl;
    for (const auto& [key, user] : users) {
        cout << "- " << user.username << " | Poziom zaufania: " << trustLevelToString(user.level) << endl;
    }
}

int main() {
    // Przykładowe operacje
    addUser("jan_kowalski", GREEN);
    addUser("anna_nowak", ORANGE);
    addUser("adam_malinowski", RED);

    updateTrustLevel("anna_nowak", GREEN);

    listUsers();

    return 0;
}