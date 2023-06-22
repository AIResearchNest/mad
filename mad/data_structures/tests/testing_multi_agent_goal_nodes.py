from mad.data_structures import GoalNode, level_order_transversal
from typing import Dict, List
import random
from typing import Dict, List, Tuple
import heapq


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
