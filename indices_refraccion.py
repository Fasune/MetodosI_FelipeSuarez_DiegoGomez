import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import os


def tuplas(ruta: str)-> list:
    f=open(ruta)
    texto_doc=f.read()
    f.close()
    
    lista_1= texto_doc.split('data: |\n')[1].split('\nSPECS')[0].split('  - type')[0].strip().split('\n        ')
    lista_final = []
    
    for k in lista_1:
        texto = k.split(' ')
        texto[0] = float(texto[0])
        texto[1] = float(texto[1])
        lista_final.append(tuple(texto))
    return lista_final


def func_graficar(ruta: str):
    tupla=tuplas(ruta)
    nombre = os.path.splitext(os.path.basename(ruta))[0] 
    x=[]
    y=[]
    for i in range(len(tupla)):
        x.append(tupla[i][0])
        y.append(tupla[i][1])

    n_prom = stats.mean(y)
    desvest = stats.pstdev(y)
    
    plt.plot(x, y)
    plt.axhline(y=n_prom, color='r')
    plt.xlabel('Longitud de onda ($\\mu$m)')
    plt.ylabel('Índice de refracción n')
    plt.legend(['n($\\lambda$)', 'n_prom'])
    plt.title(f'{nombre}; n_prom= {round(n_prom, 2)}; $\\sigma$= {round(desvest, 2)}')
    plt.grid()
    plt.savefig(f'{nombre}.png')
    plt.close()

    
def func_graf(ruta: str):
    tupla=tuplas(ruta)
    nombre = os.path.splitext(os.path.basename(ruta))[0]
    x=[]
    y=[]
    for i in range(len(tupla)):
        x.append(tupla[i][0])
        y.append(tupla[i][1])

    n_prom=stats.mean(y)
    desvest=stats.pstdev(y)
    plt.plot(x,y)
    plt.axhline(y=n_prom,color='r')
    plt.xlabel('Longitud de onda ($\\mu$m)')
    plt.ylabel('Índice de refracción n')
    plt.legend(['n($\\lambda$)','n_prom'])
    plt.title(str(nombre)+'; n_prom= '+str(round(n_prom,2))+'; $\\sigma$= '+str(round(desvest,2)))
    plt.grid()
    plt.show()


    
NOA=func_graf('Adhesivos Ópticos/NOA1348')
Kapton=func_graf('Plásticos Comerciales/Kapton')


lista_elementos = pd.read_csv('indices_refraccion.csv')
lista_rutas_yml = lista_elementos['Categoría']+'\\'+lista_elementos['Material']


def graficas(lista_rutas_yml): 
    ruta = os.getcwd()
    
    for f in lista_rutas_yml.values:
        split = f.split('\\')
        nombre = split[-1]
        carpeta = split[-2]
        
        print(ruta)
        os.chdir(os.path.join(ruta, carpeta))
        g = os.getcwd()
        print(g)
        
        func_graficar(nombre)
        
        split = g.split('\\')  # valido para Windows
        str_ruta = ''
        
        for i in range(len(split)-1):
            str_ruta += split[i]
            
            if i < (len(split) - 1):
                str_ruta += '\\'
        
        os.chdir(str_ruta)

graficas=graficas(lista_rutas_yml)