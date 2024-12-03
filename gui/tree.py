import random
import tkinter as tk
from math import pow

# Define the MinimaxNode class
class MinimaxNode:
    def __init__(self, score, player):
        self.score = score  # Minimax score
        self.children = []  # List of child nodes
        self.player = player  # Node type (1: AI, 2: Player, 3: AI Prob, 4: Player Prob)
        self.best_move = None

    def add_child(self, child_node):
        self.children.append(child_node)

class MinimaxTree:
    def __init__(self, depth, branching_factor, mode, root=None):
        self.depth = depth
        self.branching_factor = branching_factor
        self.ai_mode = mode  # 1: Normal Minimax, 2: Expected Minimax
        if root:
            self.root = root
        else:
            self.root = self.create_tree()

    def create_node(self, player):
        score = random.randint(-5, 5)  # Random score between -5 and 5
        return MinimaxNode(score, player)

    def add_children(self, node, current_depth, player):
        # Define the next player type
        if self.ai_mode == 2:  # Expected minimax
            if player == 1:
                next_player = 3
            elif player == 2:
                next_player = 4
            elif player == 3:
                next_player = 2
            elif player == 4:
                next_player = 1
        else:  # Regular minimax
            next_player = 1 if player == 2 else 2

        if current_depth < self.depth:
            for _ in range(self.branching_factor):
                child = self.create_node(next_player)
                node.add_child(child)
                self.add_children(child, current_depth + 1, next_player)

    def create_tree(self):
        root = self.create_node(1)  # Start with AI node
        self.add_children(root, 0, 1)
        return root

    # Function to calculate node positions
    def calculate_positions(self, node, depth, x, y, y_step, positions, max_width):
        positions[node] = (x, y)

        if not node.children:
            return

        total_children = len(node.children)
        total_spacing = max_width / pow(self.branching_factor, depth + 1)
        start_x = x - (total_children - 1) * total_spacing / 2

        for i, child in enumerate(node.children):
            child_x = start_x + i * total_spacing
            child_y = y + y_step
            self.calculate_positions(child, depth + 1, child_x, child_y, y_step, positions, max_width)

    # Function to draw the tree on the Tkinter Canvas
    def draw_tree(self, canvas, node, positions):
        for child in node.children:
            canvas.create_line(
                positions[node][0], positions[node][1],
                positions[child][0], positions[child][1],
                fill="black",
            )
            self.draw_tree(canvas, child, positions)

        x, y = positions[node]
        size = 12.5
        color_map = {
            1: "#FF9D00",  # AI node (circle)
            2: "#D01466",  # Player node (square)
            3: "#14D0AA",  # AI probability node (dashed circle)
            4: "#AA9DFF",  # Player probability node (dashed square)
        }
        if self.ai_mode != 2:
            if (node.player % 2) == 1:
                fill_color = color_map.get(1)
            elif (node.player % 2) == 0:
                fill_color = color_map.get(2)
            else:
                fill_color = 'gray'
        else:
            fill_color = color_map.get(node.player, "gray")

        if node.player == 1 or node.player == 3:  # AI or AI probability (circle)
            canvas.create_oval(
                x - size, y - size, x + size, y + size,
                fill=fill_color, outline=fill_color
            )
        else:  # Player or Player probability (square)
            canvas.create_rectangle(
                x - size, y - size, x + size, y + size,
                fill=fill_color, outline=fill_color
            )

        # Draw the score inside the node
        canvas.create_text(x, y, text=str(round(node.score)), fill="white", font=("Arial", 10))

    def calculate_max_width(self):
        from collections import deque

        queue = deque([(self.root, 0)])  # (node, depth)
        layer_counts = {}

        while queue:
            node, depth = queue.popleft()
            if depth not in layer_counts:
                layer_counts[depth] = 0
            layer_counts[depth] += 1

            for child in node.children:
                queue.append((child, depth + 1))

        return max(layer_counts.values())

    def visualize(self):
        root = self.root

        window = tk.Tk()
        window.title("Minimax Tree Visualization")
        window.configure(bg="#FFFFFF")

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

        min_space = 30
        max_width = min_space * (pow(self.branching_factor,self.depth) + 3)

        positions = {}
        start_y = 200
        start_x = max_width / 2
        y_step = 200

        self.calculate_positions(root, 0, start_x, start_y, y_step, positions, max_width)

        all_x = [pos[0] for pos in positions.values()]
        all_y = [pos[1] for pos in positions.values()]

        air_gap = 100
        min_width = 1000
        min_height = 700
        canvas_width = max(min_width, max(all_x) + air_gap)
        canvas_height = max(min_height, max(all_y) + air_gap)
        canvas.config(width=min_width, height=min_height, scrollregion=(0, 0, canvas_width, canvas_height))

        self.draw_tree(canvas, root, positions)

        def zoom(event):
            scale = 1.2 if event.delta > 0 else 0.8
            canvas.scale("all", 0, 0, scale, scale)
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<MouseWheel>", zoom)

        window.mainloop()

if __name__ == "__main__":
    tree = MinimaxTree(4, 7, 1)  # Depth 4, branching factor 3, expected minimax mode 2
    tree.visualize()
