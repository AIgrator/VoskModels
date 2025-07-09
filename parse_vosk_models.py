import requests
from bs4 import BeautifulSoup
import json

def parse_vosk_models():
    url = "https://alphacephei.com/vosk/models"
    print(f"Sending request to {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error requesting the page: {e}")
        return
    print("Page received successfully. Starting parsing...")
    soup = BeautifulSoup(response.content, 'html.parser')
    table_body = soup.find('tbody')
    if not table_body:
        print("Failed to find the models table on the page.")
        return
    rows = table_body.find_all('tr')
    models_list = []
    current_title = None
    for row in rows:
        cells = row.find_all('td')
        # Detect language title row (first cell is <strong> and no link)
        if len(cells) > 0 and cells[0].find('strong') and not cells[0].find('a'):
            current_title = cells[0].get_text(strip=True)
            continue
        if len(cells) < 2:
            continue
        link_tag = cells[0].find('a')
        if not link_tag or not link_tag.get('href'):
            continue
        try:
            model_name = link_tag.text.strip()
            download_url = link_tag['href'].strip()
            language_short = "unknown"
            name_parts = model_name.split('-')
            for part in name_parts:
                if len(part) == 2 and part.isalpha():
                    language_short = part
                    break
            size_text = cells[1].text.strip() if len(cells) > 1 else ""
            wer_text = cells[2].text.strip() if len(cells) > 2 else ""
            notes_text = cells[3].text.strip() if len(cells) > 3 else ""
            license_text = cells[4].text.strip() if len(cells) > 4 else ""
            model_data = {
                "name": model_name,
                "language": language_short,
                "size": size_text,
                "wer": wer_text,
                "notes": notes_text,
                "download_url": download_url,
                "license": license_text,
                "title": current_title
            }
            models_list.append(model_data)
        except Exception as e:
            print(f"Failed to process row: {row.text.strip()}. Error: {e}")
            continue
    output_filename = "vosk_models.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(models_list, f, ensure_ascii=False, indent=4)
    print(f"Parsing complete. Found {len(models_list)} models.")
    print(f"Results saved to file: {output_filename}")

if __name__ == "__main__":
    parse_vosk_models()

