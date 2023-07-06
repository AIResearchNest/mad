#Maheen tests:
import random
from typing import Dict, List, Tuple
import heapq
from mad.data_structures._multi_agent_goal_node_two import GoalNode2, level_order_transversal_two
from mad.optimize._goal_allocation import random_cost_m, agent_goal_m, compare_m, shortest_path_m, perform_auction_m, extract_node_info_m, get_agent_resources_m

import time
from typing import Dict


def test_algorithm_efficiency_m():
    
    '''
    TEST CASE 1: SAME RESOURCES
    '''
    
    print("\n\tMaheen's algorithm \n")
    print("\n\tTest case 1:\n")
    initial_goal_tree = GoalNode2("G1", random_cost_m(50, 70))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode2("G2",  random_cost_m(25, 40))

    G3 = GoalNode2("G3", random_cost_m(25,40))

    G4 = GoalNode2("G4", random_cost_m(25,40))

    G5 = GoalNode2("G5", random_cost_m(15,30))

    G6 = GoalNode2("G6", random_cost_m(15,30))

    G7 = GoalNode2("G7", random_cost_m(15,30))

    G8 = GoalNode2("G8", random_cost_m(15,30))

    G9 = GoalNode2("G9", random_cost_m(15,30))

    G10 = GoalNode2("G10", random_cost_m(5,10))

    G11 = GoalNode2("G11", random_cost_m(5,10))

    G12 = GoalNode2("G12", random_cost_m(5,10))

    G13 = GoalNode2("G13", random_cost_m(5,10))


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
    start_time = time.time()

    agent_resources = get_agent_resources_m(max_resources)


    nodes = [initial_goal_tree, G2, G3, G4, G5,G6, G7, G8, G9, G10, G11, G12, G13]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(initial_goal_tree)
    print("\nInitial cost allocation:")
    level_order_transversal_two(initial_goal_tree)
    compare_m(shortest_cost, initial_goal_tree.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(initial_goal_tree, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if (initial_goal_tree).cost <= shortest_cost or len((initial_goal_tree).get_children()) == 0:
        print(f"Node: {(initial_goal_tree).name}\tCost: {(initial_goal_tree).cost}")
        perform_auction_m((initial_goal_tree), agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two((initial_goal_tree))
    else:
            
        for name, cost in node_info.items():
            if name != (initial_goal_tree).name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two((initial_goal_tree))
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

    
   
    maheen_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Maheen Test Case# 1 time:", maheen_goal_allocation_time)


    '''
    Test Case 2: DIFFERENT MAX RESOURCES
    '''

    # Create a sample goal tree
    print("\n\tTest case 2:\n")
    initial_goal_tree = GoalNode2("G1",random_cost_m(60, 80))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode2("G2",random_cost_m(25, 45)) # level 2

    G3 = GoalNode2("G3",random_cost_m(25,45))

    G4 = GoalNode2("G4",random_cost_m(25,45))

    G5 = GoalNode2("G5",random_cost_m(15,30)) # level 3

    G6 = GoalNode2("G6",random_cost_m(15,30))

    G7 = GoalNode2("G7",random_cost_m(15,30))

    G8 = GoalNode2("G8",random_cost_m(15,30))

    G9 = GoalNode2("G9",random_cost_m(15,30)) 

    G10 = GoalNode2("G10",random_cost_m(5,15)) # level 4

    G11 = GoalNode2("G11",random_cost_m(5,15))

    G12 = GoalNode2("G12",random_cost_m(5,15))

    G13 = GoalNode2("G13",random_cost_m(5,15))

    G14 = GoalNode2("G14",random_cost_m(1,10)) # level 5

    G15 = GoalNode2("G15",random_cost_m(1,10))

    G16 = GoalNode2("G16",random_cost_m(1,10))


    initial_goal_tree.add_child(G2)
    initial_goal_tree.add_child(G3)
    initial_goal_tree.add_child(G4)

    G2.add_child(G5)
    G2.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G6)
    G2.add_child(G9)

    G6.add_child(G10)
    G6.add_child(G13)
    G9.add_child(G12)
    G9.add_child(G11)
    
    G11.add_child(G14)
    G11.add_child(G16)
    G11.add_child(G15)
    max_resources = [50,60,55] 
    
    # Test _algorithm
    start_time = time.time()
    #here
    agent_resources = get_agent_resources_m(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [initial_goal_tree, G2, G3, G4, G5,G6, G7, G8, G9, G10, G11, G12, G13]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(initial_goal_tree)
    print("\nInitial cost allocation:")
    level_order_transversal_two(initial_goal_tree)
    compare_m(shortest_cost, initial_goal_tree.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = extract_node_info_m(initial_goal_tree, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if (initial_goal_tree).cost <= shortest_cost or len((initial_goal_tree).get_children()) == 0:
        print(f"Node: {(initial_goal_tree).name}\tCost: {(initial_goal_tree).cost}")
        perform_auction_m((initial_goal_tree), agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two((initial_goal_tree))
    else:
            
        for name, cost in node_info.items():
            if name != (initial_goal_tree).name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two((initial_goal_tree))
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

    
   
    maheen_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Maheen Test Case# 2 time:", maheen_goal_allocation_time)

    '''
    Test Case 3: 
    '''

    print("Test case 3:\n")
    initial_goal_tree = GoalNode2("G1", random_cost_m(40, 60))
    # Add some goals and their costs to the goal tree
    G2 = GoalNode2("G2", random_cost_m(20, 30)) # level 2

    G3 = GoalNode2("G3",random_cost_m(20,30))

    G4 = GoalNode2("G4",random_cost_m(20,30))

    G5 = GoalNode2("G5",random_cost_m(10,15)) # level 3

    G6 = GoalNode2("G6",random_cost_m(10,15))

    G7 = GoalNode2("G7",random_cost_m(10,15))

    G8 = GoalNode2("G8",random_cost_m(10,15))

    G9 = GoalNode2("G9",random_cost_m(10,15)) 

    G10 = GoalNode2("G10",random_cost_m(5,10)) # level 4

    G11 = GoalNode2("G11",random_cost_m(5,10))

    G12 = GoalNode2("G12",random_cost_m(5,10))

    G13 = GoalNode2("G13",random_cost_m(5,10))

    G14 = GoalNode2("G14",random_cost_m(1,5)) # level 5

    G15 = GoalNode2("G15",random_cost_m(1,5))

    G16 = GoalNode2("G16",random_cost_m(1,5))


    initial_goal_tree.add_child(G2)
    initial_goal_tree.add_child(G3)
    initial_goal_tree.add_child(G4)

    G2.add_child(G5)
    G2.add_child(G7)
    G3.add_child(G8)
    G3.add_child(G6)
    G2.add_child(G9)

    G6.add_child(G10)
    G6.add_child(G13)
    G9.add_child(G12)
    G9.add_child(G11)

    G11.add_child(G14)
    G11.add_child(G16)
    G11.add_child(G15)
    max_resources = [30, 40, 35] 
    
    
    
    # Test _algorithm
    start_time = time.time()

    agent_resources = get_agent_resources_m(max_resources)


    nodes = [initial_goal_tree, G2, G3, G4, G5,G6, G7, G8, G9, G10, G11, G12, G13]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(initial_goal_tree)
    print("\nInitial cost allocation:")
    level_order_transversal_two(initial_goal_tree)
    compare_m(shortest_cost, initial_goal_tree.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(initial_goal_tree, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if (initial_goal_tree).cost <= shortest_cost or len((initial_goal_tree).get_children()) == 0:
        print(f"Node: {(initial_goal_tree).name}\tCost: {(initial_goal_tree).cost}")
        perform_auction_m((initial_goal_tree), agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two((initial_goal_tree))
    else:
            
        for name, cost in node_info.items():
            if name != (initial_goal_tree).name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two((initial_goal_tree))
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

    
   
    maheen_goal_allocation_time = time.time() - start_time

    # Print the execution times
    print("Maheen Test Case# 3 time:", maheen_goal_allocation_time)


    '''
    Test Case 4: Edge Cases
    '''


# Run the test case
test_algorithm_efficiency_m()