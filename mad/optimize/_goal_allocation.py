from mad.data_structures import GoalNode
from typing import Dict, List

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
from mad.data_structures import print_goal_tree

def _get_goals(goal_tree: GoalNode) -> List:
    """
    Takes in a goal tree and traverses it using BFS and appends each GoalNode to an output list

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree

    Returns
    -------
    output : List
        List containing each GoalNode in a Hierarchical Goal Tree
    """
    output = []
    q = []
    q.append(goal_tree)
    while q:
        current = q[0]
        q.pop(0)
        output.append(current)
        for child in current.get_children():
            q.append(child)

    return output

def _jonathan_average_cost(goal_tree: GoalNode, verbose: int = 0) -> None:
    """
    Takes in a goal tree and updates each GoalNode's agent cost to a temporary value of the average cost of all agents able to accomplish that goal

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    """
    
    # Raise an error if goal_tree is empty (???)
    if goal_tree is None:
        raise ValueError("Tree is empty!")

    # For each goal find minimum cost among available agents and assign the temporary cost to the goal
    goals = _get_goals(goal_tree)

    for goal in goals:
        
        costs = [x for x in goal.data.values()]
        
        # Average
        # avg_cost = sum(costs) / len(costs)
        # goal.cost = avg_cost
        
        # Min
        goal.cost = min(costs)
        
        if verbose > 0:
            print(f"{goal.name}: {goal.cost}")
            for agent, cost in goal.data.items():
                print(f" - {agent}: {cost}")

def _jonathan_optimal_path(goal_tree: GoalNode, max_resources: int) -> List:
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

    # Current GoalNodes children GoalNodes
    child_goals = []
    for child in goal_tree.children:
        child_goals.extend(_jonathan_optimal_path(child, max_resources))
    
    # Finds total cost of all children GoalNodes for comparison
    child_cost = sum(child.cost for child in child_goals)
    
    # Checks that a goal cost is less than the max possible resources an agent can have ands that the current GoalNode is cheaper than it's children
    if goal_tree.cost <= max_resources and goal_tree.cost < child_cost:
        selected_goals.append(goal_tree)
    # Otherwise add the children nodes
    else:
        selected_goals.extend(child_goals)
    
    return selected_goals

def _jonathan_distribute_goals(goal_nodes: List, max_resources: int, verbose: int = 0) -> Dict:
    """
    Takes in a list of GoalNodes and distributes them among available agents

    Parameters
    ----------
    goal_nodes : List
        List of GoalNodes to distribute among agents
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns : Dict
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

    # Sorts goals from most expensive min cost to least expensive min cost
    goals_sorted = list(reversed(sorted(goal_nodes, key=lambda goal: goal.cost)))

    if verbose > 0:
        # Finds worst case distribution cost
        worst_case = sum(max(node.data.values()) for node in goal_nodes)
        # Finds average case distribution cost
        a = [sum(x.data.values()) / len(x.data.values()) for x in goal_nodes]
        avg_case = sum(a)

    # Finds best case distribution cost
    best_case = sum(min(node.data.values()) for node in goal_nodes)
    
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
            if curr_resources >= curr_agent_goal_cost and agents_cost + agents_cost < sensitivity:
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
                        allocated_goals[agent].append(goal)
                        agents_resources[agent] -= curr_agent_goal_cost
                        agents_cost_total[agent] += curr_agent_goal_cost
                        goal.set_agent(agent)
                        break

                # If agent is last available agent
                if agent == least_assigned_agents[-1]:
                    raise ValueError("Not enough resources")

    return allocated_goals

def _score_allocation(agents_and_goals):
    
    # Total Cost of all goals
    score = 0

    for goals in agents_and_goals.values():
        for goal in goals:
            score += goal.cost

    agents_costs = []

    for goals in agents_and_goals.values():
        cost = 0
        for goal in goals:
            cost += goal.cost
        agents_costs.append(cost)

    # Cost differene between lowest assigned agent and max assigned agent
    difference_score = abs(max(agents_costs) - min(agents_costs))
    
    return [score, difference_score]

def jonathan_algorithm(goal_tree: GoalNode, max_resources: int, verbose: int = 0) -> Dict:
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
    
    # Takes in a goal tree and updates each GoalNode's agent cost to a temporary value of the average cost of all agents able to accomplish that goal
    if verbose > 0:
        print("Agent Costs:")

    _jonathan_average_cost(goal_tree, verbose)

    if verbose > 0:
        print()
        print("Goal Tree:")
        print_goal_tree(goal_tree)
        print()

    # Takes in a goal tree and max resources for each agent and finds the most optimal goal path based on the GoalNode.cost values through out the tree and returns a list of GoalNodes that should be accomplished
    selected_goals = _jonathan_optimal_path(goal_tree, max_resources)

    if verbose > 0:
        print("Selected Goals:")
        for goal in selected_goals:
            print(f" - {goal.name}")
        print()

    # Takes in a list of GoalNodes and distributes them among available agents
    distributed_goals = _jonathan_distribute_goals(selected_goals, max_resources, verbose)

    if verbose > 0:
        print()
        print("Goal Allocation:")
        for key, value in distributed_goals.items():
            for goal in value:
                print(f" - {key}: {goal.name}, {goal.cost}")
        
        print()
        score = _score_allocation(distributed_goals)
        print(f"Score: {score[0]}")
        print(f"Discrepancy: {score[1]}")

    # Clean up goal tree (set nodes that weren't selected costs back to None)
    all_goals = _get_goals(goal_tree)
    for goal in all_goals:
        if goal not in selected_goals:
            goal.cost = None

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
    while not _check_resources(list_goal[i], max_res):
        
        #switch to another agent to finish the goal
        list_goal[i].switch_agent() 

        #if no agent can complete this
        if list_goal[i].agent is None: 
            a = list_goal.pop(i)  
            #if no agent can complete the goal and the goal has no child
            if not a.get_children():
                return i, [], max_res
            for child in a.get_children():
                list_goal.append(child)
            return i, list_goal, max_res
        
    print(list_goal[i].name + " can be completed by " + list_goal[i].agent + "\n")

    #if there is an agent can complete this goal
    
    #if this goal does not have child nodes
    if not list_goal[i].get_children(): 
        max_res[list_goal[i].agent] -= list_goal[i].cost
        return i + 1, list_goal, max_res 
    
    d = max_res.copy()
    
    child_list: List[GoalNode] = []
    grand_child_list: List[GoalNode] = []

    subgoals_cost = 0

    for child in list_goal[i].get_children():
        while not _check_resources(child, d):
            # switch to another agent
            child.switch_agent()  

            # If no agent can finish this child goal
            if not child.agent:  
                a = child

                # if this child node does not have children nodes
                if not a.get_children():  
                    max_res[list_goal[i].agent] -= list_goal[i].cost
                    
                    # return the same list without any change
                    return i + 1, list_goal, max_res  
                
                e = []

                for grandchild in a.get_children():
                    if _check_resources(grandchild, d):
                        list_goal.append(grandchild)
                        e.append(grandchild)
                    else:
                        grandchild.switch_agent()
                        # if one grandchild could not complete, return the original goal list
                        if grandchild.agent is None:  
                            return i, list_goal, max_res
                for i in e:
                     # subtract the cost from the resource
                    d[i.agent] -= i.cost 
                    subgoals_cost += i.cost

        # if the child goal can be completed

        # add the child goal to the child list
        child_list.append(child)
        # subtract the cost from the resource  
        d[child.agent] -= child.cost  
        subgoals_cost += child.cost

    if min(subgoals_cost, list_goal[i].cost) == subgoals_cost:
        a = list_goal.pop(i)
        for child in child_list:
            list_goal.append(child)
        if grand_child_list != None:
            for grandchild in grand_child_list:
                list_goal.append(grandchild)
        return i, list_goal, max_res

    else:
        max_res[list_goal[i].agent] -= list_goal[i].cost
        return i + 1, list_goal, max_res
 
 
def optimized_goal_allocation(goal_tree: GoalNode, max_resources: List[int]) -> None:
    
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

    goal_allocation: Dict[str, List[str]] = {"grace": [], "remus": [], "franklin": []}

    list_goal = []
    list_goal.append(goal_tree)

    i = 0
    while i < len(list_goal):
        i, list_goal, max_res = _decision_algorithm(list_goal,i, max_res)
        
        for j in list_goal:
            print(j.name, " ")
        print(max_res)
    print("\n\nThe "'most'" optimized goal tre: \n")
    level_order_transversal(goal_tree)

    for goal in list_goal:
        goal_allocation[goal.agent].append(goal.name)

    print("\nTo complete the goal in the most optimized way, we can assign goals like this:\n")
    
    result, resource = goal_allocation, max_res
    
    for agent in result:
        print (agent, end = ": ")
        for i in result[agent]:
            print (i, end = " ")
        print("\n")
        print("The remaining resource of " + agent +": " + str(resource[agent]) + "\n" * 2)

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
from mad.data_structures._multi_agent_goal_node_two import GoalNode, level_order_transversal_two



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


def agent_goal_m(a: Dict[str, int], resources: Dict[str, int]) -> str:
    """
    Author: Maheen
    Decides which agent will conduct the current goal based on the agent's current available resources.

    Parameters
    ----------
    a : Dict[str, int]
        Dictionary containing the cost values for each agent.
    resources : Dict[str, int]
        Dictionary containing the available resources for each agent.

    Returns
    -------
    name: str
        Name of the agent assigned to each node.
    """
    agents = ["grace", "remus", "franklin"]

    # Assign the first three agents to the first three nodes
    if len(a) <= 3:
        agent_assigned = agents[len(a) - 1]
        resources[agent_assigned] -= a[agent_assigned]
        return agent_assigned

    # Calculate the cost difference for each agent
    cost_diff = {agent: resources[agent] - a[agent] for agent in agents}

    # Sort the agents based on the cost difference in ascending order
    sorted_agents = sorted(cost_diff, key=lambda agent: cost_diff[agent])

    # Find the first agent with a non-negative cost difference
    for agent in sorted_agents:
        if cost_diff[agent] >= 0:
            agent_assigned = agent
            resources[agent_assigned] -= a[agent_assigned]
            return agent_assigned

    # If no agent has a non-negative cost difference, choose the agent with the smallest negative cost difference
    agent_assigned = sorted_agents[0]
    resources[agent_assigned] -= a[agent_assigned]
    return agent_assigned




def perform_auction_m(node, agent_resources):
    """
    Author: Maheen
    Performs the auction process for assigning an agent to a goal node based on available agent resources based on first sealed bid algorithm.
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
    else:
        # If the winning bidder cannot cover the cost, find the second highest bidder
        bids.pop(winning_bidder)
        if len(bids) > 0:
            second_bidder = max(bids, key=bids.get)
            second_bid = bids[second_bidder]
            if second_bid >= node.cost:
                node.agent = second_bidder
                agent_resources[second_bidder] -= node.cost

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
def shortest_path_m(root_node: GoalNode) -> tuple[int, List[str], List[str]]:
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
        The shortest path cost, list of goals, and list of agents.
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


"""
########################################################
"""
