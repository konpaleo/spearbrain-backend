from pydantic import BaseModel, Field, model_validator

from app.schemas.wishbone import Wishbone


class Band(BaseModel):
    loading_length: float
    wishbone: Wishbone = Field(discriminator="type")
    knot_dead_length: float = 0.5
    stretch_coeff: float | None = None
    length: float | None = None
    phi: float | None = None

    @model_validator(mode="before")
    def check_stretch_or_length(cls, values):
        stretch = values.get("stretch_coeff")
        length = values.get("length")
        if stretch is None and length is None:
            raise ValueError("Either 'stretch_coeff' or 'length' must be provided.")
        return values
