from gtts import gTTS
import os
import sys

def text_to_speech(text, output_file):
    # Realiza la síntesis de voz
    tts = gTTS(text, lang='es')
    tts.save(output_file)

    # Reproduce el archivo de audio generado (opcional)
    os.system(f"vlc {output_file}")
    # Pasar MP3 a WAV: ffmpeg -i salida_de_audio.mp3 salida.wav

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 tts.py -t 'Texto' / python3 tts.py -f archivo_de_texto.txt")
    else:
        option = sys.argv[1]

        if option == "-t":
            text = sys.argv[2]
        elif option == "-f":
            input_file = sys.argv[2]
            # Lee el contenido del archivo de texto
            with open(input_file, 'r', encoding='utf-8') as file:
                text = file.read()
        else:
            print("Opción no válida. Usa -t para texto manual o -f para archivo de texto.")
            sys.exit(1)

        output_file = "salida_de_audio.mp3"  # Puedes cambiar el nombre si lo deseas
        text_to_speech(text, output_file)
