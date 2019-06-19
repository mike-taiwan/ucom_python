# encoding=UTF-8
import functools
import graphviz as gv

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph()
g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


import itertools

nodes1 = list('ABCD')
edges1 = [e for e in itertools.combinations(nodes1, 2)]
g3 = add_nodes(g3, nodes1)
g3 = add_edges(g3, edges1)
g3.render('graph\\demo67_g3')

nodeA = ('A', {'label': 'Toyota'})
nodeB = ('B', {'label': 'Lexus'})
nodeC = ('C', {'label': 'Ford'})
nodeD = ('D', {'label': 'Nissan'})
nodes2 = [nodeA, nodeB, nodeC, nodeD]
g4 = add_nodes(g4, nodes2)
edgeAB = (('A', 'B'), {'label': 'same holding company'})
edgeAC = (('A', 'C'), {'label': 'popular company'})
edgeBD = (('B', 'D'), {'label': 'formula racing'})
edges2 = [edgeAB, edgeAC, edgeBD]
g4 = add_edges(g4, edges2)
g4.render('graph\\demo67_g4')


def apply_style(graph, styles):
    graph.graph_attr.update((('graph' in styles) and styles['graph']) or {})
    graph.node_attr.update((('nodes' in styles) and styles['nodes']) or {})
    graph.edge_attr.update((('edges' in styles) and styles['edges']) or {})
    return graph


styles = {'graph': {
    'label': u'家用車市場',
    'fontsize': '24',
    'fontcolor': '#002299',
    'bgcolor': '#C0FFEE',
    'rankdir': 'BT',
    'fillcolor': '#FFEEC0'},
    'nodes': {
        'fontname': 'Consolas',
        'fontsize': '24',
        'shape': 'box',
        'style': 'filled',
        'fillcolor': '#C0EEFF'
    },
    'edges': {
        'style': 'dotted',
        'color': '#442299',
        'arrowhead': 'open',
        'fontname': 'COurier',
        'fontsize': '24',
        'fontcolor': '#994422'
    }
}

g5 = digraph()
g5 = apply_style(g4, styles)
g5.render('graph\\demo67_g5')
