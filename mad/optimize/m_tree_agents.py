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




#diajkstra's to find shortest path later. 

    
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

    
if __name__ == "__main__":
    main()
