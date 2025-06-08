from abc import ABC, abstractmethod

from pydantic import BaseModel, ConfigDict

from app.enums.speargun import WishboneType


class Wishbone(BaseModel, ABC):
    type: WishboneType

    @property
    @abstractmethod
    def dead_length(self) -> float:
        pass

    model_config = ConfigDict(use_enum_values=True)


class WishboneLine(Wishbone):
    type: WishboneType = WishboneType.LINE
    length: float  # in cm

    @property
    def dead_length(self) -> float:
        return self.length / 2


class WishboneMetal(Wishbone):
    type: WishboneType = WishboneType.METAL
    _dead_length: float = 2.0  # fixed

    @property
    def dead_length(self) -> float:
        return self._dead_length
