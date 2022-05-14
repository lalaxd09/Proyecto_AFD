import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
from funcion import*
from RFC import*
import matplotlib.patches as mpatches
cel=input('ingrese cel')
vacio=''
guion='-'
numero=cel.split('-')
numero.insert(0,vacio)
numero.append(guion)

G = nx.DiGraph()
estados=['','LD','G1','N','G2','NF','F']
# print(transciones_main[0])


G.add_edges_from([(estados[0],estados[1])],label=numero[0])
G.add_edges_from([(estados[1],estados[2])],label=numero[1])
G.add_edges_from([(estados[2],estados[3])],label=numero[4])
G.add_edges_from([(estados[3],estados[4])],label=numero[2])
G.add_edges_from([(estados[4],estados[5])],label=numero[4])
G.add_edges_from([(estados[5],estados[6])],label=numero[3])


values=[]
for node in G:
    if node== estados[0]:#Estado incial color verde
        values.append('white')

    elif node==estados[1]:
        values.append('Green')
    elif node == estados[6]:#Estado final color azul
        values.append('Blue')
    else:
        values.append('Gray')


edge_labels=dict([((u,v,),d['label'])#transiciones
                  for u,v,d in G.edges(data=True)])
#print('u :', u, 'v :', v,'d :',d)
# print(edge_labels)

edge_colors=['black']

pos=nx.spring_layout(G,seed=5)
# print(pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=.6,font_size=8,font_color='red')
nx.draw(G,pos, node_color =values ,with_labels=True, node_size=300,edge_color=edge_colors,connectionstyle='arc3, rad = 0.1')#edge_cmap=plt.cm.Reds)

estado_inical = mpatches.Patch(color='Green', label='Estado inicial')
estado_final=mpatches.Patch(color='Blue', label=' Estado Final')
plt.legend(handles=[estado_inical,estado_final])

plt.show()
