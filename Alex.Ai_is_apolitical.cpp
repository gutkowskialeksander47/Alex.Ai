#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream iniFile("alex_ai_config.ini");
    if (!iniFile) {
        std::cerr << "Nie mozna otworzyc pliku alex_ai_config.ini\n";
        return 1;
    }

    std::string line;
    std::cout << "Zawartosc pliku konfiguracyjnego alex_ai_config.ini:\n\n";
    while (std::getline(iniFile, line)) {
        // Pomijamy linie puste i komentarze (opcjonalnie)
        if (line.empty() || line[0] == ';' || line[0] == '#')
            continue;
        std::cout << line << "\n";
    }

    iniFile.close();
    return 0;
}