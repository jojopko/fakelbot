from flask import Flask
from config import Configure

app = Flask(__name__)
app.config.from_object(Configure)


from fakel import routes, app

