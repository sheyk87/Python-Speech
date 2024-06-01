import subprocess
import sys

if len(sys.argv) != 3:
    print("Uso: python3 mp3wav.py archivo.mp3 archivo.wav")
else:
    input_audio = sys.argv[1]
    output_audio = sys.argv[2]

    # Ejecuta el comando FFmpeg para convertir el archivo de audio de MP3 a WAV
    command = ["ffmpeg", "-i", input_audio, output_audio]
    subprocess.run(command)

    print(f"Se ha convertido {input_audio} a {output_audio}")
