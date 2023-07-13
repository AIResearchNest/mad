import random
from typing import Dict, List, Tuple
import heapq
import matplotlib.pyplot as plt


from mad.data_structures._multi_agent_goal_node_two import GoalNode2, level_order_transversal_two
from mad.optimize._goal_allocation import random_cost_m, agent_goal_m, compare_m, shortest_path_m, perform_auction_m, extract_node_info_m, get_agent_resources_m

    
        
'''
Test case where all agents have anough resources and can cover the cost and all goals are assigned an agent
'''


def testcase_1():
    root = GoalNode2("Main Goal", 100)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 10, 7, 3]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)
    return root
    
  

    
'''
Test case with resources scarcity such that all agents ran out of enough resources to cover all goals from optimal path 
'''


def testcase_2():
    root = GoalNode2("Main Goal", 100)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 10, 7, 0]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root

 
'''
Test case with lowest root value so chosen as optimal path but partial resources scarcity. 
'''

def testcase_7():
    root = GoalNode2("Main Goal", 2)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 0, 1, 0]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root 

 
 
'''
Test case with resources scarcity. 
'''

def testcase_4():
    root = GoalNode2("Main Goal", 100)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 10, 5, 1]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root 

 
    
'''
Test cases with root node as only best option/optimal optionS
'''


def testcase_3():
    root = GoalNode2("Main Goal", 1)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 10, 7, 0]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root 

'''
Test case with imbalanced resources so one has higher. 
'''

def testcase_5():
    root = GoalNode2("Main Goal", 100)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 50, 3, 8]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root 



 
'''
Test cases with goal sharing where a single goal which is part of optimal path requires 2/3 agents resources to compelte it. 
optimal path 1,3,5
'''


def testcase_6():
    root = GoalNode2("Main Goal", 100)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [ 10, 3, 8]

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root 

'''
Test case with all resources as lowest


def testcase_7():
    root = GoalNode2("Main Goal", 100)
    subgoal1 = GoalNode2("Sub Goal 1", 5)
    subgoal2 = GoalNode2("Sub Goal 2", 10)
    subgoal3 = GoalNode2("Sub Goal 3", 10)
    subgoal4 = GoalNode2("Sub Goal 4", 10)
    subgoal5 = GoalNode2("Sub Goal 5", 5)
    subgoal6 = GoalNode2("Sub Goal 6", 15)


    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal3.add_child(subgoal5)
    subgoal2.add_child(subgoal4)
    subgoal4.add_child(subgoal6)

    
    
    max_resources = [1,2,3]/ #0, 0, 0

     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6]
    agent_goal_m(nodes, max_resources)  
    return root 

'''



def calculate_goal_completion(node):
    """
    Calculates the percentage of completed goals based on agent assignments.

    Parameters:
    node (GoalNode2): The current goal node.

    Returns:
    float: The completion percentage.
    """
    if not node.children:
        if node.agent is not None:
            return 1
        else:
            return 0
    else:
        completed_goals = sum(calculate_goal_completion(child) for child in node.children)
        return completed_goals / len(node.children)

def calculate_completion_percentage(root_node):
    """
    Calculates the overall completion percentage of the goal tree.

    Parameters:
    root_node (GoalNode2): The root node of the goal tree.

    Returns:
    float: The completion percentage.
    """
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root_node)
    if root_node.cost <= shortest_cost or (len(root_node.get_children()) == 0 and root_node.agent is not None):
        return 100

    remaining_nodes = extract_node_info_m(root_node, shortest_goals[1:])
    #print(remaining_nodes)

    real_nodes = [] #instnaces to goalnode2 of shortest path goals names 
    for node_name in shortest_goals[1:]:
        for node in remaining_nodes.values():
            if node.name == node_name:
                real_nodes.append(node)
                #print(f"Node: {node.name}\tCost: {node.cost}\tAgents: {node.agent}")
                break
    
    if all(node.agent is not None or isinstance(node.agent, list) for node in real_nodes):
        return 100

    num_goals = len(real_nodes)
    completion_percentage = 0

    if num_goals > 0:
        goal_percentage = 100 / num_goals

        for node in real_nodes:
            if node.agent is not None:
                completion_percentage = completion_percentage + goal_percentage

    return completion_percentage




def plot_completion_percentages():
    '''
    draws plot of completion function'''
    completion_percentages = []

    root1 = testcase_1()
    completion_percentages.append(calculate_completion_percentage(root1))

    root2 = testcase_2()
    completion_percentages.append(calculate_completion_percentage(root2))
    
    root3 = testcase_3()
    completion_percentages.append(calculate_completion_percentage(root3))

    root4 = testcase_4()
    completion_percentages.append(calculate_completion_percentage(root4))
    
    root5 = testcase_5()
    completion_percentages.append(calculate_completion_percentage(root5))
  
    root6 = testcase_6()
    completion_percentages.append(calculate_completion_percentage(root6))
    
    ''' 
    root7 = testcase_7()
    completion_percentages.append(calculate_completion_percentage(root7))
    '''


    
    testcases = ["testcase_1", "testcase_2", "testcase_3", "testcase_4", "testcase_5", "resources_6"]

    plt.scatter(testcases, completion_percentages)
    plt.xlabel("Testcases with varying reesources")
    plt.ylabel("Completion Percentage")
    plt.title("Completion Percentage of Goals in varying resources of agents ")
    plt.ylim(0, 110)
    plt.show()




    
        


def main():
    
 

    root1 = testcase_1()
    root2 = testcase_6()
    
    level_order_transversal_two(root2)
    level_order_transversal_two(root1)
    calculate_completion_percentage(root2)
    plot_completion_percentages()
  
 

  
        
if __name__ == '__main__':
    main()
