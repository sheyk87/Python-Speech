import speech_recognition as sr
import sys

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Utiliza el motor de reconocimiento de voz de Google
        text = recognizer.recognize_google(audio, language="es-ES")
        return text
    except sr.UnknownValueError:
        return "No se pudo reconocer el audio"
    except sr.RequestError as e:
        return f"Error en la solicitud: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 stt.py audio.wav")
    else:
        audio_file = sys.argv[1]
        transcript = transcribe_audio(audio_file)
        print("Texto transcrito:")
        print(transcript)

        # Preguntar al usuario si desea guardar el resultado en un archivo
        save_to_file = input("¿Desea guardar el resultado en un archivo TXT? (s/n): ")
        if save_to_file.lower() == "s":
            file_name = input("Introduzca el nombre del archivo: ")
            file_name += ".txt"  # Agregar la extensión .txt automáticamente
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(transcript)
            print(f"Resultado guardado en '{file_name}'")
