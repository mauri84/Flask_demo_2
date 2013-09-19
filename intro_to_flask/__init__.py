from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

#app.config['MAIL_SERVER'] = 'stmp.gmail.com'
#app.config['MAIL_PORT'] = '465'
#app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USERNAME'] = 'contact@gmail.com'
#app.config['MAIL_PASSWORD'] = 'password'

#from routes import mail
#mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mauri:mauri@localhost/Flask'

from models import db
print db
db.init_app(app)

import intro_to_flask.routes