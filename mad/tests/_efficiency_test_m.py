import random
from typing import Dict, List, Tuple
import heapq
import matplotlib.pyplot as plt

# Start of class
class GoalNode2:
    """
    This class creates Multi Agent Goal Nodes

    Attributes
    ----------
    name : str
        Goal Name
    cost : int
        Cost associated with the node
    agent: str
        Agent assigned to the node
    children: List
        List of child GoalNodes, initialized with an empty list
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of child Goals
    level_order_transversal(self)
        Traverse through the tree in the level-by-level order
    """

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost
        self.agent = None
        self.children = []

    def add_child(self, a):
        self.children.append(a)

    def get_children(self) -> List:
        return self.children
    
    def __lt__(self, other):
        # Compare based on the cost attribute
        return self.cost < other.cost


def level_order_transversal_two(root) -> None:
    """
    Traverses through the goal tree and prints out the goals (with the parent node and children node in the front if the node has a child)
    along with the assigned agent for each node and costs

    Parameters
    ----------
    root: GoalNode
        The root of the goal tree
    """
    if root is None:
        return

    q = []
    q.append((root, None))  # enqueue the root into the queue

    while len(q) != 0:
        level_size = len(q)

        while level_size > 0:
            node, parent = q.pop(0)
            if parent is not None:
                print(parent.name + "|", end="")  # Print branch symbol if the node has a parent
            print(node.name + "Cost:", node.cost, "Assigned Agent:", node.agent, end="\n")

            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

            level_size -= 1

        print()  # Print a new line after traversing each level






# Function that randomizes the cost of nodes
def random_cost_m(start_range: int, end_range: int) -> int:
    """
    Author: Maheen
    This function generates a random cost for a node based on a specified cost range.

    Parameters
    ----------
    start_range: int
        The lower bound of the cost range.

    end_range: int
        The upper bound of the cost range.

    Returns
    -------
    int
        Randomized cost value for the node.
    """
    return random.randint(start_range, end_range)


def perform_auction_m(node, agent_resources):
    """
    Author: Maheen
    Performs the auction process for assigning an agent to a goal node based on available agent resources
    based on first sealed bid algorithm. If the total resources of all agents combined cannot cover the cost of the goal, 
    it uses the auction process to find the highest resource agent. It subtracts the agent's resources from the cost of the goal and repeats
    the process until the remaining cost reaches 0 
    Parameters
    ----------
    node : GoalNode
        The goal node to be assigned an agent.
    agent_resources : Dict[str, int]
        Dictionary containing the available resources for each agent.

    Returns
    -------
    None
    """
    bids = {}  # Dictionary to store the bids of each agent
    # Raise an error if goal_tree is empty (???)
    if node is None:
        raise ValueError("Tree is empty!")
    # Generate bids from each agent based on their available resources
    for agent in agent_resources:
        if agent_resources[agent] > 0:
            bids[agent] = agent_resources[agent]

    # Print agent resources before the auction
    print("Agent Resources:", agent_resources)

    # Determine the winning bidder based on the highest bid
    winning_bidder = max(bids, key=bids.get)
    winning_bid = bids[winning_bidder]

    # Check if the winning bidder can cover the cost of the goal node
    if winning_bid >= node.cost:
        node.agent = winning_bidder
        agent_resources[winning_bidder] -= node.cost
    elif len(bids) > 0:
            bids.pop(winning_bidder)
            second_bidder = max(bids,key=bids.get, default= None)
            if second_bidder is None:
                print("\n\tNo agent can cover the cost \n")
                return
            second_bid = bids[second_bidder]
            if second_bid >= node.cost:
                node.agent = second_bidder
                agent_resources[second_bidder] -= node.cost
            else:
        
                total_resources = sum(agent_resources.values())
            print("\nResources Total...:", total_resources)
            print("Cost of Goal...:", node.cost)

            if total_resources >= node.cost:
            # Generate bids from each agent based on their available resources
                bids = {agent: resource for agent, resource in agent_resources.items() if resource > 0}

                print("Agent Resources:", agent_resources)

                winning_bidder = max(bids, key=bids.get)
                winning_bid = bids[winning_bidder]

                if winning_bid <= node.cost:
                    node.agent = winning_bidder
                    if agent_resources[winning_bidder] < node.cost:
                        remaining_cost = node.cost - agent_resources[winning_bidder]
                        agent_resources[winning_bidder] = 0
                        print("Agent Updated Resources:", agent_resources)

                        assigned_agents = []
                        assigned_agents.append(winning_bidder)

                        while remaining_cost > 0:
                            agent_with_highest_resource = max(agent_resources, key=agent_resources.get)
                            resource = agent_resources[agent_with_highest_resource]

                            if resource > 0:
                                if resource <= remaining_cost:
                                    remaining_cost = remaining_cost - resource
                                    agent_resources[agent_with_highest_resource] -= resource
                                    assigned_agents.append(agent_with_highest_resource)
                                    print("Agent Updated Resources:", agent_resources)
                                else:
                                    agent_resources[agent_with_highest_resource] -= remaining_cost
                                    assigned_agents.append(agent_with_highest_resource)
                                    remaining_cost = 0
                                    print("Agent Updated Resources:", agent_resources)

                    print("\nAssigned Agents:", assigned_agents)
                    print("\nRemaining Cost:", remaining_cost)
                    node.agent = assigned_agents
                # Print agent resources after the auction
                print("Remaining Agent Resources:", agent_resources)
            else:
                print("\n\tNo agent can cover the cost \n")

    # Print agent resources after the auction
    
def compare_m(shortest_cost: int, root_node_cost: int):
    """
    Author: Maheen
    Compare the shortest path cost with the cost of the root node's agent and print the result.

    Parameters
    ----------
    shortest_cost : int
        The shortest path cost.

    root_node_cost : int
        The cost of the root node's agent.
    """
    print("\nRoot node cost", root_node_cost )
    print("\nShortest path cost", shortest_cost )
    
    if shortest_cost < root_node_cost:
        print("\nCost effective: Choose Shortest path" )
    else:
        print("\nCost effective: Choose root node")
        
 
#Diajkstraaas
def shortest_path_m(root_node: GoalNode2) -> tuple[int, List[str], List[str]]:
    """
    Author: Maheen
    Implements Dijkstra's algorithm to find the shortest path with the given conditions.

    Parameters
    ----------
    root_node : GoalNode
        The root node of the goal tree.

    Returns
    -------
    Tuple[int, List[str], List[str]]
        The shortest path cost, list of goals, and list of agents (if any)
    """
    # Initialize a priority queue to store nodes based on their costs
    pq = [(0, root_node)]  # Cost of root_node is set to 0

    # Initialize dictionaries to store costs and paths
    costs = {root_node: 0}
    paths = {root_node: []}

    # Process nodes in the priority queue until it becomes empty
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        

        # Check if the current node is the goal node
        if not current_node.children:
            # Return the shortest path cost, list of goals, and list of agents
            return current_cost, paths[current_node] + [current_node.name], [current_node.agent]

        # Explore child nodes
        for child_node in current_node.children:
            child_cost = current_cost + child_node.cost

            # Update the cost and path if a shorter path is found
            if child_node not in costs or child_cost < costs[child_node]:
                costs[child_node] = child_cost
                paths[child_node] = paths[current_node] + [current_node.name]

                # Add the child node to the priority queue
                heapq.heappush(pq, (child_cost, child_node))

    # If no goal node is found, return None
    return None
def extract_node_info_m(root_node, shortest_goals):
    """
    Author: Maheen
    Extracts node names and costs from GoalNodes that have the same name as the nodes in the shortest_goals list,
    and stores them in a dictionary.

    Parameters
    ----------
    root_node : GoalNode
        The root node of the goal tree.

    shortest_goals : List[str]
        The list of goal names representing the shortest path.

    Returns
    -------
    Dict[str, int]
        Dictionary containing node names and costs for the nodes in the shortest path.
    """
    node_info = {}

    # Traverse the tree in level order
    q = []
    q.append(root_node)

    while q:
        node = q.pop(0)
        if node.name in shortest_goals:
            node_info[node.name] = node

        children = node.get_children()
        for child in children:
            q.append(child)

    return node_info


def get_agent_resources_m(max_resources):
    '''
    Author: Maheen
    Gives agents resources
     Parameters
    ----------
    max_resources: List[int]
        
    The list of max resources for each agent

    Returns agent_resources: storing the list.
    -------
    
    '''
    agents = ["grace", "remus", "franklin"]
    agent_resources = {agent: resource for agent, resource in zip(agents, max_resources)}
    return agent_resources

def agent_goal_m(nodes, max_resources):
    if not nodes:
        print("No node has been assigned.")
        return
    root = nodes[0]
    #root node values changed. 
    
    agent_resources = get_agent_resources_m(max_resources)

 
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
    plt.xlabel("Testcases")
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
