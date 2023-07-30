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
    Takes in a root node to a GoalNode goal tree and a max resources int for all the agents and finds the most optimal goal path based on the GoalNode.cost values through out the tree and returns a list of GoalNodes that should be accomplished. The returned GoalNodes are selected by finding the cheapest possible solution to the goal tree.

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Hierarchical Multi Agent Goal Tree
    max_resources : int
        Integer value of max resources for each agent

    Returns
    -------
    selected_goals : List
        List of GoalNodes to be accomplished by agents in the domain
    """

    # Break Case: if GoalNode has no children, return [goal_tree]
    if not goal_tree.children:
        return [goal_tree]
    
    # Goals that will be returned
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
def _distribute_goals(goal_nodes: List, max_resources: Dict, verbose: int = 0) -> Dict:
    """
    Takes in a list of solution GoalNodes and max resources for each agent and distributes the goals too available agents evenly by making sure that each agent gets as equal of a percentage of the work as possible.

    Parameters
    ----------
    goal_nodes : List
        List of GoalNodes to distribute among available agents
    max_resources : Dict
        Dictionary containing each agent names as the keys and an int value of the amount of resources they have individually. Can be the same or different from agent to agent.

    Returns
    -------
    allocated_goals : Dict
        Dictionary of agent names (keys) and list of GoalNodes assigned to them (values)
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
    agents_resources = max_resources
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
def _get_results(agents_and_goals: Dict) -> List[int]:
    """
    Takes in a Dict of agent names and assigned goals and calculates result data. The returned data involves the total cost of the goal solution and distribution to the agents, the differences from the cheapest possible case, the range of cost disparity between agents, and the number of agents used out of the available agents

    Parameters
    ----------
    agents_and_goals : Dict
        Agent name as string and list of assigned GoalNodes as values

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
def dfs_goal_allocation(goal_tree: GoalNode, max_resources: Dict, verbose: int = 0) -> Dict:
    """
    The DFS Goal Allocation algorithm takes in the root of a GoalNode hierarchical goal tree and a Dict of agent names as keys and the amount of resources they each individually have as values {str: int}. 
    
    DFS Goal Allocation starts by finding the cheapest possible solution to the given GoalNode tree by using DFS to compare the sum of the leaf GoalNodes cost to the parent GoalNode's cost and passing the cheaper set of goals upward. This process of comparing the sum of the children GoalNodes costs against the cost of the parent GoalNode continues all the up the levels until finally the root GoalNode is compared to the cheapest solution from subgoals. The cheapest solution set of GoalNodes is returned and given to the distribution algorithm.

    The distribution algorithm then tries to evenly distribute the selected GoalNodes to the available agents so that each agent gets an even percentage of the cost of the solution.

    Finally, a Dict with the agent names as string and the assigned GoalNodes in a list as values is returned {str: list}.  

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        The root GoalNode of a Hierarchical Multi Agent Goal Tree
    max_resources : Dict
        Agent names as keys and the amount of resources they have (int) as values
    verbose : int = 0
        Enter number greater than 0 to be provided with output information

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

    # Find optimal solution
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

#Author: Fay
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
    bool
        Returns True if the agent has enough resources, False otherwise

    """
    
    if goal.agent:
        return max_res[goal.agent] >= goal.cost
    return False

#Author: Fay
#Time Complexity: 
def handle_unachievable_goal(goal: GoalNode, list_goal: List[GoalNode], i, max_res: Dict[str,int]):
    
    """
    Checks if an agent has enough resources to conduct a goal.

    Parameters
    ----------
    goal: GoalNode
        The current goal node

    list_goal: List[GoalNode]
        The list of goal nodes to be achieved

    max_res: Dict[str,int]  
        A dictionary with the agents as the keys and their corresponding resources as values

    Returns
    -------
    int, List[GoalNode], Dict[str, int]
        Returns the index of the next goal to be processed, the updated list_goal with children added,
        and the updated max_res if any resources are consumed during goal processing
    
    """

    goal = list_goal.pop(i)
    if not goal.get_children():
        return i, [], max_res
    for child in goal.get_children():
        list_goal.append(child)
    return i, list_goal, max_res

#Author: Fay
def _decision_algorithm(list_goal: List[GoalNode], i: int, max_res: Dict[str, int]) -> Tuple[int, List[GoalNode], Dict[str, int]]:
    
    """
    Implements a decision algorithm to assign agents to goals and manage resources

    Parameters
    ----------
    list_goal: List[GoalNode]
        The list of goal nodes to be achieved

    i: int
        The index of the current goal in the list_goal.

    max_res: Dict[str, int]
        A dictionary with the agents as the keys and their corresponding maximum available resources as values.

    Returns
    -------
    Tuple[int, List[GoalNode], Dict[str, int]]
        Returns a tuple containing:
        - The index of the next goal to be processed
        - The updated list_goal with any necessary adjustments
        - The updated max_res dictionary based on the agent-goal assignments and resource consumption

    """
    
    
    goal = list_goal[i]

    while not _check_resources(goal, max_res):
        goal.switch_agent()
        if goal.agent is None:
            return handle_unachievable_goal(goal, list_goal, i, max_res)

    if not goal.get_children():
        max_res[goal.agent] -= goal.cost
        return i + 1, list_goal, max_res 

    temp_resources = max_res.copy()
    temp_resources[goal.agent] += goal.cost
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

#Author: Fay
def allocate_goals_greedy(list_goal, max_res):
    """

    Allocates goals to agents using a greedy approach for an equal goal distribution

    Parameters
    ----------
    list_goal: List[GoalNode]
        The list of goal nodes to be achieved.

    max_res: Dict[str, int]
        A dictionary with the agents as the keys and their corresponding maximum available resources as values.

    Returns
    -------
    Dict[str, List[GoalNode]]
        Returns a dictionary that maps agents to the list of goals allocated to them.

    """

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
            if (num_goals[agent] < num_goals[cur_agent] and resource_diff <= 0) or (num_goals[agent] < num_goals[cur_agent] // 2 and ((total_resources + resource_diff)/total_resources < 1.005)):
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

#Author: Fay
def optimized_goal_allocation(goal_tree: GoalNode, max_resources: List[int], verbose: int = 0) -> Tuple[Dict[str, List[GoalNode]], Dict[str, List[str]]]:
    """
    Equally distributes goals among agents while optimizing goal allocation and minimizing total resource cost.

    Parameters
    ----------
    goal_tree : GoalNode
        The root node of the hierarchical Multi Agent Goal Tree.

    max_resources : List[int]
        A list of maximum available resources for each agent.

    verbose : int, optional
        Verbosity level (0 - no print statements, 1 - print goal allocation), by default 0

    Returns
    -------
    Tuple[Dict[str, List[GoalNode]], Dict[str, List[str]]]
        A tuple containing two dictionaries:
        1. goal_allocation: A dictionary that maps agents (keys) to the list of goals allocated to them (values)
        2. max_res: A dictionary that maps agents (keys) to the remaining resources after goal allocation (values)
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

    # Handle the case when there's only one agent
    if num_agents == 1:
        max_res: Dict[str, int] = {agents[0]: max_resources[0]}
        goal_allocation: Dict[str, List[GoalNode]] = {agents[0]: []}

        # Start with the root goal
        list_goal = [goal_tree]

        i = 0
        while list_goal and i < len(list_goal):
            i, list_goal, max_res = _decision_algorithm(list_goal, i, max_res)
            if not list_goal:
                break

        # Allocate the goals to the single agent
        goal_allocation[agents[0]] = list_goal

        if verbose:
            print(agents[0], end=": ")
            for goal in goal_allocation[agents[0]]:
                print(goal.name, end=" ")
            print("\n")
            print("The remaining resource of " + agents[0] + ": " + str(max_res[agents[0]]) + "\n" * 2)

        return goal_allocation, max_res


    # Initialize max_res with the initial resources for each agent
    max_res: Dict[str, int] = {agent: max_resources[i] for i, agent in enumerate(agents)}

    goal_allocation: Dict[str, List[GoalNode]] = {}

    for a in agents:
        goal_allocation[a] = []

    list_goal = []
    list_goal.append(goal_tree)

    i = 0
    while list_goal and i < len(list_goal):
        i, list_goal, max_res = _decision_algorithm(list_goal, i, max_res)
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
    
    Discription
    -----------
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

 


def find_node_by_name(node, name):
        #description: Helper function to find a GoalNode2 instance by its name
    if node.name == name:
        return node
    for child in node.get_children():
        result = find_node_by_name(child, name)
        if result:
            return result
    return None


def count_total_goals(goals_list):
    '''
    Author: Maheen
    
    Description
    -----------
        Helper function for `perform_auction_m` to count the total number of goals in the `goals_list`.
    
    Parameters
    ----------
        goals_list (list of dict): A list of dictionaries representing goal nodes and their costs.
        
    Returns
    -------
        int: The total number of goals in the `goals_list`.
    '''
    
    total_goals = 0

    for goals_dict in goals_list:
        total_goals += len(goals_dict)

    return total_goals





   
def shortest_path_m(goal_tree: GoalNode2) -> Tuple[int, List[str],  Dict[str, int]]:
    '''
    Author: Maheen
    
    Description
    ------------
    This function finds the most optimal goal(s) path based on the `GoalNode2.cost` values throughout the tree and returns the cost and the list of goal names to be accomplished by agents. 
    It is a hybrid approach to BFS and DFS because it recursively traverses the tree in a top-down manner, calculating the costs for all children and grandchildren of a node before moving on to the next node. Unlike BFS, the function does not explore the goal tree layer by layer from the root or like DFS it does not follow the traditional DFS approach where it fully explores one branch before backtracking. 
    Instead, it calculates the added cost for all children and grandchildren of a node and then proceeds to the next node as given in the order. Therefore, it has characteristics of both but is a customized approach tailored to the specific problem of finding the most optimal goals. The recursive nature of calculating costs for children and grandchildren nodes is akin to dynamic programming's approach of breaking down a complex problem into smaller overlapping subproblems. 
    Additionally, it can be seen as employing a branch and bound algorithm like strategy too as it recursively explores different branches of the goal tree while keeping track of the best cost found so far. 
    The function makes several cross-over pairs which involves mkaing a dictionary to store node, its children names and their respective costs added in several combinations. For instance, a pair of added cost of all children of root node, a pair with all leaf nodes added cost, and pairs of each root node's child added with its own grandchildren. Then it utilizes Heuristic Search technique guided by some rules to look over the cross-over pairs costs to compare pairs costs to identify a pair that consist of minimum cost. 
    The final result is the most optimal total cost and the list of goal names that makes the most optimal goal path in the Multi-Agent Goal Tree. 
    

    Parameters
    ----------
        goal_tree (GoalNode2): The hierarchical Multi-Agent Goal Tree.

    Returns:
        Tuple[int, List[str], Dict[str, int]]: A tuple containing:
            - The most optimal total cost.
            - List of goal names to be accomplished by agents.
            - Dictionary containing root node children names and their respective children names and their added cost.
    '''

    def calculate_cost(node: GoalNode2) -> Dict[str, int]:
        """
        Author: Maheen 
        Description: Recursively calculates the added cost for all children of the given node.

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
            Author: Maheen 
            
            Description:Recursively calculates the cost of a child node while excluding the parent's cost.

            Parameters
            ----------
            child : GoalNode2
                The current child node.
            parent_cost : int
                The cost of the parent node.

            Returns
            -------
            int:
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
        Author: Maheen 
        
        Description: Recursively calculates the added cost for all children of the given node.

        Parameters
        ----------
        node : GoalNode2
            The current node.

        Returns
        -------
        int:
            The added cost of all children of the current node.
        """
        if not node.get_children():
            return node.cost

        total_cost = node.cost
        
        for child in node.get_children():
            total_cost += _root_child_calculate_cost(child)

        return total_cost
    
    def extract_nodes_from_dict(goal_dict):
        nodes_info = []
        if isinstance(goal_dict, dict):
            for name, cost in goal_dict.items():
                node = find_node_by_name(goal_tree ,name)
                if node:
                    nodes_info.append((node))
            return nodes_info

    best_agents_children = {}         # Dictionary containing goal names and assigned agent names for the optimal path among root node children
    children_costs = {}               # Dictionary to store added costs of all children for each root node child
    min_cost_children = {} 
    
    #root node children:
    root_children = {}  # Dictionary to store root node children names and their respective costs
    root_children_total = 0
    for child in goal_tree.get_children():
        root_children[child.name] = child.cost
        root_children_total += child.cost

    # Initialize the variable to store the sum of children costs
    children_total = 0
    for child in goal_tree.get_children():
        child_cost = sum(calculate_cost(child).values())
        children_costs[child.name] = calculate_cost(child)
        min_cost_children[child.name] = child_cost
        children_total += child_cost

  
    #storing garndchildren names etc:
    for child in goal_tree.get_children():
        child_cost = sum(calculate_cost(child).values())
        children_costs[child.name] = calculate_cost(child)
        
        # Extract the sub-dictionaries as a list
    sub_dictionaries = list(children_costs.values())    

    # Comparison for best_goals_children and shortest_cost
    shortest_cost = 0
    best_goals_children = []
    #sum of node + opposite children. 
    
    both_min_sum = 0
   
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
    
    
    def check_pure_grandchildren(node, grandchildren, root_node_grandchildren, all_grandchild):
        """
        Author: Maheen
        
        Description: Recursively checks if grandchildren are purely leaf nodes of the same root node child.

        Parameters
        ----------
        node : GoalNode2
            The current node in the goal tree.
        grandchildren : dict or int
            The dictionary containing grandchildren and their costs, or an integer if it is a leaf node.
        root_node_grandchildren : set
            Set to store grandchildren keys of the root node child.
        all_grandchild : bool
            Flag to track if all grandchildren are leaf nodes.

        Returns
        -------
        bool
            True if grandchildren are purely leaf nodes of only one root node child, False otherwise.
        """
        if isinstance(grandchildren, int):
            return all_grandchild
        
        for grandchild_name, grandchild_cost in grandchildren.items():
            if all_grandchild:
                grandchild_node = find_node_by_name(node, grandchild_name)
                if grandchild_node and grandchild_node.get_children():
                    all_grandchild = False
                    break
                
            if root_node_grandchildren is None:
                root_node_grandchildren = set(grandchildren.keys())
            else:
                if set(grandchildren.keys()) != root_node_grandchildren:
                    all_grandchild = False
                    break

            # Recursively check if grandchildren are leaf nodes for nested grandchildren
            all_grandchild = check_pure_grandchildren(node, grandchild_cost, root_node_grandchildren, all_grandchild)

        return all_grandchild

    
    
    if root_children_total <= children_total:
        shortest_cost = root_children_total
        best_goals_children = root_children
    elif children_total < root_children_total and children_total < min_pair_cost:
        shortest_cost = children_total
        best_goals_children = sub_dictionaries
        #check if best_goals_children consists of purely all children of one rootnode child.
        print(best_goals_children)
        # Check if best_goals_children consists of purely all grandchildren of only one rootnode child.
        # Check if best_goals_children consists of purely all grandchildren of only one rootnode child.
        # Check if best_goals_children consists of purely all grandchildren/leaf nodes of only one rootnode child.
        root_node_grandchildren = None
        is_single_root_node_child = True
        all_grandchild = True
    
        for child_dict in best_goals_children:
            if isinstance(child_dict, dict):
                # Case 1: Child node with grandchildren
                if not child_dict:  # Skip empty dictionaries
                    break
                # Case 1: Child node with grandchildren
                child_name = next(iter(child_dict))  # Get the child node name
                grandchildren_cost_dict = child_dict[child_name]  # Get the grandchildren and their costs as a dictionary
                
                all_grandchild = check_pure_grandchildren(goal_tree, grandchildren_cost_dict, root_node_grandchildren, all_grandchild)
                is_single_root_node_child = False
                if not is_single_root_node_child:
                    break
            
    
    

        if is_single_root_node_child:
            print("best_goals_children consists of purely all grandchildren of only one rootnode child.")
        else:
            print("best_goals_children does not consist of purely all grandchildren of only one rootnode child.")
        
        if is_single_root_node_child == True:   #issue 
            # Add all the other root node's children to the optimal solution
            for child_name, child_cost in children_costs.items():
                if child_name != root_child_name:
                    best_goals_children.append({child_name: child_cost})
            
            
            #find nodes to update shortets_cost
            shortest_cost = 0
            for goal in best_goals_children:
                if goal:  # Skip empty dictionaries
                    
                    goal_name = goal.keys()  # Get the goal name (dictionary key)
                    print(goal_name, "fec")
                    nodes = extract_nodes_from_dict(goal)
                    for node in nodes:
                        shortest_cost += node.cost
                 
        
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
    
    Compare the shortest path cost with the cost of the root node's agent and prints the result.

    Parameters
    ----------
    shortest_cost : int
        The shortest path cost.

    root_node_cost : int
        The cost of the root node's agent.
        
    Returns
    -------
        None
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
    
    Description
    -----------
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
    
    Description: 
    ------------
    Gives agents resources to all agents

    Parameters
    ----------
    max_resources: List[int]
        The list of max resources for each agent

    Returns
    -------
    agent_resources: Dict
        storing the list.
    
    '''
    agents = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "trent", "karen"] #edit
    agent_resources = {agent: resource for agent, resource in zip(agents, max_resources)}
    return agent_resources



def perform_auction_m(root, goals, agents, cost):
    '''
    Author: Maheen
    
    Description
    -----------
        Implements an equal allocation algorithm. It assigns all agents to goal nodes in optimal path so that the each agent can share a percentage of the participation in covering the total cost of the optimal goals. Such that,
        the algorithm aims to distribute the goals among the agents in a way that the cost is shared evenly. It also updates the resources of each agent according to its participation. 
    
    Parameters:
    ----------
    root (GoalNode2):
        The root node representing the overall goal structure.
    goals (list of GoalNode2):
        The list of individual goal nodes to be achieved.
    agents (dict): 
        A dictionary containing agents' names as keys and their available resources as values.
    cost (float): 
        The total cost to be distributed among agents.
        
    Returns
    ------
        None
    
    '''
    
        #add when root node alone condition 
    if root == goals:
        total_agents = len(agents)
        total_goals = 1
        avg_goals_per_agent = (total_goals / total_agents)
        
   
        for agent in agents:
            root.assigned_agent.append(agent)
        
    else:    
        total_agents = len(agents)
        print(total_agents, "Total Agents")
        
        total_goals = count_total_goals(goals)
        print(total_goals, "Total_goals") 
        avg_goals_per_agent = (total_goals / total_agents) #round
        print(avg_goals_per_agent, "average")
        
        #Step1:  Extract the individual goals and costs from each GoalNode2 instance
        all_goals = extract_goalnodes_dict(root, goals)
        print(all_goals, "all goals........\n")
        
    
        # Step 2: Assign all agents to each goal
        for goal in all_goals:
            
            for agent in agents:
                goal.assigned_agent.append(agent)
            
#outside elese
    # Step 3: Update resources for each agent
    for agent_name, agent_resources in agents.items():
        resource = (avg_goals_per_agent * cost)/100
        new_resource = agent_resources - resource
        agents[agent_name] = round(new_resource, 2)  # Rounding to 2 decimal places
        print(agents[agent_name], "new agent resources")
    



def extract_goalnodes_dict(root , goal_nodes):

    """
    Author: Maheen
    
    Description
    ---------- 
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
    List[GoalNode2]:
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
                node = find_node_by_name(root, name)
                if node:
                    nodes_info.append((node))
        return nodes_info

    node_info_list = []
    # If shortest_goals is an empty list, return an empty node_info_list
    if not goal_nodes:
        return node_info_list

    # Convert single dictionary input into a list with a single element
    if isinstance(goal_nodes, dict):
        goal_nodes = [goal_nodes]

    # If shortest_goals contains dictionaries, extract nodes from the dictionaries
    for goal in goal_nodes:
        nodes_info = extract_nodes_from_dict(goal)
        node_info_list.extend(nodes_info)

    print("List of GoalNode2 instances with their costs:", node_info_list)
    return node_info_list


def agent_goal_m(nodes, max_resources) -> None:
    """
    Author: Maheen
    
    Description
    ---------- 
    This basically calls the required functions for finding optimla path, assigning agents and prints the information
    Parameters
    ----------
    nodes : list
        A list of nodes representing the goals to be assigned to agents.
    
    max_resources : list
        Gets list of maximum resources of each agent in int
        
    Returns
    -------
    cost: int
        Total Cost of optimal goals
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
        cost = root.cost
        perform_auction_m(root, root, agent_resources, cost)
        
    
        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
        
    
    else:
        node_info = extract_node_info_m(root, shortest_goals)
        cost = shortest_cost
        perform_auction_m(root, shortest_goals, agent_resources, cost)  # Pass None as the cost


        print("\n\t\tFINAL INFO\n")
        level_order_transversal_two(root)
        
    

    print("Final Agent Resources:", agent_resources)
    print("\n")
    return cost
    



#varying costs
def cost_node(node):
    """
    Author: Maheen
    
    Description
    ----------
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
    Author: Maheen
    
    Description
    ----------
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
