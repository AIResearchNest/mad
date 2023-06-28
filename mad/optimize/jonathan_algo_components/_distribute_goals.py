from typing import Dict, List
from mad.data_structures import GoalNode

def jonathan_distribute_goals(goal_nodes: List, max_resources: int, verbose: int = 0) -> Dict:
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
        allocated_goals[best_agent].append(goal)
        goal.cost = goal.data[best_agent]
        goal.agent = best_agent
        return allocated_goals

    # Else use multiple agents to solve multiple sub-goals
    agents_resources = {agent: max_resources for agent in agents}
    agents_cost_total = {agent: 0 for agent in agents}

    # Sorts goals from most expensive min cost to least expensive min cost
    goals_sorted = list(reversed(sorted(goal_nodes, key=lambda goal: goal.cost)))

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

            curr_resources = agents_resources[agent]
            curr_agent_goal_cost = goal.data[agent]
            agents_cost = agents_cost_total[agent]
            
            # Checks that agent has enough resources and agent isn't doing too much work
            if curr_resources >= curr_agent_goal_cost and agents_cost + curr_agent_goal_cost < sensitivity:
                allocated_goals[agent].append(goal)
                agents_resources[agent] -= curr_agent_goal_cost
                agents_cost_total[agent] += curr_agent_goal_cost
                goal.cost = curr_agent_goal_cost
                goal.agent = agent
                break
            
            # If agent is last available agent
            elif agent == best_agents[-1]:
                left_over_goals.append(goal)

    if left_over_goals:
        
        if verbose > 0:
            print("Left Over Goals:")
        
        for goal in left_over_goals:
            # Sorts agents from least assigned cost to most
            least_assigned_agents = sorted(agents_cost_total, key=lambda k:agents_cost_total[k])
            
            if verbose > 0:
                print(goal.name)

            for agent in least_assigned_agents:
                
                if agent in goal.data.keys():
                    curr_resources = agents_resources[agent]
                    curr_agent_goal_cost = goal.data[agent]
                    
                    if curr_resources >= curr_agent_goal_cost:
                        allocated_goals[agent].append(goal)
                        agents_resources[agent] -= curr_agent_goal_cost
                        agents_cost_total[agent] += curr_agent_goal_cost
                        goal.cost = curr_agent_goal_cost
                        goal.agent = agent
                        break

                # If agent is last available agent
                if agent == least_assigned_agents[-1]:
                    raise ValueError("Not enough resources")

    return allocated_goals
