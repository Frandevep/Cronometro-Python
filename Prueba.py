import time

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        print(f"⏳ Tiempo restante: {i} segundos", end="\r")
        time.sleep(1)  # Espera 1 segundo
    print("\n⏰ ¡Tiempo terminado!")

# Pedimos al usuario la cantidad de segundos
tiempo = int(input("Ingresa el tiempo en segundos: "))

# Iniciamos el cronómetro
cronometro(tiempo)
