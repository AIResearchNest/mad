#Maheen test:
import random
from typing import Dict, List, Tuple
import heapq
from mad.data_structures.Maheen_multi_agent_goal_nodes import GoalNode, level_order_transversal
from mad.optimize._goal_allocation import maheen_random_cost, maheen_agent_goal, maheen_compare, maheen_shortest_path, maheen_perform_auction, maheen_extract_node_info, maheen_get_agent_resources

import time
from typing import Dict
import copy
import random



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
    
    return random.randint(m, n)
# Test case
def test_algorithm_efficiency():
    # Create a sample goal tree
    initial_goal_tree = GoalNode("G1", _random_cost(50, 70))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode("G2", maheen_random_cost(25, 40))

    G3 = GoalNode("G3",maheen_random_cost(25,40))

    G4 = GoalNode("G4",maheen_random_cost(25,40))

    G5 = GoalNode("G5",maheen_random_cost(15,30))

    G6 = GoalNode("G6",maheen_random_cost(15,30))

    G7 = GoalNode("G7",maheen_random_cost(15,30))

    G8 = GoalNode("G8",maheen_random_cost(15,30))

    G9 = GoalNode("G9",maheen_random_cost(15,30))

    G10 = GoalNode("G10",maheen_random_cost(5,10))

    G11 = GoalNode("G11",maheen_random_cost(5,10))

    G12 = GoalNode("G12",maheen_random_cost(5,10))

    G13 = GoalNode("G13",maheen_random_cost(5,10))


    initial_goal_tree.add_child(G2)
    initial_goal_tree.add_child(G3)
    initial_goal_tree.add_child(G4)

    G2.add_child(G5)
    G2.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G6)
    G3.add_child(G9)
    
    G4.add_child(G10)
    G4.add_child(G11)
    G4.add_child(G12)
    G4.add_child(G13)




    # Set the maximum resources for each agent
    max_resources = [50,50,50] #Every agent has the same max_resources

    # Test _algorithm
    print("Maheen's algorithm \n")
    start_time = time.time()
    #here
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [initial_goal_tree, G2, G3, G4, G5,G6, G7, G8, G9, G10, G11, G12, G13]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(initial_goal_tree)
    print("\nInitial cost allocation:")
    level_order_transversal(initial_goal_tree)
    maheen_compare(shortest_cost, initial_goal_tree.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(initial_goal_tree, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    for name, cost in node_info.items():
        if initial_goal_tree.cost <= shortest_cost:
            print(f"Node: {initial_goal_tree.name}\tCost: {initial_goal_tree.cost}")
            maheen_perform_auction(initial_goal_tree, agent_resources)
        else:
            for name, cost in node_info.items():
                if name != initial_goal_tree.name:
                    node = next((n for n in nodes if n.name == name), None)
                    if node:
                        print(f"Node: {name}\tCost: {cost}")
                        maheen_perform_auction(node, agent_resources)
    
            level_order_transversal(initial_goal_tree)
            print("Updated Agent Resources:", agent_resources)
            print("\nFinal Info:")
    level_order_transversal(initial_goal_tree)
    print("Final Agent Resources:", agent_resources)

    #here
    
   
    maheen_initial_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Execution Time - Maheen_goal_agent_allocation:", maheen_initial_goal_allocation_time)
    #print("Execution Time - maheen_algorithm:", maheen_alogrithm)

# Run the test case
test_algorithm_efficiency()