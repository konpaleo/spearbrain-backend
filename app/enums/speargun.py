from enum import Enum


class SpeargunType(str, Enum):
    OPEN_HEAD = "open_head"
    CLOSED_HEAD = "closed_head"
    ROLLER = "roller"
    INVERT = "invert"


class SpeargunMaterial(str, Enum):
    ALUMINUM = "aluminum"
    CARBON = "carbon"
    WOOD = "wood"


class WishboneType(str, Enum):
    LINE = "line"
    METAL = "metal"
