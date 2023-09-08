import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as plc
class Mineral:
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity
    def silicato_test(self):
        if ('O' in composicion) and ('Si' in composicion):
            print('es silicato')
            self.composicion=True
        else:
            print('no es silicato')
            self.composicion=False
    def densidad_en_SI(self):
        densidad=float(self.specific_gravity)*1000
        return densidad
    def common_color(self):
        x = [0, 1, 1, 0, 0]  
        y = [0, 0, 1, 1, 0]
        plt.plot(x, y, color)
        plt.fill(x, y, color)
        plt.xlim(-1, 2)
        plt.ylim(-1, 2)
        plt.show()
        
    def dur_romp_crist(self):
        print('dureza ', dureza, ' tipo de rompimiento')