import os
import subprocess

print("\033[31mby senss\033[0m")

# Lista de aplicaciones a eliminar
aplicaciones_a_eliminar = [
    "nikto",        # Ejemplo de aplicación
    "recon-ng",     # Ejemplo de aplicación
    "theHarvester", # Ejemplo de aplicación
    "setoolkit",    # Ejemplo de aplicación
    "dmitry",       # Ejemplo de aplicación
    "faraday",      # Ejemplo de aplicación
    "wifite",       # Ejemplo de aplicación
    "reaver",       # Ejemplo de aplicación


    # Añadir más aplicaciones según sea necesario
]

# Función para eliminar aplicaciones
def eliminar_aplicaciones():
    for app in aplicaciones_a_eliminar:
        print(f"Eliminando {app}...")
        try:
            # Ejecuta el comando para eliminar la aplicación
            subprocess.run(f"sudo apt-get remove --purge -y {app}", shell=True, check=True)
            print(f"{app} ha sido eliminado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al eliminar {app}: {e}")

# Función para limpiar dependencias no necesarias
def limpiar_dependencias():
    print("Limpiando dependencias no necesarias...")
    try:
        subprocess.run("sudo apt-get autoremove -y", shell=True, check=True)
        subprocess.run("sudo apt-get clean", shell=True, check=True)
        print("Dependencias limpiadas correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al limpiar dependencias: {e}")

# Función principal
def main():
    eliminar_aplicaciones()
    limpiar_dependencias()
    print("Proceso de eliminación y limpieza completado.")

if __name__ == "__main__":
    main()
