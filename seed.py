from app.extensions import db
from app.models.users import User
from app.models.recipe_favorites import RecipeFavorite
from app.models.recipe_review import RecipeReview
from app.models.recipe_diet import RecipeDiet
from app.models.recipe_type import RecipeType
from app.models.recipe_cuisine import RecipeCuisine
from app import create_app
from admin_identifications import admin_password,admin_email,admin_first_name

app = create_app()

with app.app_context():
        db.drop_all()
        db.create_all()
        User.query.delete()
        RecipeFavorite.query.delete()
        RecipeReview.query.delete()
        RecipeDiet.query.delete()
        RecipeType.query.delete()
        RecipeCuisine.query.delete()

        """Add user admin"""
        user_admin = User(first_name = admin_first_name,last_name='', email = admin_email, password = User.hash_function(admin_password), is_oauth = False, is_admin = True)
        db.session.add_all([user_admin])
        db.session.commit()

        