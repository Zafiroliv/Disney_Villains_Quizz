import streamlit as st

# Preguntas y respuestas
preguntas = [
    ("¿Cuál es tu mayor motivación?", 
     {"Poder": "Maléfica", "Riqueza": "Scar", "Venganza": "Úrsula", "Diversión": "Hades"}),

    ("¿Cuál es tu mayor fortaleza?", 
     {"Magia": "Maléfica", "Astucia": "Scar", "Manipulación": "Úrsula", "Carisma": "Hades"}),

    ("¿Cómo te describen tus enemigos?", 
     {"Temible": "Maléfica", "Traicionero": "Scar", "Seductora": "Úrsula", "Sarcasmo puro": "Hades"})
]

st.title("¿Qué villano de Disney eres?")
st.write("Responde estas preguntas para descubrirlo:")

respuestas = []

for pregunta, opciones in preguntas:
    respuesta = st.radio(pregunta, list(opciones.keys()))
    respuestas.append(opciones[respuesta])

# Determinar el villano más elegido
resultado = max(set(respuestas), key=respuestas.count)

st.subheader(f"Eres... {resultado}!")

# Mostrar imagen (deberás subir imágenes a una carpeta "images" en tu repo)
st.image(f"images/{resultado.lower()}.jpg", caption=resultado)
