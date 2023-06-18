import sys 
import os
sys.path.append(os.path.abspath("data_structures"))
from _multi_agent_goal_nodes import GoalTree, GoalNode
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

    """
    d = {}
    d["grace"] = random.randint(m,n)
    d["remus"] = random.randint(m,n)
    d["franklin"] = random.randint(m,n)
    print(d)
    return d

def main() -> None:
    t = GoalTree()
    print("Goals List:\n")
    G1 = GoalNode("G1",_random_cost(10,20))
    G2 = GoalNode("G2",_random_cost(5,10))
    G3 = GoalNode("G3",_random_cost(5,10))
    G4 = GoalNode("G4",_random_cost(2,10))
    G5 = GoalNode("G5",_random_cost(2,10))
    G6 = GoalNode("G6",_random_cost(1,5))
    G7 = GoalNode("G7",_random_cost(1,5))
    G8 = GoalNode("G8",_random_cost(2,10))
    G9 = GoalNode("G9",_random_cost(2,10))
    
    print("\n\nGoals assigned to each agent:")
    #Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G4.add_child(G6)
    G4.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G9)

    t.set_root(G1)
    t.level_order_transversal()

if __name__ == "__main__":
    main()
