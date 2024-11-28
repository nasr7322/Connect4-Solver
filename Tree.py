import plotly.graph_objects as go
from igraph import Graph, EdgeSeq

# Define the MinimaxNode class
class MinimaxNode:
    def __init__(self, state, score, layer):
        self.state = state  # The Connect 4 board state or relevant data
        self.score = score  # Minimax score
        self.children = []  # List of child nodes
        self.layer = layer  # Layer of the tree (0 = root, 1 = AI, 2 = human, etc.)

    def add_child(self, child_node):
        self.children.append(child_node)

# Function to build the graph
def build_graph(node, graph, parent_id=None):
    node_id = len(graph.vs)
    graph.add_vertex(name=node.state, score=node.score, layer=node.layer)

    if parent_id is not None:
        graph.add_edge(parent_id, node_id)

    for child in node.children:
        build_graph(child, graph, node_id)

# Function to visualize the graph
def visualize_graph(graph):
    layout = graph.layout("rt")  # Reingold-Tilford layout for trees

    # Extract positions and edges
    positions = {k: layout[k] for k in range(len(graph.vs))}
    Xn = [positions[k][0] for k in range(len(graph.vs))]
    Yn = [-positions[k][1] for k in range(len(graph.vs))]  # Flip y-axis for top-down
    Xe = []
    Ye = []

    for edge in graph.es:
        Xe += [positions[edge.source][0], positions[edge.target][0], None]
        Ye += [-positions[edge.source][1], -positions[edge.target][1], None]  # Flip y-axis

    # Configure node appearance
    shapes = []
    colors = []
    texts = []
    for v in graph.vs:
        score = v["score"]
        layer = v["layer"]

        # Node shape and color
        if layer % 2 == 0:  # AI layer
            shapes.append("circle")
        else:  # Human layer
            shapes.append("square")

        if score < 0:
            colors.append("red")
        elif score > 0:
            colors.append("green")
        else:
            colors.append("gray")

        # Node label
        texts.append(f"{v['name']}: {score}")

    # Create traces
    edge_trace = go.Scatter(
        x=Xe,
        y=Ye,
        mode='lines',
        line=dict(color='rgb(210,210,210)', width=1),
        hoverinfo='none'
    )

    node_trace = go.Scatter(
        x=Xn,
        y=Yn,
        mode='markers+text',
        text=texts,
        textposition='top center',
        marker=dict(
            size=20,
            color=colors,
            symbol=shapes,
            line=dict(color='rgb(50,50,50)', width=1)
        )
    )

    # Layout and figure
    layout = go.Layout(
        title="Minimax Tree Visualization",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        showlegend=False,
        margin=dict(l=40, r=40, b=85, t=100),
        hovermode='closest'
    )

    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
    fig.update_layout(plot_bgcolor='rgb(248,248,248)')
    fig.show()

# Define the tree
root = MinimaxNode(state="Root", score=0, layer=0)
ai1 = MinimaxNode(state="AI1", score=5, layer=1)
human1 = MinimaxNode(state="Human1", score=-3, layer=2)
ai2 = MinimaxNode(state="AI2", score=2, layer=3)
human2 = MinimaxNode(state="Human2", score=0, layer=4)

root.add_child(ai1)
root.add_child(human1)
ai1.add_child(ai2)
human1.add_child(human2)

# Build and visualize the graph
graph = Graph(directed=True)
build_graph(root, graph)
visualize_graph(graph)
