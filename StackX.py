# import graphviz


class StackX :
    def __init__(self, size) :
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def is_full(self) :
        return self.top == (self.size - 1)

    def is_empty(self):
        return (self.top == -1)

    def push(self, item) :
            if self.is_full():
                print("Stack is full")
            else:
                self.top += 1
                self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            item = self.stack[self.top]
           # self.stack = None
            self.top -= 1
            return item

    def peak(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

    def display(self):
        print(self.stack)

    def __str__(self):
        if self.is_empty() :
            return ""
        else:
            txt = ""
            for i in range(0, self.top+1) :
                txt += str(self.stack[i]) + " : "
            return txt




    # def visualize(self, node=None):
    #     """
    #     Create a Graphviz visualization of the stack.
    #     - Visualizes the stack as a sequence of nodes with edges connecting them.
    #     - Highlights the top item in a different style (e.g., blue box).
    #     """
    #     dot = graphviz.Digraph(format="png", graph_attr={"rankdir": "BT"})  # Left-to-right layout.
    #     for i in range(self.top + 1):  # Iterate through the stack from bottom to top.
    #         # Add a node for each stack element.
    #         if i == self.top:  # Highlight the top item.
    #             dot.node(str(i), f"{self.stack[i]} (Top)", shape="box", style="filled", color="lightblue")
    #         else:  # Normal stack elements.
    #             dot.node(str(i), str(self.stack[i]), shape="ellipse")
    #         # Add an edge between consecutive stack elements, without arrowheads.
    #         if i > 0:
    #             dot.edge(str(i - 1), str(i), dir="none")  # Connect current node to the previous node.
    #     return dot  # Return the Graphviz object for rendering or exporting.