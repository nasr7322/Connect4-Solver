import random
import tkinter as tk
from math import pow

# Define the MinimaxNode class
class MinimaxNode:
    def __init__(self, score, layer):
        self.score = score  # Minimax score
        self.children = []  # List of child nodes
        self.layer = layer  # Layer of the node in the tree
        self.best_move = None

    def add_child(self, child_node):
        self.children.append(child_node)

class MinimaxTree:
    def __init__(self, depth, branching_factor, root=None):
        self.depth = depth
        self.branching_factor = branching_factor
        if root:
            self.root = root
        else:
            self.root = self.create_tree()

    def create_tree(self):
        def create_node(layer):
            score = random.randint(-5, 5)  # Random score between -5 and 5
            return MinimaxNode(score, layer)

        def add_children(node, current_depth):
            if current_depth < self.depth:
                for _ in range(self.branching_factor):
                    child = create_node(current_depth + 1)
                    node.add_child(child)
                    add_children(child, current_depth + 1)

        root = create_node(0)
        add_children(root, 0)
        return root
    
    # Function to calculate node positions
    def calculate_positions(self, node, depth, x, y, y_step, positions, count, max_width):
        # Store the position of the current node
        positions[node] = (x, y)
        
        if not node.children:
            return
        
        child_y = y + y_step
        y_step *= 0.8
        x_step = max_width / (pow(self.branching_factor, depth + 1) + 1)
        child_x = x_step * count[depth + 1]
        
        for child in node.children:
            self.calculate_positions(child, depth + 1, child_x, child_y, y_step, positions, count, max_width)
            child_x += x_step
            count[depth + 1] += 1

    # Function to draw the tree on the Tkinter Canvas
    def draw_tree(self, canvas, node, positions):
        for child in node.children:
            # Draw edges
            canvas.create_line(
                positions[node][0], positions[node][1],
                positions[child][0], positions[child][1],
                fill="black",
                
            )
            self.draw_tree(canvas, child, positions)

        # Draw the node
        x, y = positions[node]
        size = 12.5
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
        canvas.create_text(x, y, text=str(round(node.score)), fill="white", font=("Arial", 10))

    def visualize(self):
        # Set the parameters for the tree
        max_depth = self.depth
        branching_factor = self.branching_factor
        
        root = self.root
        
        # Create Tkinter window
        window = tk.Tk()
        window.title("Minimax Tree Visualization")
        window.configure(bg="#FFFFFF")
        
        # Scrollbar configuration
        canvas = tk.Canvas(window, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)

        h_scrollbar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        v_scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas = tk.Canvas(canvas, bg="white",
                           xscrollcommand=h_scrollbar.set,
                           yscrollcommand=v_scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        h_scrollbar.config(command=canvas.xview)
        v_scrollbar.config(command=canvas.yview)

        # Calculate positions
        min_space = 30
        max_width = min_space * (pow(branching_factor, max_depth) + 1)
            
        positions = {}
        start_y = 50
        start_x = max_width / 2
        y_step = 150
        
        count = [1] * (max_depth + 1)  # count of nodes at each depth
        
        self.calculate_positions(root, 0, start_x, start_y, y_step, positions, count, max_width)

        # Determine canvas size
        all_x = [pos[0] for pos in positions.values()]
        all_y = [pos[1] for pos in positions.values()]

        air_gap = 50
        min_width = 800
        min_height = 600
        canvas_width = max(min_width, max(all_x) + air_gap)
        canvas_height = max(min_height, max(all_y) + air_gap)
        canvas.config(width=min_width, height=min_height, scrollregion=(0, 0, canvas_width, canvas_height))

        # Draw the tree
        self.draw_tree(canvas, root, positions)

        # Start the Tkinter event loop
        window.mainloop()

if __name__ == "__main__":
    # Initialize and start GUI
    tree = MinimaxTree(4, 7)
    tree.visualize()