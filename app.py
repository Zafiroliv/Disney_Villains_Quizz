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
    },
    "¿Qué harías si alguien te traiciona?": {
        "a": "Le lanzaría un hechizo",
        "b": "Me vengaría con un plan perfecto",
        "c": "Le haría la vida imposible",
        "d": "Me burlaría de él y seguiría adelante"
    },
    "Si fueras un animal, ¿cuál serías?": {
        "a": "Un cuervo",
        "b": "Un león",
        "c": "Una serpiente",
        "d": "Un gato negro"
    },
    "¿Dónde te gustaría vivir?": {
        "a": "En un castillo oscuro",
        "b": "En la cima de una montaña",
        "c": "En un palacio bajo el mar",
        "d": "En el inframundo"
    },
    "¿Cuál es tu peor defecto?": {
        "a": "Soy rencoroso/a",
        "b": "Soy demasiado ambicioso/a",
        "c": "Me encanta manipular a los demás",
        "d": "Tengo un humor un poco retorcido"
    },
    "Si tuvieras un poder, ¿cuál sería?": {
        "a": "Magia oscura",
        "b": "Fuerza sobrehumana",
        "c": "Transformación y engaño",
        "d": "Control del fuego"
    }
}

# Relacionar respuestas con villanos
resultados = {
    "a": "Maléfica",
    "b": "Scar",
    "c": "Úrsula",
    "d": "Hades"
}

st.title("👿 ¿Qué villano de Disney eres? 👿")

st.write("Responde las siguientes preguntas y presiona 'Enviar' para conocer tu villano.")

# Lista para guardar respuestas
respuestas = []

# Mostrar las preguntas
for pregunta, opciones in preguntas.items():
    opcion = st.radio(pregunta, list(opciones.values()), key=pregunta)
    respuestas.append(list(opciones.keys())[list(opciones.values()).index(opcion)])

# Botón para mostrar el resultado
if st.button("Enviar"):
    # Contar la opción más elegida
    villano = max(set(respuestas), key=respuestas.count)

    # Mostrar resultado
    st.subheader(f"✨ ¡Eres {resultados[villano]}! ✨")

    # Mostrar imagen (reemplazar con enlaces reales de imágenes)
    imagenes = {
        "Maléfica": "https://upload.wikimedia.org/wikipedia/en/9/90/Maleficent_disney.png",
        "Scar": "https://upload.wikimedia.org/wikipedia/en/9/98/Scar_Lion_King.png",
        "Úrsula": "https://upload.wikimedia.org/wikipedia/en/3/3e/Ursula_Disney.png",
        "Hades": "https://upload.wikimedia.org/wikipedia/en/7/71/Hades-disney.png"
    }
    
    st.image(imagenes[resultados[villano]], width=300)
    st.write(f"Tu personalidad se parece mucho a la de {resultados[villano]}. ¡Cuidado con los héroes! 😈")
