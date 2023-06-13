class Bitacora:
    def __init__(self, planeta, capturado, creditos):
        self.planeta = planeta
        self.capturado = capturado
        self.creditos = creditos

bitacora_pila = [
    Bitacora("Tatooine", "Luke Skywalker", 10000),
    Bitacora("Hoth", "Princesa Leia", 5000),
    Bitacora("Endor", "Ewoks", 2000),
    Bitacora("Bespin", "Lando Calrissian", 8000),
    Bitacora("Coruscant", "Emperador Palpatine", 15000),
    Bitacora("Naboo", "Jar Jar Binks", 3000),
    Bitacora("Corelia", "Han Solo", 12000),
    ]

# Mostrar los planetas visitados en el orden en que hizo las misiones
print("Planetas visitados en el orden de las misiones:")
for bitacora in bitacora_pila:
    print(bitacora.planeta)
    
# Determinar cuantos creditos galacticos recaudo en total
total_creditos = 0
for bitacora in bitacora_pila:
    total_creditos += bitacora.creditos
    
print(f"Total de creditos galacticos recaudados: {total_creditos}")

# Determinar el numero de la mision en la que capturo a Han Solo y en que planeta fue
mision_han_solo = None
numero_mision = 0
for bitacora in bitacora_pila:
    numero_mision += 1
    if bitacora.capturado == "Han Solo":
        mision_han_solo = (numero_mision, bitacora.planeta)
        break
    
if mision_han_solo:
    print(f"Han Solo fue capturado en la mision {mision_han_solo[0]} en el planeta {mision_han_solo[1]}.")
else:
    print("No se encontro informacion sobre la captura de Han Solo en la bitacora.")
    