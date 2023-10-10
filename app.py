"""Flask app for Cupcakes"""
"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"


connect_db(app)

@app.route("/")
def root():
    """The homepage"""
    return render_template("index.html")

@app.route("/api/cupcakes")
def list_cupcakes():
    """lists cupcakes"""
    cupcakes = [cupcake.to_dict for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def cupcake_data(cupcake_id):
    """Get info on cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a new cupcake"""
    data = request.json
    cupcake = Cupcake( flavor=data["flavor"], rating=data["rating"], size=data["size"], image=data["image"] or None)

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.to_dict()),201)


@app.route("/api/cupcakes/<int:cupcake_id>", mehods=["PATCH"])
def update_cupcake(cupcake_id):
    """update info on a cupcake"""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = data["flavor"]
    cupcake.rating = data["rating"]
    cupcake.size = data["size"]
    cupcake.image= data["image"]

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake= cupcake.to_dict())

@app.route("/api/cupcakes/<int:cupcake_id", methods= ["DELETE"])
def delete_cupcake(cupcake_id):
    """delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())