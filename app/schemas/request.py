from pydantic import BaseModel, Field

from app.schemas.speargun import Speargun


class SpeargunRequest(BaseModel):
    speargun: Speargun = Field(discriminator="type")
