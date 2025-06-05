from pydantic import BaseModel

from app.schemas.wishbone import Wishbone


class Band(BaseModel):
    loading_length: float
    wishbone: Wishbone
    knot_dead_length: float = 0.5
    stretch_coeff: float | None = None
    length: float | None = None
    phi: float | None = None
