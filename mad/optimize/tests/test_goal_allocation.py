import pytest
import random
from mad.data_structures import GoalNode, level_order_transversal
from mad.optimize import initial_goal_allocation
from typing import Dict

#Run this by debugging

def _random_cost(m: int, n: int) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        The starting point of the range
    n: int
        The ending point of the range
    
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

def test_tree_creation() -> GoalNode:

    """
    This function creates a random test goal tree 

    Parameters
    ----------

    Returns
    ----------
    GoalNode
        Returns the root node of the test tree

    """
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

    level_order_transversal(G1)
    return G1 

def test_goal_allocation(goal: GoalNode) -> None:

    """
    This function creates a random test goal tree 
      
    Parameters
    ----------
    goal: GoalNode
        The root of the test tree

    """

    print("\nTo complete the goal in the most optimized way, we can assign goals like this:\n")
    for agent in initial_goal_allocation(goal):
        print (agent, end = ": ")
        for i in initial_goal_allocation(goal)[agent]:
            print (i, end = " ")
        print("\n")

def main():

    test_goal_allocation(test_tree_creation())

if __name__ == "__main__":
    main()