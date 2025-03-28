
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, features='html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování: {e}")
        sys.exit(1)

def scrape_voting_results(base_url, output_file):
    soup = fetch_and_parse(base_url)
    tables = soup.find_all('table')

    municipalities = []
    seen_codes = set()

    for table in soup.find_all('table'):
        rows = table.find_all('tr')
        if not rows or len(rows) < 3:
            continue

        headers = rows[0].find_all('th')
        if not headers or 'Obec' not in headers[0].text:
            continue

        for row in rows[2:]:
            cells = row.find_all('td')
            if len(cells) < 3:
                continue

            code = cells[0].text.strip()
            if code in seen_codes:
                continue
            seen_codes.add(code)

            name = cells[1].text.strip()
            link_tag = cells[0].find('a')
            if link_tag:
                href = link_tag.get('href')
                full_url = 'https://volby.cz/pls/ps2017nss/' + href
                municipalities.append((code, name, full_url))

    data = []

    for code, name, link in municipalities:
        print(f"Zpracovávám: {name} ({code})")
        sub_soup = fetch_and_parse(link)

        tables = sub_soup.find_all('table')
        if len(tables) < 1:
            continue

        summary_table = tables[0]

        voters = summary_table.find(name='td', headers='sa2')
        envelopes = summary_table.find(name='td', headers='sa3')
        valid_votes = summary_table.find(name='td', headers='sa6')

        results = {
            'Kód obce': code,
            'Název obce': name,
            'Voliči': voters.text.strip() if voters else '',
            'Vydané obálky': envelopes.text.strip() if envelopes else '',
            'Platné hlasy': valid_votes.text.strip() if valid_votes else ''
        }

        for header_prefix in ['t1', 't2']:
            party_names = sub_soup.find_all(name='td', headers=f'{header_prefix}sa1 {header_prefix}sb2')
            party_votes = sub_soup.find_all(name='td', headers=f'{header_prefix}sa2 {header_prefix}sb3')

            for name_cell, vote_cell in zip(party_names, party_votes):
                party_name = name_cell.text.strip()
                vote_count = vote_cell.text.strip()
                results[party_name] = vote_count

        data.append(results)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Hotovo! Výsledky uloženy do {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python scraper.py <URL_uzemni_celek> <vystupni_soubor.csv>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]
    scrape_voting_results(url, output_file)