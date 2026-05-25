'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.onboarding_routes import onboarding
    from app.routes.dashboard_routes import dashboard

    app.register_blueprint(onboarding)
    app.register_blueprint(dashboard)

    with app.app_context():
        db.create_all()

        return app'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# 1. Criamos as instâncias fora para outros arquivos conseguirem usar
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # 2. Configurações DIRETO aqui (para evitar o erro de "import config")
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 3. Inicializa as extensões no App
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # 4. Importa as rotas (Blueprints)
    # Certifique-se que esses arquivos existem na pasta routes!
     # # 4. Importa as rotas (Blueprints)
    from app.routes.auth_routes import auth  # Se no arquivo auth_routes o nome for 'auth'
    from app.routes.onboarding_routes import onboarding_bp
    from app.routes.dashboard_routes import dashboard_bp  # 👈 CORRIGIDO AQUI (era dashboard)

    # # 5. Registra as rotas no Flask
    app.register_blueprint(auth)
    app.register_blueprint(onboarding_bp)
    app.register_blueprint(dashboard_bp)

    # 6. Cria o banco de dados automaticamente se não existir
    with app.app_context():
        db.create_all()

    return app