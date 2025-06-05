from pydantic import BaseModel, ConfigDict

from app.enums.speargun import WishboneType


class Wishbone(BaseModel):
    type: WishboneType
    length: int

    model_config = ConfigDict(use_enum_values=True)


class WishboneLine(BaseModel):
    type: WishboneType = WishboneType.LINE


class WishboneMetal(BaseModel):
    type: WishboneType = WishboneType.METAL
