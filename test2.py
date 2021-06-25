import networkx as nx
import pydot
import os
from collections import defaultdict
import matplotlib.pyplot as plt
class Visualize_Tree():
    def __init__(self,image_name) -> None:
        self.graph = nx.Graph()
        self.image_name = image_name
        self.nodes = 0
        self.attribute_id = defaultdict(lambda: len(self.attribute_id))

    def add_node(self,attribute_name,attribute_bool):
        #update attribute
        self.attribute_id[attribute_name]
        #get current attribute id
        current_id = self.attribute_id[attribute_name]

        my_node = self.graph.add_node(attribute_name)
        # my_node = pydot.Node(current_id, label=attribute_name)
        # self.graph.add_node(my_node)        

        #make edge when node is already there
        if (self.graph.number_of_nodes()) >1:            
            self.add_edge(self.previous_id,current_id)
        
        self.previous_id = attribute_name

    def add_edge(self,previous_id,current_id):
        # my_edge = pydot.Edge(previous_id,current_id,label=True)
        self.graph.add_edge(previous_id,current_id)
        nx.draw(self.graph,with_labels=True,font_weight="bold")
        plt.savefig("path.png")
        # self.graph.add_edge(my_edge)
        # self.graph.write_png(f'data/cub/decision_tree/output_{self.image_name}.png')

tree1 = Visualize_Tree("image1")
tree1.add_node("Attribute_name: has_leg_color::olive ",True)
tree1.add_node("Attribute_name: has_leg_color::oliv2e ",False)
tree1.add_node("Attribute_name: has_leg_color::ol3ive ",True)
# G = nx.Graph()

# G.add_node(1)

# G.add_edge("bnearbagbe", 2)
# e = (2, 3)
# G.add_edge(*e)  # unpack edge tuple*

# print(G.number_of_nodes())



# nx.draw(G,with_labels=True,font_weight="bold")
# plt.savefig("path.png")