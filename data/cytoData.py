import os
import math
import pandas as pd

csv_path = os.path.abspath('/Users/hamadtria/Documents/CMI_Cours_M1/stage M1/code/Network-Tools/data/EdgeList.csv')
df = pd.read_csv(csv_path, sep=";", header = None)

nodes = set()

following_node_di = {} 
following_edges_di = {} 

followers_node_di = {} 
followers_edges_di = {}

cy_nodes = []

for i in range(1, len(df)):
    row = df.iloc[i]
    source = row[0]
    target = row[1]
    weight = row[3] if not math.isnan(float(row[3])) else '1'

    cy_edge = {"data": {"id": source + target, "source": source, "target": target, "weight": weight}}
    cy_target = {"data": {"id": target, "label": "User #" + str(target)}}
    cy_source = {"data": {"id": source, "label": "User #" + str(source)}}

    if source not in nodes:
        nodes.add(source)
        cy_nodes.append(cy_source)
    if target not in nodes:
        nodes.add(target)
        cy_nodes.append(cy_target)

    if not following_node_di.get(source):
        following_node_di[source] = []
    if not following_edges_di.get(source):
        following_edges_di[source] = []

    following_node_di[source].append(cy_target)
    following_edges_di[source].append(cy_edge)

    if not followers_node_di.get(target):
        followers_node_di[target] = []
    if not followers_edges_di.get(target):
        followers_edges_di[target] = []

    followers_node_di[target].append(cy_source)
    followers_edges_di[target].append(cy_edge)

    if source == "100XEIGILMBMSDQ@Facebook":
        genesis_node = cy_source
        genesis_node["classes"] = "genesis"
        default_elements = [genesis_node]