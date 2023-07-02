
#same as random test.py , Different random resources and different tree structures.
import random as r
#from mad.optimize import jonathan_algorithm
import random
from typing import Dict, List, Tuple
import heapq

from mad.data_structures.Maheen_multi_agent_goal_nodes import GoalNode, level_order_transversal
from mad.optimize._goal_allocation import maheen_random_cost, maheen_agent_goal, maheen_compare, maheen_shortest_path, maheen_perform_auction, maheen_extract_node_info, maheen_get_agent_resources
from mad.optimize import _score_allocation

def random_binary_symetric():

    root = GoalNode("Main Goal", maheen_random_cost(35,45))
    subgoal1 = GoalNode("Sub Goal 1", maheen_random_cost(15,25))
    subgoal2 = GoalNode("Sub Goal 2", maheen_random_cost(15,25))
    subgoal3 = GoalNode("Sub Goal 3", maheen_random_cost(5,15))
    subgoal4 = GoalNode("Sub Goal 4", maheen_random_cost(5,15))
    subgoal5 = GoalNode("Sub Goal 5", maheen_random_cost(5,15))
    subgoal6 = GoalNode("Sub Goal 6", maheen_random_cost(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    
    max_resources = [random.randint(20,50), random.randint(20,50), random.randint(20,50)]
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(root)
    print("\nInitial cost allocation:")
    level_order_transversal(root)
    print("\nAgent Initial Resources:", agent_resources)
    maheen_compare(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost:
        print(f"Node: {root.name}\tCost: {root.cost}")
        maheen_perform_auction(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    maheen_perform_auction(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")


def random_binary_left():

    root = GoalNode("Main Goal", maheen_random_cost(25,35))
    subgoal1 = GoalNode("Sub Goal 1", maheen_random_cost(15,25))
    subgoal2 = GoalNode("Sub Goal 2", maheen_random_cost(15,25))
    subgoal3 = GoalNode("Sub Goal 3", maheen_random_cost(5,15))
    subgoal4 = GoalNode("Sub Goal 4", maheen_random_cost(5,15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    
    max_resources = [random.randint(1,50), random.randint(1,50), random.randint(1,50)]
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(root)
    print("\nInitial cost allocation:")
    level_order_transversal(root)
    print("\nAgent Initial Resources:", agent_resources)
    maheen_compare(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost:
        print(f"Node: {root.name}\tCost: {root.cost}")
        maheen_perform_auction(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    maheen_perform_auction(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")

def random_root():

    root = root = GoalNode("Main Goal", maheen_random_cost(25,35))

    
    max_resources = [random.randint(20,30), random.randint(0,50), random.randint(10,40)]
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [root]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(root)
    print("\nInitial cost allocation:")
    level_order_transversal(root)
    print("\nAgent Initial Resources:", agent_resources)
    maheen_compare(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost : #or (not root.children)
        print(f"Node: {root.name}\tCost: {root.cost}")
        maheen_perform_auction(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    maheen_perform_auction(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def random_tree_symetric():

    root = GoalNode("Main Goal", maheen_random_cost(25,35))
    subgoal1 = GoalNode("Sub Goal 1", maheen_random_cost(15,25))
    subgoal2 = GoalNode("Sub Goal 2", maheen_random_cost(15,25))
    subgoal3 = GoalNode("Sub Goal 3", maheen_random_cost(15,25))
    subgoal4 = GoalNode("Sub Goal 4", maheen_random_cost(5,15))
    subgoal5 = GoalNode("Sub Goal 5", maheen_random_cost(5,15))
    subgoal6 = GoalNode("Sub Goal 6", maheen_random_cost(5,15))
    subgoal7 = GoalNode("Sub Goal 7", maheen_random_cost(5,15))
    subgoal8 = GoalNode("Sub Goal 8", maheen_random_cost(5,15))
    subgoal9 = GoalNode("Sub Goal 9", maheen_random_cost(5,15))
    subgoal10 = GoalNode("Sub Goal 10", maheen_random_cost(5,15))
    subgoal11 = GoalNode("Sub Goal 11", maheen_random_cost(5,15))
    subgoal12 = GoalNode("Sub Goal 12", maheen_random_cost(5,15))
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
    
    
    max_resources = [random.randint(25,50), random.randint(10,30), random.randint(10,40)]
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, 
             subgoal8, subgoal9, subgoal10, subgoal11, subgoal12]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(root)
    print("\nInitial cost allocation:")
    level_order_transversal(root)
    maheen_compare(shortest_cost, root.cost)
    print("\nAgent Initial Resources:", agent_resources)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost:
        print(f"Node: {root.name}\tCost: {root.cost}")
        maheen_perform_auction(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    maheen_perform_auction(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")

def random_tree_left_right():

    root = GoalNode("Main Goal", maheen_random_cost(25,35))
    subgoal1 = GoalNode("Sub Goal 1", maheen_random_cost(15,25))
    subgoal2 = GoalNode("Sub Goal 2", maheen_random_cost(15,25))
    subgoal3 = GoalNode("Sub Goal 3", maheen_random_cost(15,25))
    subgoal4 = GoalNode("Sub Goal 4", maheen_random_cost(5,15))
    subgoal5 = GoalNode("Sub Goal 5", maheen_random_cost(5,15))
    subgoal6 = GoalNode("Sub Goal 6", maheen_random_cost(5,15))
    subgoal7 = GoalNode("Sub Goal 7", maheen_random_cost(5,15))
    subgoal8 = GoalNode("Sub Goal 8", maheen_random_cost(5,15))
    subgoal9 = GoalNode("Sub Goal 9", maheen_random_cost(5,15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    
    max_resources = [random.randint(10,40), random.randint(7,30), random.randint(12,45)]
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6,subgoal7,subgoal8, subgoal9]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(root)
    print("\nInitial cost allocation:")
    level_order_transversal(root)
    print("\nAgent Initial Resources:", agent_resources)
    maheen_compare(shortest_cost, root.cost)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost:
        print(f"Node: {root.name}\tCost: {root.cost}")
        maheen_perform_auction(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    maheen_perform_auction(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    

def random_large_tree():
    
    x = 30
    y = 60
    root = GoalNode("Main Goal", maheen_random_cost(x,y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", maheen_random_cost(x,y))
    subgoal2 = GoalNode("Sub Goal 2", maheen_random_cost(x,y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", maheen_random_cost(x,y))
    subgoal4 = GoalNode("Sub Goal 4", maheen_random_cost(x,y))
    subgoal5 = GoalNode("Sub Goal 5", maheen_random_cost(x,y))
    subgoal6 = GoalNode("Sub Goal 6", maheen_random_cost(x,y))
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", maheen_random_cost(x,y))
    subgoal8 = GoalNode("Sub Goal 8", maheen_random_cost(x,y))
    subgoal9 = GoalNode("Sub Goal 9", maheen_random_cost(x,y))
    subgoal10 = GoalNode("Sub Goal 10", maheen_random_cost(x,y))
    subgoal11 = GoalNode("Sub Goal 11", maheen_random_cost(x,y))
    subgoal12 = GoalNode("Sub Goal 12", maheen_random_cost(x,y))
    subgoal13 = GoalNode("Sub Goal 13", maheen_random_cost(x,y))
    subgoal14 = GoalNode("Sub Goal 14", maheen_random_cost(x,y))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", maheen_random_cost(x,y))
    subgoal16 = GoalNode("Sub Goal 16", maheen_random_cost(x,y))
    subgoal17 = GoalNode("Sub Goal 17", maheen_random_cost(x,y))
    subgoal18 = GoalNode("Sub Goal 18", maheen_random_cost(x,y))
    subgoal19 = GoalNode("Sub Goal 19", maheen_random_cost(x,y))
    subgoal20 = GoalNode("Sub Goal 20", maheen_random_cost(x,y))
    subgoal21 = GoalNode("Sub Goal 21", maheen_random_cost(x,y))
    subgoal22 = GoalNode("Sub Goal 22", maheen_random_cost(x,y))
    subgoal23 = GoalNode("Sub Goal 23", maheen_random_cost(x,y))
    subgoal24 = GoalNode("Sub Goal 24", maheen_random_cost(x,y))
    subgoal25 = GoalNode("Sub Goal 25", maheen_random_cost(x,y))
    subgoal26 = GoalNode("Sub Goal 26", maheen_random_cost(x,y))
    subgoal27 = GoalNode("Sub Goal 27", maheen_random_cost(x,y))
    subgoal28 = GoalNode("Sub Goal 28", maheen_random_cost(x,y))
    subgoal29 = GoalNode("Sub Goal 29", maheen_random_cost(x,y))
    subgoal30 = GoalNode("Sub Goal 30", maheen_random_cost(x,y))
    
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

    
    max_resources = [random.randint(10,30), random.randint(15,30), random.randint(20,40)]
    agent_resources = maheen_get_agent_resources(max_resources)

    # Iterate through each goal node and perform the auction
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7,subgoal8, subgoal9, subgoal10,
             subgoal11, subgoal12, subgoal13, subgoal14, subgoal15, subgoal16, subgoal17, subgoal18, subgoal19, subgoal20, 
             subgoal21, subgoal22, subgoal23, subgoal24, subgoal25, subgoal26,subgoal27, subgoal28, subgoal29, subgoal30]
    shortest_cost, shortest_goals, shortest_agents = maheen_shortest_path(root)
    print("\nInitial cost allocation:")
    level_order_transversal(root)
    maheen_compare(shortest_cost, root.cost)
    print("\nAgent Initial Resources:", agent_resources)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    

    
    node_info = maheen_extract_node_info(root, shortest_goals[1:])
    print("\n\tGoal assigmnet to agents Info:\n\t")
    
    if root.cost <= shortest_cost:
        print(f"Node: {root.name}\tCost: {root.cost}")
        maheen_perform_auction(root, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    else:
            
        for name, cost in node_info.items():
            if name != root.name:
                node = next((n for n in nodes if n.name == name), None)
                if node:
                    print(f"Node: {name}\tCost: {cost}")
                    maheen_perform_auction(node, agent_resources)
        print("\n\t\tFINAL INFO\n")
        level_order_transversal(root)
    
    print("Final Agent Resources:", agent_resources)
    print("\n")
    
    

def no_goal():
    return None

def main():

    scores = []
    discrepancy = []
    
    #print
    goal_trees = []  # Create a list to store the goal trees
    function_names = ["random_large_tree", "random_binary_symmetric", "random_binary_left", "random_root",
                  "random_tree_left_right", "random_tree_symmetric", "no_goal"]  # Add the function names

    for i in range(len(function_names)):
        print("---------------------")
        print(f"Test {i}: {function_names[i]}")
        print("---------------------")

        # Call the corresponding function based on the index
        if i == 0:
            run = random_large_tree()
        elif i == 1:
            run = random_binary_symetric()
        elif i == 2:
            run = random_binary_left()
        elif i == 3:
            run = random_root()
        elif i == 4:
            run = random_tree_left_right()
        elif i == 5:
            run = random_tree_symetric()
        elif i == 6:
            run = no_goal()
        goal_trees.append(run)  # Store the goal trees in the list

        level_order_transversal(run)

    
        

        
        
if __name__ == '__main__':
    main()
