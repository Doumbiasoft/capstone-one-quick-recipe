from app.extensions import db,func



class RecipeFavorite(db.Model):
    """RecipeFavorite Model"""

    __tablename__ = "recipe_favorites"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    recipe_id = db.Column(db.Integer, nullable = False)
    title = db.Column(db.String(255), nullable = False)
    image_url = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True),server_default = func.now())
   
      