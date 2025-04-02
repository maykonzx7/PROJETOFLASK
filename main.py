from flask import Flask
from routes.home import home_route
from routes.thanks import thanks_route

app = Flask(__name__)

app.register_blueprint (home_route)
app.register_blueprint(thanks_route)

if __name__ == '__main__':
 app.run (debug=True)