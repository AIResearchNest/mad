from typing import Dict, List

from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree

from mad.optimize import jonathan_average_cost
from mad.optimize import jonathan_optimal_path
from mad.optimize import _get_goals
from mad.optimize import jonathan_distribute_goals
from mad.optimize import _score_allocation

def jonathan_algorithm(goal_tree: GoalNode, agents: List, max_resources: int) -> Dict:

    jonathan_average_cost(goal_tree)

    selected_goals = jonathan_optimal_path(goal_tree, max_resources)

    distributed_goals = jonathan_distribute_goals(selected_goals, agents, max_resources)

    return distributed_goals