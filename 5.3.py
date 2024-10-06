import requests
try:
    numerot = int(input("Anna numero (1-50): "))

    if numerot < 1 or numerot > 50:
        raise ValueError("Virhe!")

    h = requests.get(f"https://fakerapi.it/api/v1/persons?_quantity={numerot}")

    h.raise_for_status()

    data = h.json()

    print("Haetut henkilöt:")
    for person in data['data']:
        first_name = person['firstname']
        last_name = person['lastname']
        email = person["email"]
        print(f"{first_name} {last_name}, sähköposti: {email}")
finally:
    avain = input("Anna avain: ")

    with open("palaute.txt", "a") as file:
        file.write(f"Palaute: {avain}")
    print("avain in 'palaute.txt'.")