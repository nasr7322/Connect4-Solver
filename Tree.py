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
    size = 20
    fill_color = "red" if node.score < 0 else "green" if node.score > 0 else "gray"

    if node.layer % 2 == 0:  # AI layer (circle)
        canvas.create_oval(
            x - size, y - size, x + size, y + size,
            fill=fill_color, outline="black"
        )
    else:  # Human layer (square)
        canvas.create_rectangle(
            x - size, y - size, x + size, y + size,
            fill=fill_color, outline="black"
        )

    # Draw the score inside the node
    canvas.create_text(x, y, text=str(node.score), fill="white", font=("Arial", 10))

# Build the tree
root = MinimaxNode(state="Root", score=0, layer=0)
ai1 = MinimaxNode(state="AI1", score=5, layer=1)
human1 = MinimaxNode(state="Human1", score=-3, layer=2)
ai2 = MinimaxNode(state="AI2", score=2, layer=3)
human2 = MinimaxNode(state="Human2", score=0, layer=4)

root.add_child(ai1)
root.add_child(human1)
ai1.add_child(ai2)
human1.add_child(human2)

# Calculate positions
positions = {}
canvas_width = 800
canvas_height = 600
calculate_positions(root, canvas_width // 2, 50, 300, 100, positions)

# Create Tkinter window
window = tk.Tk()
window.title("Minimax Tree Visualization")

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw the tree
draw_tree(canvas, root, positions)

# Start the Tkinter event loop
window.mainloop()
