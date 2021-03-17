from gtts import gTTS
from playsound import playsound
voz = gTTS("Hola perros",lang="es-us")
NOMBRE_ARCHIVO="texto2.mp3"
with open(NOMBRE_ARCHIVO,'wb') as archivo:
    voz.write_to_fp(archivo)

playsound(NOMBRE_ARCHIVO)
