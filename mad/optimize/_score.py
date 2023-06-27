
def _score_allocation(agents_and_goals):
    score = 0

    for value in agents_and_goals.values():
        for goal in value:
            score += goal.cost
    return score