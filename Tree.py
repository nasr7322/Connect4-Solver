import random
import tkinter as tk
from math import pow

# Define the MinimaxNode class
class MinimaxNode:
    def __init__(self,score, layer):
        self.score = score  # Minimax score
        self.children = []  # List of child nodes
        self.layer = layer  # Layer of the node in the tree

    def add_child(self, child_node):
        self.children.append(child_node)

# Function to calculate node positions
def calculate_positions(node,depth, p, x, y, y_step, positions, count, max_width):
    # Store the position of the current node
    positions[node] = (x, y)
    
    if node.children == []:
        return
    
    child_y = y + y_step
    x_step = max_width // (pow(p, depth + 1) + 1)
    child_x = x_step*count[depth+1]
    index = 0
    for child in node.children:
        calculate_positions(child , depth+1 , 7, child_x,child_y,y_step, positions, count, max_width)
        child_x += x_step
        count[depth+1]+=1
    
# Function to draw the tree on the Tkinter Canvas
def draw_tree(canvas, node, positions):
    for child in node.children:
        # Draw edges
        canvas.create_line(
            positions[node][0], positions[node][1],
            positions[child][0], positions[child][1],
            fill="black"
        )
        draw_tree(canvas, child, positions)

    # Draw the node
    x, y = positions[node]
    size = 10
    fill_color = "red" if node.score < 0 else "green" if node.score > 0 else "gray"

    if node.layer % 2 == 0:  # AI layer (circle)
        canvas.create_oval(
            x - size, y - size, x + size, y + size,
            fill=fill_color, outline=fill_color
        )
    else:  # Human layer (square)
        canvas.create_rectangle(
            x - size, y - size, x + size, y + size,
            fill=fill_color, outline=fill_color
        )

    # Draw the score inside the node
    canvas.create_text(x, y, text=str(node.score), fill="white", font=("Arial", 10))

def create_tree(depth, branch_factor):
    def create_node(layer):
        score = random.randint(-5, 5)  # Random score between -5 and 5
        return MinimaxNode(score, layer)

    def add_children(node, current_depth):
        if current_depth < depth:
            for _ in range(branch_factor):
                child = create_node(current_depth + 1)
                node.add_child(child)
                add_children(child, current_depth + 1)

    root = create_node(0)
    add_children(root, 0)
    return root

def StartGui(k,root=None):
    
    # Set the parameters for the tree
    max_depth = k ##k
    branching_factor = 7 ##p
    if root is None: ##Example Tree:
        root = create_tree(max_depth, branching_factor)
    
    # Create Tkinter window
    window = tk.Tk()
    window.title("Minimax Tree Visualization")

    # Scrollbar configuration
    canvas_frame = tk.Frame(window)
    canvas_frame.pack(fill=tk.BOTH, expand=True)

    h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(canvas_frame, bg="white",
                    xscrollcommand=h_scrollbar.set,
                    yscrollcommand=v_scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    h_scrollbar.config(command=canvas.xview)
    v_scrollbar.config(command=canvas.yview)

    # Calculate positions
    positions = {}

    max_width = 1000
    ##if the minimum width between nodes is less than 30, set it to 30
    if(max_width//(pow(branching_factor,max_depth)+1) < 30):
        max_width = 30*(pow(branching_factor,max_depth)+1)
        
    positions = {}
    y_step = 150
    
    count = [1]*(max_depth+1) ##count of nodes at each depth
    
    calculate_positions(root, 0, branching_factor, max_width/2, 100, y_step, positions, count, max_width)

    # determine canvas size
    all_x = [pos[0] for pos in positions.values()]
    all_y = [pos[1] for pos in positions.values()]

    canvas_width = max(800, max(all_x)+50)
    canvas_height = max(600, max(all_y)+100)
    canvas.config(width=800,height=600,scrollregion=(0, 0, canvas_width, canvas_height))

    # Draw the tree
    draw_tree(canvas, root, positions)

    # Start the Tkinter event loop
    window.mainloop()
    
StartGui(4)