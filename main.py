import matplotlib.pyplot as plt
import networkx as nx
import statistics
import time
import itertools
from networkx import triadic_census

edge1 = []
edge2 = []

t = open("twitter_combined_result.txt", "r")
for row in t:
    row = row.split(' ')
    edge1.append(int(row[0]))
    edge2.append(int(row[1]))

G_symmetric = nx.Graph().to_undirected()
# print(edge1)
# print(edge2)

i = 0
while i < len(edge1):
    G_symmetric.add_edge(edge1[i], edge2[i])
    i += 1


plt.figure(figsize=(5,5))
nx.draw_networkx(G_symmetric)
plt.show()

deg_centrality = nx.degree_centrality(G_symmetric)
print("Dataset Degree Centrality: ")
print(deg_centrality)

close_centrality = nx.closeness_centrality(G_symmetric)
print("Dataset Closeness Centrality: ")
print(close_centrality)

bet_centrality = nx.betweenness_centrality(G_symmetric, normalized=True,
                                           endpoints=False)
print("Dataset Betweeness Centrality: ")
print(bet_centrality)


def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()


# plot_degree_dist(nx.gnp_random_graph(100, 0.5, directed=True))
plot_degree_dist(G_symmetric)
plt.show()

def betweenness_plot_degree_dist(G):
    bet_centrality1 = nx.betweenness_centrality(G_symmetric, normalized=True,
                                               endpoints=False)
    plt.hist(bet_centrality1)
    plt.show()


betweenness_plot_degree_dist(G_symmetric)
plt.show()


def closeness_plot_degree_dist(G):
    close_centrality1 = nx.closeness_centrality(G_symmetric)
    plt.hist(close_centrality1)
    plt.show()


closeness_plot_degree_dist(G_symmetric)
plt.show()

print("Mean: Closeness Centrality: ")
meanStatClose = statistics.mean(close_centrality)
print(meanStatClose)
print("Mean: Betweenness Centrality: ")
meanStatBetw = statistics.mean(bet_centrality)
print(meanStatBetw)
print("Median: Closeness Centrality: ")
medianStatClose = statistics.median(close_centrality)
print(medianStatClose)
print("Median: Betweenness Centrality: ")
medianStatBetw = statistics.median(bet_centrality)
print(medianStatBetw)
print("Standard: Closeness Centrality: ")
standardDevStatClose = statistics.stdev(close_centrality)
print(standardDevStatClose)
print("Standard Deviation: Betweenness Centrality: ")
standardDevStatBetw = statistics.stdev(bet_centrality)
print(standardDevStatBetw)

