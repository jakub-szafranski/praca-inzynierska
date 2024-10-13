from dataclasses import dataclass
import yaml

from environment import Action


@dataclass
class AgentPosition:
    x: int
    y: int

    def __post_init__(self):
        with open("config.yml", "r") as file:
            self.config = yaml.safe_load(file)
        self.walls = self.config.get("walls", [])

    def update(self, action: Action) -> None:
        new_x, new_y = self.x, self.y

        if action == Action.UP:
            new_y = min(self.y + 1, self.config["grid_height"] - 1)
        elif action == Action.DOWN:
            new_y = max(self.y - 1, 0)
        elif action == Action.LEFT:
            new_x = max(self.x - 1, 0)
        elif action == Action.RIGHT:
            new_x = min(self.x + 1, self.config["grid_width"] - 1)
        elif action == Action.STAY:
            new_x, new_y = self.x, self.y

        if [new_x, new_y] not in self.walls:
            self.x, self.y = new_x, new_y
        
