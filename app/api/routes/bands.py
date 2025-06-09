from fastapi import APIRouter

from app.schemas.request import SpeargunRequest

router = APIRouter()


@router.post(
    "/calculate-length",
    summary="Calculate band length",
    description="Calculate the required band length based on speargun configuration. You must provide either the desired stretch coefficient.",
    tags=["Bands"],
)
def calculate_band_lengths(payload: SpeargunRequest):
    return {"band_lengths": payload.speargun.calculate_band_lengths()}


@router.post(
    "/calculate-stretch",
    summary="Calculate band stretch",
    description="Calculate the band stretch of each band, based on speargun configuration. You must provide the band length.",
    tags=["Bands"],
)
def calculate_bands_stretch(payload: SpeargunRequest):
    return {"band_lengths": payload.speargun.calculate_band_streches()}
