from dataclasses import dataclass

from openhands.core.schema import ObservationType
from openhands.events.observation.observation import Observation


@dataclass
class ExpandObservation(Observation):
    """The exact text returned for a previous compressed observation."""

    source_observation_id: str
    observation: str = ObservationType.EXPAND

    @property
    def message(self) -> str:
        return f'Expanded observation {self.source_observation_id}.'
