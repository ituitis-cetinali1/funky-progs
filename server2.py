import os

from bottle import Bottle
from pathlib import Path

def home_page():
    return Path("/resume/index.html").read_text()





def create_app():
    app = Bottle()
    app.route("/", "GET", home_page)
    return app


application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

#app.route("/resume", "GET", resume_page)
