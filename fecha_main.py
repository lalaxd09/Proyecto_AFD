import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
from funcion import fecha
from fecha_datos import*


fecha_i=input("Ingrese fecha")
fecha(fecha_i)
estados,trancisiones=fechas_datos(fecha_i)


#estaods:letras,numeros
#transciones:.,@,
G = nx.DiGraph()


#G.add_edges_from([('letras', 'direccion')], label=".")

G.add_edges_from([(estados[0],estados[1])],label=trancisiones[0])
G.add_edges_from([(estados[1],estados[2])],label=trancisiones[0])
#G.add_edges_from([('exten),('E','F')], weight=3)
#G.add_edges_from([('C','F')], weight=4)
#for G in

"""val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                              'H': 0.0}"""

#values = [val_map.get(node, 0.45) for node in G.nodes()]
values=['gray']
#para las transiciones
edge_labels=dict([((u,v,),d['label'])
                 for u,v,d in G.edges(data=True)])
                    #print('u :', u, 'v :', v,'d :',d)
print(edge_labels)
#red_edges = [('C','D'),('D','A')]
edge_colors=['black']
#edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

pos=nx.spring_layout(G)
print(pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=.5,font_size=20)
nx.draw(G,pos, node_color =values ,with_labels=True, node_size=2000,edge_color=edge_colors)#edge_cmap=plt.cm.Reds)
pylab.show()