import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores

blp = Blueprint("Items", "items", description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item deleted"}
        except:
            abort(404, message="item not found")

    def put(self, item_id):
        item_data = request.get_json()
        item = items[item_id]
        if "name" not in item_data or "price" not in item_data:
            abort(400, message="name and price are required fields")

        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="item not found")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(store_id):
        item_data = request.get_json()

        if ("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
            abort(400, message="price, store_id, name and store_id are required fields")

        for item in items.values():
            if item["name"] == item_data["name"]:
                abort(400, message="item already exists")

        if item_data["store_id"] not in stores:
            abort(404, message="store not found")

        item_id = uuid.uuid4().hex
        item = {**item_data,  "id": item_id}
        items[item_id] = item
        return item, 201
