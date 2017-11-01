import sys
import heapq
import FileReader

if len(sys.argv) != 2:
	print("Wrong number of arguments")
	print("Usage: " + sys.argv[0] + " <input-file>")
	exit(1)

nodeDict = FileReader.read(str(sys.argv[1]))

# task final order
taskOrder = []

# next nodes to process heap
nextNodeHeap = []

# find no input nodes
for nodeId, node in nodeDict.iteritems():
	if len(node.incoming.keys()) == 0:
		# add to "next to visit" heap and delete of remaining nodes
		heapq.heappush(nextNodeHeap, node)

# while there are unvisited nodes
while len(nodeDict.keys()) > 0:
	presentNode = heapq.heappop(nextNodeHeap)
	taskOrder.append(presentNode)
	# remove from unvisited nodes
	del nodeDict[presentNode.nodeId]

	for nodeId, node in presentNode.outcoming.iteritems():
		# delete incoming connection on outcoming nodes
		del node.incoming[presentNode.nodeId]
		# if node doesn't have incoming nodes, add to next heap
		if len(node.incoming.keys()) == 0:
			heapq.heappush(nextNodeHeap, node)

for task in taskOrder:
	print(task.nodeId),
