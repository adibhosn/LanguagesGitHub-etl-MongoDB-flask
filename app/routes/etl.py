from flask import Blueprint, request, jsonify
from app.services.github_etl import Github_ETLRepositorys
from app.models.repository import MongoDBRepository

etl_blueprint = Blueprint('etl', __name__)

@etl_blueprint.route('/etl', methods=['POST'])
def run_etl():
    data = request.get_json()
    repo_owner = data.get('owner')
    github_token = data.get('token')
    if not repo_owner or not github_token:
        return jsonify({"error": "Missin the 'owner' or 'token' in request"}), 400

    etl = Github_ETLRepositorys(owner=repo_owner, token=github_token)
    try:
        df = etl.run_etl_pipeline()
        return jsonify({"message": f"ETL executed for {repo_owner}", "raw": len(df)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@etl_blueprint.route('/etl/<owner>', methods=['DELETE'])
def delete_owner_languages(owner):
    db = MongoDBRepository()
    result = db.languages_collection.delete_many({"owner": owner})
    if result.deleted_count > 0:
        return jsonify({"message": f"Data from '{owner}' removed."}), 200
    else:
        return jsonify({"message": f"No data found for the owner '{owner}'."}), 404