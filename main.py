import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
data = pd.read_csv('friends.csv')
friends_graph = nx.from_pandas_edgelist(data, source='ID', target='friendID')

print(nx.draw_networkx(friends_graph))
plt.show()

most_influential = nx.degree_centrality(friends_graph)
most_influential = sorted(most_influential, key=most_influential.get, reverse=True)
print('самый цениральный по степенной центральности:', most_influential[0])

most_influential1 = nx.eigenvector_centrality(friends_graph, max_iter=2500)
most_influential1 = sorted(most_influential1, key=most_influential1.get, reverse=True)
print('самый центральный по собственному вектору', most_influential1[0])

most_influential2 = nx.betweenness_centrality(friends_graph)
most_influential2 = sorted(most_influential2, key=most_influential2.get, reverse=True)
print('самый центральный по посредничеству', most_influential2[0])

most_influential3 = nx.closeness_centrality(friends_graph)
most_influential3 = sorted(most_influential3, key=most_influential3.get, reverse=True)
print('самый центральный по близости', most_influential3[0])
