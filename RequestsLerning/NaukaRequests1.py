import requests

url = "https://randomuser.me/api/"
response = requests.get(url)

if response.status_code == 200:
    
    data = response.json()  # Konwersja odpowiedzi do formatu JSON
    user = data["results"][0]  # Pobranie użytkownika / co kolwiek pobierzemy i numer lp

    name = f'{user["name"]["first"]} {user["name"]["last"]}'
    gender = "Mężczyzna" if user["gender"] == "male" else "Kobieta"
    location = f'{user["location"]["city"]}, {user["location"]["country"]}'
    email = user["email"]
    picture = user["picture"]["large"]

    print("\n Wylosowany użytkownik:")
    print(f" Imię i nazwisko: {name}")
    print(f" Płeć: {gender}")
    print(f" Lokalizacja: {location}")
    print(f" E-mail: {email}")
    print(f" Zdjęcie: {picture}")

else:
    print(f"błąd! Kod: {response.status_code}")

    