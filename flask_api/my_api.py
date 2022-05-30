"""
Anytime time we pass data, it needs to be serialized 

I am creating this API for a collection of music

"""
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class MusicModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(20), nullable=False)
    song = db.Column(db.String(20), nullable=False)
    streams = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"Artist: {self.artist}, Song: {self.song}, Streams: {self.views}"

# db.create_all()

my_music = {}

search_put = reqparse.RequestParser()

search_put.add_argument("artist", type=str, help="An artist is required", required=True)
search_put.add_argument("song", type=str, help="A song is required", required=True)
search_put.add_argument("streams", type=int, help="There was no amount of streams entered", required=True)

# determines how info is serialized 
resource_fields = {
    'id': fields.Integer,
    'artist': fields.String,
    'song':fields.String,
    'streams':fields.Integer
}

def itm_not_incl(itm_id):
    if itm_id not in my_music:
        abort(404, message="Could not find this item")

def chk_itm_dbl(itm_id):
    if itm_id in my_music:
        abort(409, message="This item already exists..")

class SearchQuery(Resource):
    @marshal_with(resource_fields)
    def get(self, itm_id):
        itm_not_incl(itm_id)
        my_query = MusicModel.query.filter_by(id=itm_id).first()
        return my_query 
        # return my_music[itm_id]
    @marshal_with(resource_fields)
    def post(self, itm_id):
        args = search_put.parse_args()
        music = MusicModel(id=itm_id, artist=args['artist'],song=args['song'], streams=args['streams'])
        db.session.add(music)
        db.session.commit() # permanently adds to DB
        # my_music[itm_id] = args
        # return my_music[itm_id], 201 

    def delete(self, itm_id):
        itm_not_incl(itm_id)
        del my_music[itm_id]
        return '', 204 

# add the resource to API and make it accessible at the URL
# We can also add parameters for our resource
# api.add_resource(Google, "/doesthiswork")
api.add_resource(SearchQuery, "/playlist/<int:itm_id>")


if __name__ == "__main__":
    app.run(debug=True)

