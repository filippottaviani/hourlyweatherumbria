import requests
import keys

# Definisco le coordinate delle città
terni = "TERNI", "42.58598160906223", "12.611514716492035"
perugia = "PERUGIA", "43.11703773436079", "12.362215968044929"
orvieto = "ORVIETO", "42.71693758195354", "12.112869423063852"
foligno = "FOLIGNO", "42.9562053514725", "12.703210868153604"
citta_di_castello = "CITTA' DI CASTELLO", "43.458797328776505", "12.242326808299188"
norcia = "NORCIA", "42.79235444680194", "13.092800749063501"


def current_weather(city):
    url = "https://api.openweathermap.org/data/3.0/onecall?lat=" + city[1] + "&lon=" + city[2] + "&appid=" + keys.api_key
    response = requests.get(url).json()

    # Prelevo le info utili
    temperature = response['current']['temp'] - 273.15
    humidity = response['current']['humidity']
    description = response['current']['weather'][0]['description']

    result = f"#{city[0]}:\n{description}\n {temperature:.2f}°C\n {humidity}% H2O\n\n"

    return result
