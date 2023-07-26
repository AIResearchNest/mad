from mad.data_structures import GoalNode
from typing import Dict, List, Tuple
import random
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
# Time Complexity: O(n * m); n = nodes, m = children
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
# Time Complexity: O(n * m); n = nodes, m = agents
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

    # Gather all agents available O(n * m)
    agents = []
    for goal in goal_nodes:
        for agent in goal.data:
            if agent not in agents:
                agents.append(agent)

    allocated_goals = {agent: [] for agent in agents}
    
    # If main goal is cheapest use best agent
    if len(goal_nodes) == 1:
        goal = goal_nodes[0]
        best_agents = sorted(goal.data, key=lambda k: goal.data[k])

        for agent in best_agents:
            curr_resources = max_resources[agent]
            curr_agent_goal_cost = goal.data[agent]

            if curr_resources >= curr_agent_goal_cost:
                allocated_goals[agent].append(goal)
                goal.set_agent(agent)
                return allocated_goals
            
        raise ValueError("Not enough resources")

    # Else use multiple agents to solve multiple sub-goals
    # agents_resources = {agent: max_resources for agent in agents}
    agents_resources = max_resources
    agents_cost_total = {agent: 0 for agent in agents}

    # Goal Prioritization
    # Sorts goals from most descrepancy between solutions to least descrepancy
    for goal in goal_nodes:
        goal.find_descrepancy()

    # O(n log n)
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
    
    # O(n * m)
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
            if (curr_resources >= curr_agent_goal_cost and agents_cost + curr_agent_goal_cost < sensitivity) or (curr_resources >= curr_agent_goal_cost and agents_cost < sensitivity and len(agents) > len(goal_nodes)):
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
        
        # O(n * m)
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
# Time Complexity: O(n * m) n = nodes, m = agents
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
    
    values = list(max_resources.values())
    if all(value == values[0] for value in values):
        resources = list(max_resources.values())[0]
    else:
        resources = sum(x for x in max_resources.values()) / len(max_resources.values())

    selected_goals = _optimal_path(goal_tree, resources)

    if verbose > 0:
        print("Selected Goals:")
        for goal in selected_goals:
            print(f" - {goal.name}")
        print()

    # Takes in a list of GoalNodes and distributes them among available agents
    distributed_goals = _distribute_goals(selected_goals, max_resources, verbose)

    if verbose > 0:
        total_cost, skew, discrepancy, num_agents = _get_results(distributed_goals)
        agents_used = 0
        print()
        print("Goal Allocation:")
        for agent, goals in distributed_goals.items():
            if len(distributed_goals[agent]) != 0:
                agents_used += 1
            for goal in goals:
                print(f" - {agent}: {goal.name}, {goal.cost}")
        print()
        print(f"Cost: {total_cost}")
        print(f"Skew: {skew}")
        print(f"Discrepancy: {discrepancy}")
        print(f'Number of Agents Used: {agents_used} / {num_agents}')

    return distributed_goals

"""
########################################################
"""

"""
Fay's Algorithm
########################################################
"""
from typing import Dict, List, Tuple
from mad.data_structures import GoalNode
import heapq
import copy
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
    return False


def handle_unachievable_goal(goal, list_goal, i, max_res):
    goal = list_goal.pop(i)
    if not goal.get_children():
        return i, [], max_res
    for child in goal.get_children():
        list_goal.append(child)
    return i, list_goal, max_res

def _decision_algorithm(list_goal: List[GoalNode], i: int, max_res: Dict[str, int], num_agents: int) -> Tuple[int, List[GoalNode], Dict[str, int]]:
    goal = list_goal[i]

    while not _check_resources(goal, max_res):
        goal.switch_agent()
        if goal.agent is None:
            return handle_unachievable_goal(goal, list_goal, i, max_res)

    if not goal.get_children():
        max_res[goal.agent] -= goal.cost
        return i + 1, list_goal, max_res 

    temp_resources = max_res.copy()
    child_list, grand_child_list, subgoals_cost = [], [], 0
    sorted_children = sorted(goal.get_children(), key=lambda x: x.cost if x.cost is not None else float('inf'), reverse=True)

    for child in sorted_children:
        while not _check_resources(child, temp_resources):
            child.switch_agent()
            if not child.agent:
                if not child.get_children():
                    max_res[goal.agent] -= goal.cost
                    return i + 1, list_goal, max_res  

                for grandchild in child.get_children():
                    if _check_resources(grandchild, temp_resources):
                        list_goal.append(grandchild)
                        grand_child_list.append(grandchild)
                    else:
                        grandchild.switch_agent()
                        if grandchild.agent is None:
                            return i, list_goal, max_res
                for grandchild in grand_child_list:
                    temp_resources[grandchild.agent] -= grandchild.cost 
                    subgoals_cost += grandchild.cost
        child_list.append(child)
        temp_resources[child.agent] -= child.cost  
        subgoals_cost += child.cost

    if subgoals_cost <= goal.cost:
        list_goal.remove(goal)
        list_goal.extend(child_list)
        return i, list_goal, max_res

    else:
        max_res[goal.agent] -= goal.cost
        return i + 1, list_goal, max_res
    
def allocate_goals_greedy(list_goal, max_res):
    # Initialize the goal allocation dictionary
    if len(list_goal) == 1:
        return {list_goal[0].agent: [list_goal[0]]}
    goal_allocation = {agent: [] for agent in max_res.keys()}

    # Initialize a dictionary to keep track of the number of goals assigned to each agent
    num_goals = {agent: 0 for agent in max_res.keys()}
    
    # Calculate total resources of all goals
    total_resources = sum([goal.cost for goal in list_goal])

    for goal in list_goal:
        num_goals[goal.agent] += 1


    for goal in list_goal:
        # Sort the agents based on remaining resources and the number of goals assigned to each agent
        sorted_agents = sorted(max_res.keys(), key=lambda agent: (num_goals[agent], goal.data[agent]))
        total_resources = sum([goal.cost for goal in list_goal])

        # Select the current agent handling the goal
        cur_agent = goal.agent
        assigned = False

        for agent in sorted_agents:
            # Skip the current agent
            if agent == cur_agent:
                continue
            if max_res[agent] < goal.data[agent]:
                continue
            resource_diff = goal.data[agent] - goal.cost
            if (num_goals[agent] <= num_goals[cur_agent] and resource_diff <= 0) or (num_goals[agent] < num_goals[cur_agent] and ((total_resources + resource_diff)/total_resources < 1.005)):
                goal_allocation[agent].append(goal)

                # Update the remaining resources of the agents
                max_res[agent] -= goal.data[agent]
                max_res[cur_agent] += goal.cost

                goal.set_agent(agent)


                # Increment the count of goals assigned to the agent
                num_goals[agent] += 1

                # Decrement the count of goals assigned to the current agent
                num_goals[cur_agent] -= 1

                assigned = True
                break

        # If the goal was not reassigned to a new agent, give it back to the current agent
        if not assigned:
            goal_allocation[cur_agent].append(goal)
            num_goals[cur_agent] += 1


    return goal_allocation




def optimized_goal_allocation(goal_tree: GoalNode, max_resources: List[int], verbose: int = 0) -> Tuple[Dict[str, List[GoalNode]], Dict[str, List[str]]]:
    """
    Equally distributes goals among agents while optimizing goal allocation and minimizing total resource cost.

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree 
    max_resources : List[int]
        List of maximum resources for each agent
    verbose : int, optional
        Verbosity level (0 - no print statements, 1 - print goal allocation), by default 0

    Returns
    -------
    goal_allocation: Dict
        Allocates list of goals (value) to each agent (key)
    """

    if goal_tree is None:
        raise ValueError("Goal tree is empty.")

    i = 0
    same_resources = True
    num_agents = len(max_resources)

    while i < num_agents - 1 and same_resources:
        same_resources = max_resources[i] == max_resources[i+1]
        i += 1

    agents = list(goal_tree.data.keys())
    # Initialize max_res with the initial resources for each agent
    max_res: Dict[str, int] = {agent: max_resources[i] for i, agent in enumerate(agents)}

    goal_allocation: Dict[str, List[GoalNode]] = {}

    for a in agents:
        goal_allocation[a] = []

    list_goal = []
    list_goal.append(goal_tree)

    i = 0
    while list_goal and i < len(list_goal):
        i, list_goal, max_res = _decision_algorithm(list_goal, i, max_res, num_agents)
    if not list_goal:
        return ()
    
    goal_allocation = allocate_goals_greedy(list_goal, max_res)

    if verbose:
        for agent in goal_allocation:
            print(agent, end=": ")
            for goal in goal_allocation[agent]:
                print(goal.name, end=" ")
            print("\n")
            print("The remaining resource of " + agent + ": " + str(max_res[agent]) + "\n" * 2)

    return goal_allocation, max_res





"""
########################################################
"""




"""
Maheen's Algorithm
########################################################
"""
import random as r
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
#Diajkstraaas

   
def shortest_path_m(goal_tree: GoalNode2) -> Tuple[int, List[str],  Dict[str, int]]:
    """
    Finds the most optimal goal path based on the GoalNode2.cost values throughout the tree and returns the cost
    and the list of goal names to be accomplished by agents.

    Parameters
    ----------
    goal_tree : GoalNode2
        Hierarchical Multi Agent Goal Tree.
    max_resources : List[int]
        List of max amount of resources each agent has available.

    Returns
    -------
    Tuple[int, List[str], Dict[str, Dict[str, int]]]
        Tuple containing:
        - The most optimal total cost.
        - List of goal names to be accomplished by agents.
        - Dictionary containing root node children names and their respective children names and their added cost.
    """

    def calculate_cost(node: GoalNode2) -> Dict[str, int]:
        """
        Recursively calculates the added cost for all children of the given node.

        Parameters
        ----------
        node : GoalNode2
            The current node.

        Returns
        -------
        Dict[str, int]
            A dictionary containing the added cost of all children of the current node.
        """
        def calculate_child_cost(child: GoalNode2, parent_cost: int) -> int:
            """
            Recursively calculates the cost of a child node while excluding the parent's cost.

            Parameters
            ----------
            child : GoalNode2
                The current child node.
            parent_cost : int
                The cost of the parent node.

            Returns
            -------
            int
                The added cost of the child node and its descendants.
            """
            if not child.get_children():
                return child.cost

            child_cost = child.cost
            for grandchild in child.get_children():
                child_cost += calculate_child_cost(grandchild, parent_cost=node.cost)

            return child_cost

        if not node.get_children():
            return {}

        children_costs = {}
        for child in node.get_children():
            child_cost = calculate_child_cost(child, parent_cost=node.cost)
            children_costs[child.name] = child_cost

        return children_costs
    
    def _root_child_calculate_cost(node: GoalNode2) -> int:
        """
        Recursively calculates the added cost for all children of the given node.

        Parameters
        ----------
        node : GoalNode2
            The current node.

        Returns
        -------
        int
            The added cost of all children of the current node.
        """
        if not node.get_children():
            return node.cost

        total_cost = node.cost
        
        for child in node.get_children():
            total_cost += _root_child_calculate_cost(child)

        return total_cost

    # Data structures to store the optimal path information
    #min_cost_children = float('inf')  # Minimum cost among children of the root node
       # List of goal names for the optimal path among root node children
    best_agents_children = {}         # Dictionary containing goal names and assigned agent names for the optimal path among root node children
    children_costs = {}               # Dictionary to store added costs of all children for each root node child
    min_cost_children = {} 
    
    #root node children:
    root_children = {}  # Dictionary to store root node children names and their respective costs
    root_children_total = 0
    for child in goal_tree.get_children():
        root_children[child.name] = child.cost
        root_children_total += child.cost
    #print("root children total=",root_children_total)
    #print("root children nodes:", root_children)
    
    #children's children
     # Update the min_cost_children dictionary with each child name and its cost
    # Initialize the variable to store the sum of children costs
    children_total = 0
    for child in goal_tree.get_children():
        child_cost = sum(calculate_cost(child).values())
        children_costs[child.name] = calculate_cost(child)
        min_cost_children[child.name] = child_cost
        children_total += child_cost
    #print("Children total=",children_total)  
    #print("Each root child's children added sum each", min_cost_children)
  
    #storing garndchildren names etc:
    for child in goal_tree.get_children():
        child_cost = sum(calculate_cost(child).values())
        children_costs[child.name] = calculate_cost(child)
        #print(child_cost) # Cost of parents has been removed , it gives only cost of children now. 
        # Extract the sub-dictionaries as a list
    sub_dictionaries = list(children_costs.values())    
    #print("List of nodes",sub_dictionaries)

    
    #comparsion for best_goals_children and shortest_cost
    # Comparison for best_goals_children and shortest_cost
    shortest_cost = 0
    best_goals_children = []
    #sum of node + opposite children. 
    
    both_min_sum = 0
    #both_min_sum =  
    #print(both_min_sum)
    
    # Cross-over approach: Find the minimum pair of children's costs
    min_pair_cost = float('inf')
    all_crossover_pairs = []
    min_pair_list = []
    for root_child_name, root_child_cost in root_children.items():
        for child_name, child_cost in min_cost_children.items():
            if root_child_name != child_name:  # Avoid making a pair with its own children
                pair_cost = root_child_cost + child_cost
                #print(pair_cost)
                min_pair_list.append(pair_cost)
                #print(min_pair_list)
                min_pair_cost = min(min_pair_list)
                #print(min_pair_cost)
                    
                # Store all crossover pairs for later comparison
                all_crossover_pairs.append({root_child_name: root_child_cost, child_name: child_cost})
        #print("all",all_crossover_pairs)
    
    
    if root_children_total <= children_total:
        shortest_cost = root_children_total
        best_goals_children = root_children
    elif children_total < root_children_total and children_total < min_pair_cost:
        shortest_cost = children_total
        best_goals_children = sub_dictionaries
    else:

        # Check if any pair in all_crossover_pairs sums to be equal to min_pair_cost
        matching_pairs = [pair for pair in all_crossover_pairs if pair[list(pair.keys())[0]] + pair[list(pair.keys())[1]] == min_pair_cost]

        if matching_pairs:
            # Randomly choose one pair from the matching pairs
            best_pair = r.choice(matching_pairs)
            shortest_cost = min_pair_cost
            #print("hbfbhwjrf", best_pair)
            best_goals_children.append(best_pair)
        

       

    print("Shortest cost =", shortest_cost)
    print("Best goals =", best_goals_children)
    
    
    return shortest_cost, best_goals_children

   
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
    Extracts GoalNode2 instances that have the same name as the nodes in the shortest_goals list,
    and stores them in a list.

    Parameters
    ----------
    root_node : GoalNode2
        The root node of the goal tree.

    shortest_goals : Dict[str, int] or List[Dict[str, int]]
        The dictionary or list of dictionaries representing the shortest path,
        where each dictionary contains node names and costs.

    Returns
    -------
    List[GoalNode2]
        List containing GoalNode2 instances with the same names as the nodes in the shortest path.
    """

    def find_node_by_name(node, name):
        # Helper function to find a GoalNode2 instance by its name
        if node.name == name:
            return node
        for child in node.get_children():
            result = find_node_by_name(child, name)
            if result:
                return result
        return None

    def extract_nodes_from_dict(goal_dict):
        nodes_info = []
        if isinstance(goal_dict, dict):
            for name, cost in goal_dict.items():
                node = find_node_by_name(root_node, name)
                if node:
                    nodes_info.append((node))
        return nodes_info

    node_info_list = []
    # If shortest_goals is an empty list, return an empty node_info_list
    if not shortest_goals:
        return node_info_list

    # Convert single dictionary input into a list with a single element
    if isinstance(shortest_goals, dict):
        shortest_goals = [shortest_goals]

    # If shortest_goals contains dictionaries, extract nodes from the dictionaries
    for goal in shortest_goals:
        nodes_info = extract_nodes_from_dict(goal)
        node_info_list.extend(nodes_info)

    print("List of GoalNode2 instances with their costs:", node_info_list)
    return node_info_list



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
    agents = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "trent", "karen"] #edit
    agent_resources = {agent: resource for agent, resource in zip(agents, max_resources)}
    return agent_resources




def perform_auction_m(node, agent_resources):
    """
    Author: Maheen
    Performs the auction process for assigning an agent to a goal node based on available agent resources based on the
    first sealed bid algorithm.
    If none of the agent's resources individually can cover the cost of the goal, then it shares the goal completion
    with multiple agents based on bidding winners until either the goal is completed or all agents run out of resources.

    Parameters
    ----------
    node : GoalNode2
        The goal node to be assigned an agent.
    agent_resources : Dict[str, int]
        Dictionary containing the available resources for each agent.

    Returns
    -------
    None
    """
    bids = {}  # Dictionary to store the bids of each agent

    # Create a participation dictionary to track the participation values of each agent in the goal's cost

    # Raise an error if the goal tree is empty
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
        # Deduct the cost value from the winning bidder's resources
        agent_resources[winning_bidder] -= node.cost
        node.assigned_agent = winning_bidder
    elif len(bids) > 0:
        bids.pop(winning_bidder)
        second_bidder = max(bids, key=bids.get)
        second_bid = bids[second_bidder]
        if second_bid >= node.cost:
            # Deduct the cost value from the second bidder's resources
            agent_resources[second_bidder] -= node.cost
            node.assigned_agent = second_bidder
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
                    # Deduct the cost value from the winning bidder's resources
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
                        node.assigned_agent = assigned_agents
                        # Print agent resources after the auction
                        print("Remaining Agent Resources:", agent_resources)
                    else:
                        print("\n\tNo agent can cover the cost\n")






def agent_goal_m(nodes, max_resources):
    """
    Author: Maheen
    Description: This basically calls the required functions and prints the info. This function assigns agents to goals by
                 calculating the shortest path using Dijkstra's and performing an auction-based allocation.

    Parameters:
    - nodes (list): A list of nodes representing the goals to be assigned to agents.
    - max_resources: Gets list of maximum resources of each agent in int

    Returns:
    - None
    """
    if not nodes:
        print("No node has been assigned.")
        return
    root = nodes[0]
    # root node values changed.
    agent_resources = get_agent_resources_m(max_resources)
   

    shortest_cost, shortest_goals = shortest_path_m(root)
    #print("qerfgthguju  ",shortest_goals[-1])
    
    print("\n\t Initial cost allocation:\n")
    level_order_transversal_two(root)
    print("\nAgent Initial Resources:", agent_resources)
    print("\nList of Goals for minimum cost:", shortest_goals)
    compare_m(shortest_cost, root.cost)
    

    node_info = extract_node_info_m(root, shortest_goals)
    #print(node_info)
    print("\n\tGoal assignment to agents Info:\n\t")

    if root.cost <= shortest_cost or len(root.get_children()) == 0:
        perform_auction_m(root, agent_resources)
        
    
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
    
    else:
        node_info = extract_node_info_m(root, shortest_goals)

        # If shortest_goals contains dictionaries, extract nodes from the dictionaries
        if isinstance(shortest_goals, dict):
            for node in node_info:
                if node.name != root.name:
                    found_node = next((n for n in nodes if n.name == node.name), None)
                    if found_node:
                        perform_auction_m(found_node, agent_resources)  # Pass the cost to perform_auction_m
        else:  # If shortest_goals contains only node names
            for node in node_info:
                if node.name != root.name:
                    found_node = next((n for n in nodes if n.name == node.name), None)
                    if found_node:
                        perform_auction_m(found_node, agent_resources)  # Pass None as the cost


        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)

    print("Final Agent Resources:", agent_resources)
    print("\n")



#varying costs
def cost_node(node):
    """
    Assigns the minimum value from the agents' dictionary of the node as the node's cost.

    Parameters
    ----------
    node : GoalNode22
        The node for which the cost needs to be assigned.

    Returns
    -------
    None
    """
    if node.agents:
        node.cost = min(node.agents.values())
    else:
        node.cost = 0

#sane costs

def equal_node(node):
    """
    Finds the minimum cost from the node's agents dictionary and assigns it as node.cost.
    Also changes all dictionary values to the minimum cost, except for the assigned agent.

    Parameters
    ----------
    node: GoalNode22
        The node for which to find the minimum cost and update the dictionary values.

    Returns
    -------
    None
    """
    if node.agents:
        min_cost = min(node.agents.values())  # Find the minimum cost from the agents dictionary

        # Update all dictionary values to the minimum cost, except for the assigned agent
        for agent in node.agents:
            if agent != node.assigned_agent:
                node.agents[agent] = min_cost

        # If the node has an assigned agent, set its value to 0
        if node.assigned_agent:
            node.agents[node.assigned_agent] = 0

        # Assign the minimum cost to node.cost
        node.cost = min_cost




"""
########################################################
"""
