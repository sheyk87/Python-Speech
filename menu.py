import os

def main_menu():
    while True:
        print("Menú:")
        print("1 - TTS")
        print("2 - STT")
        print("3 - MP3 a WAV")
        print("4 - Salir")

        choice = input("Elije una opción (1/2/3/4): ")

        if choice == "1":
            tts_option = input("Elige una opción para ingresar texto:\n1 - Introducir texto manualmente\n2 - Cargar texto desde un archivo\nElije una opción (1/2): ")
            if tts_option == "1":
                text = input("Introduce el texto: ")
                os.system(f"python3 tts.py -t '{text}'")
            elif tts_option == "2":
                file_name = input("Introduce el nombre del archivo de texto: ")
                os.system(f"python3 tts.py -f {file_name}")
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
        elif choice == "2":
            audio_file = input("Introduce el nombre del archivo de audio WAV (solo el nombre): ")
            audio_file += ".wav"
            os.system(f"python3 stt.py {audio_file}")
        elif choice == "3":
            mp3_file = input("Introduce el nombre del archivo MP3 (solo el nombre): ")
            mp3_file += ".mp3"
            wav_file = input("Introduce el nombre del archivo WAV de salida (solo el nombre): ")
            wav_file += ".wav"
            os.system(f"python3 mp3wav.py {mp3_file} {wav_file}")
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main_menu()
