from enum import Enum


class SpeargunType(str, Enum):
    OPEN_HEAD = "OpenHead"
    CLOSED_HEAD = "ClosedHead"
    ROLLER = "Roller"
    INVERT = "Invert"


class SpeargunMaterial(str, Enum):
    ALUMINUM = "Aluminum"
    CARBON = "Carbon"
    WOOD = "Wood"


class WishboneType(str, Enum):
    LINE = "line"
    METAL = "Metal"
