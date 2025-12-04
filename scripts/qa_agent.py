
import json
import pandas as pd
import openpyxl
import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def read_excel(path):
    df = pd.read_excel(path)
    return df.to_string()

def analyse_ticket_with_openai(text):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Tu es un agent QA. Analyse ce ticket et renvoie un JSON structuré avec : type, criticité, résumé, équipe cible."},
                {"role": "user", "content": text}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    text = read_excel(file)
    print("=== JSON PRODUIT PAR L'AGENT QA ===")
    print(analyse_ticket_with_openai(text))
