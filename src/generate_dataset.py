from faker import Faker
import pandas as pd
import random

fake = Faker()

productos = [
    "Laptop",
    "Mouse",
    "Teclado",
    "Monitor",
    "Audífonos",
    "Silla Gamer",
    "Disco SSD",
    "Memoria RAM",
    "Webcam",
    "Impresora"
]

vendedores = [
    "Carlos Gómez",
    "María Pérez",
    "Juan Rodríguez",
    "Laura Sánchez",
    "Andrés López",
    "Sofía Martínez"
]

categorias = {
    "Laptop": "Computadores",
    "Mouse": "Accesorios",
    "Teclado": "Accesorios",
    "Monitor": "Monitores",
    "Audífonos": "Audio",
    "Silla Gamer": "Muebles",
    "Disco SSD": "Almacenamiento",
    "Memoria RAM": "Componentes",
    "Webcam": "Video",
    "Impresora": "Oficina"
}

ciudades = [
    "Barranquilla",
    "Bogotá",
    "Medellín",
    "Cali",
    "Cartagena",
    "Bucaramanga",
    "Santa Marta",
    "Pereira"
]

metodos_pago = [
    "Tarjeta",
    "Efectivo",
    "Transferencia",
    "Nequi",
    "Daviplata"
]

datos = []

for _ in range(8000):

    producto = random.choice(productos)

    cantidad = random.randint(1,5)

    precio = random.randint(40,4000)*1000

    descuento = random.choice([0,5,10,15,20])

    subtotal = cantidad * precio

    total = subtotal - (subtotal * descuento/100)

    datos.append({

        "Fecha": fake.date_between("-2y","today"),

        "Ciudad": random.choice(ciudades),

        "Producto": producto,

        "Categoría": categorias[producto],

        "Cantidad": cantidad,

        "Precio Unitario": precio,

        "Descuento (%)": descuento,

        "Total Venta": total,

        "Método Pago": random.choice(metodos_pago),
        
        "Vendedor": random.choice(vendedores),

    })

df = pd.DataFrame(datos)

df.to_csv("Data/retail_sales_dataset.csv",index=False)

print(df.head())

print("\nDataset creado correctamente.")