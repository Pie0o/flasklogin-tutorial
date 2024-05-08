"""Database models."""

from Flask_Login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .roles import Role

class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "flasklogin-users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    role = db.Column(db.Enum(Role), index=False, unique=False, nullable=False, default=Role.SUBSCRIBER)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User id={self.id}, name={self.name}, email={self.email}>"

    def sign_up_role(role)
    #create function to check user role and if none assign subscriber role