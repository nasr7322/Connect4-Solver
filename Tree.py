import tkinter as tk
from math import pow

# Define the MinimaxNode class
class MinimaxNode:
    def __init__(self, state, score, layer):
        self.state = state  # The Connect 4 board state or relevant data
        self.score = score  # Minimax score
        self.children = []  # List of child nodes
        self.layer = layer  # Layer of the tree (0 = root, 1 = AI, 2 = human, etc.)

    def add_child(self, child_node):
        self.children.append(child_node)

# Function to calculate node positions
def calculate_positions(node, x, y, x_step, y_step, positions, parent_position=None):
    positions[node] = (x, y)
    num_children = len(node.children)
    if num_children > 1:
        x_step = 50

    start_x = x - (num_children - 1) * x_step / 2
    for i, child in enumerate(node.children):
        child_x = start_x + i * x_step
        child_y = y + y_step
        calculate_positions(child, child_x, child_y, x_step / 2, y_step, positions, (x, y))

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

# Build the tree
root = MinimaxNode(state="Root", score=0, layer=0)
human0 = MinimaxNode(state="Col0", score=2, layer=1)
human1 = MinimaxNode(state="Col1", score=0, layer=1)
human2 = MinimaxNode(state="Col2", score=-1, layer=1)
human3 = MinimaxNode(state="Col3", score=0, layer=1)
human4 = MinimaxNode(state="Col4", score=-3, layer=1)
human5 = MinimaxNode(state="Col5", score=4, layer=1)
human6 = MinimaxNode(state="Col6", score=1, layer=1)

root.add_child(human0)
root.add_child(human1)
root.add_child(human2)
root.add_child(human3)
root.add_child(human4)
root.add_child(human5)
root.add_child(human6)

ai0 = MinimaxNode(state="AI0", score=3, layer=2)
ai1 = MinimaxNode(state="AI1", score=-2, layer=2)
ai2 = MinimaxNode(state="AI2", score=1, layer=2)
ai3 = MinimaxNode(state="AI3", score=0, layer=2)
ai4 = MinimaxNode(state="AI4", score=-1, layer=2)
ai5 = MinimaxNode(state="AI5", score=2, layer=2)
ai6 = MinimaxNode(state="AI6", score=4, layer=2)
ai7 = MinimaxNode(state="AI7", score=3, layer=2)
ai8 = MinimaxNode(state="AI8", score=-2, layer=2)
ai9 = MinimaxNode(state="AI9", score=1, layer=2)
ai10 = MinimaxNode(state="AI10", score=0, layer=2)
ai11 = MinimaxNode(state="AI11", score=-1, layer=2)
ai12 = MinimaxNode(state="AI12", score=2, layer=2)
ai13 = MinimaxNode(state="AI13", score=4, layer=2)


human0.add_child(ai0)
human0.add_child(ai1)
human0.add_child(ai2)
human1.add_child(ai3)
human2.add_child(ai4)
human2.add_child(ai5)
human3.add_child(ai6)
human3.add_child(ai7)
human3.add_child(ai8)
human5.add_child(ai9)
human6.add_child(ai10)
human6.add_child(ai11)
human6.add_child(ai12)
human6.add_child(ai13)

# Calculate positions
positions = {}
canvas_width = 800
canvas_height = 600
calculate_positions(root, canvas_width // 2, 50, 300, 100, positions)

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

# Calculate positions and determine canvas bounds
positions = {}
x_step_initial = 300  # Adjust for initial horizontal spacing
y_step = 100  # Vertical spacing
calculate_positions(root, 400, 50, x_step_initial, y_step, positions)

# Dynamically determine canvas size
all_x = [pos[0] for pos in positions.values()]
all_y = [pos[1] for pos in positions.values()]

canvas_width = max(800, max(all_x) + 100)
canvas_height = max(600, max(all_y) + 100)

canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

# Draw the tree
draw_tree(canvas, root, positions)

# Start the Tkinter event loop
window.mainloop()