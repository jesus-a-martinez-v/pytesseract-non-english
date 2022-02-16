# Importamos las dependencias del proyecto.
from argparse import ArgumentParser

import cv2
import pytesseract
from textblob import TextBlob

# Definimos el menú del programa.
argument_parser = ArgumentParser()
argument_parser.add_argument('-i', '--image', type=str, required=True, help='Ruta a la imagen de entrada.')
argument_parser.add_argument('-l', '--lang', type=str, required=True, help='Lenguaje que Tesseract usará al escanear.')
argument_parser.add_argument('-t', '--to', type=str, default='en', help='Lenguaje al cual traduciremos el texto')
argument_parser.add_argument('-p', '--psm', type=int, default=13, help='Modo PSM de Tesseract.')
arguments = vars(argument_parser.parse_args())

# Cargamos la imagen de entrada y la convertimos de BGR --> RGB.
image = cv2.imread(arguments['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Mostramos la imagen en pantalla.
cv2.imshow('Imagen', image)
cv2.waitKey(0)

# Configuramos Tesseract con el lenguaje de origen y el modo de segmentación de página recibido en los argumentos de
# entrada.
options = f'-l {arguments["lang"]} --psm {arguments["psm"]}'
text = pytesseract.image_to_string(image, config=options)

# Mostramos el texto antes de la traducción.
print('TEXTO ORIGINAL')
print(text)
print('----')

# Traducimos el texto usando TextBlob
text_blob = TextBlob(text)
translated = text_blob.translate(to=arguments['to'])

# Imprimimos el texto traducido.
print('TRADUCIDO')
print(translated)

# Destruimos las ventanas creadas.
cv2.destroyAllWindows()
