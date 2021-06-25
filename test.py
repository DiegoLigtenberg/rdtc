from typing import DefaultDict
import pydot
import os
from collections import defaultdict
os.environ["PATH"] += os.pathsep + r"C:\Users\diego\anaconda3\envs\rdtc\Lib\site-packages"


class Visualize_Tree():
    def __init__(self,image_name) -> None:
        self.graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white')
        self.image_name = image_name
        self.nodes = 0
        self.attribute_id = defaultdict(lambda: len(self.attribute_id))

    def add_node(self,attribute_name,attribute_bool):
        #update attribute
        self.attribute_id[attribute_name]
        #get current attribute id
        current_id = self.attribute_id[attribute_name]

        my_node = pydot.Node(current_id, label=attribute_name)        
        self.graph.add_node(my_node)        

        #make edge when node is already there
        if len(self.attribute_id) >1:            
            self.add_edge(self.previous_id,current_id)
        
        self.previous_id = current_id

    def add_edge(self,previous_id,current_id):
        my_edge = pydot.Edge(previous_id,current_id,label=True)
        self.graph.add_edge(my_edge)
        self.graph.write_png(f'data/cub/decision_tree/output_{self.image_name}.png')



treelist = []
tree1 = Visualize_Tree("image1")
tree1.add_node("Attribute_name: has_leg_color::olive ",True)
tree1.add_node("Attribute_name: has_leg_color::oliv2e ",True)
tree1.add_node("Attribute_name: has_leg_color::ol3ive ",True)
# print(Visualize_Tree.get_val())
# tree1.add_node("is is happy",True)
# tree1.add_node("is black",False)
# tree1.add_node("is black",False)
# tree1.add_node("is red",False)
# tree1.add_node("is red",False)
# tree1.add_node("is black",False)
newstr=[]
for i in range (0,5):
    newstr.append(str(i))
newstr = "".join(newstr)
print((newstr))
# d = defaultdict(lambda: len(d))
# d["bird is white"] 
# d["bird is red"] 
# d["bird is red"] 

# print(d)




# graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white')

# # Add nodes
# my_node = pydot.Node('a', label='head is black')
# graph.add_node(my_node)
# # Or, without using an intermediate variable:
# graph.add_node(pydot.Node('b', shape='circle'))

# my_node = pydot.Node('q', label='head is black')
# graph.add_node(my_node)
# # Or, without using an intermediate variable:
# graph.add_node(pydot.Node('z', shape='circle'))


# # Add edges
# # my_edge = pydot.Edge('a', 'b', color='true')
# my_edge = pydot.Edge('a', 'b', label=True)
# graph.add_edge(my_edge)
# # Or, without using an intermediate variable:
# graph.add_edge(pydot.Edge('b', 'q', label=False))

# # Or, without using an intermediate variable:
# graph.add_edge(pydot.Edge('b', 'c', label=False))
# # Or, without using an intermediate variable:
# graph.add_edge(pydot.Edge('c', '', label=False))
# graph.write_png('output.png')