from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, Field, validator, field_validator

from model import AssetAdministrationShell
from model.asset_administration_shell import AssetKind, DefineModelType


class AASSchema(BaseModel):
    """
    Defines how a new Asset Administration Shell to be inserted should be represented.
    """
    aas_id: str = Field(...,
                        description="The globally unique identification of the element")
    id_short: str = Field(...,
                          description="A short name of the element")
    asset_kind: AssetKind = Field(default=AssetKind.INSTANCE,
                                  description="Denotes whether the Asset is of kind 'Type' or 'Instance'")
    global_asset_id: str = Field(...,
                                 description="Global identifier of the asset the AAS represents")
    version: Optional[str] = Field(None, description="Version of the element")
    revision: Optional[str] = Field(None, description="Revision of the element")
    description: Optional[str] = Field(None, description="Description or comments on the element")

    @field_validator("version", "revision", mode="before")
    @classmethod
    def convert_to_string(cls, v: Union[str, float, int]) -> Union[str, None]:
        if v is not None:
            return str(v)
        return None


class AASUpdateSchema(AASSchema):
    """
    Defines how an existing Asset Administration Shell should be updated.
    Inherits from AASSchema, simply adding update_aas_id as a parameter.
    """
    update_aas_id: str = Field(None,
                               description="New AAS ID to update in the database")


class AASSearchSchema(BaseModel):
    """
    Defines the structure representing the search, which will be based on the AAS ID.
    The ID needs to be UTF8-BASE64-URL-encoded.
    """
    aas_id: str = Field(...,
                        description="The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded).")


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


class IdEncodeDecodeSchema(BaseModel):
    """
    Defines the response schema for encoded and decoded IDs.
    """
    encode_aas_id: str
    decode_aas_id: str


class ModelTypeSchema(BaseModel):
    type_model: DefineModelType = DefineModelType.aas


def show_encode_decode_ids(ids: IdEncodeDecodeSchema):
    """
    Returns a representation of the encoded and decoded identifiers.
    """
    return {
        "encode_aas_id": ids.encode_aas_id,
        "decode_aas_id": ids.decode_aas_id
    }


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
