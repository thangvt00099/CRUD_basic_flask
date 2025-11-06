from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Khởi tạo db
db = SQLAlchemy()

# Xem các biến môi trường: Get-ChildItem Env: hoặc gci env:
# Lọc theo từ khóa: gci env: | Where-Object { $_.Name -like "*FLASK*" }

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' 
    db.init_app(app)

    # Admin
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .models import User

    app.debug=True
    return app