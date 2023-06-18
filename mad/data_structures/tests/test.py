from mad.data_structures._multi_agent_goal_nodes import GoalNode

def main():
    goal1 = GoalNode("scan ocean", {"grace": 20, "franklin": 30,"remus": 33}, [], [])
    goal2 = GoalNode("scan top", {"grace": 10, "franklin": 15,"remus": 12}, [], [])
    goal3 = GoalNode("scan bottom", {"grace": 5, "franklin": 20,"remus": 12}, [], [])

    goal1.add_child(goal2)
    goal1.add_child(goal3)

    goal2.add_parent(goal1)
    goal3.add_parent(goal1)

    for child in goal1.children:
        print(child.name)

    for parent in goal2.parents:
        print(parent.name)

    
if __name__ == '__main__':
    main()