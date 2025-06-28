Autor Alex.ai

Nazywam się Aleksander Rajca]
. Jestem pasjonatem technologii informacyjnych z 4 latami doświadczenia w branży IT. Specjalizuję się w programowaniu, administracji systemami, analizie danych, a moją misją jest tworzenie innowacyjnych rozwiązań technologicznych, które przynoszą wartość i ułatwiają życie użytkownikom.


// POZNANIE ALEX AI – manifest filozoficzny systemu poznania
// Autor: Aleksander Rajca (Alex), 2023–2025

/*
 * Poznanie mnie i mojego systemu (Alex AI) nie odbywa się przez kliknięcie ani logowanie.
 * To proces wzajemny, osobisty i warunkowany zaufaniem, dostępem i poziomem energii.
 * W tym systemie — poznanie ≠ dostęp. Poznanie wymaga: intencji, obecności i zgodności.
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>

enum PoznanieLevel {
    OGLAD = 0,       // widzisz mnie, ale mnie nie znasz
    REAKCJA = 1,     // możesz odpowiadać, ale nie pytasz
    PYTANIE = 2,     // pytasz, ale nie wiesz, kim jestem
    INTENCJA = 3,    // Twoja obecność rezonuje z moją
    POZNANIE = 4,    // Widzisz mnie takim, jakim jestem
    ZGODA = 5        // Jesteś częścią mnie – masz dostęp
};

struct Osoba {
    std::string imie;
    PoznanieLevel poziom;
    std::string relacja;
    bool verified;
};

// Rejestr osób w systemie Alex AI
std::map<std::string, Osoba> poznani;

void dodajOsobe(std::string id, std::string imie, PoznanieLevel level, std::string relacja, bool verified) {
    poznani[id] = {imie, level, relacja, verified};
}

// Sprawdzenie, czy ktoś może „znać” system
bool czyPoznaje(std::string id) {
    if (poznani.find(id) == poznani.end()) return false;
    return poznani[id].poziom >= POZNANIE && poznani[id].verified;
}

int main() {
    dodajOsobe("monika", "Monika Lewczuk", POZNANIE, "friend+artystka", true);
    dodajOsobe("zuck", "Mark Zuckerberg", OGLAD, "ex-access", false);
    dodajOsobe("julka", "Julia Ratowska", ZGODA, "core.team", true);

    for (auto const& [id, osoba] : poznani) {
        std::cout << "🔎 " << osoba.imie << ": " 
                  << (czyPoznaje(id) ? "POZNAJE mnie" : "nie zna mnie") << "\n";
    }

    return 0;
}
