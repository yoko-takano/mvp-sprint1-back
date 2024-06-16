from flask_openapi3 import Info, OpenAPI, Tag
from flask import redirect, jsonify
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote

from logger import logger
from model import Session
from model.asset_administration_shell import AssetAdministrationShell, AssetKind
from schemas import ErrorSchema
from schemas.asset_administration_shell import AASSchema, show_aas, AASListSchema, show_aas_list, AASDelSchema, \
    AASSearchSchema, AASViewSchema

# First definitions
info = Info(title="Asset Administration Shell Repository", version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)

# Defining tags
home_tag = Tag(
    name="Documentation",
    description="Document Selection: Swagger, Redoc or RapiDoc"
)
aas_tag = Tag(
    name="Asset Administration Shell",
    description="This interface allows managing Asset Administration Shells"
)


@app.get("/", tags=[home_tag])
def home():
    """
    Redirects to /openapi, the screen that allows choosing the documentation style.
    """
    return redirect('/openapi')


def check_existing_id_short(session, id_short, aas_id):
    """
    Check if another Asset Administration Shell with the same id_short exists in the database,
    excluding the current AAS with aas_id.
    """
    return session.query(AssetAdministrationShell).filter(
        AssetAdministrationShell.id_short == id_short,
        AssetAdministrationShell.aas_id != aas_id
    ).first()


def check_required_fields(form: AASSchema):
    """
    Checks if the required fields 'aas_id', 'id_short', and 'global_asset_id' are not empty or whitespace only.
    Returns True if all required fields are valid, otherwise False.
    """
    required_fields = ['aas_id', 'id_short', 'global_asset_id']

    for field in required_fields:
        value = getattr(form, field)
        if not value:
            return False

    return True


def strip_whitespace(form: AASSchema):
    """
    Strip leading and trailing whitespace from all relevant fields in the form.
    """
    form.aas_id = form.aas_id.strip()
    form.id_short = form.id_short.strip()
    form.global_asset_id = form.global_asset_id.strip()
    if form.version:
        form.version = form.version.strip()
    if form.revision:
        form.revision = form.revision.strip()
    if form.description:
        form.description = form.description.strip()


@app.post("/aas", tags=[aas_tag],
          responses={"200": AASViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def post_aas(form: AASSchema):
    """
    Creates a new Asset Administration Shell.
    """

    # Strip whitespace from fields
    strip_whitespace(form)

    # Validate required fields
    if not check_required_fields(form):
        error_msg = "Fields 'aas_id', 'id_short', and 'global_asset_id' are required and cannot be empty"
        logger.warning(f"Error creating Asset Administration Shell: {error_msg}")
        return jsonify({"message": error_msg}), 400

    aas = AssetAdministrationShell(
        aas_id=form.aas_id,
        id_short=form.id_short,
        asset_kind=AssetKind(form.asset_kind),
        global_asset_id=form.global_asset_id,
        version=form.version,
        revision=form.revision,
        description=form.description
    )

    logger.debug(f"Creating Asset Administration Shell with ID: {aas.aas_id}")
    session = Session()

    try:
        # Verify if aas_id already exists in database
        existing_aas_id = session.query(AssetAdministrationShell).filter_by(aas_id=aas.aas_id).one_or_none()
        if existing_aas_id:
            error_msg = f"Asset Administration Shell already exists with ID: {aas.aas_id}"
            logger.warning(f"Error creating Asset Administration Shell: {aas.aas_id}, {error_msg}")
            return jsonify({"message": error_msg}), 409

        # Verify if id_short already exists in database
        existing_id_short = session.query(AssetAdministrationShell).filter_by(id_short=aas.id_short).one_or_none()
        if existing_id_short:
            error_msg = f"Asset Administration Shell already exists with Id Short: {aas.id_short}"
            logger.warning(f"Error creating Asset Administration Shell: {aas.id_short}, {error_msg}")
            return jsonify({"message": error_msg}), 409

        session.add(aas)
        session.commit()
        logger.debug(f"Asset Administration Shell with ID {aas.aas_id} created successfully")
        return jsonify(show_aas(aas)), 200

    except IntegrityError as e:
        # Handle IntegrityError specifically
        error_msg = f"Asset Administration Shell already exists"
        logger.warning(f"Error creating Asset Administration Shell: {aas.aas_id}, {error_msg}")
        return jsonify({"message": error_msg}), 409

    except Exception as e:
        # Handle unexpected errors
        error_msg = f"Could not save new Asset Administration Shell"
        logger.warning(f"Error creating Asset Administration Shell '{aas.aas_id}', {error_msg}")
        return jsonify({"message": error_msg}), 400

    finally:
        session.close()


@app.get("/aas_list", tags=[aas_tag],
         responses={"200": AASListSchema, "404": ErrorSchema})
def get_aas_list():
    """
    Returns all Asset Administration Shells.
    """
    logger.debug(f"Collecting Asset Administration Shells")
    session = Session()

    try:
        aas_list = session.query(AssetAdministrationShell).all()
        if not aas_list:
            return jsonify({"Asset Administration Shells": []}), 200
        else:
            logger.debug(f"{len(aas_list)} Asset Administration Shells found")
            return jsonify(show_aas_list(aas_list)), 200

    finally:
        session.close()


@app.get("/aas", tags=[aas_tag],
         responses={"200": AASViewSchema, "404": ErrorSchema})
def get_aas(query: AASSearchSchema):
    """
    Returns a specific Asset Administration Shell by its Unique Identifier.
    """
    aas_id = query.aas_id
    logger.debug(f"Collecting data for Asset Administration Shell #{aas_id}")
    session = Session()

    try:
        aas = session.query(AssetAdministrationShell).filter(AssetAdministrationShell.aas_id == aas_id).first()
        if not aas:
            error_msg = "Asset Administration Shell not found"
            logger.warning(f"Error finding Asset Administration Shell: {aas_id}, {error_msg}")
            return jsonify({"message": error_msg}), 404
        else:
            logger.debug(f"Asset Administration Shell data #{aas_id} found")
            return jsonify(show_aas(aas)), 200

    finally:
        session.close()


@app.delete("/aas", tags=[aas_tag],
            responses={"200": AASDelSchema, "404": ErrorSchema})
def delete_aas(query: AASSearchSchema):
    """
    Deletes an Asset Administration Shell.
    """
    aas_id = unquote(unquote(query.aas_id))
    logger.debug(f"Deleting data from Asset Administration Shell #{aas_id}")
    session = Session()

    try:
        count = session.query(AssetAdministrationShell).filter(AssetAdministrationShell.aas_id == aas_id).delete()
        session.commit()

        if count:
            logger.debug(f"Deleting Asset Administration Shell #{aas_id}")
            return jsonify({"message": "Asset Administration Shell deleted", "aas_id": aas_id}), 200
        else:
            error_msg = "Asset Administration Shell not found in database"
            logger.warning(f"Error deleting AAS #{aas_id}, {error_msg}")
            return jsonify({"message": error_msg}), 404
    finally:
        session.close()


@app.put("/aas", tags=[aas_tag],
         responses={"200": AASSchema, "404": ErrorSchema})
def put_aas(form: AASSchema):
    """
    Updates an existing Asset Administration Shell.
    """
    aas_id = form.aas_id
    logger.debug(f"Updating data for Asset Administration Shell #{aas_id}")
    session = Session()

    try:
        # Verify if AAS with the aas_id exists in database
        aas = session.query(AssetAdministrationShell).filter(AssetAdministrationShell.aas_id == aas_id).first()
        if not aas:
            error_msg = "Asset Administration Shell not found in database"
            logger.warning(f"Error updating Asset Administration Shell #{aas_id}, {error_msg}")
            return jsonify({"message": error_msg}), 404

        # Verify if another AAS with the same id_short already exists
        existing_id_short = check_existing_id_short(session, form.id_short, aas_id)
        if existing_id_short:
            error_msg = f"Another Asset Administration Shell already exists with Id Short: {form.id_short}"
            logger.warning(f"Error updating Asset Administration Shell #{aas_id}, {error_msg}")
            return jsonify({"message": error_msg}), 409

        # Strip whitespace from fields
        strip_whitespace(form)

        # Validate required fields
        if not check_required_fields(form):
            error_msg = "Fields 'aas_id', 'id_short', and 'global_asset_id' are required and cannot be empty"
            logger.warning(f"Error updating Asset Administration Shell #{aas_id}, {error_msg}")
            return jsonify({"message": error_msg}), 400

        aas.id_short = form.id_short
        aas.asset_kind = AssetKind(form.asset_kind)
        aas.global_asset_id = form.global_asset_id
        aas.version = form.version
        aas.revision = form.revision
        aas.description = form.description

        session.commit()
        logger.debug(f"Updated Asset Administration Shell #{aas_id}")
        return jsonify(show_aas(aas)), 200

    finally:
        session.close()
