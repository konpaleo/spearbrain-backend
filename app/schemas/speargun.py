from typing import Literal

from pydantic import BaseModel, ConfigDict

from app.enums.speargun import SpeargunMaterial, SpeargunType
from app.schemas.band import Band
from app.schemas.shaft import Shaft


class SpeargunBase(BaseModel):
    type: SpeargunType
    bands: list[Band]
    shaft: Shaft | None = None
    material: SpeargunMaterial | None = None

    model_config = ConfigDict(use_enum_values=True)


class SpeargunOpen(SpeargunBase):
    type: Literal[SpeargunType.OPEN_HEAD] = SpeargunType.OPEN_HEAD
    muzzle_dead_length: float = 2

    def get_effective_length(self, band: Band) -> float:
        return band.loading_length - band.wishbone.dead_length - band.knot_dead_length

    def calculate_band_lengths(self) -> list[float | None]:
        return [self._calculate_single_band_length(band) for band in self.bands]

    def _calculate_single_band_length(self, band: Band) -> float | None:
        """
        Length refers to one circular band, from end to end.
        """
        effective_length = self.get_effective_length(band)
        length = (
            2 * ((effective_length / band.stretch_coeff) + band.knot_dead_length)
            + self.muzzle_dead_length
        )
        return round(length, 2)

    def calculate_band_streches(self) -> list[float | None]:
        return [self._calculate_single_band_strech(band) for band in self.bands]

    def _calculate_single_band_strech(self, band: Band) -> float | None:
        effective_length = self.get_effective_length(band)
        stretch = effective_length * (
            1 / (((band.length - self.muzzle_dead_length) / 2) - band.knot_dead_length)
        )
        return round(stretch, 2)


class SpeargunClosed(SpeargunBase):
    type: Literal[SpeargunType.CLOSED_HEAD] = SpeargunType.CLOSED_HEAD

    def get_effective_length(self, band: Band) -> float:
        return (
            band.loading_length - band.wishbone.dead_length - 2 * band.knot_dead_length
        )

    def calculate_band_lengths(self) -> list[float | None]:
        return [self._calculate_single_band_length(band) for band in self.bands]

    def _calculate_single_band_length(self, band: Band) -> float | None:
        """
        Length refers to one band, from end to end.
        """
        effective_length = self.get_effective_length(band)
        length = (effective_length / band.stretch_coeff) + 2 * band.knot_dead_length
        return round(length, 2)

    def calculate_band_streches(self) -> list[float | None]:
        return [self._calculate_single_band_strech(band) for band in self.bands]

    def _calculate_single_band_strech(self, band: Band) -> float | None:
        effective_length = self.get_effective_length(band)
        stretch = effective_length / (band.length - 2 * band.knot_dead_length)
        return round(stretch, 2)


class SpeargunRoller(SpeargunBase):
    type: Literal[SpeargunType.ROLLER] = SpeargunType.ROLLER


class SpeargunInvert(SpeargunBase):
    type: Literal[SpeargunType.INVERT] = SpeargunType.INVERT


Speargun = SpeargunOpen | SpeargunClosed | SpeargunRoller | SpeargunInvert
