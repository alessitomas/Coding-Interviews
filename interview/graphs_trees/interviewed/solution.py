from collections import deque

class GraphNode:
    def __init__(self, value=None):
        self.value = value	
        self.adjacent = []


def has_route(start_node: GraphNode, end_node: GraphNode) -> bool:
	if start_node is None or end_node is None:
		return False
	queue = deque()
	queue.append(start_node)
	visited = set()
	while len(queue) > 0:
		cur_node = queue.pop()
		visited.add(cur_node)
		if cur_node == end_node:
			return True
		for neig in cur_node.adjacent:
			if not neig in visited:
				queue.append(neig)
		
	return False
	
