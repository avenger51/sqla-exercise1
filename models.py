from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect the database to the Flask app."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User table to instantiate."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.Text, nullable=False, unique=False)
    last_name  = db.Column(db.Text, nullable=False, unique=False)
    image_url = db.Column(db.Text, nullable=False, unique=False)
    
    def __repr__(self):
        usr = self
        return f"<User {usr.id} {usr.first_name} {usr.last_name} {usr.image_url}>"
#testing
    @classmethod
    def get_users_by_image_url(cls, image_url):
        return cls.query.filter_by(image_url=image_url).all()

 

