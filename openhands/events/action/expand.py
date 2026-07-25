from dataclasses import dataclass
from typing import ClassVar

from openhands.core.schema import ActionType
from openhands.events.action.action import Action, ActionSecurityRisk


@dataclass
class ExpandAction(Action):
    """Expands a previous compressed observation by visible observation id."""

    source_observation_id: str
    thought: str = ''
    action: str = ActionType.EXPAND
    runnable: ClassVar[bool] = True
    security_risk: ActionSecurityRisk | None = None

    @property
    def message(self) -> str:
        return f'Expanding observation: {self.source_observation_id}'
