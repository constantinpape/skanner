# TODO numba optimization ?!
# TODO should be simple to rewrite this to also return parents !


def dfs(graph, node, parent, visited_nodes):
    """ Depth-first search starting from node to check whether it
        can be reached via cycle in graph.
    """
    visited_nodes.append(node)
    # iterate over all neighbors of the current node
    for ngb in graph.neighbors(node):
        # if this is the parent of the current node, continue
        if ngb == parent:
            continue
        # if this node was already visited, we have found a cycle
        if ngb in visited_nodes:
            return True
        # perform dfs search starting from ngb node
        if dfs(graph, ngb, node, visited_nodes):
            return True


# TODO can we get n_nodes from graph
def has_cycle(graph, n_nodes):
    """ Check if given graph has a cycle
    """
    visited_nodes = []
    # TODO get number of nodes from skan graph
    # iterate overa all nodes
    for node in range(n_nodes):
        if node in visited_nodes:
            continue
        if dfs(graph, node, -1, visited_nodes):
            return True
    return False
