import math

from pydantic import BaseModel


class Shaft(BaseModel):
    phi: float  # diameter in mm
    length: float  # in cm
    density: float = 8000  # stainless steel in kg/m3

    @property
    def estimated_shaft_weight(self) -> float:
        phi_m = self.phi / 1000
        length_m = self.length / 100
        volume_m3 = math.pi * ((phi_m / 2) ** 2) * length_m
        weight_gr = (volume_m3 * self.density) * 1000
        return round(weight_gr, 2)
