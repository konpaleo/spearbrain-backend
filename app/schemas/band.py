from pydantic import BaseModel, ConfigDict


class Band(BaseModel):
    length: float | None
    stretch_coeff: float | None

    model_config = ConfigDict(use_enum_values=True)
