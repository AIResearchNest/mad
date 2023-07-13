import random
from typing import Dict, List, Tuple
import heapq
import matplotlib.pyplot as plt

# Start of class

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




def perform_auction_m(node, agent_resources):
    """
    Author: Maheen
    Performs the auction process for assigning an agent to a goal node based on available agent resources based on first sealed bid algorithm. 
    If none of the agent's resources individually can cover the cost of goal then it shares the goal completion with multiple agent based on bidding winners until 
    either goal is completed or all agents run out of resources.  
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
            second_bidder = max(bids, key=bids.get)
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



def agent_goal_m(nodes, max_resources):
    """
    Author: Maheen
    Description:    This basically calls the required functions and prints the info. This function assigns agents to goals by
                 calculating the shortest path using dijkstra's and performing an auction-based allocation. 
              

    Parameters:
    - nodes (list): A list of nodes representing the goals to be assigned to agents.
    -max_resources: Gets list of maximum resources of each agent in int

    Returns:
    - None
   
    """
    if not nodes:
        print("No node has been assigned.")
        return
    root = nodes[0]
    #root node values changed. 
    agent_resources = get_agent_resources_m(max_resources)

 
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root)
    print("\n\t Initial cost allocation:\n")
    level_order_transversal_two(root)
    print("\nAgent Initial Resources:", agent_resources)
    print("\nList of Goals for minimum cost:", shortest_goals[1:]) 
    compare_m(shortest_cost, root.cost)
        
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
    
   


def calculate_resources_usage(root_node, max_resources):
    """
    Calculates the resources of each agent being used based on their assignments.

    Parameters:
    root_node (GoalNode2): The root node of the goal tree.
    max_resources (List[int]): List of maximum resources for each agent.

    Returns:
    Dict[str, int]: Dictionary containing the resources used by each agent.
    """
    shortest_cost, shortest_goals, shortest_agents = shortest_path_m(root_node)
    agent_resources = get_agent_resources_m(max_resources)
    
    

    

    if root_node.cost <= shortest_cost or (len(root_node.get_children()) == 0 and root_node.agent is not None):
        # Only calculate the resources used by the root node agent
        if isinstance(root_node.agent, str):
            agent_resources[root_node.agent] -= root_node.cost
        elif isinstance(root_node.agent, list):
            for agent in root_node.agent:
                agent_resources[agent] -= root_node.cost
    else:
        remaining_nodes = extract_node_info_m(root_node, shortest_goals[1:])
        real_nodes = []

        for node_name in shortest_goals[1:]:
            for node in remaining_nodes.values():
                if node.name == node_name:
                    real_nodes.append(node)
                    break
        
        
        def calculate_resources(nodes):
            nonlocal agent_resources

            for node in nodes:
                if isinstance(node.agent, str):
                    agent_resources[node.agent] = node.cost
                elif isinstance(node.agent, list):
                     for agent in node.agent:
                         agent_resources[agent] = node.cost ##
                else:
                    calculate_resources(node.children)

            # Set resources to 0 for agents not present in the nodes' agents list
            for agent in agent_resources:
                if agent not in [node.agent for node in nodes]:
                    agent_resources[agent] = 0

        calculate_resources(real_nodes)

    return agent_resources




def plot(root_node, max_resources):
    """
    Draws a bar plot showing the resources used by each agent.

    The x-axis represents the agent names (grace, remus, franklin),
    and the y-axis represents the amount of resources used.

    
    """

    agent_resources = calculate_resources_usage(root_node,  max_resources)

    agents = list(agent_resources.keys())
    resources = list(agent_resources.values())

    plt.bar(agents, resources, color='mediumpurple')
    plt.xlabel("Agents")
    plt.ylabel("Resources Used")
    plt.title("Agent Resources Usage")
    
    # Add y-axis values on each bar
    for i, value in enumerate(resources):
        plt.annotate(str(value), xy=(i, value), ha='center', va='bottom')
    plt.show()


    
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
    
    
    max_resources = [ 45, 60, 70]
     
 
    nodes = [root,subgoal1, subgoal2, subgoal3, subgoal4, subgoal5, subgoal6,subgoal7,subgoal8, subgoal9]
    agent_goal_m(nodes, max_resources)
    return root

def _scalability_test_tree():

    """

                    A
                    / | \
                B  C  D
                / |  /\  | \
                E  F  G S H  I
            /|    / \   /| \ 
            J K   L  M  N O  P
            / \           / \
            Q   R         T   U
        / \         
        V   W
    """

    goal_tree = GoalNode2("A", random_cost_m (45,60))
    B = GoalNode2("B", random_cost_m (25,35))
    C = GoalNode2("C", random_cost_m (25,35))
    D = GoalNode2("D", random_cost_m (25,35))
    E = GoalNode2("E", random_cost_m (15,20))
    F = GoalNode2("F", random_cost_m (15,20))
    G = GoalNode2("G", random_cost_m (15,20))
    S = GoalNode2("S", random_cost_m (15,20))
    H = GoalNode2("H", random_cost_m (15,20))
    I = GoalNode2("I", random_cost_m (15,20))
    J = GoalNode2("J", random_cost_m (10,15))
    K = GoalNode2("K", random_cost_m (10,15))
    L = GoalNode2("L", random_cost_m (10,15))
    M = GoalNode2("M", random_cost_m (10,15))
    N = GoalNode2("N", random_cost_m (10,15))
    O = GoalNode2("O", random_cost_m (10,15))
    P = GoalNode2("P", random_cost_m (10,15))
    Q = GoalNode2("Q", random_cost_m (5,10))
    R = GoalNode2("R", random_cost_m (5,10))
    T = GoalNode2("T", random_cost_m (5,10))
    U = GoalNode2("U", random_cost_m (5,10))
    V = GoalNode2("V", random_cost_m (1,5))
    W = GoalNode2("W", random_cost_m (1,5))

    goal_tree.add_child(B)
    goal_tree.add_child(C)
    goal_tree.add_child(D)

    B.add_child(E)
    B.add_child(F)
    C.add_child(G)
    C.add_child(S)
    D.add_child(H)
    D.add_child(I)

    E.add_child(J)
    E.add_child(K)
    G.add_child(L)
    G.add_child(M)
    I.add_child(N)
    I.add_child(O)
    I.add_child(P)

    J.add_child(Q)
    J.add_child(R)
    Q.add_child(V)
    Q.add_child(W)
    O.add_child(T)
    O.add_child(U)
    
      
    
    max_resources = [ 45, 60, 70]
     
 
    nodes = [goal_tree, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W]

    agent_goal_m(nodes, max_resources)



    return goal_tree



def main():
    root1 = _scalability_test_tree()
    max_resources1 = [45, 60, 70]
    root2 = random_tree_left_right()
    

    level_order_transversal_two(root1)
    agent_resources = calculate_resources_usage(root1, max_resources1)
    plot(root1, max_resources1)

if __name__ == '__main__':
    main()

