from flask import Blueprint, request, jsonify
from server.models import db, Plant

plant_bp = Blueprint("plant_bp", __name__)

# GET /plants
@plant_bp.route("/plants", methods=["GET"])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200

# GET /plants/<id>
@plant_bp.route("/plants/<int:id>", methods=["GET"])
def get_plant(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.to_dict()), 200

# POST /plants
@plant_bp.route("/plants", methods=["POST"])
def create_plant():
    data = request.get_json()
    try:
        plant = Plant(
            name=data["name"],
            image=data["image"],
            price=data["price"]
        )
        db.session.add(plant)
        db.session.commit()
        return jsonify(plant.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PATCH /plants/<id>
@plant_bp.route("/plants/<int:id>", methods=["PATCH"])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()
    try:
        if "name" in data:
            plant.name = data["name"]
        if "image" in data:
            plant.image = data["image"]
        if "price" in data:
            plant.price = data["price"]

        db.session.commit()
        return jsonify(plant.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# DELETE /plants/<id>
@plant_bp.route("/plants/<int:id>", methods=["DELETE"])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    try:
        db.session.delete(plant)
        db.session.commit()
        return jsonify({"message": f"Plant {id} deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
