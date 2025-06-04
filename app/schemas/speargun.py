from pydantic import BaseModel, ConfigDict

from app.enums.speargun import SpeargunMaterial, SpeargunType


class SpeargunBase(BaseModel):
    type: SpeargunType
    material: SpeargunMaterial

    model_config = ConfigDict(use_enum_values=True)


class SpeargunOpen(SpeargunBase):
    type: SpeargunType = SpeargunType.OPEN_HEAD
    material: SpeargunMaterial

    model_config = ConfigDict(use_enum_values=True)


class SpeargunClosed(SpeargunBase):
    type: SpeargunType = SpeargunType.CLOSED_HEAD
    material: SpeargunMaterial

    model_config = ConfigDict(use_enum_values=True)


class SpeargunRoller(SpeargunBase):
    type: SpeargunType = SpeargunType.ROLLER
    material: SpeargunMaterial

    model_config = ConfigDict(use_enum_values=True)


class SpeargunInvert(SpeargunBase):
    type: SpeargunType = SpeargunType.INVERT
    material: SpeargunMaterial

    model_config = ConfigDict(use_enum_values=True)
