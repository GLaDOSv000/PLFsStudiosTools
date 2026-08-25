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

def SolicitarArchivo():
    print("")
    print("")
    print("")
    print("")
    print("")
    temp = input("Suelte el archivo aqui: ")
    if temp[-1:] == " ":
        temp = temp[:len(temp) - 1]
        temp = temp.strip("'\"")
    else:
        temp = temp.strip("'\"")



    return(temp)

def procesarimg(stringruta):
    img = Image.open(stringruta).convert("RGB")
    r, g, b = img.split()
    cero = Image.new("L", img.size, 0)
    img_new_final = Image.merge("RGB", (r, r, r))
    #img_new_final = img_new.convert("L")
    #arr = np.array(img_new, dtype=np.float32) / 255.0
    #gris_lineal = np.mean(arr, axis=2)
    #resultado = (gris_lineal * 255).astype(np.uint8)
    #img_new_final = Image.fromarray(resultado)
    print("output/" + os.path.basename(stringruta) + "_oclussion.png")
    img_new_final.save("output/" + os.path.basename(stringruta) + "_oclussion.png")

    img_new_final = Image.merge("RGB", (b, b, b))
    #arr = np.array(img_new, dtype=np.float32) / 255.0
    #gris_lineal = np.mean(arr, axis=2)
    #resultado = (gris_lineal * 255).astype(np.uint8)
    #img_new_final = Image.fromarray(resultado)
    print("output/" + os.path.basename(stringruta) + "_metalness.png")
    img_new_final.save("output/" + os.path.basename(stringruta) + "_metalness.png")

    img_new_final = Image.merge("RGB", (g, g, g))
    #arr = np.array(img_new, dtype=np.float32) / 255.0
    #gris_lineal = np.mean(arr, axis=2)
   # resultado = (gris_lineal * 255).astype(np.uint8)
  #  img_new_final = Image.fromarray(resultado)
    print("output/" + os.path.basename(stringruta) + "_roughness.png")
    img_new_final.save("output/" + os.path.basename(stringruta) + "_roughness.png")

    print("Terminado. Abra /output")



def main():
    clearScreen()
    actualfile = SolicitarArchivo()
    print (actualfile)
    procesarimg(actualfile)
    input("Enter to reset")
    main()


main()


