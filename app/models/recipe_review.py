from app.extensions import db,func



class RecipeReview(db.Model):
    """RecipeReview Model"""

    __tablename__ = "recipe_reviews"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    recipe_id = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.String(255), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    created_at = db.Column(db.DateTime(timezone = True),server_default = func.now())
   
      