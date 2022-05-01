import networkx as nx
import matplotlib.pyplot as plt
import pylab
from funcion import*
from correo_recorrer import*

import matplotlib.patches as mpatches

correo_=input("Ingrese correo electronico")
c_electronico(correo_)
transciones_main=datos_automata(correo_)


#estaods:letras,numeros
#transciones:.,@,
G = nx.DiGraph()
estados=['S','A','C','P','E']
print(transciones_main[0])



#G.add_edges_from([('letras', 'direccion')], label=".")

G.add_edges_from([(estados[0],estados[1])],label=transciones_main[0])
G.add_edges_from([(estados[1],estados[2])],label=transciones_main[1])
G.add_edges_from([(estados[2],estados[3])],label=transciones_main[2])
G.add_edges_from([(estados[3],estados[4])],label=transciones_main[3])

#G.add_edges_from([('exten),('E','F')], weight=3)
#G.add_edges_from([('C','F')], weight=4)
#for G in"""

"""val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                              'H': 0.0}"""

#values = [val_map.get(node, 0.45) for node in G.nodes()]

values=[]
for node in G:
    if node== estados[0]:#Estado incial color verde
        values.append('Green')

    elif node == estados[4]:#Estado final color azul
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

pos=nx.spring_layout(G,seed=5)
print(pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=.5,font_size=10)
nx.draw(G,pos, node_color =values ,with_labels=True, node_size=1000,edge_color=edge_colors,connectionstyle='arc3, rad = 0.1')#edge_cmap=plt.cm.Reds)

estado_inical = mpatches.Patch(color='Green', label='Estado inicial')
estado_final=mpatches.Patch(color='Blue', label=' Estado Final')
plt.legend(handles=[estado_inical,estado_final])

plt.show()


#pylab.show()

