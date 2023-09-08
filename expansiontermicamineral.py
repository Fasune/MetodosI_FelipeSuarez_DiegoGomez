import numpy as np
from mineral import Mineral
import pandas as pd
import matplotlib.pyplot as plt

class ExpansionTermicaMineral():
    def __init__(self, Mineral, archivo):
        list_temp=[]
        list_vol=[]
    def expansion_t(self):
        df = pd.read_csv(self.archivo)
        self.temperatura = df['celsius_temperature'].values
        self.volumen = df['volumencc'].values
        #self.temperatura = df['Temperatura (Celsius)'].values
        #self.volumen = df['Volumen (cm^3)'].values
        arreglo_temp=np.array([])
        arreglo_vol=np.array([])
        for i in range(1,(len(self.temperatura)-1)):
            der_temp=(self.temperatura[i+1]-self.temperatura[i-1])/(2*self.temperatura[i+1])
            der_vol=(self.volumen[i+1]-self.volumen[i-1])/(2*self.volumen[i+1])
            np.append(arreglo_temp,der_temp)
            np.append(arreglo_vol,der_vol)
        alpha = (1/self.temperatura[1:-1])*(arreglo_vol/arreglo_vol)
        prom_alpha= np.mean(alpha)
        #exact_temp = np.diff(self.temperatura)
        #exact_volumen = np.diff(self.volumen)
        global_error=np.std(arreglo_alpha)/np.sqrt(len(arreglo_alpha))

        fig, self.ax1 = plt.subplots()
        self.ax1.set_xlabel('Temperatura (Celsius)')
        self.ax1.set_ylabel('Coeficiente alpha')
        self.ax1.plot(self.temperatura, self.volumen)
        self.ax1.tick_params(axis='y', labelcolor=color)
        plt.title(f'Expansión Térmica de {self.nombre}')
        plt.show()
        return prom_alpha, global_error
