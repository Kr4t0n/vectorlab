"""
DFS is a graph walking algorithm standing for
depth first searching.
"""

from ...base import Stack


def dfs(adj_mat, start_node, end_node, return_visited=False):
    r"""Depth-first search (DFS) is an algorithm for traversing
    or searching tree or graph data structure. It starts from an
    arbitrary tree node and explores as far as possible along each
    branch before backtracking.

    Parameters
    ----------
    adj_mat : array_like, scipy.sparse.spmatrix, shape (n_nodes, n_nodes)
        The adjacency matrix of a graph.
    start_node : int
        The node index to start searching.
    end_node : int
        The node index to stop searching.
    return_visited : bool, optional
        If return the visited nodes.

    Returns
    -------
    path : list
        The path from start node to end node using DFS algorithm. If
        there is no path from start node to end node, a None value is
        returned.
    visited : list
        The order of nodes being visited.
    """

    path_stack = Stack()
    path_stack.push([start_node])

    visited = [start_node]

    while path_stack:
        path = path_stack.pop()

        current_node = path[-1]

        if current_node == end_node:
            return (path, visited) if return_visited else path
        else:
            next_hops = adj_mat.getrow(current_node).indices

            next_hops_unvisited = set(next_hops) - set(visited)

            for next_hop in next_hops_unvisited:
                path_stack.push(path + [next_hop])
                visited.append(next_hop)

    return (None, visited) if return_visited else None
