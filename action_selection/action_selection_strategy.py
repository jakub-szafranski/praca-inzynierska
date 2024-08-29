from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from environment import BaseState, Action

class ActionSelectionStrategy(ABC):
    @abstractmethod
    def select_action(self, state: BaseState, q_values) -> Action:
        pass