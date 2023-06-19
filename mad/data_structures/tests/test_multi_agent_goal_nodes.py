from mad.data_structures import GoalNode, level_order_transversal
from typing import Dict, List
import random

def _random_cost(m: int, n: int) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        the starting point of the range
    n: int
        the ending point of the range

    Returns
    -------
    
    Dict[str,int]
        A dictionary with the agents as keys and corresponding costs as values
        
    """
    d = {}
    d["grace"] = random.randint(m,n)
    d["remus"] = random.randint(m,n)
    d["franklin"] = random.randint(m,n)
    print(d)
    return d

def main() -> None:
    G1 = GoalNode("G1",_random_cost(10,20))
    G2 = GoalNode("G2",_random_cost(5,10))
    G3 = GoalNode("G3",_random_cost(5,10))
    G4 = GoalNode("G4",_random_cost(2,10))
    G5 = GoalNode("G5",_random_cost(2,10))
    G6 = GoalNode("G6",_random_cost(1,5))
    G7 = GoalNode("G7",_random_cost(1,5))
    G8 = GoalNode("G8",_random_cost(2,10))
    G9 = GoalNode("G9",_random_cost(2,10))
    
    print("\n\nGoals assignment:")
    #Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G4.add_child(G6)
    G4.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G9)

    level_order_transversal(G1)

if __name__ == "__main__":
    main()