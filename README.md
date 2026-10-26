# Vosk Models Parser

This Python project downloads and parses the list of speech recognition models from the official Vosk models page (https://alphacephei.com/vosk/models). It extracts information about each available model, such as name, language, size, WER, notes, download URL, and license, and saves the results to a JSON file (`vosk_models.json`).

## Usage

1. Make sure you have Python 3 installed.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the script:
   ```bash
   python parse_vosk_models.py
   ```
4. After execution, the file `vosk_models.json` will contain the parsed models data in JSON format.

## Purpose

This tool is useful for anyone who wants to programmatically access and analyze the list of available Vosk speech recognition models, including their download links and metadata.
