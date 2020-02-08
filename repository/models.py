from app import ps_db


class User(ps_db.Model):
    """
    User model will hold data of user
    """

    id = ps_db.Column(ps_db.Integer, primary_key=True)
    first_name = ps_db.Column(ps_db.String, nullable=False)
    last_name = ps_db.Column(ps_db.String, nullable=False)
    username = ps_db.Column(ps_db.String, nullable=False)
    password = ps_db.Column(ps_db.String, nullable=False)
    email = ps_db.Column(ps_db.String, nullable=False)
