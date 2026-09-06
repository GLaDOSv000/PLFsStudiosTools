from PIL import Image
import os

valueselectRoughness = 0
valueselectMetalness = 0

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-PLF's-Studios---Creador-de-imagenes-a-partir-de-valor-de-material------v1.0-------")
    print("")
def espacios():
    print("")
    print("")
    print("")
    print("")
    print("")

def pedirimput():
    valueselectMetalness = input("Inserte el valor de Metalness (0-100) : ")
    print("")
    valueselectRoughness = input("Inserte el valor de Roughness (0-100) :")
    return {valueselectMetalness, valueselectRoughness}

matriz_valores = [
    [0, 25, 50],
    [50, 100, 50],
    [25, 0, 100]
]

def procesarimg():
    height = len(matriz_valores)
    width = len(matriz_valores[0])
    #print(len(matriz_valores))
    #value = 100
    variablesT = pedirimput()
    variables = list(variablesT)
    
    valueselectRoughness = variables[0]
    valueselectMetalness = variables[1]
    
    #roughness
    datos_planos = bytes([int(int(valueselectRoughness) * 2.55) for fila in matriz_valores for val in fila])
    img = Image.frombytes('L', (width, height), datos_planos)
    img_upscaled = img.resize((128, 128), Image.Resampling.NEAREST)
    img_upscaled.save("output/roughness"+str(valueselectRoughness)+".png")
    print("output/roughness"+str(valueselectRoughness)+".png")
    #metalness
    datos_planos = bytes([int(int(valueselectMetalness) * 2.55) for fila in matriz_valores for val in fila])
    img = Image.frombytes('L', (width, height), datos_planos)
    img_upscaled = img.resize((128, 128), Image.Resampling.NEAREST)
    img_upscaled.save("output/metalness_"+str(valueselectMetalness)+".png")
    print("output/metalness_"+str(valueselectMetalness)+".png")
    print("")
    print("Terminado. Abra /output")


def main():
    clearScreen()
    #pedirimput()
    procesarimg()
    #actualfile = SolicitarArchivo()
    #print (actualfile)
    #procesarimg(actualfile)
    espacios()
    input("Enter to reset")
    main()


main()