%pip install gurobipy

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import networkx as nx

arquivo="Fluxo_maximo_6_8.txt"

with open(arquivo, "r") as f:
    linhas = f.readlines()

vertice,arcos =linhas[0].split()
vertice_ori,vertice_dis=linhas[1].split()

vertice=int(vertice)
arcos=int(arcos)
vertice_ori=int(vertice_ori)
vertice_dis=int(vertice_dis)

vertices_de_para=np.zeros((arcos, 3))

for i in range(arcos):
  for j in range(3):
    vertices_de_para[i,j]=int(linhas[i + 2].split()[j])


graph = nx.DiGraph()
for i in range(arcos):
  graph.add_edge(vertices_de_para[i][0], vertices_de_para[i][1], capacity=int(vertices_de_para[i][2]))

graph.sources = [vertice_ori]

m = gp.Model()



x = m.addVars(graph.edges, vtype=GRB.CONTINUOUS, name="x")
for i in graph.nodes:
  if i not in graph.sources:
    m.addConstr(sum(x[i, j] for j in graph.nodes if (i, j) in graph.edges) - sum(x[j, i] for j in graph.nodes if (j, i) in graph.edges) == 0, "flow_conservation_%s" % i)


for i, j in graph.edges:
  m.addConstr(x[i, j] <= graph.get_edge_data(i, j)['capacity'])

# Set the objective
m.setObjective(sum(x[i, j] for i in graph.nodes for j in graph.nodes if (i, j) in graph.edges), GRB.MAXIMIZE)

# Solve the model
m.optimize()

# Print the solution
if m.status == GRB.OPTIMAL:
  print("O fluxo maximo é", m.objVal)
  for i in graph.nodes:
    for j in graph.nodes:
      if (i, j) in graph.edges:
        print("O fluxo de %s para %s é %g" % (i, j, x[i, j].x))
