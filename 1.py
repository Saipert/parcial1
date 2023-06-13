# Desarrollar una funcion recursiva que permita contar cuantas veces aparece una determinada palabra, en un vector de palabras
def contar_palabra(palabra, vector_palabras):
    if not vector_palabras:
        return 0
    else:
        if vector_palabras[0] == palabra:
            return 1 + contar_palabra(palabra, vector_palabras[1:])
        else:
            return contar_palabra(palabra, vector_palabras[1:])

vector = ["river", "boca", "racing", "independiente", "river", "river", "velez"]
buscar_palabra = "river"
contador = contar_palabra(buscar_palabra, vector)
print(f"La palabra '{buscar_palabra}' aparece {contador} veces.")