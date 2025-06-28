// query_netz_config.cpp
// Wewnętrzna sieć komunikacji systemu Alex AI
// System „Ty do mnie – ja do ciebie”
// System „ Ja do was - wy do mnie 
// Autor: Aleksander Rajca

#include <iostream>
#include <map>
#include <vector>
#include <string>

enum AccessLevel {
    NONE = 0,
    VIEW = 1,
    SEND = 2,
    REPLY = 3,
    ADMIN = 5,
    ROOT = 10
};

struct User {
    std::string name;
    std::string role;
    AccessLevel access;
};

struct Message {
    std::string from;
    std::string to;
    std::string content;
};

class QueryNetz {
private:
    std::map<std::string, User> users;
    std::vector<Message> history;

public:
    void registerUser(std::string id, std::string name, std::string role, AccessLevel level) {
        users[id] = {name, role, level};
    }

    bool canCommunicate(const std::string& from, const std::string& to) {
        return users[from].access >= SEND && users[to].access >= REPLY;
    }

    void sendMessage(std::string from, std::string to, std::string content) {
        if (canCommunicate(from, to)) {
            history.push_back({from, to, content});
            std::cout << "📨 [" << from << " ➝ " << to << "] " << content << "\n";
        } else {
            std::cout << " Dostęp zabroniony: " << from << " ↔ " << to << "\n";
        }
    }

    void printUsers() {
        std::cout << " Zarejestrowani użytkownicy Query.netz:\n";
        for (const auto& [id, user] : users) {
            std::cout << "- " << user.name << " (" << user.role << "), Dostęp: " << user.access << "\n";
        }
    }
};

int main() {
    QueryNetz netz;

    // Rejestracja użytkowników
    netz.registerUser("alex", "Aleksander Rajca", "CEO", ROOT);
    netz.registerUser("sandra", "Sandra Gutkowska", "Admin", CEO);
    netz.registerUser("julka", "Julia Ratowska", "Leader", SEND);
    netz.registerUser("monika", "Monika Lewczuk", "Artist", REPLY);
    netz.registerUser("zuck", "Zuck", "Blocked", NONE);

    netz.printUsers();

    // Przykładowe wiadomości
    netz.sendMessage("alex", "monika", "Cześć! Pracujemy dziś z G.project?");
    netz.sendMessage("julka", "alex", "Potrzebuję dostępu do pliku SAP.");
    netz.sendMessage("zuck", "alex", "Czy mogę wrócić?");

    return 0;
}
