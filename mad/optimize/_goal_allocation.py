from mad.data_structures import GoalNode
from typing import Dict, List, Tuple

# private function should be as follows
def _helper_func():
    pass

def initial_goal_allocation(goal_tree: GoalNode,
                            max_resources: int) -> Dict:
    
    """
    Optimizes allocation of goals to multiple agents

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Heirarichal Multi Agent Goal Tree 
    max_resources : int
        Maximum resources available for each agent

    Returns
    -------
    goal_allocation: Dict
        Allocates list of goals (value) to each agent (key)
    """

    # write your code here

    # Raise an error if goal_tree is empty

    pass



"""
Jonathan's Algorithm
########################################################
"""
from mad.data_structures import print_goal_tree, print_tree_and_agents

# Author: Jonathan
# Time Complexity: O(n * k); n = number of goal nodes, k = average children per goal
def _optimal_path(goal_tree: GoalNode, max_resources: int) -> List:
    """
    Takes in a goal tree and max resources for each agent and finds the most optimal goal path based on the GoalNode.cost values through out the tree and returns a list of GoalNodes that should be accomplished

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns
    -------
    selected_goals : List
        List of GoalNodes to be accomplished by agents in the world
    """
    
    # Break Case: if GoalNode has no children, return [goal_tree]
    if not goal_tree.children:
        return [goal_tree]
    
    # Goals that will be returned upwards for each recursion call
    selected_goals = []

    # Current GoalNode's children GoalNodes
    child_goals = []
    for child in goal_tree.children:
        child_goals.extend(_optimal_path(child, max_resources))
    
    # Finds total cost of all children GoalNodes for comparison
    child_cost = sum(min(child.data.values()) for child in child_goals)
    goal_tree_cost = min(goal_tree.data.values())
    
    # Checks that a goal cost is less than the max possible resources an agent can have ands that the current GoalNode is cheaper than it's children
    if goal_tree_cost <= max_resources and goal_tree_cost < child_cost:
        selected_goals.append(goal_tree)
    # Otherwise add the children nodes
    else:
        selected_goals.extend(child_goals)
    
    return selected_goals

# Author: Jonathan
# Time Complexity: O(n * m) n = number of nodes, m = max agents per goal
def _distribute_goals(goal_nodes: List, max_resources: int, verbose: int = 0) -> Dict:
    """
    Takes in a list of GoalNodes and distributes them among available agents

    Parameters
    ----------
    goal_nodes : List
        List of GoalNodes to distribute among agents
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns
    -------
    allocated_goals : Dict
        Dictionary of agent names (keys) and list of GoalNodes assigned (values)
    """

    agents = []
    for goal in goal_nodes:
        for agent in goal.data:
            if agent not in agents:
                agents.append(agent)

    allocated_goals = {agent: [] for agent in agents}
    
    # If main goal is cheapest use best agent
    if len(goal_nodes) == 1:
        goal = goal_nodes[0]
        best_agent = min(goal.data, key=lambda k: goal.data[k])
        agent_goal_cost = goal.data[best_agent]

        if max_resources >= agent_goal_cost:
            allocated_goals[best_agent].append(goal)
            goal.set_agent(best_agent)
            return allocated_goals
        else:
            raise ValueError("Not enough resources")

    # Else use multiple agents to solve multiple sub-goals
    agents_resources = {agent: max_resources for agent in agents}
    agents_cost_total = {agent: 0 for agent in agents}

    # Goal Prioritization
    # Sorts goals from most descrepancy between solutions to least descrepancy
    for goal in goal_nodes:
        goal.find_descrepancy()

    goals_sorted = list(reversed(sorted(goal_nodes, key=lambda goal: goal.descrepancy)))

    if verbose > 0:
        # Finds worst case distribution cost
        worst_case = sum(max(goal.data.values()) for goal in goal_nodes)
        # Finds average case distribution cost
        avg_case = sum(sum(goal.data.values()) / len(goal.data.values()) for goal in goal_nodes)

    # Finds best case distribution cost
    best_case = sum(min(goal.data.values()) for goal in goal_nodes)
    
    # Finds percent of costs each agent should accomplish in terms of best case allocation
    sensitivity = best_case / len(agents)
    
    if verbose > 0:
        print(f"Worst Case: {worst_case}")
        print(f"Avg Case: {avg_case}")
        print(f"Best Case: {best_case}")
        print(f"Sensitivity: {sensitivity}")
        print()
    
    left_over_goals = []
    for goal in goals_sorted:
        # List of agents from best fit to worst fit
        best_agents = sorted(goal.data, key=lambda k: goal.data[k])

        for agent in best_agents:
            # Agent resources
            curr_resources = agents_resources[agent]
            # Agent total cost already assigned
            agents_cost = agents_cost_total[agent]
            # Agent cost to acheive this goal
            curr_agent_goal_cost = goal.data[agent]
            
            # Checks that agent has enough resources and agent isn't doing too much work based on sensitivity
            # if curr_resources >= curr_agent_goal_cost and agents_cost + curr_agent_goal_cost < sensitivity:
            if curr_resources >= curr_agent_goal_cost and agents_cost < sensitivity:
                # Update agent
                allocated_goals[agent].append(goal)
                agents_resources[agent] -= curr_agent_goal_cost
                agents_cost_total[agent] += curr_agent_goal_cost
                # Update GoalNode
                goal.set_agent(agent)
                break

            # If agent is last available agent
            elif agent == best_agents[-1]:
                left_over_goals.append(goal)

    if left_over_goals:
        
        if verbose > 0:
            print("Left Over Goals:")
        
        for goal in left_over_goals:
            # Sorts agents from least assigned agent to most assigned
            least_assigned_agents = sorted(agents_cost_total, key=lambda k:agents_cost_total[k])
            
            if verbose > 0:
                print(f" - {goal.name}")

            for agent in least_assigned_agents:
                
                # If agent can accomplish this goal
                if agent in goal.data.keys():
                    curr_resources = agents_resources[agent]
                    curr_agent_goal_cost = goal.data[agent]
                    
                    # If agent has enough resources, assign the goal
                    if curr_resources >= curr_agent_goal_cost:
                        # Update agent
                        allocated_goals[agent].append(goal)
                        agents_resources[agent] -= curr_agent_goal_cost
                        agents_cost_total[agent] += curr_agent_goal_cost
                        # Update GoalNode
                        goal.set_agent(agent)
                        break

                # If agent is last available agent
                if agent == least_assigned_agents[-1]:
                    raise ValueError("Not enough resources")

    return allocated_goals

# Author: Jonathan
# Time Complexity: O(n * m) n = nodes, m = agents
def _get_results(agents_and_goals: Dict) -> List:
    """
    Takes in dict of agents' name and assigned goals and returns a list of results

    Parameters
    ----------
    agents_and_goals : Dict
        Agent name as string and list of GoalNodes as values

    Returns 
    -------
    [total_cost, skew, discrepancy, number_agents_used] : List of ints
        List containing: total_cost = cost of allocation, skew = difference between best case allocation and chosen allocation, discrepancy = difference of most assigned agents' cost and least assigned agents' cost, num_agents_used = number of used/available agents
    """

    best_case = 0
    total_cost = 0
    agents_used = []
    agents_costs = []

    for agent in agents_and_goals.keys():

        curr_agent_cost = 0

        for goal in agents_and_goals[agent]:
            best_case += min(goal.data.values())
            curr_agent_cost += goal.cost
            
            for agent in goal.data.keys():
                if agent not in agents_used:
                    agents_used.append(agent)
        
        agents_costs.append(curr_agent_cost)
        total_cost += curr_agent_cost

    discrepancy = abs(max(agents_costs) - min(agents_costs))
    skew = abs(best_case - total_cost)

    return [total_cost, skew, discrepancy, len(agents_used)]

# Author: Jonathan
# Time Complexity: O(n + m * a) n = nodes, m = selected goals, a = number of agents
def dfs_goal_allocation(goal_tree: GoalNode, max_resources: int, verbose: int = 0) -> Dict:
    """
    Takes in a goal tree and finds optimal goals to accomplish the main goal and distributes them to agents evenly

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns
    -------
    Returns : Dict
        Dictionary of agent names (keys) and list of GoalNodes assigned (values)
    """
    
    if verbose > 0:
        print("Agent Costs:")
        print_tree_and_agents(goal_tree)
        print()
        print("Goal Tree:")
        print_goal_tree(goal_tree)
        print()

    # Finds the cheapest path to solve the goal tree and returns a list of chosen GoalNodes
    selected_goals = _optimal_path(goal_tree, max_resources)

    if verbose > 0:
        print("Selected Goals:")
        for goal in selected_goals:
            print(f" - {goal.name}")
        print()

    # Takes in a list of GoalNodes and distributes them among available agents
    distributed_goals = _distribute_goals(selected_goals, max_resources, verbose)

    if verbose > 0:
        total_cost, skew, discrepancy, num_agents_used = _get_results(distributed_goals)
        print()
        print("Goal Allocation:")
        for key, value in distributed_goals.items():
            for goal in value:
                print(f" - {key}: {goal.name}, {goal.cost}")
        print()
        print(f"Cost: {total_cost}")
        print(f"Skew: {skew}")
        print(f"Discrepancy: {discrepancy}")
        print(f'Number of Agents: {num_agents_used}')

    return distributed_goals

"""
########################################################
"""

"""
Fay's Algorithm
########################################################
"""

from typing import Dict, List, Tuple
from mad.data_structures import GoalNode, level_order_transversal

def _check_resources(goal: GoalNode, max_res: Dict[str, int]) -> bool:
    """
    Checks if an agent has enough resources to conduct a goal.

    Parameters
    ----------
    goal: GoalNode
        The current goal node

    max_res: Dict[str,int]  
        A dictionary with the agents as the keys and their corresponding resources as values

    Returns
    -------
        Returns True if the agent has enough resources, False otherwise.

    """
    if goal.agent:
        return max_res[goal.agent] >= goal.cost


def _decision_algorithm(list_goal: List[GoalNode], i: int, max_res: Dict[str, int]) -> Tuple[int, List[GoalNode], Dict[str, int]]:
    """
    Decides whether to choose the current goal or its subgoals
    
    Parameters
    ----------
    list_goal : List[GoalNode]
        A list of the goals needed to be achieved
    i: int
        The current index
    max_res: Dict[str,int]
        A dictionary with the agents as the keys and their corresponding resources as values
    
    Returns
    -------
        Returns a tuple containing: the updated index, the modified list of goals, the updated dictionary of maximum resources

    """

    goal = list_goal[i]

    # Check if the current goal can be completed by any agent
    while not _check_resources(goal, max_res):
        # Try switching to another agent
        goal.switch_agent() 

        # If no agent can complete this goal
        if goal.agent is None: 
            goal = list_goal.pop(i)

            # If the goal has no child, return empty list_goal
            if not goal.get_children():
                return i, [], max_res

            # Add child goals to list_goal
            for child in goal.get_children():
                list_goal.append(child)
            
            return i, list_goal, max_res
    
    #print(goal.name + " can be completed by " + goal.agent + "\n")

    # If the current goal does not have child nodes
    if not goal.get_children(): 
        max_res[goal.agent] -= goal.cost
        return i + 1, list_goal, max_res 
    
    d = max_res.copy()
    
    child_list: List[GoalNode] = []
    grand_child_list: List[GoalNode] = []

    subgoals_cost = 0

    # Sort the children goals in descending order of their costs
    children = sorted(goal.get_children(), key=lambda x: x.cost if x.cost is not None else float('inf'), reverse=True)
    for child in children:
        while not _check_resources(child, d):
            # Switch to another agent
            child.switch_agent()  

            # If no agent can finish this child goal
            if not child.agent:  
                a = child

                # If this child node does not have children nodes
                if not a.get_children():  
                    max_res[goal.agent] -= goal.cost
                    
                    # Return the same list without any change
                    return i + 1, list_goal, max_res  
                
                e = []

                for grandchild in a.get_children():
                    if _check_resources(grandchild, d):
                        list_goal.append(grandchild)
                        e.append(grandchild)
                    else:
                        grandchild.switch_agent()
                        # If one grandchild could not complete, return the original goal list
                        if grandchild.agent is None:  
                            return i, list_goal, max_res
                for goal in e:
                     # Subtract the cost from the resource
                    d[goal.agent] -= goal.cost 
                    subgoals_cost += goal.cost

        # If the child goal can be completed
        # Add the child goal to the child list
        child_list.append(child)
        # Subtract the cost from the resource  
        d[child.agent] -= child.cost  
        subgoals_cost += child.cost

    if min(subgoals_cost, goal.cost) == subgoals_cost:
        list_goal.remove(goal)
        for child in child_list:
            list_goal.append(child)
        if grand_child_list:
            for grandchild in grand_child_list:
                list_goal.append(grandchild)
        return i, list_goal, max_res

    else:
        max_res[goal.agent] -= goal.cost
        return i + 1, list_goal, max_res


def optimized_goal_allocation(goal_tree: GoalNode, max_resources: List[int], verbose: int = 0) -> Tuple[Dict[str, List[GoalNode]], Dict[str, List[str]]]:
    
    """
    Optimizes allocation of goals to multiple agents

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree 

    Returns
    -------
    goal_allocation: Dict
        Allocates list of goals (value) to each agent (key)
    
    """

    if goal_tree is None:
        raise ValueError("Goal tree is empty.")

    #Dictionary that contains the name and the max resource of each agent
    max_res: Dict[str,int] = {}
    
    #Name of the agents
    agents = ["grace", "remus", "franklin"]
    
    for i in range(len(agents)):
        max_res[agents[i]] = max_resources[i]

    goal_allocation: Dict[str, List[GoalNode]] = {"grace": [], "remus": [], "franklin": []}

    list_goal = []
    list_goal.append(goal_tree)

    i = 0
    while i < len(list_goal):
        i, list_goal, max_res = _decision_algorithm(list_goal,i, max_res)
    """
        for j in list_goal:
            print(j.name, " ")
        print(max_res)
    print("\n\nThe "'most'" optimized goal tre: \n")
    level_order_transversal(goal_tree)
    """    
        

    for goal in list_goal:
        goal_allocation[goal.agent].append(goal)

    #print("\nTo complete the goal in the most optimized way, we can assign goals like this:\n")
    
    if verbose:
        for agent in goal_allocation:
            print (agent, end = ": ")
            for goal in goal_allocation[agent]:
                print (goal.name, end = " ")
            print("\n")
            print("The remaining resource of " + agent +": " + str(max_res[agent]) + "\n" * 2)

    return goal_allocation, max_res
"""
########################################################
"""




"""
Maheen's Algorithm
########################################################
"""
import random
from typing import Dict, List, Tuple
import heapq
from mad.data_structures._multi_agent_goal_node_two import GoalNode2, level_order_transversal_two



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
        shortest_cost (int): This represents the shortest path cost from the root node to the goal node.
        shortest_goals (List[str]): This is a list of goal names representing the shortest path from the root node to the goal node.
        shortest_agents (List[str]): This is a list of agent names representing the agents assigned to the goals along the shortest path.

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
            node_info[node.name] = node.cost

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
  
   



"""
########################################################
"""
