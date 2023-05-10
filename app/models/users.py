from app.extensions import db,bcrypt,func


def hash_function(value):
      return bcrypt.generate_password_hash(value).decode("utf8")

def hash_function_check(old_password_hash,new_password_hash):
      return bcrypt.check_password_hash(old_password_hash, new_password_hash)


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    full_name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    password_reset_token = db.Column(db.Text)
    oauth_provider = db.Column(db.Text)
    oauth_uid = db.Column(db.Text)
    oauth_access_token = db.Column(db.Text)
    oauth_refresh_token = db.Column(db.Text)
    oauth_expires_at = db.Column(db.DateTime)
    is_oauth = db.Column(db.Boolean,nullable = False)
    created_at = db.Column(db.DateTime(timezone = True),server_default = func.now())
    updated_at = db.Column(db.DateTime(timezone = True),server_default = func.now())
    is_active = db.Column(db.Boolean, nullable = False, default = True)
    is_admin = db.Column(db.Boolean, nullable = False, default = False)

    def __repr__(self):
        return f"<User {self.id} {self.full_name} {self.email}>"


      