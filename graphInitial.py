import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

G = nx.DiGraph()

link_data = pd.read_csv("D:\Resilience Network\data\Link_Info.csv")
routes = {}

for i in range(len(link_data)):
    link_id = link_data["LnCode"][i]
    if(routes.get(link_id)):
        routes[link_id].append((link_data["LnkStart"][i],link_data["LnkEnd"][i]))
    else:
        routes[link_id] = [(link_data["LnkStart"][i],link_data["LnkEnd"][i])]
    print("{}\t{}".format(link_data["LnkStart"][i],link_data["LnkEnd"][i]))
    G.add_edge(link_data["LnkStart"][i],link_data["LnkEnd"][i])
#
# G.add_node(1)
# G.add_nodes_from([2,3])
# G.add_edges_from([(1,2),(1,3)])
# print(G.nodes)
# data = nx.spring_layout(G)
# print(G.edges)
# nx.draw_networkx_nodes(G,data,cmap = plt.get_cmap("jet"))
# nx.draw_networkx_edges(G,data,G.edges)
# plt.show()

data = nx.spring_layout(G)
plt.figure(figsize = (30,30))
print(G.edges)
nx.draw_networkx_nodes(G,data,cmap = plt.get_cmap("Paired"))
nx.draw_networkx_labels(G,data)
colors = ["r","b","k","c","y","m","g"]
for i,k in enumerate(routes.keys()):
    nx.draw_networkx_edges(G,data,routes[k],edge_color = colors[i % 7],edge_cmap = plt.cm.Blues)
plt.savefig("D:\Resilience Network\graph_trains.png")
plt.show()

stat_set = set()

for stat in link_data["LnkStart"]:
    stat_set.add(stat)


print(stat_set)
print(len(stat_set))
nx.write_graphml(G,"D:\Resilience Network\graphInitial.graphml")