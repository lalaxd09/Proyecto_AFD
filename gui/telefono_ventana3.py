import networkx as nx
import matplotlib.pyplot as plt
import pylab
from funcion import*
from fecha_datos import*
import matplotlib.patches as mpatches
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk


def grafico_telefono(cel):
    vacio = ''
    guion = '-'
    numero = cel.split('-')
    numero.insert(0, vacio)
    numero.append(guion)

    G = nx.DiGraph()
    estados = ['', 'LD', 'G1', 'N', 'G2', 'NF', 'F']
    # print(transciones_main[0])

    G.add_edges_from([(estados[0], estados[1])], label=numero[0])
    G.add_edges_from([(estados[1], estados[2])], label=numero[1])
    G.add_edges_from([(estados[2], estados[3])], label=numero[4])
    G.add_edges_from([(estados[3], estados[4])], label=numero[2])
    G.add_edges_from([(estados[4], estados[5])], label=numero[4])
    G.add_edges_from([(estados[5], estados[6])], label=numero[3])

    values = []
    for node in G:
        if node == estados[0]:  # Estado incial color verde
            values.append('white')

        elif node == estados[1]:
            values.append('Green')
        elif node == estados[6]:  # Estado final color azul
            values.append('Blue')
        else:
            values.append('Gray')

    edge_labels = dict([((u, v,), d['label'])  # transiciones
                        for u, v, d in G.edges(data=True)])
    # print('u :', u, 'v :', v,'d :',d)
    # print(edge_labels)

    edge_colors = ['black']
    f = plt.Figure(figsize=(5, 5), dpi=100)
    plt.title('Automata Télefono')
    pos = nx.spring_layout(G, seed=5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=.6, font_size=8, font_color='red')
    nx.draw(G, pos, node_color=values, with_labels=True, node_size=300, edge_color=edge_colors,
            connectionstyle='arc3, rad = 0.1')  # edge_cmap=plt.cm.Reds)

    estado_inical = mpatches.Patch(color='Green', label='Estado inicial')
    estado_final = mpatches.Patch(color='Blue', label=' Estado Final')
    plt.legend(handles=[estado_inical, estado_final])

    plt.show()


def ventana3():
    ventana3 = tk.Toplevel()
    ventana3.title('Télefono')
    etiqueta = tk.Label(ventana3, text='Validación de télefono')
    etiqueta.grid(row=1,column=4)
    entrada = tk.Entry(ventana3)
    entrada.grid(row=2,column=4)
    button1 = tk.Button(ventana3, text='Inciar',command=lambda: grafico_telefono(entrada.get()))
    button1.grid(row=3,column=4)
    tituloG=tk.Label(ventana3,text='Gramatica')
    tituloG.grid(row=4, column=4)
    gramatica=tk.Label(ventana3,text='LD->[0-9]A')
    gramatica.grid(row=5,column=4)
    gramaticaA = tk.Label(ventana3, text="G1->['-']L2")
    gramaticaA.grid(row=6, column=4)
    gramaticaC = tk.Label(ventana3, text='L2->[0-9]G2')
    gramaticaC.grid(row=7, column=4)
    gramaticaP= tk.Label(ventana3, text="G2->['-']E")
    gramaticaP.grid(row=8, column=4)
    gramaticaE = tk.Label(ventana3, text="L3->['0-9]F")
    gramaticaE.grid(row=9, column=4)
    gramaticaF = tk.Label(ventana3, text="F->ϵ")
    gramaticaF.grid(row=10, column=4)