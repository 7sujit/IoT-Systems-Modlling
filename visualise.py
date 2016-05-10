#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(Actor, UseCase, node_pairs):
    u = []
    d = []
    G = nx.DiGraph()
    _g = nx.Graph();
    _g.add_edges_from(node_pairs);
    nl = _g.nodes();
    offset=0.1
    for item in node_pairs:
        x = (item[1], item[0])
        if(x in node_pairs):
            u.append(item)
        else:
            d.append(item)
    G.add_nodes_from(nl)
    pos = nx.shell_layout(G)
    print u
    print '=================='
    print d
    # nx.draw(G, pos, font_size = 8, with_labels=False, node_color='m')
    # nx.draw_networkx_nodes(G, pos, nodelist = nl, node_color = 'm');
    nx.draw_networkx_nodes(G, pos, nodelist = Actor.values(), node_color = 'm');
    nx.draw_networkx_nodes(G, pos, nodelist = UseCase.values(), node_color = 'y');
    nx.draw_networkx_edges(G, pos, edgelist = u, edge_color='r', arrows=False)
    nx.draw_networkx_edges(G, pos, edgelist = d, edge_color='g', arrows=True)
    for p in pos:
        pos[p][1] -= offset
    nx.draw_networkx_labels(G,pos,font_size=10,font_color='b' )
    # plt.savefig("figure_1.png")
    plt.show()



if __name__ == '__main__':
    array = [ str(i) for i in range(3)]
    draw_graph(array)
