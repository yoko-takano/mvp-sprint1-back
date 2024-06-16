from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from model import AssetAdministrationShell
from model.asset_administration_shell import AssetKind


class AASSchema(BaseModel):
    """
    Defines how a new Asset Administration Shell to be inserted should be represented.
    """
    aas_id: str = "something_10293DWSds"
    id_short: str = "Air_Central_023_AAS"
    asset_kind: AssetKind = AssetKind.INSTANCE
    global_asset_id: str = "https://example.com/id/assets/"
    version: Optional[str] = "1.0"
    revision: Optional[str] = "1.3"
    description: Optional[str] = "Description or comments on the element to be created"


class AASSearchSchema(BaseModel):
    """
    Defines the structure representing the search, which will be based on the AAS ID.
    The ID needs to be UTF8-BASE64-URL-encoded.
    """
    aas_id: str = "something10293DWSds"


class AASViewSchema(BaseModel):
    id: int = 1
    aas_id: str = "something_10293DWSds"
    id_short: str = "Air_Central_023_AAS"
    asset_kind: AssetKind = AssetKind.INSTANCE
    global_asset_id: str = "https://example.com/id/assets/"
    version: Optional[str] = "1.0"
    revision: Optional[str] = "1.3"
    description: Optional[str] = "Description or comments on the element to be created"
    creation_date: Optional[datetime]


class AASListSchema(BaseModel):
    """
    Defines how a list of Asset Administration Shell will be returned.
    """
    list_aas: List[AASViewSchema]


class AASDelSchema(BaseModel):
    """
    Defines the structure of the data returned after a delete request.
    """
    message: str
    aas_id: str


def show_aas(aas: AssetAdministrationShell):
    """
    Returns a representation of the AAS following the schema defined in AASSchema.
    """
    return {
        "id": aas.id,
        "aas_id": aas.aas_id,
        "id_short": aas.id_short,
        "asset_kind": aas.asset_kind.value,
        "global_asset_id": aas.global_asset_id,
        "version": aas.version,
        "revision": aas.revision,
        "description": aas.description,
    }


def show_aas_list(aas_list: List[AssetAdministrationShell]):
    """
    Returns a representation of the AAS following the schema defined in ListAASSchema.
    """
    result = []
    for aas in aas_list:
        result.append(
            {
                "id": aas.id,
                "aas_id": aas.aas_id,
                "id_short": aas.id_short,
                "asset_kind": aas.asset_kind.value,
                "global_asset_id": aas.global_asset_id,
                "version": aas.version,
                "revision": aas.revision,
                "description": aas.description,
            })
    return {"Asset Administration Shells": result}
