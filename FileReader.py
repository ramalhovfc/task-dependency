import os
import re
import Node
spaceSplitter = re.compile("[ ]")


def read(fileName):
	if not os.path.exists(fileName):
		print("Can not read file: " + fileName)
		exit(1)

	taskFile = open(fileName, 'r')
	fileLine = taskFile.readline()

	if len(fileLine) > 0:
		taskHeader = fileLine.strip()
		fields = spaceSplitter.split(taskHeader)

		if len(fields) != 2:
			print("Syntax error in input file on task/rule header")
			exit(1)

		numberOfTasks = int(fields[0])
		numberOfRules = int(fields[1])
		nodeDict = {}

		i = 0
		while i < numberOfRules:
			rule = taskFile.readline().strip()
			ruleFields = spaceSplitter.split(rule)

			if len(ruleFields) < 2:
				print("Syntax error in input file on line:" + str(i))
				exit(1)

			if int(ruleFields[0]) in nodeDict:
				node = nodeDict[int(ruleFields[0])]
			else:
				# create node
				node = Node.Node(int(ruleFields[0]))
				nodeDict[int(ruleFields[0])] = node

			# number of dependencies
			numberOfDependencies = int(ruleFields[1])

			if len(ruleFields) != numberOfDependencies + 2:
				print("Wrong number of dependencies on line:" + str(i+1))

			j = 0
			while j < numberOfDependencies:
				ruleId = j + 2
				dependency = int(ruleFields[ruleId])

				if dependency in nodeDict:
					nodeDep = nodeDict[dependency]
				else:
					# create dependency node
					nodeDep = Node.Node(dependency)
					nodeDict[dependency] = nodeDep

				# link dependency
				node.incoming[dependency] = nodeDep
				nodeDep.outcoming[node.nodeId] = node

				j += 1

			i += 1

		taskFile.close()
		return nodeDict

	return None
