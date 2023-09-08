import expansiontermicamineral as expter
from lista_minerales import arreglo_todos_minerales
print(arreglo_todos_minerales)
# Para la olivina
olivina = expter.ExpansionTermicaMineral(arreglo_todos_minerales[0], "olivine_angel_2017.csv")
olivina.ax1
# Para el grafito
grafito = expter.ExpansionTermicaMineral(lista_minerales.arreglo_todos_minerales[-1], "graphite_mceligot_2016.csv")
grafito.ax1