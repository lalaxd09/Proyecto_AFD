import networkx as nx
import matplotlib.pyplot as plt
import pylab
from funcion import*
from correo_recorrer import*
import matplotlib.patches as mpatches
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk



def diagrama_correo_electronico(correo):
    transciones_main = datos_automata(correo)
    G = nx.DiGraph()
    estados=['S','A','C','P','E']
    #print(transciones_main[0])


    G.add_edges_from([(estados[0],estados[1])],label=transciones_main[0])
    G.add_edges_from([(estados[1],estados[2])],label=transciones_main[1])
    G.add_edges_from([(estados[2],estados[3])],label=transciones_main[2])
    G.add_edges_from([(estados[3],estados[4])],label=transciones_main[3])


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
    #print(edge_labels)
#red_edges = [('C','D'),('D','A')]
    edge_colors=['black']
#edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    f = plt.Figure(figsize=(5, 5), dpi=100)
    pos=nx.spring_layout(G,seed=5)#print(pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=.5,font_size=10)
    nx.draw(G,pos, node_color =values ,with_labels=True, node_size=1000,edge_color=edge_colors,connectionstyle='arc3, rad = 0.1')#edge_cmap=plt.cm.Reds)

    estado_inical = mpatches.Patch(color='Green', label='Estado inicial')
    estado_final=mpatches.Patch(color='Blue', label=' Estado Final')
    plt.legend(handles=[estado_inical,estado_final])

    plt.show()

    return f


def ventana2():
    ventana2 = tk.Toplevel()
    ventana2.title('Correo Electronico')
    etiqueta = tk.Label(ventana2, text='Validación de correo electronico')
    etiqueta.grid(row=1,column=4)
    entrada = tk.Entry(ventana2)
    entrada.grid(row=2,column=4)
    button1 = tk.Button(ventana2, text='Inciar',command=lambda: c_electronico(entrada.get()))
    button1.grid(row=3,column=4)
    tituloG=tk.Label(ventana2,text='Gramatica')
    tituloG.grid(row=4, column=4)
    gramatica=tk.Label(ventana2,text='S->[/w]A')
    gramatica.grid(row=5,column=4)
    gramaticaA = tk.Label(ventana2, text="A->['@']C")
    gramaticaA.grid(row=6, column=4)
    gramaticaC = tk.Label(ventana2, text='C->[A-Z]P')
    gramaticaC.grid(row=7, column=4)
    gramaticaP= tk.Label(ventana2, text="A->['.'][A-Z]E")
    gramaticaP.grid(row=8, column=4)
    gramaticaE = tk.Label(ventana2, text="E->ϵ")
    gramaticaE.grid(row=9, column=4)

    # create matplotlib canvas using figure `f` and assign to widget `window`
    #canvas = FigureCanvasTkAgg(c_electronico(entrada.get()), ventana2)

    # get canvas as tkinter's widget and `gird` in widget `window`
    #canvas.get_tk_widget().grid(row=10, column=4)


# get canvas as tkinter's widget and `gird` in widget `window`

