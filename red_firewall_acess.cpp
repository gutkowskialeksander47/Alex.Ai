// RedFirewall - Authorization Roles Structure // Author: Aleksander Rajca // License ID: JRAR-1708MAI

#include <string> #include <vector>

struct Role { std::string name; std::string tag; std::string description; };

std::vector<Role> globalRoles = { 

{"CEO", "@Zuck", "Plan projektu: Dropbox, Microsoft, Audi, Google"}, 

{"CEO", "@Musk", "Licencjodawca i operator technologiczny"},
 
{"Redaktor", "@RE", "Nadzór nad artykułami o alex.ai w czasie rzeczywistym"}, 

{"Sponsor", "", "Sponsorzy mają prywatny list w Samsung Notes"},

 {"Moderator", "@M", "Moderacja w systemie"}, 

{"Globalny Moderator", "@GM", "Globalna moderacja treści"}, 

{"Deweloper", "@D", "Deweloper środowiska Alex AI"}, 

{"Junior Admin", "@J", "Pomoc techniczna i rejestracja"},

 {"Head Admin", "@H", "Nadzór systemowy"}, 

{"Właściciel", "@W", "Właściciel danych lub systemu"},

 {"Globalny Administrator", "@GA", "Globalna administracja systemem"}, 

{"Internal Administrator", "@IA", "Administrator wewnętrzny projektu"},

 {"Query", "Query", "Uprawnienie do przetwarzania danych i zapytań"}, 

{"Marketing Zone", "@MA zone", "Zarząd Marketingu i strefy SQLMZ"}, 

{"Google Operator", "", "Operator projektu Google"}, 

{"Meta Admin", "", "Global Internal Administrator Meta"},

 {"Opiekun Projektu", "Bonus RPK", "Opieka merytoryczna nad projektem"}, 
{"Nvidia", "", "Zarząd wsparcia sprzętowego"}, {"Intel Admin", "", "Administrator generacji technologii"}, 

{"Microsoft Admin", "", "Administrator systemów Microsoft"},

 {"NASA Admin", "", "Administrator danych satelitarnych i kosmicznych"},

 {"Saturn/MediaMarkt", "", "Zarząd zasobów elektronicznych"}, 

{"Adidas", "", "Zarząd treningu personalnego"}, 

{"Nike", "", "Zarząd odzieży i sprzętu sportowego"}, {"Decathlon", "", "Zarząd sprzętu sportowego i wyczynowego"}, 

{"Tauron", "", "Zamknięte środowisko technologiczne"},

 {"Europa Admin", "", "Administrator danych regionalnych"}, 
{"Schengen", "", "Zarząd granic Schengen"}, {"USA", "", "Administrator systemów USA"}, {"Asia", "", "Administrator systemów azjatyckich"},

 {"Africa", "", "Administrator systemów afrykańskich"}, 
{"Australia", "", "Administrator systemów australijskich"},
 {"Zoll", "", "Administrator celny i graniczny"}, {"InterPol", "", "Wsparcie IT i HR międzynarodowe"}, 
{"Police", "", "Administrator Policji"}, {"Copywrite", "", "Ochrona praw autorskich"} };

// Można dalej rozwijać jako json, xml, albo interfejs API dla Red Firewall

