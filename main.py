import json
import requests
from datetime import datetime

# Liste des pays
countries = [
    "AR.en", "AR.es",
    "AT.de",
    "AU.en",
    "BE.fr", "BE.nl",
    "BG.en",
    "BR.en", "BR.pt",
    "CA.en", "CA.fr",
    "CH.de", "CH.fr", "CH.it",
    "CL.en", "CL.es",
    "CN.zh",
    "CO.en", "CO.es",
    "CY.en",
    "CZ.en",
    "DE.de",
    "DK.en",
    "EE.en",
    "ES.es",
    "FI.en",
    "FR.fr",
    "GB.en",
    "GR.en",
    "HK.zh",
    "HR.en",
    "HU.en",
    "IE.en",
    "IT.it",
    "JP.ja",
    "KR.ko",
    "LT.en",
    "LU.de", "LU.fr",
    "LV.en",
    "MT.en",
    "MX.en", "MX.es",
    "NL.nl",
    "NO.en",
    "NZ.en",
    "PE.en", "PE.es",
    "PL.en",
    "PT.pt",
    "RO.en",
    "RU.ru",
    "SE.en",
    "SI.en",
    "SK.en",
    "US.en", "US.es",
    "ZA.en"
]

for country in countries:
    url = f'https://raw.githubusercontent.com/blawar/titledb/master/{country}.json'
    response = requests.get(url)
    original_data = response.json()

    # Obtenir la date actuelle
    current_date = datetime.now()

    # Filtrer les jeux qui ne sont pas encore sortis
    unreleased_games = {game_id: game_info for game_id, game_info in original_data.items() if "releaseDate" in game_info and game_info["releaseDate"] and game_info["releaseDate"] > int(current_date.strftime('%Y%m%d'))}

    # Écrire les données filtrées dans un nouveau fichier JSON
    sorted_unreleased_games = sorted(unreleased_games.items(), key=lambda x: x[1]["releaseDate"])

    # Écrire les données triées dans un nouveau fichier JSON sur une seule ligne sans espaces
    with open(f'{country}.json', 'w') as outfile:
        json.dump(dict(sorted_unreleased_games), outfile, separators=(',', ':'))

    print(f"Le fichier '{country}.json' a été créé avec succès.")
