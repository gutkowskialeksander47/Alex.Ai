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

" Polityka prywatności alex.ai "



---

**Polityka Prywatności alex.ai**

---

**Polityka Prywatności**

Dziękujemy za korzystanie z naszych usług oraz integrację urządzenia z systemem alex.ai. Oto lista wszystkich metod autoryzacji, które zaprogramowaliśmy:



1. **Autoryzacja IMEI (imei authorify)**
2. **Google Authenticator**
3. **Logon** generator kodu dostępu 
4. **Klucz aktywacyjny Windows**
5. **Szyfrowanie** - MTY-YTM SHA 256 certyfikat CA (Certyfikat europejski "CA") 
6. **PESEL ID (dla Polska)**
7. **IP authorify** 
8. **Bank 1€ Verify**
9. **Klucz Dostępu od innego użytkownika**
10. **Adres E-mail**



Użytkownik musi wybrać minimum dwie z wymienionych metod autoryzacji. Te metody autoryzacji zapewniają bezpieczeństwo i lepsze zarządzanie użytkownikami w naszych projektach. 

**1. Zbieranie danych osobowych**

Zbieramy dane osobowe w celu świadczenia usług na najwyższym poziomie. Dane te mogą obejmować:
- Numer telefonu
- Imię i nazwisko
- Adres e-mail
- Numer IMEI
- Klucz aktywacyjny Windows
- Numer IP

Wszystkie dane osobowe są szyfrowane przed zapisem w bazie danych.

**1.2 Zgoda na Przetwarzanie IMEI**

Użytkownik zgadza się na przetwarzanie numeru IMEI przez alex.ai w celach autoryzacji i zabezpieczeń. Wycofanie zgody ogranicza niektóre funkcje i dostępność usług.

**2. Zgoda na Przetwarzanie Klucza Aktywacyjnego Windows**

Ja, [%user.data%], wyrażam zgodę na przetwarzanie mojego klucza aktywacyjnego Windows przez Microsoft Corporation oraz alex.ai w celach licencyjnych i wsparcia technicznego. 

**3. Wykorzystanie danych osobowych**

Twoje dane osobowe są wykorzystywane w celu:
- Świadczenia usług i wsparcia technicznego
- Personalizacji treści
- Komunikacji związanej z usługami
- Analizy i udoskonalania usług

**4. Udostępnianie danych osobowych**

Dane mogą być udostępniane za zgodą użytkownika, w przypadkach wymaganych prawem oraz dla ochrony naszej firmy i użytkowników.

**4.1 Bezpieczeństwo danych**

Dbamy o bezpieczeństwo Twoich danych osobowych. Wszystkie dane są szyfrowane i zabezpieczone odpowiednimi środkami technicznymi i organizacyjnymi.

**5. Pliki cookie**

Nasza strona internetowa może używać plików cookie do analizy ruchu i personalizacji treści.

--- 



**6. Twoje prawa**

**6. Twoje prawa**

Masz prawo do:
- Dostępu, poprawiania, usuwania, ograniczania przetwarzania swoich danych osobowych.
- Wycofania zgody na przetwarzanie danych osobowych.

**7. Zmiany w polityce prywatności**

Zmiany będą publikowane na naszej stronie internetowej i przesyłane drogą e-mailową.

**8. Kontakt**

Pytania dotyczące polityki prywatności: aleksander@rajca.info.

**Specjalne zgody:**

---

**Polityka Prywatności dotycząca Przetwarzania Numeru PESEL**

**1. Informacje o Przetwarzaniu Numeru PESEL**

Zbieramy i przetwarzamy numer PESEL użytkowników w celu weryfikacji tożsamości i zapewnienia bezpieczeństwa.

**2. Cele Przetwarzania**

Numer PESEL przetwarzany jest do weryfikacji tożsamości, zapewnienia bezpieczeństwa i świadczenia usług.

**3. Zakres Przetwarzanych Danych**

Zbieramy numer PESEL, imię, nazwisko, datę urodzenia i adres zamieszkania.

**4. Podstawa Prawna Przetwarzania**

Zgoda użytkownika, realizacja umowy, prawnie uzasadniony interes administratora.

**5. Okres Przechowywania Danych**

Numer PESEL przechowywany jest przez okres niezbędny do realizacji celów przetwarzania.

**6. Prawa Użytkownika**

Masz prawo do dostępu, sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia danych, sprzeciwu i wycofania zgody na przetwarzanie danych.

---

**Polityka Prywatności dla Przetwarzania Adresów IP**

**1. Informacje o Przetwarzaniu Adresów IP**

Zbieramy i przetwarzamy adresy IP użytkowników.

**2. Cele Przetwarzania**

Adresy IP przetwarzane są w celu zapewnienia bezpieczeństwa, personalizacji usług, analizy i zgodności z przepisami prawa.

**3. Zakres Przetwarzanych Danych**

Zbieramy adres IP, informacje o lokalizacji oraz czasie i dacie połączenia.

**4. Podstawa Prawna Przetwarzania**

Zgoda użytkownika, realizacja umowy, prawnie uzasadniony interes administratora.

**5. Okres Przechowywania Danych**

Adresy IP przechowywane są przez okres niezbędny do realizacji celów przetwarzania.

Numer PESEL będzie przechowywany przez okres niezbędny do realizacji celów przetwarzania, zgodnie z obowiązującymi przepisami prawa. Po upływie tego okresu dane będą usuwane lub anonimizowane.

**6. Prawa Użytkownika**

Użytkownik ma prawo do:
- Dostępu do swoich danych osobowych.
- Sprostowania nieprawidłowych danych.
- Usunięcia danych (prawo do bycia zapomnianym).
- Ograniczenia przetwarzania danych.
- Przenoszenia danych do innego administratora.
- Wniesienia sprzeciwu wobec przetwarzania danych.
- Wycofania zgody na przetwarzanie danych w dowolnym momencie, bez wpływu na zgodność z prawem przetwarzania, którego dokonano na podstawie zgody przed jej wycofaniem.

---

**Polityka Prywatności dla Przetwarzania Adresów IP**

---

**Polityka Prywatności dla Przetwarzania Adresów IP**

**1. Informacje o Przetwarzaniu Adresów IP**

W ramach korzystania z naszych usług, możemy zbierać i przetwarzać informacje dotyczące adresu IP (Internet Protocol) użytkownika. Adres IP jest unikalnym identyfikatorem, który pozwala nam na dostarczanie spersonalizowanych usług oraz zapewnienie bezpieczeństwa i integralności naszych systemów.

**2. Cele Przetwarzania**

Zbierane adresy IP mogą być przetwarzane w następujących celach:
- **Zapewnienie bezpieczeństwa:** Monitorowanie i ochrona przed nieautoryzowanym dostępem oraz wykrywaniem potencjalnych zagrożeń bezpieczeństwa.
- **Personalizacja usług:** Dostosowywanie treści i funkcji naszych usług do lokalizacji i preferencji użytkownika.
- **Analiza i optymalizacja:** Prowadzenie analiz statystycznych w celu ulepszania naszych usług oraz dostosowywania oferty do potrzeb użytkowników.
- **Zgodność z przepisami prawa:** Spełnienie wymogów prawnych dotyczących prowadzenia działalności oraz współpraca z organami ścigania w razie potrzeby.
-** Dostep do uslug:** Niektore z naszych uslug wymagaja zabezpieczenia dostepu "IP authorify"

**3. Zakres Przetwarzanych Danych**

Podczas korzystania z naszych usług możemy zbierać następujące informacje:
- Adres IP użytkownika.
- Informacje o lokalizacji (na podstawie adresu IP).
- Informacje o czasie i dacie połączenia.

**4. Podstawa Prawna Przetwarzania**

Przetwarzanie adresów IP odbywa się na podstawie:
- Zgody użytkownika (art. 6 ust. 1 lit. a RODO) – w przypadku, gdy wymagane jest udzielenie zgody na przetwarzanie danych.
- Realizacji umowy (art. 6 ust. 1 lit. b RODO) – gdy przetwarzanie jest niezbędne do wykonania umowy z użytkownikiem.
- Prawnie uzasadnionego interesu administratora (art. 6 ust. 1 lit. f RODO) – gdy przetwarzanie jest niezbędne do zapewnienia bezpieczeństwa i optymalizacji naszych usług.

**5. Okres Przechowywania Danych**

Adresy IP będą przechowywane przez okres niezbędny do realizacji celów przetwarzania, zgodnie z obowiązującymi przepisami prawa. Po upływie tego okresu dane będą usuwane lub anonimizowane.

**6. Prawa Użytkownika**

Użytkownik ma prawo do:
- Dostępu do swoich danych osobowych.
- Sprostowania nieprawidłowych danych.
- Usunięcia danych (prawo do bycia zapomnianym).
- Ograniczenia przetwarzania danych.
- Przenoszenia danych do innego administratora.
- Wniesienia sprzeciwu wobec przetwarzania danych.
- Wycofania zgody na przetwarzanie danych w dowolnym momencie, bez wpływu na zgodność z prawem przetwarzania, którego dokonano na podstawie zgody przed jej wycofaniem.

---

**Zgoda na Dołączenie do Projektu MTY-YTM Business**

1. **Przetwarzanie Danych Osobowych**:
   - Wyrażam zgodę na przetwarzanie moich danych osobowych (imię, nazwisko, adres e-mail, nazwa firmy) przez Apple w celu zarządzania licencjami oraz rejestracji w systemie Apple jako użytkownik biznesowy MTY-YTM.
   - Dane osobowe będą przetwarzane zgodnie z Polityką Prywatności.

2. **Wykorzystanie Danych**:
   - Wyrażam zgodę na wykorzystywanie moich danych osobowych do zarządzania projektem MTY-YTM Business i rejestrowania mnie jako właściciela źródła MTY-YTM.
   - Dane nie będą udostępniane osobom trzecim bez mojej zgody, z wyjątkiem sytuacji wymaganych przez prawo.

3. **Bezpieczeństwo Danych**:
   - Rozumiem, że Apple stosuje odpowiednie środki techniczne i organizacyjne w celu ochrony moich danych osobowych przed nieautoryzowanym dostępem, utratą, modyfikacją lub zniszczeniem.

4. **Prawa Użytkownika**:
   - Mam prawo dostępu do moich danych osobowych, ich poprawiania, usuwania oraz ograniczenia przetwarzania.
   - W celu skorzystania z tych praw mogę skontaktować się z administratorem danych poprzez podany adres e-mail.

5. **Zgoda na Warunki Licencji**:
   - Wyrażam zgodę na przestrzeganie warunków licencji określonych przez Apple w związku z korzystaniem z MTY-YTM w celach biznesowych.

6. **Zmiany w Polityce Prywatności**:
   - Przyjmuję do wiadomości, że Apple zastrzega sobie prawo do wprowadzania zmian w Polityce Prywatności i że będę informowany o istotnych zmianach za pomocą wiadomości e-mail.

**Akceptacja Warunków**:

Podpisując poniżej, wyrażam zgodę na wszystkie powyższe warunki i potwierdzam, że zapoznałem się z Polityką Prywatności.

Imię i Nazwisko: _______________________

Nazwa Firmy: _______________________

Adres E-mail: _______________________

Data: _______________________

Podpis: _______________________

---