from app.extensions import db,bcrypt,func
from app.models.recipe_favorites import RecipeFavorite
from app.models.recipe_review import RecipeReview

class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
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
    recipe_favorites = db.relationship("RecipeFavorite", backref="user", cascade="all, delete-orphan")
    recipe_reviews = db.relationship("RecipeReview", backref="user", cascade="all, delete-orphan")


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User {self.id} {self.first_name} {self.last_name} {self.email} {self.is_admin}>"
    @classmethod
    def hash_function(cls,value):
      """This function will encrypt any value in input parameters"""
      return bcrypt.generate_password_hash(value).decode("utf8")
    @classmethod
    def hash_function_check(cls,old_password_hash,new_password_hash):
            """This function will check any encrypt value in input parameters"""
            return bcrypt.check_password_hash(old_password_hash, new_password_hash)
    @classmethod
    def register(cls, first_name, last_name, email, password,is_oauth):
        """Register user w/hashed password & return user."""

        password_hashed = bcrypt.generate_password_hash(password).decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(first_name=first_name, last_name=last_name,email=email,password=password_hashed,is_oauth = is_oauth)

    @classmethod
    def login(cls, email, password):
        """Validate that user exists & password is correct. Return user if valid; else return False."""

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            #return user instance
            return user
        else:
            return False

    def get_users():
        return User.query

    def get_user_by_id(id):
        return User.query.get_or_404(id)

    def add_users(user):
        final_user=user
        db.session.add(final_user)
        try:
            db.session.commit()
        except:
            return False
        return final_user

    def update_users(id, firstname, lastname):
        user = User.query.get_or_404(id)
        user.first_name = firstname
        user.last_name = lastname
        db.session.add(user)
        try:
            db.session.commit()
        except:
            return False
        return user

    def delete_users(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        try:
            db.session.commit()
        except:
            return False
        return True

    def update_password(id, password):
        user = User.query.get_or_404(id)
        user.password = password
        db.session.add(user)
        try:
            db.session.commit()
        except:
            return False
        return True

    def is_favorite(self,recipe_id):
        """ Is this user has a favorite recipe? """

        favorites = [favorite for favorite in self.recipe_favorites if favorite.recipe_id == recipe_id and favorite.user_id == self.id]
        return len(favorites) == 1


      