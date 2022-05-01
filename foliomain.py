import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
from funcion import FolioFiscal
from folio_fiscal import*
import matplotlib.patches as mpatches


ff=input("Ingrese Folio Fiscal")
FolioFiscal(ff)
trancisiones=f_f(ff)


#estaods:letras,numeros
#transciones:.,@,
G = nx.DiGraph()

estados=('','P','G1','S','G2','T','G4','C','G5','Q','F')
#G.add_edges_from([('letras', 'direccion')], label=".")

G.add_edges_from([(estados[0],estados[1])],label=trancisiones[0])
G.add_edges_from([(estados[1],estados[2])],label=trancisiones[1])
G.add_edges_from([(estados[2],estados[3])],label=trancisiones[2])
G.add_edges_from([(estados[3],estados[4])],label=trancisiones[3])
G.add_edges_from([(estados[4],estados[5])],label=trancisiones[4])
G.add_edges_from([(estados[5],estados[6])],label=trancisiones[5])
G.add_edges_from([(estados[6],estados[7])],label=trancisiones[6])
G.add_edges_from([(estados[7],estados[8])],label=trancisiones[7])
G.add_edges_from([(estados[8],estados[9])],label=trancisiones[8])
G.add_edges_from([(estados[9],estados[10])],label=trancisiones[9])


#values = [val_map.get(node, 0.45) for node in G.nodes()]
values=[]
for node in G:
    if node== estados[0]:
        values.append('White')
    elif node==estados[1]:
        values.append('Green')

    elif node == estados[10]:
        values.append('Blue')
    else:
        values.append('Gray')
#para las transiciones
edge_labels=dict([((u,v,),d['label'])
                 for u,v,d in G.edges(data=True)])
                    #print('u :', u, 'v :', v,'d :',d)
print(edge_labels)
#red_edges = [('C','D'),('D','A')]
edge_colors=['black']
#edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
arc_rad = 0.2
pos=nx.spring_layout(G,seed=10)
print(pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=.5,font_size=7,font_color='red')
nx.draw(G,pos, node_color =values ,with_labels=True, node_size=500,edge_color=edge_colors, connectionstyle=f'arc3, rad = {arc_rad}')
estado_inical = mpatches.Patch(color='Green', label='Estado inicial')
estado_final=mpatches.Patch(color='Blue', label=' Estado Final')
plt.legend(handles=[estado_inical,estado_final])

pylab.show()