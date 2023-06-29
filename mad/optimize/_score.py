
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