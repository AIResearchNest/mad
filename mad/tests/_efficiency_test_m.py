import random as r
from typing import Dict, List, Tuple
import heapq
import matplotlib.pyplot as plt
from mad.data_structures._multi_agent_goal_node_two import GoalNode2, level_order_transversal_two
from mad.optimize._goal_allocation import  cost_node, equal_node,agent_goal_m, compare_m, shortest_path_m, perform_auction_m, extract_node_info_m, get_agent_resources_m
from final_tests import _random_cost, _equal_cost



def average_cost(root: GoalNode2) -> float:
    """
    Calculates the average cost and Total resources used of Goalnodes.

    Parameters
    ----------
    root : GoalNode2
        The root node of the goal tree.

    Returns
    -------
    float
        The average cost of the nodes with an assigned agent.
    """
    resources_usage = 0
    agent_count = 0

    def traverse(node):
        nonlocal resources_usage, agent_count
        if node.assigned_agent != "":
            resources_usage += node.cost
            agent_count += 1
        for child in node.get_children():
            traverse(child)

    traverse(root)

    if agent_count > 0:
        average_resources = resources_usage / agent_count
        print("Total Resources Used",resources_usage)
        print("Agents Used",agent_count)
        print("Below as: (average_resources, resources_usage, agent_count)")
        return average_resources, resources_usage, agent_count
    else:
        return 0




'''
   SCENE-1a:
   all random trees with 3 agents and resources as 50, 60, 70.
   UNEQUAL TREE STRUCTURES
       
'''

def random_binary_symetric_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0 )
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0 )
    subgoal6 = GoalNode2("Sub Goal 6", 0 )

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)
   
    
    root.agents = _random_cost(25, 45, num_agent)
    subgoal1.agents = _random_cost(15, 20, num_agent)
    subgoal2.agents = _random_cost(15, 20, num_agent)
    subgoal3.agents = _random_cost(5, 15, num_agent)
    subgoal4.agents = _random_cost(5, 15, num_agent)
    subgoal5.agents = _random_cost(5, 15, num_agent)
    subgoal6.agents = _random_cost(5, 15, num_agent)
    
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    cost_node(subgoal1)  # Assign cost to subgoal1
    cost_node(subgoal2)  # Assign cost to subgoal2
    cost_node(subgoal3)
    cost_node(subgoal4)
    cost_node(subgoal5)
    cost_node(subgoal6)
    
    
    
    nodes = [root,subgoal1,subgoal2,subgoal3,subgoal4,subgoal5,subgoal6]    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root




def random_binary_left_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    root.agents = _random_cost(25, 45, num_agent)
    subgoal1.agents = _random_cost(15, 20, num_agent)
    subgoal2.agents = _random_cost(15, 20, num_agent)
    subgoal3.agents = _random_cost(5, 15, num_agent)
    subgoal4.agents = _random_cost(5, 15, num_agent)
    
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    cost_node(subgoal1)  # Assign cost to subgoal1
    cost_node(subgoal2)  # Assign cost to subgoal2
    cost_node(subgoal3)
    cost_node(subgoal4)

    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root

def random_binary_right_m(num_agent, new_max_resources):

    
    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    root.agents = _random_cost(25, 45, num_agent)
    subgoal1.agents = _random_cost(15, 20, num_agent)
    subgoal2.agents = _random_cost(15, 20, num_agent)
    subgoal3.agents = _random_cost(5, 15, num_agent)
    subgoal4.agents = _random_cost(5, 15, num_agent)
    
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    cost_node(subgoal1)  # Assign cost to subgoal1
    cost_node(subgoal2)  # Assign cost to subgoal2
    cost_node(subgoal3)
    cost_node(subgoal4)

    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    

    return root


def random_root_m(num_agent, new_max_resources):

    root = root = GoalNode2("Main Goal", 0)
    root.agents = _random_cost(25,30,num_agent)
    cost_node(root)
    
    nodes = [root] 
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root



def random_tree_symetric_m(num_agent, new_max_resources):


    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    

    root.agents = _random_cost(25, 45, num_agent)
    subgoal1.agents = _random_cost(15, 20, num_agent)
    subgoal2.agents = _random_cost(15, 20, num_agent)
    subgoal3.agents = _random_cost(5, 15, num_agent)
    subgoal4.agents = _random_cost(5, 15, num_agent)
    subgoal5.agents = _random_cost(5, 15, num_agent)
    subgoal6.agents = _random_cost(5, 15, num_agent)
    subgoal7.agents = _random_cost(5, 15, num_agent)
    subgoal8.agents = _random_cost(5, 15, num_agent)
    subgoal9.agents = _random_cost(5, 15, num_agent)
    subgoal10.agents = _random_cost(5, 15, num_agent)
    subgoal11.agents = _random_cost(5, 15, num_agent)
    subgoal12.agents = _random_cost(5, 15, num_agent)
    
    
    
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    cost_node(subgoal1)  # Assign cost to subgoal1
    cost_node(subgoal2)  # Assign cost to subgoal2
    cost_node(subgoal3)
    cost_node(subgoal4)
    
    cost_node(subgoal5)  # Assign cost to subgoal1
    cost_node(subgoal6)  # Assign cost to subgoal2
    cost_node(subgoal7)
    cost_node(subgoal8)


    cost_node(subgoal9)  # Assign cosxst to subgoal1
    cost_node(subgoal10)  # Assign cost to subgoal2
    cost_node(subgoal11)
    cost_node(subgoal12)


    

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
    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    
    return root

def random_tree_left_right_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    

    root.agents = _random_cost(25, 45, num_agent)
    subgoal1.agents = _random_cost(15, 20, num_agent)
    subgoal2.agents = _random_cost(15, 20, num_agent)
    subgoal3.agents = _random_cost(5, 15, num_agent)
    subgoal4.agents = _random_cost(5, 15, num_agent)
    subgoal5.agents = _random_cost(5, 15, num_agent)
    subgoal6.agents = _random_cost(5, 15, num_agent)
    subgoal7.agents = _random_cost(5, 15, num_agent)
    subgoal8.agents = _random_cost(5, 15, num_agent)
    subgoal9.agents = _random_cost(5, 15, num_agent)

    
    
    
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    cost_node(subgoal1)  # Assign cost to subgoal1
    cost_node(subgoal2)  # Assign cost to subgoal2
    cost_node(subgoal3)
    cost_node(subgoal4)
    
    cost_node(subgoal5)  # Assign cost to subgoal1
    cost_node(subgoal6)  # Assign cost to subgoal2
    cost_node(subgoal7)
    cost_node(subgoal8)


    cost_node(subgoal9)  # Assign cosxst to subgoal1
  


    

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9]
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root

def random_large_binary_tree_m(num_agent, new_max_resources):
    
     
    x = 40
    y = 60
    root = GoalNode2("Main Goal", 0)
    
    root.agents =_random_cost(x,y, num_agent)
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    
    x = 23
    y = 30
    subgoal1 = GoalNode2("Sub Goal 1",0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    
    subgoal1.agents =_random_cost(x,y, num_agent)
    subgoal2.agents =_random_cost(x,y, num_agent)
    cost_node(subgoal1)  # Assign cost to subgoal2
    cost_node(subgoal2)
    
    x = 10
    y = 20
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal3.agents =_random_cost(x,y, num_agent)
    subgoal4.agents =_random_cost(x,y,num_agent)
    subgoal5.agents =_random_cost(x,y, num_agent)
    subgoal6.agents =_random_cost(x,y, num_agent)
    

    cost_node(subgoal3)  # Assign cost to subgoal1
    cost_node(subgoal4)  # Assign cost to subgoal2
    cost_node(subgoal5)
    cost_node(subgoal6)

    
    x = 5
    y = 10
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    subgoal13 = GoalNode2("Sub Goal 13", 0)
    subgoal14 = GoalNode2("Sub Goal 14", 0)
    
    subgoal7.agents =_random_cost(x,y, num_agent)
    subgoal8.agents =_random_cost(x,y, num_agent)
    subgoal9.agents =_random_cost(x,y, num_agent)
    subgoal10.agents =_random_cost(x,y, num_agent)
    subgoal11.agents =_random_cost(x,y, num_agent)
    subgoal12.agents =_random_cost(x,y, num_agent)
    subgoal13.agents =_random_cost(x,y, num_agent)
    subgoal14.agents =_random_cost(x,y, num_agent)
    
    
    cost_node(subgoal7)  # Assign cost to subgoal1
    cost_node(subgoal8)  # Assign cost to subgoal2
    cost_node(subgoal9)
    cost_node(subgoal10)
    cost_node(subgoal11)  # Assign cost to subgoal1
    cost_node(subgoal12)  # Assign cost to subgoal2
    cost_node(subgoal13)
    cost_node(subgoal14)


    x = 3
    y = 6
    subgoal15 = GoalNode2("Sub Goal 15", 0) 
    subgoal16 = GoalNode2("Sub Goal 16", 0)
    subgoal17 = GoalNode2("Sub Goal 17", 0)
    subgoal18 = GoalNode2("Sub Goal 18", 0)
    subgoal19 = GoalNode2("Sub Goal 19", 0)
    subgoal20 = GoalNode2("Sub Goal 20", 0)
    subgoal21 = GoalNode2("Sub Goal 21", 0)
    subgoal22 = GoalNode2("Sub Goal 22", 0)
    subgoal23 = GoalNode2("Sub Goal 23", 0)
    subgoal24 = GoalNode2("Sub Goal 24", 0)
    subgoal25 = GoalNode2("Sub Goal 25", 0)
    subgoal26 = GoalNode2("Sub Goal 26", 0)
    subgoal27 = GoalNode2("Sub Goal 27", 0)
    subgoal28 = GoalNode2("Sub Goal 28", 0)
    subgoal29 = GoalNode2("Sub Goal 29", 0)
    subgoal30 = GoalNode2("Sub Goal 30", 0)
    
    
    subgoal15.agents =_random_cost(x,y, num_agent)
    subgoal16.agents =_random_cost(x,y, num_agent)
    subgoal17.agents =_random_cost(x,y, num_agent)
    subgoal18.agents =_random_cost(x,y, num_agent)
    subgoal19.agents =_random_cost(x,y, num_agent)
    subgoal20.agents =_random_cost(x,y, num_agent)
    subgoal21.agents =_random_cost(x,y, num_agent)
    subgoal22.agents =_random_cost(x,y, num_agent)
    subgoal23.agents =_random_cost(x,y, num_agent)
    subgoal24.agents =_random_cost(x,y, num_agent)
    subgoal25.agents =_random_cost(x,y, num_agent)
    subgoal26.agents =_random_cost(x,y, num_agent)
    subgoal27.agents =_random_cost(x,y, num_agent)
    subgoal28.agents =_random_cost(x,y, num_agent)
    subgoal29.agents =_random_cost(x,y, num_agent)
    subgoal30.agents =_random_cost(x,y, num_agent)
    
    
    

    cost_node(subgoal15)  # Assign cost to subgoal1
    cost_node(subgoal16)  # Assign cost to subgoal2
    cost_node(subgoal17)
    cost_node(subgoal18)
    cost_node(subgoal19)  # Assign cost to subgoal1
    cost_node(subgoal20)  # Assign cost to subgoal2
    cost_node(subgoal21)
    cost_node(subgoal22)
    cost_node(subgoal23)  # Assign cost to subgoal1
    cost_node(subgoal24)  # Assign cost to subgoal2
    cost_node(subgoal25)
    cost_node(subgoal26)
    cost_node(subgoal27)  # Assign cost to subgoal1
    cost_node(subgoal28)  # Assign cost to subgoal2
    cost_node(subgoal29)
    cost_node(subgoal30)

    
    #child
    
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
    
    

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12, subgoal13,subgoal14, subgoal15, subgoal16, subgoal17,subgoal18, subgoal19, subgoal20, subgoal21, subgoal22,
             subgoal23, subgoal24, subgoal25, subgoal26, subgoal27, subgoal28, subgoal29, subgoal30] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    

    return root

def random_large_tree_m(num_agent, new_max_resources):
        
    x = 40
    y = 60
    root = GoalNode2("Main Goal", 0)
    
    root.agents =_random_cost(x,y, num_agent)
    cost_node(root)  # Assign minimum cost from dictioanry to to the node
    
    x = 13
    y = 20
    subgoal1 = GoalNode2("Sub Goal 1",0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    
    subgoal1.agents =_random_cost(x,y, num_agent)
    subgoal2.agents =_random_cost(x,y, num_agent)
    subgoal3.agents =_random_cost(x,y, num_agent)
    cost_node(root)
    cost_node(subgoal1)  # Assign cost to subgoal2
    cost_node(subgoal2)
    cost_node(subgoal3)  # Assign cost to subgoal1
    
    x = 4
    y = 7
    
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    
    subgoal4.agents =_random_cost(x,y,num_agent)
    subgoal5.agents =_random_cost(x,y, num_agent)
    subgoal6.agents =_random_cost(x,y, num_agent)
    

   
    cost_node(subgoal4)  # Assign cost to subgoal2
    cost_node(subgoal5)
    cost_node(subgoal6)

    

    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    
    x= 1
    y= 3
    subgoal13 = GoalNode2("Sub Goal 13", 0)
    subgoal14 = GoalNode2("Sub Goal 14", 0)
    
    subgoal7.agents =_random_cost(x,y, num_agent)
    subgoal8.agents =_random_cost(x,y, num_agent)
    subgoal9.agents =_random_cost(x,y, num_agent)
    subgoal10.agents =_random_cost(x,y, num_agent)
    subgoal11.agents =_random_cost(x,y, num_agent)
    subgoal12.agents =_random_cost(x,y, num_agent)
    subgoal13.agents =_random_cost(x,y, num_agent)
    subgoal14.agents =_random_cost(x,y, num_agent)
    
    
    cost_node(subgoal7)  # Assign cost to subgoal1
    cost_node(subgoal8)  # Assign cost to subgoal2
    cost_node(subgoal9)
    cost_node(subgoal10)
    cost_node(subgoal11)  # Assign cost to subgoal1
    cost_node(subgoal12)  # Assign cost to subgoal2
    cost_node(subgoal13)
    cost_node(subgoal14)

    subgoal15 = GoalNode2("Sub Goal 15", 0) 
    subgoal16 = GoalNode2("Sub Goal 16", 0)
    subgoal17 = GoalNode2("Sub Goal 17", 0)
    subgoal18 = GoalNode2("Sub Goal 18", 0)
    subgoal19 = GoalNode2("Sub Goal 19", 0)
    subgoal20 = GoalNode2("Sub Goal 20", 0)
    subgoal21 = GoalNode2("Sub Goal 21", 0)
    subgoal22 = GoalNode2("Sub Goal 22", 0)
    subgoal23 = GoalNode2("Sub Goal 23", 0)
    subgoal24 = GoalNode2("Sub Goal 24", 0)
    subgoal25 = GoalNode2("Sub Goal 25", 0)
    subgoal26 = GoalNode2("Sub Goal 26", 0)
    subgoal27 = GoalNode2("Sub Goal 27", 0)
    subgoal28 = GoalNode2("Sub Goal 28", 0)
    subgoal29 = GoalNode2("Sub Goal 29", 0)
    subgoal30 = GoalNode2("Sub Goal 30", 0)
    
    
    subgoal31 = GoalNode2("Sub Goal 31", 0) 
    subgoal32 = GoalNode2("Sub Goal 32", 0)
    subgoal33 = GoalNode2("Sub Goal 33", 0)
    subgoal34 = GoalNode2("Sub Goal 34", 0)
    subgoal35 = GoalNode2("Sub Goal 35", 0)
    subgoal36 = GoalNode2("Sub Goal 36", 0)
    subgoal37 = GoalNode2("Sub Goal 37", 0)
    subgoal38 = GoalNode2("Sub Goal 38", 0)
    subgoal39 = GoalNode2("Sub Goal 39", 0)
    
    subgoal15.agents =_random_cost(x,y, num_agent)
    subgoal16.agents =_random_cost(x,y, num_agent)
    subgoal17.agents =_random_cost(x,y, num_agent)
    subgoal18.agents =_random_cost(x,y, num_agent)
    subgoal19.agents =_random_cost(x,y, num_agent)
    subgoal20.agents =_random_cost(x,y, num_agent)
    subgoal21.agents =_random_cost(x,y, num_agent)
    subgoal22.agents =_random_cost(x,y, num_agent)
    subgoal23.agents =_random_cost(x,y, num_agent)
    subgoal24.agents =_random_cost(x,y, num_agent)
    subgoal25.agents =_random_cost(x,y, num_agent)
    subgoal26.agents =_random_cost(x,y, num_agent)
    subgoal27.agents =_random_cost(x,y, num_agent)
    subgoal28.agents =_random_cost(x,y, num_agent)
    subgoal29.agents =_random_cost(x,y, num_agent)
    subgoal30.agents =_random_cost(x,y, num_agent)

    subgoal31.agents =_random_cost(x,y, num_agent)
    subgoal32.agents =_random_cost(x,y, num_agent)
    subgoal33.agents =_random_cost(x,y, num_agent)
    subgoal34.agents =_random_cost(x,y, num_agent)
    subgoal35.agents =_random_cost(x,y, num_agent)
    subgoal36.agents =_random_cost(x,y, num_agent)
    subgoal37.agents =_random_cost(x,y, num_agent)
    subgoal38.agents =_random_cost(x,y, num_agent)
    subgoal39.agents =_random_cost(x,y, num_agent)
    
    
    

    cost_node(subgoal15)  # Assign cost to subgoal1
    cost_node(subgoal16)  # Assign cost to subgoal2
    cost_node(subgoal17)
    cost_node(subgoal18)
    cost_node(subgoal19)  # Assign cost to subgoal1
    cost_node(subgoal20)  # Assign cost to subgoal2
    cost_node(subgoal21)
    cost_node(subgoal22)
    cost_node(subgoal23)  # Assign cost to subgoal1
    cost_node(subgoal24)  # Assign cost to subgoal2
    cost_node(subgoal25)
    cost_node(subgoal26)
    cost_node(subgoal27)  # Assign cost to subgoal1
    cost_node(subgoal28)  # Assign cost to subgoal2
    cost_node(subgoal29)
    cost_node(subgoal30)
    cost_node(subgoal31)
    cost_node(subgoal32)
    cost_node(subgoal33)
    cost_node(subgoal33)
    cost_node(subgoal34)
    cost_node(subgoal35)
    cost_node(subgoal36)
    cost_node(subgoal37)
    cost_node(subgoal38)
    cost_node(subgoal39)


    
    #child
    
     
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

    subgoal4.add_child(subgoal13)
    subgoal4.add_child(subgoal14)
    subgoal4.add_child(subgoal15)
    subgoal5.add_child(subgoal16)
    subgoal5.add_child(subgoal17)
    subgoal5.add_child(subgoal18)
    subgoal6.add_child(subgoal19)
    subgoal6.add_child(subgoal20)
    subgoal6.add_child(subgoal21)
    subgoal7.add_child(subgoal22)
    subgoal7.add_child(subgoal23)
    subgoal7.add_child(subgoal24)
    subgoal8.add_child(subgoal25)
    subgoal8.add_child(subgoal26)
    subgoal8.add_child(subgoal27)
    subgoal9.add_child(subgoal28)
    subgoal9.add_child(subgoal29)
    subgoal9.add_child(subgoal30)
    subgoal10.add_child(subgoal31)
    subgoal10.add_child(subgoal32)
    subgoal10.add_child(subgoal33)
    subgoal11.add_child(subgoal34)
    subgoal11.add_child(subgoal35)
    subgoal11.add_child(subgoal36)
    subgoal12.add_child(subgoal37)
    subgoal12.add_child(subgoal38)
    subgoal12.add_child(subgoal39)


    
    

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12, subgoal13,subgoal14, subgoal15, subgoal16, subgoal17,subgoal18, subgoal19, subgoal20, subgoal21, subgoal22,
             subgoal23, subgoal24, subgoal25, subgoal26, subgoal27, subgoal28, subgoal29, subgoal30, subgoal31, subgoal32, subgoal33, 
             subgoal34, subgoal35, subgoal37, subgoal38, subgoal39] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    

    return root
    
    
def random_tree_1_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11",0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    
    root.agents = _random_cost(30, 45, num_agent)
        
    subgoal1.agents =_random_cost(15, 25, num_agent)
    subgoal2.agents =_random_cost(1, 8, num_agent)
    subgoal3.agents = _random_cost(1, 8, num_agent)
    
    subgoal4.agents = _random_cost(1, 8, num_agent)
    subgoal5.agents = _random_cost(1, 8, num_agent)
    subgoal6.agents = _random_cost(1, 8, num_agent)
    subgoal7.agents = _random_cost(5, 15, num_agent)
    subgoal8.agents = _random_cost(5, 15, num_agent)
    subgoal9.agents = _random_cost(1, 6, num_agent)
    subgoal10.agents = _random_cost(1, 6, num_agent)
    subgoal11.agents = _random_cost(1, 6, num_agent)
    subgoal12.agents = _random_cost(1, 6, num_agent)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal7.add_child(subgoal9)
    subgoal7.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)
    
    cost_node(root)
    cost_node(subgoal1)  # Assign cost to subgoal2
    cost_node(subgoal2)
    cost_node(subgoal3)  # Assign cost to subgoal1

    cost_node(subgoal4)  # Assign cost to subgoal2
    cost_node(subgoal5)
    cost_node(subgoal6)
    cost_node(subgoal7)  # Assign cost to subgoal2
    cost_node(subgoal8)
    cost_node(subgoal9)  # Assign cost to subgoal1

    cost_node(subgoal10)  # Assign cost to subgoal2
    cost_node(subgoal11)
    cost_node(subgoal12)
    
     

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root


def random_tree_2_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11",0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal7.add_child(subgoal9)
    subgoal7.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)
    
    root.agents = _random_cost(30, 45, num_agent)
        
    subgoal1.agents =_random_cost(6, 12, num_agent)
    subgoal2.agents =_random_cost(6, 12, num_agent)
    subgoal3.agents = _random_cost(6, 12, num_agent)
    
    subgoal4.agents = _random_cost(6,12, num_agent)
    subgoal5.agents = _random_cost(3, 6 , num_agent)
    subgoal6.agents = _random_cost(3, 6, num_agent)
    subgoal7.agents = _random_cost(3, 6, num_agent)
    subgoal8.agents = _random_cost(3, 6, num_agent)
    subgoal9.agents = _random_cost(3, 6, num_agent)
    subgoal10.agents = _random_cost(3, 6, num_agent)
    subgoal11.agents = _random_cost(3, 6, num_agent)
    subgoal12.agents = _random_cost(3, 6, num_agent)


    
    cost_node(root)
    cost_node(subgoal1)  # Assign cost to subgoal2
    cost_node(subgoal2)
    cost_node(subgoal3)  # Assign cost to subgoal1

    cost_node(subgoal4)  # Assign cost to subgoal2
    cost_node(subgoal5)
    cost_node(subgoal6)
    cost_node(subgoal7)  # Assign cost to subgoal2
    cost_node(subgoal8)
    cost_node(subgoal9)  # Assign cost to subgoal1

    cost_node(subgoal10)  # Assign cost to subgoal2
    cost_node(subgoal11)
    cost_node(subgoal12)
    
     

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root



'''
SCENE 1B:
all equal trees with 3 agents and resources as 50. 
EQUAL TREE STRUCTURES
'''



def equal_binary_symetric_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0 )
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0 )
    subgoal6 = GoalNode2("Sub Goal 6", 0 )

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)
   
    
    root.agents = _equal_cost(25, 45, num_agent)
    subgoal1.agents = _equal_cost(15, 20, num_agent)
    subgoal2.agents = _equal_cost(15, 20, num_agent)
    subgoal3.agents = _equal_cost(5, 15, num_agent)
    subgoal4.agents = _equal_cost(5, 15, num_agent)
    subgoal5.agents = _equal_cost(5, 15, num_agent)
    subgoal6.agents = _equal_cost(5, 15, num_agent)
    
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    equal_node(subgoal1)  # Assign cost to subgoal1
    equal_node(subgoal2)  # Assign cost to subgoal2
    equal_node(subgoal3)
    equal_node(subgoal4)
    equal_node(subgoal5)
    equal_node(subgoal6)
    
    
    
    nodes = [root,subgoal1,subgoal2,subgoal3,subgoal4,subgoal5,subgoal6]    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root




def equal_binary_left_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    root.agents = _equal_cost(25, 45, num_agent)
    subgoal1.agents = _equal_cost(15, 20, num_agent)
    subgoal2.agents = _equal_cost(15, 20, num_agent)
    subgoal3.agents = _equal_cost(5, 15, num_agent)
    subgoal4.agents = _equal_cost(5, 15, num_agent)
    
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    equal_node(subgoal1)  # Assign cost to subgoal1
    equal_node(subgoal2)  # Assign cost to subgoal2
    equal_node(subgoal3)
    equal_node(subgoal4)

    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root

def equal_binary_right_m(num_agent, new_max_resources):

    
    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal2.add_child(subgoal3)
    subgoal2.add_child(subgoal4)

    root.agents = _equal_cost(25, 45, num_agent)
    subgoal1.agents = _equal_cost(15, 20, num_agent)
    subgoal2.agents = _equal_cost(15, 20, num_agent)
    subgoal3.agents = _equal_cost(5, 15, num_agent)
    subgoal4.agents = _equal_cost(5, 15, num_agent)
    
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    equal_node(subgoal1)  # Assign cost to subgoal1
    equal_node(subgoal2)  # Assign cost to subgoal2
    equal_node(subgoal3)
    equal_node(subgoal4)

    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    

    return root


def equal_root_m(num_agent, new_max_resources):

    root = root = GoalNode2("Main Goal", 0)
    root.agents = _equal_cost(25,30,num_agent)
    equal_node(root)
    
    nodes = [root] 
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root



def equal_tree_symetric_m(num_agent, new_max_resources):


    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    

    root.agents = _equal_cost(25, 45, num_agent)
    subgoal1.agents = _equal_cost(15, 20, num_agent)
    subgoal2.agents = _equal_cost(15, 20, num_agent)
    subgoal3.agents = _equal_cost(5, 15, num_agent)
    subgoal4.agents = _equal_cost(5, 15, num_agent)
    subgoal5.agents = _equal_cost(5, 15, num_agent)
    subgoal6.agents = _equal_cost(5, 15, num_agent)
    subgoal7.agents = _equal_cost(5, 15, num_agent)
    subgoal8.agents = _equal_cost(5, 15, num_agent)
    subgoal9.agents = _equal_cost(5, 15, num_agent)
    subgoal10.agents = _equal_cost(5, 15, num_agent)
    subgoal11.agents = _equal_cost(5, 15, num_agent)
    subgoal12.agents = _equal_cost(5, 15, num_agent)
    
    
    
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    equal_node(subgoal1)  # Assign cost to subgoal1
    equal_node(subgoal2)  # Assign cost to subgoal2
    equal_node(subgoal3)
    equal_node(subgoal4)
    
    equal_node(subgoal5)  # Assign cost to subgoal1
    equal_node(subgoal6)  # Assign cost to subgoal2
    equal_node(subgoal7)
    equal_node(subgoal8)


    equal_node(subgoal9)  # Assign cosxst to subgoal1
    equal_node(subgoal10)  # Assign cost to subgoal2
    equal_node(subgoal11)
    equal_node(subgoal12)


    

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
    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    
    return root

def equal_tree_left_right_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    

    root.agents = _equal_cost(25, 45, num_agent)
    subgoal1.agents = _equal_cost(15, 20, num_agent)
    subgoal2.agents = _equal_cost(15, 20, num_agent)
    subgoal3.agents = _equal_cost(5, 15, num_agent)
    subgoal4.agents = _equal_cost(5, 15, num_agent)
    subgoal5.agents = _equal_cost(5, 15, num_agent)
    subgoal6.agents = _equal_cost(5, 15, num_agent)
    subgoal7.agents = _equal_cost(5, 15, num_agent)
    subgoal8.agents = _equal_cost(5, 15, num_agent)
    subgoal9.agents = _equal_cost(5, 15, num_agent)

    
    
    
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    equal_node(subgoal1)  # Assign cost to subgoal1
    equal_node(subgoal2)  # Assign cost to subgoal2
    equal_node(subgoal3)
    equal_node(subgoal4)
    
    equal_node(subgoal5)  # Assign cost to subgoal1
    equal_node(subgoal6)  # Assign cost to subgoal2
    equal_node(subgoal7)
    equal_node(subgoal8)


    equal_node(subgoal9)  # Assign cosxst to subgoal1
  


    

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9]
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root

def equal_large_binary_tree_m(num_agent, new_max_resources):
    
     
    x = 40
    y = 60
    root = GoalNode2("Main Goal", 0)
    
    root.agents =_equal_cost(x,y, num_agent)
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    
    x = 23
    y = 30
    subgoal1 = GoalNode2("Sub Goal 1",0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    
    subgoal1.agents =_equal_cost(x,y, num_agent)
    subgoal2.agents =_equal_cost(x,y, num_agent)
    equal_node(subgoal1)  # Assign cost to subgoal2
    equal_node(subgoal2)
    
    x = 10
    y = 20
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal3.agents =_equal_cost(x,y, num_agent)
    subgoal4.agents =_equal_cost(x,y,num_agent)
    subgoal5.agents =_equal_cost(x,y, num_agent)
    subgoal6.agents =_equal_cost(x,y, num_agent)
    

    equal_node(subgoal3)  # Assign cost to subgoal1
    equal_node(subgoal4)  # Assign cost to subgoal2
    equal_node(subgoal5)
    equal_node(subgoal6)

    
    x = 5
    y = 10
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    subgoal13 = GoalNode2("Sub Goal 13", 0)
    subgoal14 = GoalNode2("Sub Goal 14", 0)
    
    subgoal7.agents =_equal_cost(x,y, num_agent)
    subgoal8.agents =_equal_cost(x,y, num_agent)
    subgoal9.agents =_equal_cost(x,y, num_agent)
    subgoal10.agents =_equal_cost(x,y, num_agent)
    subgoal11.agents =_equal_cost(x,y, num_agent)
    subgoal12.agents =_equal_cost(x,y, num_agent)
    subgoal13.agents =_equal_cost(x,y, num_agent)
    subgoal14.agents =_equal_cost(x,y, num_agent)
    
    
    equal_node(subgoal7)  # Assign cost to subgoal1
    equal_node(subgoal8)  # Assign cost to subgoal2
    equal_node(subgoal9)
    equal_node(subgoal10)
    equal_node(subgoal11)  # Assign cost to subgoal1
    equal_node(subgoal12)  # Assign cost to subgoal2
    equal_node(subgoal13)
    equal_node(subgoal14)


    x = 3
    y = 6
    subgoal15 = GoalNode2("Sub Goal 15", 0) 
    subgoal16 = GoalNode2("Sub Goal 16", 0)
    subgoal17 = GoalNode2("Sub Goal 17", 0)
    subgoal18 = GoalNode2("Sub Goal 18", 0)
    subgoal19 = GoalNode2("Sub Goal 19", 0)
    subgoal20 = GoalNode2("Sub Goal 20", 0)
    subgoal21 = GoalNode2("Sub Goal 21", 0)
    subgoal22 = GoalNode2("Sub Goal 22", 0)
    subgoal23 = GoalNode2("Sub Goal 23", 0)
    subgoal24 = GoalNode2("Sub Goal 24", 0)
    subgoal25 = GoalNode2("Sub Goal 25", 0)
    subgoal26 = GoalNode2("Sub Goal 26", 0)
    subgoal27 = GoalNode2("Sub Goal 27", 0)
    subgoal28 = GoalNode2("Sub Goal 28", 0)
    subgoal29 = GoalNode2("Sub Goal 29", 0)
    subgoal30 = GoalNode2("Sub Goal 30", 0)
    
    
    subgoal15.agents =_equal_cost(x,y, num_agent)
    subgoal16.agents =_equal_cost(x,y, num_agent)
    subgoal17.agents =_equal_cost(x,y, num_agent)
    subgoal18.agents =_equal_cost(x,y, num_agent)
    subgoal19.agents =_equal_cost(x,y, num_agent)
    subgoal20.agents =_equal_cost(x,y, num_agent)
    subgoal21.agents =_equal_cost(x,y, num_agent)
    subgoal22.agents =_equal_cost(x,y, num_agent)
    subgoal23.agents =_equal_cost(x,y, num_agent)
    subgoal24.agents =_equal_cost(x,y, num_agent)
    subgoal25.agents =_equal_cost(x,y, num_agent)
    subgoal26.agents =_equal_cost(x,y, num_agent)
    subgoal27.agents =_equal_cost(x,y, num_agent)
    subgoal28.agents =_equal_cost(x,y, num_agent)
    subgoal29.agents =_equal_cost(x,y, num_agent)
    subgoal30.agents =_equal_cost(x,y, num_agent)
    
    
    

    equal_node(subgoal15)  # Assign cost to subgoal1
    equal_node(subgoal16)  # Assign cost to subgoal2
    equal_node(subgoal17)
    equal_node(subgoal18)
    equal_node(subgoal19)  # Assign cost to subgoal1
    equal_node(subgoal20)  # Assign cost to subgoal2
    equal_node(subgoal21)
    equal_node(subgoal22)
    equal_node(subgoal23)  # Assign cost to subgoal1
    equal_node(subgoal24)  # Assign cost to subgoal2
    equal_node(subgoal25)
    equal_node(subgoal26)
    equal_node(subgoal27)  # Assign cost to subgoal1
    equal_node(subgoal28)  # Assign cost to subgoal2
    equal_node(subgoal29)
    equal_node(subgoal30)

    
    #child
    
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
    
    

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12, subgoal13,subgoal14, subgoal15, subgoal16, subgoal17,subgoal18, subgoal19, subgoal20, subgoal21, subgoal22,
             subgoal23, subgoal24, subgoal25, subgoal26, subgoal27, subgoal28, subgoal29, subgoal30] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    

    return root

def equal_large_tree_m(num_agent, new_max_resources):
        
    x = 40
    y = 60
    root = GoalNode2("Main Goal", 0)
    
    root.agents =_equal_cost(x,y, num_agent)
    equal_node(root)  # Assign minimum cost from dictioanry to to the node
    
    x = 13
    y = 20
    subgoal1 = GoalNode2("Sub Goal 1",0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    
    subgoal1.agents =_equal_cost(x,y, num_agent)
    subgoal2.agents =_equal_cost(x,y, num_agent)
    subgoal3.agents =_equal_cost(x,y, num_agent)
    equal_node(root)
    equal_node(subgoal1)  # Assign cost to subgoal2
    equal_node(subgoal2)
    equal_node(subgoal3)  # Assign cost to subgoal1
    
    x = 4
    y = 7
    
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    
    subgoal4.agents =_equal_cost(x,y,num_agent)
    subgoal5.agents =_equal_cost(x,y, num_agent)
    subgoal6.agents =_equal_cost(x,y, num_agent)
    

   
    equal_node(subgoal4)  # Assign cost to subgoal2
    equal_node(subgoal5)
    equal_node(subgoal6)

    

    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11", 0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    
    x= 1
    y= 3
    subgoal13 = GoalNode2("Sub Goal 13", 0)
    subgoal14 = GoalNode2("Sub Goal 14", 0)
    
    subgoal7.agents =_equal_cost(x,y, num_agent)
    subgoal8.agents =_equal_cost(x,y, num_agent)
    subgoal9.agents =_equal_cost(x,y, num_agent)
    subgoal10.agents =_equal_cost(x,y, num_agent)
    subgoal11.agents =_equal_cost(x,y, num_agent)
    subgoal12.agents =_equal_cost(x,y, num_agent)
    subgoal13.agents =_equal_cost(x,y, num_agent)
    subgoal14.agents =_equal_cost(x,y, num_agent)
    
    
    equal_node(subgoal7)  # Assign cost to subgoal1
    equal_node(subgoal8)  # Assign cost to subgoal2
    equal_node(subgoal9)
    equal_node(subgoal10)
    equal_node(subgoal11)  # Assign cost to subgoal1
    equal_node(subgoal12)  # Assign cost to subgoal2
    equal_node(subgoal13)
    equal_node(subgoal14)

    subgoal15 = GoalNode2("Sub Goal 15", 0) 
    subgoal16 = GoalNode2("Sub Goal 16", 0)
    subgoal17 = GoalNode2("Sub Goal 17", 0)
    subgoal18 = GoalNode2("Sub Goal 18", 0)
    subgoal19 = GoalNode2("Sub Goal 19", 0)
    subgoal20 = GoalNode2("Sub Goal 20", 0)
    subgoal21 = GoalNode2("Sub Goal 21", 0)
    subgoal22 = GoalNode2("Sub Goal 22", 0)
    subgoal23 = GoalNode2("Sub Goal 23", 0)
    subgoal24 = GoalNode2("Sub Goal 24", 0)
    subgoal25 = GoalNode2("Sub Goal 25", 0)
    subgoal26 = GoalNode2("Sub Goal 26", 0)
    subgoal27 = GoalNode2("Sub Goal 27", 0)
    subgoal28 = GoalNode2("Sub Goal 28", 0)
    subgoal29 = GoalNode2("Sub Goal 29", 0)
    subgoal30 = GoalNode2("Sub Goal 30", 0)
    
    
    subgoal31 = GoalNode2("Sub Goal 31", 0) 
    subgoal32 = GoalNode2("Sub Goal 32", 0)
    subgoal33 = GoalNode2("Sub Goal 33", 0)
    subgoal34 = GoalNode2("Sub Goal 34", 0)
    subgoal35 = GoalNode2("Sub Goal 35", 0)
    subgoal36 = GoalNode2("Sub Goal 36", 0)
    subgoal37 = GoalNode2("Sub Goal 37", 0)
    subgoal38 = GoalNode2("Sub Goal 38", 0)
    subgoal39 = GoalNode2("Sub Goal 39", 0)
    
    subgoal15.agents =_equal_cost(x,y, num_agent)
    subgoal16.agents =_equal_cost(x,y, num_agent)
    subgoal17.agents =_equal_cost(x,y, num_agent)
    subgoal18.agents =_equal_cost(x,y, num_agent)
    subgoal19.agents =_equal_cost(x,y, num_agent)
    subgoal20.agents =_equal_cost(x,y, num_agent)
    subgoal21.agents =_equal_cost(x,y, num_agent)
    subgoal22.agents =_equal_cost(x,y, num_agent)
    subgoal23.agents =_equal_cost(x,y, num_agent)
    subgoal24.agents =_equal_cost(x,y, num_agent)
    subgoal25.agents =_equal_cost(x,y, num_agent)
    subgoal26.agents =_equal_cost(x,y, num_agent)
    subgoal27.agents =_equal_cost(x,y, num_agent)
    subgoal28.agents =_equal_cost(x,y, num_agent)
    subgoal29.agents =_equal_cost(x,y, num_agent)
    subgoal30.agents =_equal_cost(x,y, num_agent)

    subgoal31.agents =_equal_cost(x,y, num_agent)
    subgoal32.agents =_equal_cost(x,y, num_agent)
    subgoal33.agents =_equal_cost(x,y, num_agent)
    subgoal34.agents =_equal_cost(x,y, num_agent)
    subgoal35.agents =_equal_cost(x,y, num_agent)
    subgoal36.agents =_equal_cost(x,y, num_agent)
    subgoal37.agents =_equal_cost(x,y, num_agent)
    subgoal38.agents =_equal_cost(x,y, num_agent)
    subgoal39.agents =_equal_cost(x,y, num_agent)
    
    
    

    equal_node(subgoal15)  # Assign cost to subgoal1
    equal_node(subgoal16)  # Assign cost to subgoal2
    equal_node(subgoal17)
    equal_node(subgoal18)
    equal_node(subgoal19)  # Assign cost to subgoal1
    equal_node(subgoal20)  # Assign cost to subgoal2
    equal_node(subgoal21)
    equal_node(subgoal22)
    equal_node(subgoal23)  # Assign cost to subgoal1
    equal_node(subgoal24)  # Assign cost to subgoal2
    equal_node(subgoal25)
    equal_node(subgoal26)
    equal_node(subgoal27)  # Assign cost to subgoal1
    equal_node(subgoal28)  # Assign cost to subgoal2
    equal_node(subgoal29)
    equal_node(subgoal30)
    equal_node(subgoal31)
    equal_node(subgoal32)
    equal_node(subgoal33)
    equal_node(subgoal33)
    equal_node(subgoal34)
    equal_node(subgoal35)
    equal_node(subgoal36)
    equal_node(subgoal37)
    equal_node(subgoal38)
    equal_node(subgoal39)


    
    #child
    
     
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

    subgoal4.add_child(subgoal13)
    subgoal4.add_child(subgoal14)
    subgoal4.add_child(subgoal15)
    subgoal5.add_child(subgoal16)
    subgoal5.add_child(subgoal17)
    subgoal5.add_child(subgoal18)
    subgoal6.add_child(subgoal19)
    subgoal6.add_child(subgoal20)
    subgoal6.add_child(subgoal21)
    subgoal7.add_child(subgoal22)
    subgoal7.add_child(subgoal23)
    subgoal7.add_child(subgoal24)
    subgoal8.add_child(subgoal25)
    subgoal8.add_child(subgoal26)
    subgoal8.add_child(subgoal27)
    subgoal9.add_child(subgoal28)
    subgoal9.add_child(subgoal29)
    subgoal9.add_child(subgoal30)
    subgoal10.add_child(subgoal31)
    subgoal10.add_child(subgoal32)
    subgoal10.add_child(subgoal33)
    subgoal11.add_child(subgoal34)
    subgoal11.add_child(subgoal35)
    subgoal11.add_child(subgoal36)
    subgoal12.add_child(subgoal37)
    subgoal12.add_child(subgoal38)
    subgoal12.add_child(subgoal39)


    
    

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12, subgoal13,subgoal14, subgoal15, subgoal16, subgoal17,subgoal18, subgoal19, subgoal20, subgoal21, subgoal22,
             subgoal23, subgoal24, subgoal25, subgoal26, subgoal27, subgoal28, subgoal29, subgoal30, subgoal31, subgoal32, subgoal33, 
             subgoal34, subgoal35, subgoal37, subgoal38, subgoal39] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)
    

    return root
    
    
def equal_tree_1_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11",0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    
    root.agents = _equal_cost(30, 45, num_agent)
        
    subgoal1.agents =_equal_cost(15, 25, num_agent)
    subgoal2.agents =_equal_cost(1, 8, num_agent)
    subgoal3.agents = _equal_cost(1, 8, num_agent)
    
    subgoal4.agents = _equal_cost(1, 8, num_agent)
    subgoal5.agents = _equal_cost(1, 8, num_agent)
    subgoal6.agents = _equal_cost(1, 8, num_agent)
    subgoal7.agents = _equal_cost(5, 15, num_agent)
    subgoal8.agents = _equal_cost(5, 15, num_agent)
    subgoal9.agents = _equal_cost(1, 6, num_agent)
    subgoal10.agents = _equal_cost(1, 6, num_agent)
    subgoal11.agents = _equal_cost(1, 6, num_agent)
    subgoal12.agents = _equal_cost(1, 6, num_agent)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal7.add_child(subgoal9)
    subgoal7.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)
    
    equal_node(root)
    equal_node(subgoal1)  # Assign cost to subgoal2
    equal_node(subgoal2)
    equal_node(subgoal3)  # Assign cost to subgoal1

    equal_node(subgoal4)  # Assign cost to subgoal2
    equal_node(subgoal5)
    equal_node(subgoal6)
    equal_node(subgoal7)  # Assign cost to subgoal2
    equal_node(subgoal8)
    equal_node(subgoal9)  # Assign cost to subgoal1

    equal_node(subgoal10)  # Assign cost to subgoal2
    equal_node(subgoal11)
    equal_node(subgoal12)
    
     

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root


def equal_tree_2_m(num_agent, new_max_resources):

    root = GoalNode2("Main Goal", 0)
    subgoal1 = GoalNode2("Sub Goal 1", 0)
    subgoal2 = GoalNode2("Sub Goal 2", 0)
    subgoal3 = GoalNode2("Sub Goal 3", 0)
    subgoal4 = GoalNode2("Sub Goal 4", 0)
    subgoal5 = GoalNode2("Sub Goal 5", 0)
    subgoal6 = GoalNode2("Sub Goal 6", 0)
    subgoal7 = GoalNode2("Sub Goal 7", 0)
    subgoal8 = GoalNode2("Sub Goal 8", 0)
    subgoal9 = GoalNode2("Sub Goal 9", 0)
    subgoal10 = GoalNode2("Sub Goal 10", 0)
    subgoal11 = GoalNode2("Sub Goal 11",0)
    subgoal12 = GoalNode2("Sub Goal 12", 0)
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal7.add_child(subgoal9)
    subgoal7.add_child(subgoal10)
    subgoal4.add_child(subgoal11)
    subgoal4.add_child(subgoal12)
    
    root.agents = _equal_cost(30, 45, num_agent)
        
    subgoal1.agents =_equal_cost(6, 12, num_agent)
    subgoal2.agents =_equal_cost(6, 12, num_agent)
    subgoal3.agents = _equal_cost(6, 12, num_agent)
    
    subgoal4.agents = _equal_cost(6,12, num_agent)
    subgoal5.agents = _equal_cost(3, 6 , num_agent)
    subgoal6.agents = _equal_cost(3, 6, num_agent)
    subgoal7.agents = _equal_cost(3, 6, num_agent)
    subgoal8.agents = _equal_cost(3, 6, num_agent)
    subgoal9.agents = _equal_cost(3, 6, num_agent)
    subgoal10.agents = _equal_cost(3, 6, num_agent)
    subgoal11.agents = _equal_cost(3, 6, num_agent)
    subgoal12.agents = _equal_cost(3, 6, num_agent)


    
    equal_node(root)
    equal_node(subgoal1)  # Assign cost to subgoal2
    equal_node(subgoal2)
    equal_node(subgoal3)  # Assign cost to subgoal1

    equal_node(subgoal4)  # Assign cost to subgoal2
    equal_node(subgoal5)
    equal_node(subgoal6)
    equal_node(subgoal7)  # Assign cost to subgoal2
    equal_node(subgoal8)
    equal_node(subgoal9)  # Assign cost to subgoal1

    equal_node(subgoal10)  # Assign cost to subgoal2
    equal_node(subgoal11)
    equal_node(subgoal12)
    
     

    nodes = [root, subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6, subgoal7, subgoal8, subgoal9, subgoal10, subgoal11,
             subgoal12] 
    
    
    max_resources = new_max_resources

    agent_goal_m(nodes, max_resources)

    return root





def main():
    '''
    root = random_tree_2(3, [50, 50, 50])
    average_resources = average_cost(root)
    print("Average Cost:", average_resources)
    '''
    #testcase(agent no., [resources])
    
    '''
    Test_case [] for scenrio 1 when:
    a) * Same agents: True, Equal costs: True, Same resources: TRUE
    b) * Same agents: True, Equal costs: True, Same resources: False

    '''
    
    test_cases = [ (equal_binary_symetric_m(3, [50, 50, 50]), "equal BINARY SYMMETRIC TREE, Same resources: TRUE"), #equal
        (equal_binary_left_m(3, [50, 50, 50]), "equal BINARY LEFT TREE, Same resources: TRUE"),
        (equal_binary_right_m(3, [50, 50, 50]), "equal BINARY RIGHT TREE, Same resources: TRUE"),
        (equal_root_m(3, [50, 50, 50]), "equal ROOT-ONLY TREE, Same resources: TRUE "),
        (equal_tree_symetric_m(3, [50, 50, 50]), "equal SYMMETRIC TREE, Same resources: TRUE"),
        (equal_tree_left_right_m(3, [50, 50, 50]), "equal LEFT RIGHT TREE, Same resources: TRUE"),
        (equal_large_binary_tree_m(3, [50, 50, 50]), "equal LARGE BINARY TREE, Same resources: TRUE"), #7
        (equal_large_tree_m(3, [50, 50, 50]), "equal LARGE TREE, Same resources: TRUE"),
        (equal_tree_1_m(3, [50, 50, 50]), "equal TREE -1, Same resources: TRUE" ),
        (equal_tree_2_m(3, [50, 50, 50]), "equal TREE -2, Same resources: TRUE" ),
        
        (random_binary_symetric_m(3, [50, 60, 70]), "RANDOM BINARY SYMMETRIC TREE, Same resources: FALSE"),
        (random_binary_left_m(3, [50, 60, 70]), "RANDOM BINARY LEFT TREE, Same resources: FALSE"),
        (random_binary_right_m(3, [50, 60, 70]), "RANDOM BINARY RIGHT TREE, Same resources: FALSE"),
        (random_root_m(3, [50, 60, 70]), "RANDOM ROOT-ONLY TREE, Same resources: FALSE"),
        (random_tree_symetric_m(3, [50, 60, 70]), "RANDOM SYMMETRIC TREE, Same resources: FALSE"),
        (random_tree_left_right_m(3, [50, 60, 70]), "RANDOM LEFT RIGHT TREE, Same resources: FALSE"),
        (random_large_binary_tree_m(3, [50, 60, 70]), "RANDOM LARGE BINARY TREE, Same resources: FALSE"), #7
        (random_large_tree_m(3, [50, 60, 70]), "RANDOM LARGE TREE, Same resources: FALSE"),
        (random_tree_1_m(3, [50, 60, 70]), "RANDOM TREE -1, Same resources: FALSE"),
        (random_tree_2_m(3, [50, 60, 70]), "RANDOM TREE -2, Same resources: FALSE")
   ]
    for tree, tree_name in test_cases:
        print("\n \t _____ANALYSIS______ \n")
        average_resources = average_cost(tree)
        print(f"Average Cost ({tree_name}): {average_resources}")

    '''
    #UNCOMMENT THIS FOR SCENERIO 2
        test_case_two [] for scenerio  when:
    a) * Same agents: True, Equal costs: False, Same resources: TRUE
    b) * Same agents: True, Equal costs: False, Same resources: False  
    
    test_cases_two = [(random_binary_symetric_m(3, [50, 50, 50]), "RANDOM BINARY SYMMETRIC TREE, Same resources: TRUE"),
        (random_binary_left_m(3, [50, 50, 50]), "RANDOM BINARY LEFT TREE, Same resources: TRUE"),
        (random_binary_right_m(3, [50, 50,50]), "RANDOM BINARY RIGHT TREE, Same resources: TRUE"),
        (random_root_m(3, [50, 50,50]), "RANDOM ROOT-ONLY TREE, Same resources: TRUE"),
        (random_tree_symetric_m(3, [50, 50,50]), "RANDOM SYMMETRIC TREE, Same resources: TRUE"),
        (random_tree_left_right_m(3, [50, 50,50]), "RANDOM LEFT RIGHT TREE, Same resources: TRUE"),
        (random_large_binary_tree_m(3, [50, 50,50]), "RANDOM LARGE BINARY TREE , Same resources: TRUE"), #7
        (random_large_tree_m(3, [50, 50,50]), "RANDOM LARGE TREE , Same resources: TRUE"),
        (random_tree_1_m(3, [50, 50,50]), "RANDOM TREE -1, Same resources: TRUE"),
        (random_tree_2_m(3, [50, 50,50]), "RANDOM TREE -2, Same resources: TRUE"), 
        
        (random_binary_symetric_m(3, [50, 60, 70]), "RANDOM BINARY SYMMETRIC TREE, Same resources: FALSE"),
        (random_binary_left_m(3, [50, 60, 70]), "RANDOM BINARY LEFT TREE, Same resources: FALSE"),
        (random_binary_right_m(3, [50, 60, 70]), "RANDOM BINARY RIGHT TREE, Same resources: FALSE"),
        (random_root_m(3, [50, 60, 70]), "RANDOM ROOT-ONLY TREE, Same resources: FALSE"),
        (random_tree_symetric_m(3, [50, 60, 70]), "RANDOM SYMMETRIC TREE, Same resources: FALSE"),
        (random_tree_left_right_m(3, [50, 60, 70]), "RANDOM LEFT RIGHT TREE, Same resources: FALSE"),
        (random_large_binary_tree_m(3, [50, 60, 70]), "RANDOM LARGE BINARY TREE, Same resources: FALSE"), #7
        (random_large_tree_m(3, [50, 60, 70]), "RANDOM LARGE TREE, Same resources: FALSE"),
        (random_tree_1_m(3, [50, 60, 70]), "RANDOM TREE -1, Same resources: FALSE"),
        (random_tree_2_m(3, [50, 60, 70]), "RANDOM TREE -2, Same resources: FALSE")
        
        ]
        
    for tree, tree_name in test_cases_two:
        print("\n \t _____ANALYSIS______ \n")
        average_resources = average_cost(tree)
        print(f"Average Cost ({tree_name}): {average_resources}")
         '''

      
 
      
'''
    #UNCOMMENT THIS FOR SCENERIO 3
        test_case_two [] for scenerio  when:
    a) * Same agents: False, Equal costs: False, Same resources: True
    b) * Same agents: False, Equal costs: False, Same resources: False

    test_cases_three = [(random_binary_symetric_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM BINARY SYMMETRIC TREE, Same resources: TRUE"),
        (random_binary_left_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM BINARY LEFT TREE, Same resources: TRUE"),
        (random_binary_right_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM BINARY RIGHT TREE, Same resources: TRUE"),
        (random_root_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM ROOT-ONLY TREE, Same resources: TRUE"),
        (random_tree_symetric_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM SYMMETRIC TREE, Same resources: TRUE"),
        (random_tree_left_right_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM LEFT RIGHT TREE, Same resources: TRUE"),
        (random_large_binary_tree_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM LARGE BINARY TREE , Same resources: TRUE"), #7
        (random_large_tree_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM LARGE TREE , Same resources: TRUE"),
        (random_tree_1_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM TREE -1, Same resources: TRUE"),
        (random_tree_2_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "RANDOM TREE -2, Same resources: TRUE"), 
        
        (random_binary_symetric_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM BINARY SYMMETRIC TREE, Same resources: FALSE"),
        (random_binary_left_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM BINARY LEFT TREE, Same resources: FALSE"),
        (random_binary_right_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM BINARY RIGHT TREE, Same resources: FALSE"),
        (random_root_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM ROOT-ONLY TREE, Same resources: FALSE"),
        (random_tree_symetric_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM SYMMETRIC TREE, Same resources: FALSE"),
        (random_tree_left_right_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM LEFT RIGHT TREE, Same resources: FALSE"),
        (random_large_binary_tree_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM LARGE BINARY TREE, Same resources: FALSE"), #7
        (random_large_tree_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM LARGE TREE, Same resources: FALSE"),
        (random_tree_1_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM TREE -1, Same resources: FALSE"),
        (random_tree_2_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "RANDOM TREE -2, Same resources: FALSE")
        
        ]
        
    for tree, tree_name in test_cases_three:
        average_resources = average_cost(tree)
        print(f"Average Cost ({tree_name}): {average_resources}")
         '''



'''
    #UNCOMMENT THIS FOR SCENERIO 4
        test_case_two [] for scenerio  when:
    a) * Same agents: False, Equal costs: True, Same resources: True
    b) * Same agents: False, Equal costs: True, Same resources: False 

    test_cases_four = [ (equal_binary_symetric_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal BINARY SYMMETRIC TREE, Same resources: TRUE"), #equal
        (equal_binary_left_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal BINARY LEFT TREE, Same resources: TRUE"),
        (equal_binary_right_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal BINARY RIGHT TREE, Same resources: TRUE"),
        (equal_root_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal ROOT-ONLY TREE, Same resources: TRUE "),
        (equal_tree_symetric_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal SYMMETRIC TREE, Same resources: TRUE"),
        (equal_tree_left_right_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal LEFT RIGHT TREE, Same resources: TRUE"),
        (equal_large_binary_tree_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal LARGE BINARY TREE, Same resources: TRUE"), #7
        (equal_large_tree_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal LARGE TREE, Same resources: TRUE"),
        (equal_tree_1_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal TREE -1, Same resources: TRUE" ),
        (equal_tree_2_m(10, [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "equal TREE -2, Same resources: TRUE" ),
        
        (equal_binary_symetric_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal BINARY SYMMETRIC TREE, Same resources: False"), 
        (equal_binary_left_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal BINARY LEFT TREE, Same resources: False"),
        (equal_binary_right_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal BINARY RIGHT TREE, Same resources: False"),
        (equal_root_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal ROOT-ONLY TREE, Same resources: False"),
        (equal_tree_symetric_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal SYMMETRIC TREE,Same resources: False"),
        (equal_tree_left_right_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal LEFT RIGHT TREE, Same resources: False"),
        (equal_large_binary_tree_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal LARGE BINARY TREE, Same resources: False"), #7
        (equal_large_tree_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal LARGE TREE, Same resources: False"),
        (equal_tree_1_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal TREE -1, Same resources: False" ),
        (equal_tree_2_m(10, [50, 60, 70, 50, 60, 70, 50, 60, 70, 50]), "equal TREE -2, Same resources: False" ) ]
        
    for tree, tree_name in test_cases_four:
        average_resources = average_cost(tree)
        print(f"Average Cost ({tree_name}): {average_resources}")
    '''     
      
      


# export cost_node and equal_node too from goal_allocation 
# _random_cost, _equal_cost same as jonathan. 
#average_cost put with testcases. 

    

if __name__ == '__main__':
    main()


  
    
