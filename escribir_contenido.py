"""

    Programado por Luis Cabrera Benito 
  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
    
    Blog:       https://parzibyte.me/blog
    Ayuda:      https://parzibyte.me/blog/contrataciones-ayuda/
    Contacto:   https://parzibyte.me/blog/contacto/
"""
import argparse
import glob
import os
import sys
creditos = """
    Programado por Luis Cabrera Benito 
  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \\
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
    
    Blog:       https://parzibyte.me/blog
    Ayuda:      https://parzibyte.me/blog/contrataciones-ayuda/
    Contacto:   https://parzibyte.me/blog/contacto/
"""
comentario_comun = {
    'inicio': '/*',
    'fin': '*/',
}
comentarios = {
    'txt': {
        'inicio': '',
        'fin': '',
    },
    'ts': comentario_comun,
    'js': comentario_comun,
    'ino': comentario_comun,
    'java': comentario_comun,
    'php': {
        'inicio': "<?php\n/*",
        'fin': '*/ ?>',
    },
    'py': {
        'inicio': '"""',
        'fin': '"""',
    },
    'html': {
        'inicio': '<!--',
        'fin': '-->',
    },
    'go': comentario_comun,
    'c': comentario_comun,
}
parser = argparse.ArgumentParser()
parser.add_argument("extension", help="Extensión de los archivos a modificar")
parser.add_argument("directorio_archivos",
                    help="Ubicación de directorio que tiene los archivos con determinada extensión")
argumentos = parser.parse_args()
if not comentarios.get(argumentos.extension):
    print("Extensión {} todavía no soportada".format(argumentos.extension))
    sys.exit(-1)

comentarios_archivo_actual = comentarios[argumentos.extension]
directorio = argumentos.directorio_archivos
os.chdir(directorio)
for nombre_archivo in glob.glob("*."+argumentos.extension):
    ruta = directorio+"/"+nombre_archivo
    with open(ruta, "r") as archivo:
        contenido = comentarios_archivo_actual["inicio"] + "\n" + \
            creditos + \
            comentarios_archivo_actual["fin"] + "\n" + archivo.read()
    with open(ruta, "w") as archivo:
        archivo.write(contenido)
    print("Agregados créditos a {}".format(ruta))
