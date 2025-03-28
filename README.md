# Volební Scraper – Poslanecká sněmovna ČR 2017

Tento projekt slouží ke scrapování výsledků voleb do Poslanecké sněmovny Parlamentu České republiky, konkrétně z oficiálního webu [volby.cz](https://www.volby.cz). Skript načte volební data jednotlivých obcí v konkrétním okrese, získá základní statistiky a hlasy pro jednotlivé strany a uloží je do CSV souboru.

## Požadavky

Nejprve je třeba nainstalovat závislosti pomocí `requirements.txt`:

```bash
pip install -r requirements.txt
```


## Jak spustit skript

Skript spustíte jednoduše z příkazové řádky:

```bash
python main.py
```

Výstupní CSV soubor `vysledky.csv` bude obsahovat:

- Kód obce
- Název obce
- Počet voličů
- Počet vydaných obálek
- Počet platných hlasů
- Hlasy pro jednotlivé strany

## Ukázka použití

Například při spuštění s URL pro okres **Šumperk**:

```python main.py  "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4206", "vysledkySUMP.csv"
```

Skript projde všechny obce v okrese Šumperk, načte jejich detailní volební výsledky a zapíše je do `vysledkySUMP.csv`.

## Výstupní ukázka (CSV)

| Kód obce | Název obce | Voliči | Vydané obálky | Platné hlasy | Občanská demokratická strana || ... |
|----------|------------|--------|----------------|---------------|----------------------------|------|
| 525588   | Bludov     | 2504   | 1632           | 1615          | 178                        | .....|

## Autor

Tento nástroj byl vytvořen pro edukační a analytické účely. Data pochází z veřejně dostupného webu volby.cz.
