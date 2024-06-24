import requests
import random
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from io import BytesIO

def obtener_pokemon_aleatorio():
    # Obtener un número aleatorio entre 1 y 898 (número total de Pokémon en la Pokédex nacional)
    pokemon_id = random.randint(1, 898)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        nombre = pokemon_data['name']
        imagen_url = pokemon_data['sprites']['front_default']
        return nombre, imagen_url
    else:
        return None, None

def mostrar_pokemon():
    nombre, imagen_url = obtener_pokemon_aleatorio()
    if nombre and imagen_url:
        response = requests.get(imagen_url)
        imagen_pokemon = Image.open(BytesIO(response.content))
        imagen_pokemon = imagen_pokemon.resize((200, 200), Image.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen_pokemon)
        
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk
        etiqueta_nombre.config(text=nombre.capitalize())
    else:
        etiqueta_nombre.config(text="No se pudo obtener el Pokémon")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Pokémon Aleatorio")

# Establecer el tamaño mínimo de la ventana
ventana.minsize(300, 300)

# Etiqueta para mostrar el nombre del Pokémon
etiqueta_nombre = Label(ventana, text="", font=("Arial", 20))
etiqueta_nombre.pack()

# Etiqueta para mostrar la imagen del Pokémon
etiqueta_imagen = Label(ventana)
etiqueta_imagen.pack()

# Botón para obtener un Pokémon aleatorio
boton = Button(ventana, text="Obtener Pokémon Aleatorio", command=mostrar_pokemon)
boton.pack()

# Centrar la ventana en la pantalla
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Ejecutar la aplicación
ventana.mainloop()
