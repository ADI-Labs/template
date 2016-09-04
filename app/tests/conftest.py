import pytest


@pytest.yield_fixture(scope="session")
def app():
    from app import app
    with app.app_context():
        yield app


@pytest.yield_fixture(scope="session")
def db():
    from app import db
    db.drop_all()
    db.create_all()
    load_data(db)
    yield db
    db.drop_all()


def load_data(db):
    """Insert test data here"""
    pass

@pytest.yield_fixture(scope="function")
def transaction(db):
    with db.engine.connect() as connection:
        transaction = connection.begin()
        db.session = db.create_scoped_session(options={"bind": connection})

        db.session.begin_nested()
        yield db.session

        transaction.rollback()
        db.session.remove()

@pytest.yield_fixture(scope="function")
def multi_transaction(db):
    yield db.session
    db.session.remove()
    db.drop_all()
    db.create_all()
    load_data(db)
