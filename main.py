import os

herramientas = [
    ["imageSplitter.py", "Separador de texturas de UE"],
    ["RobloxMaterialImageCreator.py", "Generador de texturas a partir de valor de material"]
]

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-PLF's-Studios---Selector-de-herramientas------v1.0-------")
    print("")
def espacios():
    print("")
    print("")
    print("")
    print("")
    print("")


def ejecutar(numdeherramienta):
    if os.name == "nt":
        os.system("python " + herramientas[numdeherramienta][0])
    else:
        os.system("python3 " + herramientas[numdeherramienta][0])

def main():
    cont = 0
    clearScreen()
    for archiv in herramientas:
        cont = cont + 1
        print(str(cont)+ " - " + archiv[1])
    print("")

    seleccion = input("Seleccione el numero [1]: ")
    if seleccion == "" :
        ejecutar(0)
    else:
        ejecutar(int(seleccion) - 1)

    
    


main()