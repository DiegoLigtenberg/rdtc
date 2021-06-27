import csv
from matplotlib import image
from numpy.core.fromnumeric import shape
import pydot
import os
from collections import defaultdict
from graphviz import Digraph

os.environ["PATH"] += os.pathsep + r"C:\Users\diego\anaconda3\envs\rdtc\Lib\site-packages\graphviz"

class Visualize_Tree():
    def __init__(self,image_name) -> None:
        self.graph = Digraph(format='png')
        self.image_name = image_name
        self.nodes = 0
        self.attribute_id = defaultdict(lambda: len(self.attribute_id))

    def add_node(self,attribute_name,attribute_bool):
        #update attribute
        self.attribute_id[attribute_name]
        #get current attribute id
        current_id = self.attribute_id[attribute_name]
        self.attribute_bool = attribute_bool
        self.attribute_name = attribute_name

        #initialize current image
        self.graph.node(str(current_id),'',shape='plain') 
        self.graph.node(str(current_id),image='ground_truth.png')

        #initalize next image
        self.graph.node(str(current_id+1),'',shape='plain') 
        self.graph.node(str(current_id+1),image='ground_truth.png')

        #initialize bar chart
        self.graph.node(str(attribute_name),'',shape='plain')
        self.graph.node(str(attribute_name),image='ground_table.png')       
        
        #make edge when node is already there
        if len(self.attribute_id) >0:            
            self.add_edge(str(current_id),str(current_id+1))
            self.add_edge_bar(str(current_id),str(attribute_name))
    
        self.previous_name = attribute_name

    def add_edge(self,previous_id,current_id):
        self.graph.edge(previous_id,current_id,label=f'{self.attribute_name}={str(self.attribute_bool)}')
        self.graph.render(f'output_')
    
    def add_edge_bar(self,previous_id,current_id):
        self.graph.edge(previous_id,current_id)
        self.graph.render(f'output_')
        # self.graph.write_png(f'data/cub/decision_tree/output_{self.image_name}.png')


tree1 = Visualize_Tree("image1")
tree1.add_node("Attribute_name has_leg_colorolive ",str(True))
tree1.add_node("Attribute_name has_leg_coloroliv2e ",str(True))
tree1.add_node("Attribute_name has_leg_colorol3ive ",str(False))
tree1.add_node("Attribute_name has_leg3_colorol3ive ",str(False))
import matplotlib.pyplot as plt

# # Create a Simple Bar Plot of Three People's Ages

# # Create a List of Labels for x-axis
# names = ["Brad", "Bill", "Bob"]

# # Create a List of Values (Same Length as Names List)
# ages = [9, 5, 10]

# # Make the Chart
# plt.bar(names, ages)

# # Show the Chart
# plt.show()


# G = Digraph(format='png')


# G.node('A', 'King Arthur')
# G.node('A',image='output.png')
# G.node('B', 'Sir Bedevere the Wise')
# G.node('L', 'Sir Lancelot the Brave')

# G.edges(['AB', 'AL'])
# G.edge('B', 'L', constraint='false',label="0.5 0.3  0.2")


# G.render('output2',view=True)










# region
# for i, line in enumerate(f):
#     # if(i==attribute_idx[image_id]-1):
#     attribute_name = line[3:].replace('\n','').replace(" ","")
#     names.append(attribute_name)


# with open ("data/cub/decision_tree/decision.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     names.append("true_class_id")
#     writer.writerow(names)
#     # writer.writerow(["a",3,54,5])
# endregion