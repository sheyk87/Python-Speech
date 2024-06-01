import pyttsx3

# Inicializa el motor de síntesis de voz
engine = pyttsx3.init()

# Obtiene la lista de voces disponibles
voices = engine.getProperty('voices')

# Encuentra y selecciona una voz masculina en español
for voice in voices:
    if "spanish-latin-am" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Convierte texto en voz
text = "Hola, esta es una voz de hombre en español."
engine.say(text)

# Reproduce la voz
engine.runAndWait()
