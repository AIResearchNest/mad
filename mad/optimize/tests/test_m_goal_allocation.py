import random
from typing import Dict, List, Tuple
import heapq
import pytest
from mad.data_structures import GoalNode, level_order_transversal
from mad.data_structures.tests import _random_cost 
from mad.optimize import m_goal_allocation



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
