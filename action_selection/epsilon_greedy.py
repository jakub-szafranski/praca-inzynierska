from __future__ import annotations
import random
from typing import TYPE_CHECKING
from collections import defaultdict

from environment import Action
from .action_selection_strategy import ActionSelectionStrategy

if TYPE_CHECKING:
    from environment.state import BaseState


class EpsilonGreedy(ActionSelectionStrategy):
    def __init__(self, epsilon: float) -> None:
        self.epsilon: float = epsilon

    def select_action(self, state: BaseState, q_values: defaultdict) -> Action:
        if random.random() < self.epsilon:
            return random.choice(list(Action))
        else:
            max_value = -float("inf")
            best_action = None
            for action in Action:
                if q_values[state][action] > max_value:
                    max_value = q_values[state][action]
                    best_action = action
            return best_action

