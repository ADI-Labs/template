import os

class Config:
    HOST = os.environ["FLASK_HOST"]
    PORT = int(os.environ["FLASK_PORT"])
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']

    fmt = "postgresql://{user}:{password}@{host}:{port}/{db}"
    SQLALCHEMY_DATABASE_URI = fmt.format(
        user=os.environ["PG_USER"],
        password=os.environ["PG_PASSWORD"],
        host=os.environ["PG_HOST"],
        port=os.environ["PG_PORT"],
        db=os.environ["PG_DB"],
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
