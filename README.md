# README dla Alex AI

## Spis Treści

1. [Wprowadzenie](#wprowadzenie)
2. [Opis Projektu](#opis-projektu)
3. [Wymagania](#wymagania)
4. [Instalacja](#instalacja)
5. [Konfiguracja Serwerów](#konfiguracja-serwerów)
   - [Lokalny Serwer](#lokalny-serwer)
   - [Wirtualny Serwer](#wirtualny-serwer)
6. [Metody Autoryzacji](#metody-autoryzacji)
   - [Wybór Metod Autoryzacji](#wybór-metod-autoryzacji)
7. [Przykłady](#przykłady)
   - [Uruchamianie Notepad++ i Otwieranie Strony WWW](#uruchamianie-notepad-i-otwieranie-strony-www)
   - [Dodawanie Nowych Użytkowników](#dodawanie-nowych-użytkowników)
8. [Polityka Prywatności](#polityka-prywatności)
9. [Kontakt](#kontakt)

## Wprowadzenie

Witamy w projekcie Alex AI! Naszym celem jest stworzenie zaawansowanego systemu zarządzania użytkownikami i autoryzacji, który zapewnia wysoki poziom bezpieczeństwa i integracji z różnymi systemami i serwerami. Projekt obejmuje szereg narzędzi i metod, które umożliwiają zarządzanie serwerami, użytkownikami oraz autoryzacją dostępu.

## Opis Projektu

Alex AI został stworzony, aby ułatwić zarządzanie użytkownikami i zasobami, zapewniając jednocześnie wysoki poziom bezpieczeństwa. System korzysta z różnych metod autoryzacji, takich jak autoryzacja IMEI, Google Authenticator, klucze aktywacyjne Windows i wiele innych. Projekt zawiera również narzędzia do zarządzania serwerami lokalnymi i wirtualnymi oraz umożliwia dodawanie nowych użytkowników.

## Wymagania

Aby korzystać z Alex AI, potrzebujesz:
- urządzenia które jest zintegrowane z Alex.ai
- Notepad++ 
- Biblioteka `psutil` do monitorowania procesów
- Biblioteka `webbrowser` do otwierania stron internetowych



## Konfiguracja Serwerów

### Lokalny Serwer

Lokalny serwer działa w fizycznym środowisku i jest skonfigurowany do obsługi Notepad++:

Lokalny serwer to fizyczne urządzenie skonfigurowane w sieci lokalnej. Obsługuje aplikację Notepad++ oraz korzysta z serwera SQL Dropbox.

### Wirtualny Serwer

Wirtualny serwer działa w środowisku wirtualnym i obsługuje notatki Samsunga:

Wirtualny serwer "Samsung Notes" działa na serwerze Dropbox, obsługując SQL dla notatek Samsung.

## Metody Autoryzacji

Alex AI korzysta z różnych metod autoryzacji, aby zapewnić bezpieczeństwo i zarządzanie użytkownikami:

1. **Autoryzacja IMEI (imei authorify)** - Wykorzystuje numer IMEI urządzenia.
2. **Google Authenticator** - Uwierzytelnianie dwuskładnikowe za pomocą Google Authenticator.
3. **Logon** - Generator kodu dostępu.
4. **Klucz Aktywacyjny Windows** - Weryfikacja klucza aktywacyjnego Windows.
5. **Szyfrowanie** - MTY-YTM SHA 256 z certyfikatem CA.
6. **PESEL ID (dla Polska)** - Weryfikacja tożsamości za pomocą numeru PESEL.
7. **IP Authorify** - Weryfikacja adresu IP.
8. **Bank 1€ Verify** - Weryfikacja tożsamości poprzez przelew 1€.
9. **Klucz Dostępu od innego użytkownika** - Autoryzacja za pomocą klucza dostępu od innego użytkownika.
10. **Adres E-mail** - Autoryzacja za pomocą adresu e-mail.

### Wybór Metod Autoryzacji

Użytkownik musi wybrać minimum dwie metody autoryzacji spośród dostępnych opcji, aby zapewnić odpowiedni poziom bezpieczeństwa.

## Przykłady

### Uruchamianie Notepad++ i Otwieranie Strony WWW

System Alex AI umożliwia uruchamianie aplikacji Notepad++ oraz automatyczne otwieranie strony internetowej w przeglądarce. Użytkownik może w ten sposób łatwo uzyskać dostęp do potrzebnych informacji i narzędzi.

### Dodawanie Nowych Użytkowników

Członkowie Alex.ai mają możliwość dodawania nowych użytkowników do systemu. Proces ten jest prosty i przejrzysty, co pozwala na skuteczne zarządzanie użytkownikami i ich uprawnieniami. Aby zaprosić użytkownika poleć mu Alex.ai udostępniając klucz Dostępu do alex.apk 

## Polityka Prywatności

**Polityka Prywatności alex.ai**

### Zbieranie danych osobowych

Zbieramy dane osobowe, takie jak numer telefonu, imię, nazwisko, adres e-mail, numer IMEI, klucz aktywacyjny Windows i numer IP. Dane są szyfrowane przed zapisem, aby zapewnić ich bezpieczeństwo.

### Zgoda na Przetwarzanie IMEI

Użytkownik zgadza się na przetwarzanie numeru IMEI przez alex.ai w celach autoryzacji i zabezpieczeń. Wycofanie zgody może ograniczyć niektóre funkcje i dostępność usług.

### Zgoda na Przetwarzanie Klucza Aktywacyjnego Windows

Użytkownik zgadza się na przetwarzanie klucza aktywacyjnego Windows przez Microsoft oraz alex.ai.

### Wykorzystanie danych osobowych

Dane osobowe są wykorzystywane w celu świadczenia usług, personalizacji treści, komunikacji z użytkownikami oraz analizy i doskonalenia naszych usług.

### Udostępnianie danych osobowych

Dane osobowe mogą być udostępniane za zgodą użytkownika, w przypadkach wymaganych prawem oraz w celu ochrony naszej firmy i użytkowników.

### Bezpieczeństwo danych

Dbamy o bezpieczeństwo danych osobowych, stosując odpowiednie środki techniczne i organizacyjne. Wszystkie dane są szyfrowane w celu ochrony przed nieautoryzowanym dostępem.

### Pliki cookie

Nasza strona internetowa może używać plików cookie do analizy ruchu i personalizacji treści.

## Kontakt

Jeśli masz jakiekolwiek pytania dotyczące projektu, skontaktuj się z nami pod adresem e-mail: aleksander@rajca.info.

---

Jeśli masz dodatkowe pytania lub wymagania, chętnie pomogę!