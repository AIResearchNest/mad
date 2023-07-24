from mad.data_structures import GoalNode, GoalNode2, print_goal_tree, print_tree_and_agents
from mad.optimize import dfs_goal_allocation, agent_goal_m
import random as r

def _random_cost(m: int, n: int, agents: int):
    AGENTS = ["grace", "remus", "franklin", "john", "alice", "jake", "anna", "tommy", "trent", "karen"]

    d = {}
    for i in range(agents):
        d[AGENTS[i]] = r.randint(m,n)

    return d

def print_goal_tree1(node, indent=0):
    prefix = "  " * indent
    print(f"{prefix}- {node.name}: {node.assigned_agent}")
    for child in node.children:
        print_goal_tree1(child, indent + 1)

def cost_node(node):
    if node.agents:
        node.cost = min(node.agents.values())
    else:
        node.cost = 0

def print_tree_and_agents1(node):
    q = []
    q.append(node)

    while q:
        current = q[0]
        q.pop(0)
        print(f"- {current.name}: {current.cost}")

        for agent in current.agents.keys():
            print(f"   - {agent}: {current.agents[agent]}")

        for child in current.get_children():
            q.append(child)


# Scoring
def get_goals_m(root):
    
    goals = []
    
    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        goals.append(current)

        for child in current.get_children():
            q.append(child)

    return goals

def get_total_cost_m(root):
    
    total_cost = 0
    
    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        if current.assigned_agent != "":
            total_cost += current.agents[current.assigned_agent]

        for child in current.get_children():
            q.append(child)

    return total_cost

def get_agents_used_m(root):

    agents_used = []

    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        if current.assigned_agent != "":
            if current.assigned_agent not in agents_used:
                agents_used.append(current.assigned_agent)

        for child in current.get_children():
            q.append(child)
    
    return len(agents_used)

def get_discrepancy_m(root):

    num_agents = len(root.agents)
    agents_used = {}

    q = []
    q.append(root)

    while q:
        current = q[0]
        q.pop(0)

        if current.assigned_agent != "":
            if current.assigned_agent not in agents_used.keys():
                agents_used[current.assigned_agent] = current.agents[current.assigned_agent]
            else:
                agents_used[current.assigned_agent] += current.agents[current.assigned_agent]
        for child in current.get_children():
            q.append(child)
    
    return abs(max(agents_used.values()) - min(agents_used.values()))


# r.sesed(1)
num_agents = 2

root_agents = _random_cost(25, 45, num_agents)
subgoal1_agents = _random_cost(15, 20, num_agents)
subgoal2_agents = _random_cost(15, 20, num_agents)
subgoal3_agents = _random_cost(5, 15, num_agents)
subgoal4_agents = _random_cost(5, 15, num_agents)
subgoal5_agents = _random_cost(5, 15, num_agents)
subgoal6_agents = _random_cost(5, 15, num_agents)
subgoal7_agents = _random_cost(1, 5, num_agents)
subgoal8_agents = _random_cost(1, 5, num_agents)
subgoal9_agents = _random_cost(1, 5, num_agents)
subgoal10_agents = _random_cost(1, 5, num_agents)



# GoalNode
root = GoalNode("Main Goal", root_agents)
subgoal1 = GoalNode("Sub Goal 1", subgoal1_agents)
subgoal2 = GoalNode("Sub Goal 2", subgoal2_agents)
subgoal3 = GoalNode("Sub Goal 3", subgoal3_agents)
subgoal4 = GoalNode("Sub Goal 4", subgoal4_agents)
subgoal5 = GoalNode("Sub Goal 5", subgoal5_agents)
subgoal6 = GoalNode("Sub Goal 6", subgoal6_agents)

root.add_child(subgoal1)
root.add_child(subgoal2)
subgoal1.add_child(subgoal3)
subgoal1.add_child(subgoal4)
subgoal2.add_child(subgoal5)
subgoal2.add_child(subgoal6)

print_tree_and_agents(root)

dfs_goal_allocation(root, {"grace": 50, "remus": 50, "franklin": 50}, 1)
print("\n")


# GoalNode2
rootm = GoalNode2("Main Goal", 0)
subgoal1m = GoalNode2("Sub Goal 1", 0 )
subgoal2m = GoalNode2("Sub Goal 2", 0)
subgoal3m = GoalNode2("Sub Goal 3", 0)
subgoal4m = GoalNode2("Sub Goal 4", 0)
subgoal5m = GoalNode2("Sub Goal 5", 0 )
subgoal6m = GoalNode2("Sub Goal 6", 0 )
subgoal7m = GoalNode2("Sub Goal 7", 0)
subgoal8m = GoalNode2("Sub Goal 8", 0)
subgoal9m = GoalNode2("Sub Goal 9", 0 )
subgoal10m = GoalNode2("Sub Goal 10", 0 )

rootm.add_child(subgoal1m)
rootm.add_child(subgoal2m)
subgoal1m.add_child(subgoal3m)
subgoal1m.add_child(subgoal4m)
subgoal2m.add_child(subgoal5m)
subgoal2m.add_child(subgoal6m)
subgoal3m.add_child(subgoal7m)
subgoal4m.add_child(subgoal8m)
subgoal5m.add_child(subgoal9m)
subgoal6m.add_child(subgoal10m)

rootm.agents = root_agents
subgoal1m.agents = subgoal1_agents
subgoal2m.agents = subgoal2_agents
subgoal3m.agents = subgoal3_agents
subgoal4m.agents = subgoal4_agents
subgoal5m.agents = subgoal5_agents
subgoal6m.agents = subgoal6_agents
subgoal7m.agents = subgoal7_agents
subgoal8m.agents = subgoal8_agents
subgoal9m.agents = subgoal9_agents
subgoal10m.agents = subgoal10_agents

cost_node(rootm)  # Assign minimum cost from dictioanry to to the node
cost_node(subgoal1m)  # Assign cost to subgoal1
cost_node(subgoal2m)  # Assign cost to subgoal2
cost_node(subgoal3m)
cost_node(subgoal4m)
cost_node(subgoal5m)
cost_node(subgoal6m)
cost_node(subgoal7m)
cost_node(subgoal8m)
cost_node(subgoal9m)
cost_node(subgoal10m)

print_tree_and_agents1(rootm)

nodes = [rootm,subgoal1m,subgoal2m,subgoal3m,subgoal4m,subgoal5m,subgoal6m,subgoal7m,subgoal8m,subgoal9m,subgoal10m]    

max_resources = [50,50]

agent_goal_m(nodes, max_resources)

print_goal_tree1(rootm)

for goal in get_goals_m(rootm):
    print(goal.name)

print(f"TC: {get_total_cost_m(rootm)}")
print(f"AU: {get_agents_used_m(rootm)}")
print(f"D: {get_discrepancy_m(rootm)}")