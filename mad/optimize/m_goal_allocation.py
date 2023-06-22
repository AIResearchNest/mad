from typing import Dict, List, Tuple
from mad.data_structures import GoalNode
import random 
import heapq

# Function that randomly assigns goals to agents
def _agent_goal(a: Dict[str, int]) -> str:
    """
    Decides which agent will conduct the current goal randomly.

    Parameters
    ----------
    a : Dict[str, int]
        Dictionary containing the cost values for each agent.

    Returns
    -------
    name: str
        Name of the randomly chosen agent.
    """
    agents = list(a.keys())
    name = random.choice(agents)
    return name



def compare(shortest_cost: int, root_node_cost: int):
    print("\nRoot node cost", root_node_cost )
    print("\nShortest path cost", shortest_cost )
    
    if shortest_cost < root_node_cost:
        print("\nCost effective: Choose Shortest path" )
    else:
        print("\nCost effective: Choose root node")
        
    """
    Compare the shortest path cost with the cost of the root node's agent and print the result.

    Parameters
    ----------
    shortest_cost : int
        The shortest path cost.

    root_node_cost : int
        The cost of the root node's agent.
    """
#Diajkstraaas
def dijkstra_shortest_path(root_node: GoalNode) -> Tuple[int, List[str], List[str]]:
    """
    Implements Dijkstra's algorithm to find the shortest path with the given conditions.

    Parameters
    ----------
    root_node : GoalNode
        The root node of the goal tree.

    Returns
    -------
    Tuple[int, List[str], List[str]]
        The shortest path cost, list of goals, and list of agents.
    """
    # Initialize a priority queue to store nodes based on their costs
    pq = [(0, root_node)]  # Cost of root_node is set to 0

    # Initialize dictionaries to store costs and paths
    costs = {root_node: 0}
    paths = {root_node: []}

    # Process nodes in the priority queue until it becomes empty
    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # Check if the current node is the goal node
        if not current_node.children:
            # Return the shortest path cost, list of goals, and list of agents
            return current_cost, paths[current_node] + [current_node.name], [current_node.agent]

        # Explore child nodes
        for child_node in current_node.children:
            child_cost = current_cost + child_node.cost

            # Update the cost and path if a shorter path is found
            if child_node not in costs or child_cost < costs[child_node]:
                costs[child_node] = child_cost
                paths[child_node] = paths[current_node] + [current_node.name]

                # Add the child node to the priority queue
                heapq.heappush(pq, (child_cost, child_node))

    # If no goal node is found, return None
    return None

def main() -> None:
    pass

if __name__ == "__main__":
    main()

