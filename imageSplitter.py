from PIL import Image
import os
import numpy as np

actualfile = ""
temp = ""
img = ""
img_name = ""

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-PLF's-Studios---Separador-de-texturas-de-UE------v0.1-------")
def espacios():
    print("")
    print("")
    print("")
    print("")
    print("")

def SolicitarArchivo():
    espacios()
    temp = input("·         Suelte el archivo aqui:         · ")
    if temp[-1:] == " ":
        temp = temp[:len(temp) - 1]
        temp = temp.strip("'\"")
    else:
        temp = temp.strip("'\"")
    return(temp)

def procesarimg(stringruta):
    print("")
    decidir = input("roughness color? y/n [n]: ")
    print("")
    img = Image.open(stringruta).convert("RGB")
    r, g, b = img.split()
    cero = Image.new("L", img.size, 0)

    #OCLUSSION
    img_new_final = Image.merge("RGB", (r, r, r))
    print("output/" + os.path.basename(stringruta) + "_oclussion.png")
    img_new_final.save("output/" + os.path.basename(stringruta) + "_oclussion.png")

    #METAlNESS
    img_new_final = Image.merge("RGB", (b, b, b))
    print("output/" + os.path.basename(stringruta) + "_metalness.png")
    img_new_final.save("output/" + os.path.basename(stringruta) + "_metalness.png")

    #ROUGHNESS
    if decidir == "y":
        img_new_final = Image.merge("RGB", (cero, g, cero))
        print("output/" + os.path.basename(stringruta) + "_roughness_color.png")
        img_new_final.save("output/" + os.path.basename(stringruta) + "_roughness_color.png")
    else:
        img_new_final = Image.merge("RGB", (g, g, g))
        print("output/" + os.path.basename(stringruta) + "_roughness.png")
        img_new_final.save("output/" + os.path.basename(stringruta) + "_roughness.png")
    

    print("Terminado. Abra /output")



def main():
    clearScreen()
    actualfile = SolicitarArchivo()
    print (actualfile)
    procesarimg(actualfile)
    espacios()
    input("Enter to reset")
    main()


main()


