import random as r
from typing import Dict, List, Tuple
import heapq

from mad.data_structures._multi_agent_goal_node_two import GoalNode2, level_order_transversal_two
from mad.optimize._goal_allocation import random_cost_m, agent_goal_m, compare_m, shortest_path_m, perform_auction_m, extract_node_info_m, get_agent_resources_m
'''
Test cases with same resources for each agent for different tree structures.
Fucntion whose name ends i _s are ones in which resources for each agent are same. 
'''

def random_binary_symetric_s():

    root = GoalNode2("Main Goal", random_cost_m(35,45))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(5,15))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    
    max_resources = [50, 50, 50]
    agent_resources = get_agent_resources_m(max_resources)

  
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")


def random_binary_left_s():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(5,15))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    
    max_resources = [50, 50, 50]
    agent_resources = get_agent_resources_m(max_resources)

  
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:])  
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")

def random_root_s():

    root = root = GoalNode2("Main Goal", random_cost_m(25,35))

    
    max_resources = [50, 50, 50]
    agent_resources = get_agent_resources_m(max_resources)

  
    nodes = [root]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:])  
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def random_tree_symetric_s():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(15,25))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(5,15))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(5,15))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(5,15))
    subgoal10 = GoalNode2("Sub Goal 10", random_cost_m(5,15))
    subgoal11 = GoalNode2("Sub Goal 11", random_cost_m(5,15))
    subgoal12 = GoalNode2("Sub Goal 12", random_cost_m(5,15))
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)
    
    
    max_resources = [50, 50, 50]
    agent_resources = get_agent_resources_m(max_resources)

  
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, 
             subgoal8, subgoal9, subgoal10, subgoal11, subgoal12]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:])  
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")

def random_tree_left_right_s():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(15,25))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(5,15))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(5,15))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    
    max_resources = [50, 50, 50]
    agent_resources = get_agent_resources_m(max_resources)

  
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6,subgoal7,subgoal8, subgoal9]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:])  
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def random_large_tree_s():
    
    x = 30
    y = 60
    root = GoalNode2("Main Goal", random_cost_m(x,y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(x,y))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(x,y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(x,y))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(x,y))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(x,y))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(x,y))
    x = 5
    y = 10
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(x,y))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(x,y))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(x,y))
    subgoal10 = GoalNode2("Sub Goal 10", random_cost_m(x,y))
    subgoal11 = GoalNode2("Sub Goal 11", random_cost_m(x,y))
    subgoal12 = GoalNode2("Sub Goal 12", random_cost_m(x,y))
    subgoal13 = GoalNode2("Sub Goal 13", random_cost_m(x,y))
    subgoal14 = GoalNode2("Sub Goal 14", random_cost_m(x,y))

    x = 3
    y = 6
    subgoal15 = GoalNode2("Sub Goal 15", random_cost_m(x,y))
    subgoal16 = GoalNode2("Sub Goal 16", random_cost_m(x,y))
    subgoal17 = GoalNode2("Sub Goal 17", random_cost_m(x,y))
    subgoal18 = GoalNode2("Sub Goal 18", random_cost_m(x,y))
    subgoal19 = GoalNode2("Sub Goal 19", random_cost_m(x,y))
    subgoal20 = GoalNode2("Sub Goal 20", random_cost_m(x,y))
    subgoal21 = GoalNode2("Sub Goal 21", random_cost_m(x,y))
    subgoal22 = GoalNode2("Sub Goal 22", random_cost_m(x,y))
    subgoal23 = GoalNode2("Sub Goal 23", random_cost_m(x,y))
    subgoal24 = GoalNode2("Sub Goal 24", random_cost_m(x,y))
    subgoal25 = GoalNode2("Sub Goal 25", random_cost_m(x,y))
    subgoal26 = GoalNode2("Sub Goal 26", random_cost_m(x,y))
    subgoal27 = GoalNode2("Sub Goal 27", random_cost_m(x,y))
    subgoal28 = GoalNode2("Sub Goal 28", random_cost_m(x,y))
    subgoal29 = GoalNode2("Sub Goal 29", random_cost_m(x,y))
    subgoal30 = GoalNode2("Sub Goal 30", random_cost_m(x,y))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    
    max_resources = [50, 50, 50]
    agent_resources = get_agent_resources_m(max_resources)

  
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7,subgoal8, subgoal9, subgoal10,
             subgoal11, subgoal12, subgoal13, subgoal14, subgoal15, subgoal16, subgoal17, subgoal18, subgoal19, subgoal20, 
             subgoal21, subgoal22, subgoal23, subgoal24, subgoal25, subgoal26,subgoal27, subgoal28, subgoal29, subgoal30]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:])  
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def no_goal_s():
    return None



'''
Test cases with different resources for each agent which are generated
using randomized function for different tree structures.
'''

def random_binary_symetric():

    root = GoalNode2("Main Goal", random_cost_m(35,45))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(5,15))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    
    max_resources = [ random_cost_m(0,15),  random_cost_m(0,30),  random_cost_m(0,20)]
    agent_resources = get_agent_resources_m(max_resources)


    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    print("\nAgent Initial Resources:", agent_resources)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")


def random_binary_left():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(5,15))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    
    max_resources = [ random_cost_m(1,50),  random_cost_m(1,50),  random_cost_m(1,50)]
    agent_resources = get_agent_resources_m(max_resources)


    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    print("\nAgent Initial Resources:", agent_resources)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")

def random_root():

    root = root = GoalNode2("Main Goal", random_cost_m(25,35))

    
    max_resources = [ random_cost_m(20,30),  random_cost_m(0,50),  random_cost_m(10,40)]
    agent_resources = get_agent_resources_m(max_resources)


    nodes = [root]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    print("\nAgent Initial Resources:", agent_resources)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0: 
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def random_tree_symetric():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(15,25))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(5,15))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(5,15))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(5,15))
    subgoal10 = GoalNode2("Sub Goal 10", random_cost_m(5,15))
    subgoal11 = GoalNode2("Sub Goal 11", random_cost_m(5,15))
    subgoal12 = GoalNode2("Sub Goal 12", random_cost_m(5,15))
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)
    
    
    max_resources = [ random_cost_m(25,50),  random_cost_m(10,30),  random_cost_m(10,40)]
    agent_resources = get_agent_resources_m(max_resources)

 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, 
             subgoal8, subgoal9, subgoal10, subgoal11, subgoal12]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nAgent Initial Resources:", agent_resources)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")

def random_tree_left_right():

    root = GoalNode2("Main Goal", random_cost_m(25,35))
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(15,25))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(15,25))
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(15,25))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(5,15))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(5,15))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(5,15))
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(5,15))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(5,15))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    
    max_resources = [ random_cost_m(10,40),  random_cost_m(7,30),  random_cost_m(12,45)]
    agent_resources = get_agent_resources_m(max_resources)

 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6,subgoal7,subgoal8, subgoal9]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    print("\nAgent Initial Resources:", agent_resources)
    compare_m(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def random_large_tree():
    
    x = 30
    y = 60
    root = GoalNode2("Main Goal", random_cost_m(x,y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode2("Sub Goal 1", random_cost_m(x,y))
    subgoal2 = GoalNode2("Sub Goal 2", random_cost_m(x,y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode2("Sub Goal 3", random_cost_m(x,y))
    subgoal4 = GoalNode2("Sub Goal 4", random_cost_m(x,y))
    subgoal5 = GoalNode2("Sub Goal 5", random_cost_m(x,y))
    subgoal6 = GoalNode2("Sub Goal 6", random_cost_m(x,y))
    x = 5
    y = 10
    subgoal7 = GoalNode2("Sub Goal 7", random_cost_m(x,y))
    subgoal8 = GoalNode2("Sub Goal 8", random_cost_m(x,y))
    subgoal9 = GoalNode2("Sub Goal 9", random_cost_m(x,y))
    subgoal10 = GoalNode2("Sub Goal 10", random_cost_m(x,y))
    subgoal11 = GoalNode2("Sub Goal 11", random_cost_m(x,y))
    subgoal12 = GoalNode2("Sub Goal 12", random_cost_m(x,y))
    subgoal13 = GoalNode2("Sub Goal 13", random_cost_m(x,y))
    subgoal14 = GoalNode2("Sub Goal 14", random_cost_m(x,y))

    x = 3
    y = 6
    subgoal15 = GoalNode2("Sub Goal 15", random_cost_m(x,y))
    subgoal16 = GoalNode2("Sub Goal 16", random_cost_m(x,y))
    subgoal17 = GoalNode2("Sub Goal 17", random_cost_m(x,y))
    subgoal18 = GoalNode2("Sub Goal 18", random_cost_m(x,y))
    subgoal19 = GoalNode2("Sub Goal 19", random_cost_m(x,y))
    subgoal20 = GoalNode2("Sub Goal 20", random_cost_m(x,y))
    subgoal21 = GoalNode2("Sub Goal 21", random_cost_m(x,y))
    subgoal22 = GoalNode2("Sub Goal 22", random_cost_m(x,y))
    subgoal23 = GoalNode2("Sub Goal 23", random_cost_m(x,y))
    subgoal24 = GoalNode2("Sub Goal 24", random_cost_m(x,y))
    subgoal25 = GoalNode2("Sub Goal 25", random_cost_m(x,y))
    subgoal26 = GoalNode2("Sub Goal 26", random_cost_m(x,y))
    subgoal27 = GoalNode2("Sub Goal 27", random_cost_m(x,y))
    subgoal28 = GoalNode2("Sub Goal 28", random_cost_m(x,y))
    subgoal29 = GoalNode2("Sub Goal 29", random_cost_m(x,y))
    subgoal30 = GoalNode2("Sub Goal 30", random_cost_m(x,y))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    
    max_resources = [ random_cost_m(10,30),  random_cost_m(15,30),  random_cost_m(20,40)]
    agent_resources = get_agent_resources_m(max_resources)

 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7,subgoal8, subgoal9, subgoal10,
             subgoal11, subgoal12, subgoal13, subgoal14, subgoal15, subgoal16, subgoal17, subgoal18, subgoal19, subgoal20, 
             subgoal21, subgoal22, subgoal23, subgoal24, subgoal25, subgoal26,subgoal27, subgoal28, subgoal29, subgoal30]
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\nInitial cost allocation:")
    level_order_transversal_two(root)
    compare_m(shortest_cost, root.cost)
    print("\nAgent Initial Resources:", agent_resources)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    

    
    node_info = extract_node_info_m(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        print(f"Node: {root.name}\tCost: {root.cost}")
        perform_auction_m(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    perform_auction_m(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    
    

def no_goal():
    return None



def main():

    scores = []
    discrepancy = []
    
 
    goal_trees = []  # Create a list to store the goal trees
    function_names = ["random_large_tree_s", "random_binary_symmetric_s", "random_binary_left_s", 
                      "random_root_s","random_tree_left_right_s", "random_tree_symmetric_s", "no_goal_s", 
                  "random_large_tree", "random_binary_symmetric", "random_binary_left", "random_root",
                  "random_tree_left_right", "random_tree_symmetric", "no_goal"]  # Add the function names

    for i in range(len(function_names)):
        print("---------------------")
        print(f"Test {i}: {function_names[i]}")
        print("---------------------")

        # Call the corresponding function based on the index
        if i == 0:
            run = random_large_tree_s()
        elif i == 1:
            run = random_binary_symetric_s()
        elif i == 2:
            run = random_binary_left_s()
        elif i == 3:
            run = random_root_s()
        elif i == 4:
            run = random_tree_left_right_s()
        elif i == 5:
            run = random_tree_symetric_s()
        elif i == 6:
            run = no_goal_s()
        elif i == 7:
            run = random_large_tree()
        elif i == 8:
            run = random_binary_symetric()
        elif i == 9:
            run = random_binary_left()
        elif i == 10:
            run = random_root()
        elif i == 11:
            run = random_tree_left_right()
        elif i == 12:
            run = random_tree_symetric()
        elif i == 13:
            run = no_goal()
        goal_trees.append(run)  # Store the goal trees in the list

        level_order_transversal_two(run)

    
        

        
        
if __name__ == '__main__':
    main()
