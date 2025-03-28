Popis projektu
Tento projekt slouží ke scrapingu výsledku z voleb do Poslanecké sněmovny v roce 2017 na úrovni okresů, respektive konkrétních obcí.

Instalace knihoven
Knihovny použité v kódu, jsou uloženy v souboru reqirements.txt. Ten lze (optimálně ve virtuálním prostředí) spustit následovně:

Spuštení skriptu
Spuštění souboru main.py v rámci příkazového řádku vyžaduje dva povinné argumenty: odkaz územního celku a název výsledného souboru.

Jakmile proběhne extrakce dat, budou uloženy v souboru určeného názvu.

Ukázka fungování skriptu
Výsledky hlasování pro okres Šumperk

První argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7105
Druhý argument: vysledkySUMP.csv

Spuštění skriptu:
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7105" vysledkySUMP.csv
