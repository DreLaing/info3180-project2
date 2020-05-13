from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask 
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

ENV = "Prod"
if ENV == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/project2"
else:
    app.debug =False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vnnvuhcekuzqyd:16df6f82deb87a58364faff2c3e27f7c0514ab15d8e8e97a12c08b20891b72b6@ec2-3-91-139-25.compute-1.amazonaws.com:5432/d14568lhhki1l9"

csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "thisisasecret"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning 
app.config['UPLOAD_FOLDER']="./app/static/uploads"#this is where the profile pictures will be uploaded 
app.config['PHOTOS']="./app/static/photos"#this is where the potho that are posted will go 

db = SQLAlchemy(app)
#login mangement 
login_maneger=LoginManager() 
login_maneger.init_app(app)

login_maneger.login_view='login'


app.config.from_object(__name__) 

from app import views 
