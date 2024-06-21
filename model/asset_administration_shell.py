from datetime import datetime
import enum
from typing import Union, Any
from sqlalchemy import Column, String, Enum, DateTime, Integer
from model.base import Base


class DefineModelType(enum.Enum):
    """
    Defines the model type, can be Asset Administration Shell or Asset
    """
    aas = "aas"
    asset = "asset"


class AssetKind(enum.Enum):
    """
    Enumeration of denoting whether an asset is a type asset or an instance asset.
    \f
    :param TYPE: Hardware or software element which specifies the common attributes shared by all instances of the type.
    :param INSTANCE: Concrete, clearly identifiable component of a certain type.
    """
    TYPE = "Type"
    INSTANCE = "Instance"


class AssetAdministrationShell(Base):
    """
    Represents an Asset Administration Shell.
    \f
    :param aas_id: The globally unique identification of the element.
    :param id_short: A short name of the element.
    :param asset_kind: Denotes whether the Asset is of kind “Type” or “Instance”.
    :param global_asset_id: Global identifier of the asset the AAS represents.
    :param version: Version of the element (optional).
    :param revision: Revision of the element (optional).
    :param description: Description or comments on the element (optional).
    :param creation_date: Creation date of the Asset Administration Shell (optional).
    """
    __tablename__ = 'asset_administration_shell'

    id = Column("pk_aas", Integer, primary_key=True)
    aas_id = Column(String(2000), unique=True)
    id_short = Column(String(128), unique=True)
    asset_kind = Column(Enum(AssetKind, name='asset_kind_enum'), nullable=False)
    global_asset_id = Column(String(2000), nullable=False)
    version = Column(String(4))
    revision = Column(String(4))
    description = Column(String(1023))
    creation_date = Column(DateTime, default=datetime.now())

    def __init__(
            self,
            aas_id: str,
            id_short: str,
            asset_kind: AssetKind,
            global_asset_id: str,
            version: Union[str, None] = None,
            revision: Union[str, None] = None,
            description: Union[str, None] = None,
            creation_date: Union[DateTime, None] = None,
            *args: Any,
            **kwargs: Any
    ) -> None:
        """
        Initializes an Asset Administration Shell instance.
        \f
        Arguments:
            aas_id: The globally unique identification of the element.
            id_short: This attribute is a short name of the element.
            asset_kind: Denotes whether the Asset is of kind “Type” or “Instance”.
            global_asset_id: Global identifier of the asset the AAS is representing.
            version: Version of the element (optional).
            revision: Revision of the element (optional).
            description: Description or comments on the element (optional).
            creation_date: Creation date of the Asset Administration Shell (optional).
        """
        super().__init__(*args, **kwargs)
        self.aas_id = aas_id
        self.id_short = id_short
        self.asset_kind = asset_kind
        self.global_asset_id = global_asset_id
        self.version = version
        self.revision = revision
        self.description = description
        self.creation_date = creation_date if creation_date else datetime.now()
