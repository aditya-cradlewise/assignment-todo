from flask import Blueprint, request, jsonify
from app.service.todo_service import TodoService
from app.entity.todo_entity import list_entity, item_entity

bp = Blueprint("todo", __name__)
service = TodoService()

# LIST ROUTES

# CREATE LIST
@bp.route("/lists", methods=["POST"])
def create_list():
    data = request.get_json()
    list_id = service.create_list(data.get("title"))
    return jsonify({"id": list_id}), 201


# GET ALL LISTS
@bp.route("/lists", methods=["GET"])
def get_lists():
    lists = service.get_lists()
    return jsonify([list_entity(l) for l in lists]), 200


# GET SINGLE LIST
@bp.route("/lists/<int:list_id>", methods=["GET"])
def get_list(list_id):
    list_data = service.get_list(list_id)
    return jsonify(list_entity(list_data)), 200


# UPDATE LIST
@bp.route("/lists/<int:list_id>", methods=["PUT"])
def update_list(list_id):
    data = request.get_json()
    service.update_list(list_id, data.get("title"))
    return jsonify({"message": "List updated"}), 200


# DELETE LIST
@bp.route("/lists/<int:list_id>", methods=["DELETE"])
def delete_list(list_id):
    service.delete_list(list_id)
    return jsonify({"message": "List deleted"}), 200


# ARCHIVE LIST
@bp.route("/lists/<int:list_id>/archive", methods=["PUT"])
def archive_list(list_id):
    service.archive_list(list_id)
    return jsonify({"message": "List archived"}), 200



# ITEM ROUTES

# CREATE ITEM
@bp.route("/lists/<int:list_id>/items", methods=["POST"])
def create_item(list_id):
    data = request.get_json()
    item_id = service.create_item(
        list_id,
        data.get("title"),
        data.get("due_date"),
    )
    return jsonify({"id": item_id}), 201


# GET ITEMS BY LIST
@bp.route("/lists/<int:list_id>/items", methods=["GET"])
def get_items(list_id):
    items = service.get_items(list_id)
    return jsonify([item_entity(i) for i in items]), 200


# MARK ITEM COMPLETE
@bp.route("/items/<int:item_id>/complete", methods=["PUT"])
def mark_complete(item_id):
    service.mark_complete(item_id)
    return jsonify({"message": "Item marked complete"}), 200

# ARCHIVE ITEM
@bp.route("/items/<int:item_id>/archive", methods=["PUT"])
def archive_item(item_id):
    service.archive_item(item_id)
    return jsonify({"message": "Item archived"}), 200


# DELETE ITEM
@bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    service.delete_item(item_id)
    return jsonify({"message": "Item deleted"}), 200