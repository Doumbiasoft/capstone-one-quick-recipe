from app.extensions import db



class RecipeCuisine(db.Model):
    """RecipeCuisine Model"""

    __tablename__ = "recipe_cuisines"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    image_url = db.Column(db.String(255), nullable = False, default=None)
    is_active = db.Column(db.Boolean, nullable = False,default=True)
   
      