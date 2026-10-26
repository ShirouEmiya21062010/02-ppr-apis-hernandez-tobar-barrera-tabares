
import requests

URL_CARTS = "https://dummyjson.com/carts?limit=0"

response = requests.get(URL_CARTS)

if response.status_code == 200:
    carts = response.json()["carts"]

    print("Total de carritos:", len(carts))

    for cart in carts:
        print(cart)

else:
    print("Error al obtener carritos:", response.status_code)
    exit()
