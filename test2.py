import csv
import numpy as np

a = np.zeros(100)
print(list(a))
f = open("data/cub/attributes.txt", "r")
names = []



for i, line in enumerate(f):
    # if(i==attribute_idx[image_id]-1):
    attribute_name = line[3:].replace('\n','').replace(" ","")
    names.append(attribute_name)


with open ("data/cub/decision_tree/decision.csv","w",newline="") as file:
    writer = csv.writer(file)
    names.append("true_class_id")
    writer.writerow(names)
    # writer.writerow(["a",3,54,5])

