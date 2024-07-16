import os
import math
import pandas as pd

EdgeList_csv_path = os.path.abspath('/Users/hamadtria/Documents/CMI_Cours_M1/stage_M1/code/Network-Tools/data/EdgeList.csv')
NodeList_csv_path = os.path.abspath('/Users/hamadtria/Documents/CMI_Cours_M1/stage_M1/code/Network-Tools/data/NodeList.csv')

df = pd.read_csv(EdgeList_csv_path, sep=";", header=0)
nodes_df = pd.read_csv(NodeList_csv_path, sep=";", header=0)

# Merge node types for source nodes
df = df.merge(nodes_df[['_nodeID', 'viewIcon']], left_on='_sourceID', right_on='_nodeID', how='left')
df.rename(columns={'viewIcon': 'source_type'}, inplace=True)
df.drop(columns=['_nodeID'], inplace=True)

# Merge node types for target nodes
df = df.merge(nodes_df[['_nodeID', 'viewIcon']], left_on='_targetID', right_on='_nodeID', how='left')
df.rename(columns={'viewIcon': 'target_type'}, inplace=True)
df.drop(columns=['_nodeID'], inplace=True)

node_types = nodes_df['viewIcon'].unique()

nodes = set()

following_node_di = {} 
following_edges_di = {} 

followers_node_di = {} 
followers_edges_di = {}

cy_nodes = []
cy_edges = []

for i in range(1, len(df)):
    row = df.iloc[i]
    source = row.iloc[0]
    target = row.iloc[1]
    weight = row.iloc[3] if not math.isnan(float(row.iloc[3])) else '1'
    source_type = row.iloc[4]
    target_type = row.iloc[5]

    cy_edge = {"data": {"id": source + target, "source": source, "target": target, "weight": weight, "source_type": source_type, "target_type": target_type}}
    cy_target = {"data": {"id": target, "label": "User #" + str(target)}, "classes": target_type}
    cy_source = {"data": {"id": source, "label": "User #" + str(source)}, "classes": source_type}
    cy_edges.append(cy_edge)

    ############## Data wrangling for cytoscape page ##############
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