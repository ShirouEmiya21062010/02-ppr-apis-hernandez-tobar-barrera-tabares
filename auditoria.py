
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

totales_por_carrito = []
totales_por_usuario = {}

for cart in carts:
    user_id = cart["userId"]
    total = 0

    # Recorrer los productos de cada carrito
    for producto in cart["products"]:
        if producto["discountPercentage"] < 12:
            total += producto["quantity"]

    # Guardar total de cada carrito para la Tarea 3
    totales_por_carrito.append({
        "cartId": cart["id"],
        "userId": user_id,
        "total": total
    })

    # Acumular los productos válidos por usuario
    totales_por_usuario[user_id] = totales_por_usuario.get(user_id, 0) + total

# Mostrar resultados por usuario
print("\n===== PRODUCTOS VÁLIDOS POR USUARIO =====")

for user_id, total in totales_por_usuario.items():
    respuesta = requests.get(f"https://dummyjson.com/users/{user_id}")

    if respuesta.status_code == 200:
        usuario = respuesta.json()
        nombre = usuario["firstName"] + " " + usuario["lastName"]
    else:
        nombre = "Desconocido"

    print(f"Usuario: {nombre} | ID: {user_id} | Productos válidos: {total}")

print("\nTotal de usuarios:", len(totales_por_usuario))
print("Total de productos válidos:", sum(totales_por_usuario.values()))