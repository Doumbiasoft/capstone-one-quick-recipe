from app.extensions import db,os,ADMIN_FIRST_NAME,ADMIN_LAST_NAME,ADMIN_EMAIL,ADMIN_PASSWORD
from app.models.users import User
from app.models.recipe_favorites import RecipeFavorite
from app.models.recipe_review import RecipeReview
from app import create_app
from admin_identifications import admin_password,admin_email,admin_first_name

app = create_app()

with app.app_context():
        db.drop_all()
        db.create_all()
        User.query.delete()
        RecipeFavorite.query.delete()
        RecipeReview.query.delete()


        """Add user admin"""
        user_admin = User(first_name = os.environ.get(ADMIN_FIRST_NAME,admin_first_name) ,last_name = os.environ.get(ADMIN_LAST_NAME,''), email = os.environ.get(ADMIN_EMAIL,admin_email), password = User.hash_function(os.environ.get(ADMIN_PASSWORD,admin_password)), is_oauth = False, is_admin = True)
        db.session.add_all([user_admin])
        db.session.commit()

        