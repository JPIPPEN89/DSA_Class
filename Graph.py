import graphviz

class Graph:
    def __init__(self, directed=False):
        self.node_list = {}
        self.directed = False

    def add_node(self, node):
        if node not in self.node_list:
            self.node_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.node_list and node2 in self.node_list:
            self.node_list[node1].append(node2)
            if not self.directed:
                self.node_list[node2].append(node1)

    def display_graph(self):
        for node, neighbors in self.node_list.items():
            print(f"{node} -> {', '.join(str(n) for n in neighbors)}")

    def find_node(self, target):
        connections = self.node_list.get(target)
        return connections

    def remove_edge(self, node1, node2):
        if node1 in self.node_list and node2 in self.node_list:
            if node2 in self.node_list[node1]:
                self.node_list[node1].remove(node2)

            if not self.directed and node1 in self.node_list[node2]:
                self.node_list[node2].remove(node1)

    def remove_node(self, node):
        if node in self.node_list:
            del self.node_list[node]

        for neighbor in self.node_list.values():
            if node in neighbor:
                neighbor.remove(node)


    def visualize(self, filename="graph_output", arrow_style="none"):
        """Generates a Graphviz visualization of the graph with custom arrow styles."""
        dot = graphviz.Digraph() if self.directed else graphviz.Graph()

        # Ensure filename has no extension
        filename = filename.rsplit(".", 1)[0]

        # Convert nodes to string-safe names
        for node in self.node_list:
            dot.node(str(node))

        # Track added edges to prevent duplicates
        added_edges = set()

        for node, neighbors in self.node_list.items():
            for neighbor in neighbors:
                edge = (str(node), str(neighbor))
                reverse_edge = (str(neighbor), str(node))

                if self.directed or edge not in added_edges:
                    # Set arrow style: "none" (no arrows) or "both" (double arrows)
                    dot.edge(*edge, dir=arrow_style)

                    if not self.directed:
                        added_edges.add(edge)
                        added_edges.add(reverse_edge)

        try:
            output_path = dot.render(filename, format="png", cleanup=True)
            print(f"Graph visualization saved at: {output_path}")
        except graphviz.ExecutableNotFound:
            print("Error: Graphviz executable not found. Ensure Graphviz is installed and in your system PATH.")
