from flask import Blueprint, jsonify
from app.models.repository import MongoDBRepository

languages_blueprint = Blueprint('languages', __name__)

# This route will return the statistics of languages used in the repositories
@languages_blueprint.route('/languages', methods=['GET'])
def get_languages():
    db = MongoDBRepository()
    stats = db.get_language_stats()
    return jsonify(stats)