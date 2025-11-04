from flask import Blueprint, request, jsonify
import src.models.models as models

bp = Blueprint("routes1", __name__)

# CREATE (POST) -> /api/items
@bp.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data"}), 400

    created = models.create(data)
    return jsonify(created), 201


# READ (GET) -> /api/items
@bp.route("/items", methods=["GET"])
def get_items():
    return jsonify(models.get_all())


# READ ONE (GET) -> /api/items/<id>
@bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = models.get_by_id(item_id)

    if not item:
        return jsonify({"error": "Record not found"}), 404

    return jsonify(item)


# UPDATE (PUT) -> /api/items/<id>
@bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data"}), 400

    updated = models.update(item_id, data)

    if not updated:
        return jsonify({"error": "Record not found"}), 404

    return jsonify(updated)


# DELETE (DELETE) -> /api/items/<id>
@bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    deleted = models.delete(item_id)

    if not deleted:
        return jsonify({"error": "Record not found"}), 404

    return jsonify({"deleted": deleted})
