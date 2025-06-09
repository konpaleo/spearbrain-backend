from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.enums.speargun import WishboneType


class WishboneBase(BaseModel):
    type: WishboneType

    model_config = ConfigDict(use_enum_values=True)


class WishboneLine(WishboneBase):
    type: Literal[WishboneType.LINE] = WishboneType.LINE
    length: float  # in cm

    @property
    def dead_length(self) -> float:
        return self.length / 2


class WishboneMetal(WishboneBase):
    type: Literal[WishboneType.METAL] = WishboneType.METAL
    _dead_length: float = 2.0

    @property
    def dead_length(self) -> float:
        return self._dead_length


# Discriminated Union for parsing
Wishbone = WishboneLine | WishboneMetal
