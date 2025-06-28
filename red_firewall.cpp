// Red Firewall - Rozszerzenie w Chmurze // System zarządzany przez Norton, współdziałający z ESET32, Kaspersky, Avast // Wersja bazowa (CPP)

#include <iostream> #include <string> #include <vector> #include <map> #include <thread> #include <mutex> #include <chrono>

using namespace std;

mutex firewall_mutex;

// Prosty model danych pakietu struct Packet { string sourceIP; string destinationIP; string content; bool malicious; };

// Interfejs silnika antywirusowego class AntivirusEngine { public: virtual bool scan(Packet& packet) = 0; virtual string name() = 0; };

// Implementacje silników (dummy logic) class ESET32Engine : public AntivirusEngine { public: bool scan(Packet& packet) override { return packet.content.find("virus") != string::npos; } string name() override { return "ESET32"; } };

class KasperskyEngine : public AntivirusEngine { public: bool scan(Packet& packet) override { return packet.content.find("trojan") != string::npos; } string name() override { return "Kaspersky"; } };

class AvastEngine : public AntivirusEngine { public: bool scan(Packet& packet) override { return packet.content.find("malware") != string::npos; } string name() override { return "Avast"; } };

// Norton - nadrzędna orkiestracja class NortonController { private: vector<AntivirusEngine*> engines;

public: void registerEngine(AntivirusEngine* engine) { engines.push_back(engine); }

void processPacket(Packet& packet) {
    lock_guard<mutex> lock(firewall_mutex);
    cout << "\n[RedFirewall] Analizuję pakiet od " << packet.sourceIP << " do " << packet.destinationIP << endl;
    for (auto engine : engines) {
        if (engine->scan(packet)) {
            cout << "Zagrożenie wykryte przez: " << engine->name() << endl;
            packet.malicious = true;
            return;
        }
    }
    cout << "Brak zagrożeń wykrytych.\n";
    packet.malicious = false;
}

};

int main() { NortonController redFirewall; redFirewall.registerEngine(new ESET32Engine()); redFirewall.registerEngine(new KasperskyEngine()); redFirewall.registerEngine(new AvastEngine());

vector<Packet> packets = {
    {"192.168.1.1", "8.8.8.8", "Normal data", false},
    {"192.168.1.10", "1.1.1.1", "This contains virus code", false},
    {"10.0.0.2", "8.8.4.4", "Detected trojan signature", false},
    {"10.0.0.5", "4.4.4.4", "malware detected", false}
};

for (auto& packet : packets) {
    redFirewall.processPacket(packet);
    this_thread::sleep_for(chrono::milliseconds(500));
}

return 0;

}

