from app.extensions import db,func,JSONB


class RecipeFavorite(db.Model):
    """RecipeFavorite Model"""

    __tablename__ = "recipe_favorites"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    recipe_id = db.Column(db.Integer, nullable = False)
    name = db.Column(db.Text, nullable = False)
    tag = db.Column(db.Text, nullable = False)
    thumbnail_url = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    data = db.Column(JSONB, nullable = False)
    created_at = db.Column(db.DateTime(timezone = True),server_default = func.now())
   
      