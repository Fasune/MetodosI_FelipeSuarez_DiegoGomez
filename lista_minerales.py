import numpy as np
import matplotlib.pyplot as plt
import mineral as mf

file=open("minerales.txt", 'r',encoding="utf8")
arreglo_cadalinea=file.readlines()
#print(len(arreglo_cadalinea))
#arreglo_todos_minerales=np.array([])
arreglo_todos_minerales=[]
for i in range(1,len(arreglo_cadalinea)):
        arreglo_cadaitem=arreglo_cadalinea[i].rstrip().split('\t')
        arreglo_cadaitem[7]
        ##print(arreglo_cadaitem,len(arreglo_cadaitem))
        clase_mineral=mf.Mineral(arreglo_cadaitem[0],arreglo_cadaitem[1],arreglo_cadaitem[2],arreglo_cadaitem[3],arreglo_cadaitem[4],arreglo_cadaitem[5],arreglo_cadaitem[6],arreglo_cadaitem[7])
        print(clase_mineral)
        #np.append(arreglo_todos_minerales,clase_mineral)
        arreglo_todos_minerales.append(clase_mineral)
file.close()
#print(arreglo_todos_minerales, 'hey')
conteo_silicato=0
for i in range(len(arreglo_todos_minerales)):
        if arreglo_todos_minerales[i].composicion==True:
                conteo_silicato+=1
densidada=[]
for i in range(len(arreglo_todos_minerales)):
        densidada.append(arreglo_todos_minerales[i].densidad_en_SI())
densidad_promedio=np.mean(densidada)
