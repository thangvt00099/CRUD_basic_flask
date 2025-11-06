from . import db, create_app

#  python -m myapp.init_db || Tạo db như 1 module
app = create_app()
with app.app_context():
    db.create_all()
    print("Database created!")