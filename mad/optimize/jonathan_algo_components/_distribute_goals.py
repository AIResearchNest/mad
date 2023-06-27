from typing import Dict, List
from mad.data_structures import GoalNode

def jonathan_distribute_goals(goal_nodes: List, agents: List, max_resources: int) -> Dict:
    """
    Takes in a list of GoalNodes and distributes them among available agents

    Parameters
    ----------
    goal_nodes : List
        List of GoalNodes to distribute among agents
    agents : List
        List of string names of agents available
    max_resources : int
        Value for the max amount of resources each agent has available

    Returns : Dict
        Dictionary of agent names (keys) and list of GoalNodes assigned (values)
    """

    allocated_goals = {agent: [] for agent in agents}
    
    # If main goal is cheapest
    if len(goal_nodes) == 1:
        goal = goal_nodes[0]
        best_agent = min(goal.data, key=lambda k: goal.data[k])
        allocated_goals[best_agent].append(goal)
        goal.cost = goal.data[best_agent]
        goal.agent = best_agent
        return allocated_goals

    # Else multiple agents
    agents_resources = {agent: max_resources for agent in agents}
    agents_cost_total = {agent: 0 for agent in agents}

    # Sorts goals from cheapest average cost to most expensive
    goals_sorted = list(reversed(sorted(goal_nodes, key=lambda goal: goal.cost)))

    # Takes worst case distribution cost and divides by the amount of agents
    # sensitivity = sum(max(node.data.values()) for node in goal_nodes) / len(agents)
    print(f"Worst Case: {sum(max(node.data.values()) for node in goal_nodes)}")
    # sensitivity = sum(node.cost for node in goals_sorted) / len(agents)
    print(f"Avg Case: {sum(node.cost for node in goals_sorted)}")
    sensitivity = sum(min(node.data.values()) for node in goal_nodes) / len(agents)
    print(f"Best Case: {sum(min(node.data.values()) for node in goal_nodes)}")
    print(f"Sensitivity: {sensitivity}")

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
    print()
    if left_over_goals:
        print("Left Over Goals:")
        for goal in left_over_goals:

            # sort agents from least total cost to most
            least_assigned_agents = sorted(agents_cost_total, key=lambda k:agents_cost_total[k])
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
                    print(" ".join(x for x in least_assigned_agents))
                    print(f"Not enough resources: {agent}")
                    return allocated_goals

    return allocated_goals
