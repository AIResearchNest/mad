from typing import Dict, List
from mad.data_structures import GoalNode

def jonathan_distribute_goals(goal_nodes, agents, max_resources) -> Dict:
    
    allocated_goals = {agent: [] for agent in agents}
    agents_resources = {agent: max_resources for agent in agents}
    agents_cost_total = {agent: 0 for agent in agents}
    goals_sorted = list(reversed(sorted(goal_nodes, key=lambda goal: goal.cost)))
    # sensitivity = goal_nodes[0].cost * 2 // len(agents)
    sensitivity = sum(max(node.data.values()) for node in goal_nodes) / len(agents)
    print(sensitivity)

    for goal in goals_sorted:
        best_agents = sorted(goal.data, key=lambda k: goal.data[k])

        for i, agent in enumerate(best_agents):
            resources = agents_resources[agent]
            agent_goal_cost = goal.data[agent]
            agents_cost = agents_cost_total[agent]
            
            if resources >= agent_goal_cost and agents_cost < sensitivity:
                allocated_goals[agent].append(goal)
                agents_resources[agent] -= agent_goal_cost
                agents_cost_total[agent] += agent_goal_cost
                goal.cost = agent_goal_cost
                goal.agent = agent
                break
            elif i == len(best_agents) - 1:
                print("Not enough resources")
                return allocated_goals

    return allocated_goals



















# Takes a list of GoalNodes and returns a dict of agent and assignments
# def jonathan_distribute_goals(goal_nodes, agents, max_resources) -> Dict:
    
#     allocated_goals = {agent: [] for agent in agents}
#     agents_resources = {agent: max_resources for agent in agents}
    
#     goals_per_agent = len(goal_nodes) // len(agents)
#     left_over_goals = len(goal_nodes) % len(agents)

#     goals_sorted = list(reversed(sorted(goal_nodes, key=lambda goal: goal.cost)))

#     if left_over_goals > 0:
#         for goal in goals_sorted[:left_over_goals]:
#             best_agents = sorted(goal.data, key=lambda k: goal.data[k])

#             for agent in best_agents:
#                 resources = agents_resources[agent]
#                 agent_goal_cost = goal.data[agent]
#                 if resources >= agent_goal_cost and len(allocated_goals[agent]) < 1:
#                     allocated_goals[agent].append(goal)
#                     agents_resources[agent] -= agent_goal_cost
#                     goal.cost = agent_goal_cost
#                     goal.agent = agent
#                     break

#     agents_goals_left = {agent: goals_per_agent for agent in agents}

#     for goal in goals_sorted[left_over_goals:]:
#         best_agents = sorted(goal.data, key=lambda k: goal.data[k])

#         for i, agent in enumerate(best_agents):
#             resources = agents_resources[agent]
#             agent_goal_cost = goal.data[agent]
#             goals_left = agents_goals_left[agent]
#             if resources >= agent_goal_cost and 0 < goals_left <= goals_per_agent:
#                 allocated_goals[agent].append(goal)
#                 agents_resources[agent] -= agent_goal_cost
#                 agents_goals_left[agent] -= 1
#                 goal.cost = agent_goal_cost
#                 goal.agent = agent
#                 break
#             elif i == len(best_agents) - 1:
#                     print("Not enough resources")
#                     return allocated_goals
            
#     return allocated_goals
