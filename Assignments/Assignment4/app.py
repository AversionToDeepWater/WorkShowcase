from flask import Flask, jsonify, request
#just realised I intended to name the file db_utils not utilis but spelling is hard :((
from db_utils import get_all_kdramas_db, delete_kdrama_by_id, add_new_kdrama_db, add_new_rating_db

app = Flask(__name__)


@app.route("/kdramas", methods=["GET"])
def get_all_kdramas():
    return jsonify(get_all_kdramas_db())


@app.route("/kdramas/add", methods=["POST"])
def add_new_kdramas():
    new_kdrama_dict = request.get_json()
    return jsonify(add_new_kdrama_db(new_kdrama_dict))

@app.route("/kdramas/addratings", methods=["POST"])
def add_new_ratings():
    new_kdrama_dict = request.get_json()
    return jsonify(add_new_rating_db(new_rating_dict))

@app.route("/kdramas/remove/<int:id>", methods=["DELETE"])
def del_user_by_id(id):
    return jsonify(delete_kdrama_by_id(id))



if __name__ == "__main__":
    app.run(debug=True)