from flask import Flask
from application.database import db_session
app = Flask(__name__)

# As in the declarative approach, you need to close the session
# after each request or application context shutdown. 
# Put this into your application module:
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# routes
from application import routes