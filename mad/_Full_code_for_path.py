# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158
import random
from typing import Dict, List, Tuple
import heapq
# Start of class
class GoalNode:
    """
    This class creates Multi Agent Goal Nodes

    Attributes
    ----------
    name : str
        Goal Name
    data : dict
        Dictionary containing the key as the agent and the value as the planning cost
    children: List
        List of child GoalNodes, initialized with an empty list
    agent: str
        Agent that costs the least
    cost: int
        Most optimized cost
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of child Goals
    level_order_transversal(self)
        Tranverse through the tree in the level-by-level order
    
    """

    def __init__(self, name: str, data: Dict) -> None:
        self.name = name 
        self.data = data
        self.children = []
        self.agent = _agent_goal(data)
        self.cost = self.data[self.agent]

    def add_child(self, a):
        self.children.append(a)

    def get_children(self) -> List:
        return self.children
def level_order_transversal(root) -> list:
        
        """
        Transverses through the goal tree and prints out the goals (with the parent node in the front if the node has a parent)

        Parameters
        ----------
        root : GoalNode
            The root of the goal tree

        """
        result = []
        if root is None:
            return result

        q = []
        q.append((root, None)) # enqueue the root into the queue

        while len(q) != 0:
            level_size = len(q)

            while level_size > 0:
                node, parent = q.pop(0)
                if parent is not None:
                    print(parent.name + "|", end="")  # Print branch symbol if the node has a parent
                print(node.name + " " + node.agent, end="\t")

                children = node.get_children()
                for child in children:
                    q.append((child, node))  # Add the children into the queue along with their parent

                level_size -= 1

            
        return result


# Function that randomizes the range of agent's cost
def _random_cost(start_range: int, end_range: int) -> Dict[str, int]:
    """
    This function generates random costs for agents based on a specified cost range.

    Parameters
    ----------
    start_range: int
        The lower bound of the cost range.

    end_range: int
        The upper bound of the cost range.

    Returns
    -------
    Dict[str, int]
        A dictionary containing the agents as keys and their respective randomized costs as values.
    """
    d = {}
    agents = ["grace", "remus", "franklin"]
    for agent in agents:
        d[agent] = random.randint(start_range, end_range)
    
    print (d)
    return d


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




    
def main():
    print("\n\nAgents cost assignment:\n")
    G1 = GoalNode("G1", _random_cost(1, 20))  # Assigning all goals random agent's cost values from 1-20
    G2 = GoalNode("G2",_random_cost(1, 20))
    G3 = GoalNode("G3",_random_cost(1, 20))
    G4 = GoalNode("G4",_random_cost(1, 20))
    G5 = GoalNode("G5",_random_cost(1, 20))
  
    
    print("\nAgents assignmnet to Goals:\n")
    #Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)

    level_order_transversal(G1)

    #shortest_cost, shortest_goals, shortest_agents = _optimize_tree(G1)
    shortest_cost, shortest_goals, shortest_agents = dijkstra_shortest_path(G1)

    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    print("\nList of Agents:", shortest_agents)
    compare(shortest_cost, G1.cost)

if __name__ == "__main__":
    main()
