import streamlit as st

# Definir preguntas y opciones
preguntas = {
    "¿Qué te motiva más?": {
        "a": "El poder",
        "b": "La venganza",
        "c": "La riqueza",
        "d": "La diversión"
    },
    "¿Cómo prefieres resolver problemas?": {
        "a": "Con magia y engaños",
        "b": "Con fuerza bruta",
        "c": "Con estrategias y manipulación",
        "d": "Haciendo que otros lo hagan por mí"
    },
    "¿Cuál es tu frase favorita?": {
        "a": "Espejito, espejito...",
        "b": "Yo soy el amo de todo lo que veo",
        "c": "Pobres almas en desgracia...",
        "d": "La vida es un juego, ¡y yo hago las reglas!"
    }
}

resultados = {
    "a": "Maléfica",
    "b": "Scar",
    "c": "Úrsula",
    "d": "Hades"
}

st.title("¿Qué villano de Disney eres?")

respuestas = []
for pregunta, opciones in preguntas.items():
    opcion = st.radio(pregunta, list(opciones.values()))
    respuestas.append(list(opciones.keys())[list(opciones.values()).index(opcion)])

# Contar la opción más elegida
villano = max(set(respuestas), key=respuestas.count)

st.subheader(f"Eres {resultados[villano]}!")

st.image(f"https://example.com/{resultados[villano].lower()}.jpg", width=300)  # Reemplazar con imágenes reales
