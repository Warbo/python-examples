import pydot, pickle, random, math, sys, os

if os.path.exists(sys.argv[1]):
	file = open(sys.argv[1], 'r')
	graph = pickle.load(file)
	file.close()
else:
	graph = pydot.Dot(name='Graph')

for x in range(2, len(sys.argv), 2):
	graph.add_edge(pydot.Edge(sys.argv[x], sys.argv[x + 1]))

graph.write_png('graph.png', prog='dot')

file = open(sys.argv[1], 'w')
pickle.dump(graph, file)
file.close()
