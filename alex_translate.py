# alex_translate.py

def translate_text(text, target_lang):
    # MOCK funkcja tłumacząca – do podmiany na API Google Translate
    # Wersja symboliczna, zgłaszająca potrzebę wsparcia wielojęzyczności dla alex.ai/global
    return f"[TŁUMACZENIE DLA '{target_lang}' NIEZREALIZOWANE – ZAPOTRZEBOWANIE DO GOOGLE: {text}]"

def main():
    print("🌐 Alex.ai – Global Translation Request Console")
    source_text = input("Wpisz tekst do przetłumaczenia: ")
    target_language = input("Wpisz docelowy język (np. 'en' dla angielskiego, 'de' dla niemieckiego): ")

    translated_text = translate_text(source_text, target_language)
    print(f"\n📄 Przetłumaczony tekst: {translated_text}")

if __name__ == "__main__":
    main()


from googletrans import Translator

def translate_diary(filename, target_lang):
    translator = Translator()
    output_lines = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print(f"📘 Tłumaczę plik '{filename}' na język: {target_lang}...\n")

        for line in lines:
            if line.strip():  # pomijaj puste linie
                translation = translator.translate(line.strip(), dest=target_lang)
                output_lines.append(translation.text)
            else:
                output_lines.append('')  # zachowaj puste linie

        output_filename = f"translated_{target_lang}_{filename}"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in output_lines:
                output_file.write(line + '\n')

        print(f"✅ Gotowe! Przetłumaczony plik zapisany jako '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Nie znaleziono pliku: {filename}")
    except Exception as e:
        print(f"❌ Błąd podczas tłumaczenia: {str(e)}")

def main():
    print("📝 Alex.ai – Tłumaczenie pamiętnika")
    filename = input("Ogólny : ")
    target_lang = input(".EN (np. en, de, fr): ")

    translate_diary(filename, target_lang)

if __name__ == "__main__":
    main()