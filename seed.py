from app.extensions import db
from app.models.users import User
from app import create_app

app = create_app()

with app.app_context():
        db.drop_all()
        db.create_all()

        User.query.delete()

        # Add user admin
        user_admin = User(full_name='administrator', email='quickrecipe@ymail.com', password="khvdhvkhvevhi", is_oauth=False, is_admin=True)
       
        db.session.add_all([user_admin])
        db.session.commit()

        