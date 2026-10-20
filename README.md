# Textový Analyzátor

Slovní a číselný analyzátor textu napsaný v Pythonu jako 1. projekt pro Engeto Online Python Akademii.

## Popis projektu

Tento program slouží k jednoduché textové analýze zadaných textových vzorků. Po bezpečné autentizaci uživatele umožní výběr jednoho z dostupných textů a provede jeho kompletní rozbor (počet slov, délky slov, čísla v textu a jejich součet) včetně grafického znázornění.

## Klíčové funkce

* **Autentizace uživatele:** Přihlášení registrovaným uživatelským jménem a heslem.
* **Dynamické načítání textů:** Program funguje univerzálně pro libovolný počet uložených textů (zjišťováno pomocí `len()`).
* **Robustní validace vstupů:** Bezpečná kontrola uživatelské volby (pouze platná čísla v dostupném rozsahu). V případě neplatného vstupu program zobrazí varování a bezpečně se ukončí.
* **Textová analýza:**
  * Celkový počet slov v textu.
  * Počet slov začínajících velkým písmenem.
  * Počet slov napsaných celkově velkými písmeny.
  * Počet slov napsaných celkově malými písmeny.
  * Počet číselných řetězců a výpočet jejich celkového součtu.
* **Sloupcový graf:** Přehledný textový graf četnosti délek slov zarovnaný do sloupců pomocí metody `.ljust()`.

## Požadavky a spuštění

Ke spuštění projektu potřebujete mít nainstalovaný Python (verze 3.x).

### Spuštění skriptu:

1. Otevřete terminál ve složce s projektem.
2. Spusťte skript příkazem:
   ```bash
   python main.py
3. Zadejte přihlašovací jméno a heslo (např. bob / 123).
4. Zvolte číslo textu k analýze podle zobrazené nabídky.

## Ukázka výstupu

Enter the username: bob
Enter the password: 123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers: 85
----------------------------------------
LEN|  OCCURRENCES   |NR.
----------------------------------------
1  | *              | 1
2  | ***            | 3
3  | **********     | 10
4  | ***********    | 11
5  | **********     | 10
