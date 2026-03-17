from pathlib import Path
import shutil


def mostrar_banner():
    print("=" * 50)
    print("        ACTUALIZADOR-JULIOCITO-WARRIOR")
    print("=" * 50)
    print("Sincroniza archivos faltantes entre carpetas")
    print()

mostrar_banner()

def pedir_ruta(mensaje):

    while True:
        #strip() permite que no acepte los espacios en blanco
        entrada_usuario = input(f"Diga la ruta {mensaje} donde quieres actualizar: ").strip()

        if not entrada_usuario: #Si esta vacia le dice y vuelve a empezar el loop
            print("La ruta no puede estar vacia")
            continue #continue significa vuelva a empezar el loop
        carpeta_ruta = Path(entrada_usuario)
        if not carpeta_ruta.exists():
            print("La ruta no existe")
            continue
        if not carpeta_ruta.is_dir():
            print("La ruta debe ser a un directorio no a archivo")
            continue
        print("Ruta valida", carpeta_ruta, "\n")
        return carpeta_ruta

print("Ruta Origen: \n")
origen_ruta = pedir_ruta("origen desde")
print("Ruta Destino: \n")
destino_ruta = pedir_ruta("destino a")

print(f"Origen: {origen_ruta}\nDestino: {destino_ruta}")



lista_archivos = []

for archivo in origen_ruta.rglob("*"):
    if archivo.is_file():
        lista_archivos.append(archivo)



cantidad_archivos = len(lista_archivos)


procesados_archivos = 0
faltantes = []

ancho_barra = 20
for archivo in lista_archivos:
    procesados_archivos += 1

    porcentaje = procesados_archivos / cantidad_archivos
    bloques_llenos = int(porcentaje * ancho_barra)
    bloques_vacios = ancho_barra - bloques_llenos

    barra = "#" * bloques_llenos + "-" * bloques_vacios

    print(f"\rProcesando {procesados_archivos}/{cantidad_archivos} [{barra}] {porcentaje*100:.1f}%", end="", flush=True)

    ruta_relativa = archivo.relative_to(origen_ruta)
    archivo_destino = destino_ruta / ruta_relativa
    if archivo_destino.parent.exists():
        if not archivo_destino.exists():
            shutil.copy(archivo, archivo_destino)
            faltantes.append(str(ruta_relativa))

print("\n\n")
print(f"*"*50 + f" FALTANTES({len(faltantes)}) " + "*"*50)
print("\n")
for faltante in enumerate(faltantes, start=1):
    print(f"{faltante}\n")
input("\nPresione Enter para salir...")





