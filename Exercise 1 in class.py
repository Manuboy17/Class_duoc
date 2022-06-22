import numpy as np
arregloU = np.random.randint(100,size=(1,10))
print(arregloU)
nro = int(input("Ingrese su numero"))
if nro not in arregloU:
    print(f"El numero {nro} no esta en el arreglo")
else:
    print(f"El numero {nro} esta en el arreglo") 