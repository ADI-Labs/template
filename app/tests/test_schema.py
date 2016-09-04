from app.schema import Example

def test_example_1(db, multi_transaction):
    for __ in range(10):
        db.session.add(Example(name="hello"))
        db.session.commit()
    assert Example.query.count() == 10

def test_example_2(db, transaction):
    db.session.add(Example(name="hello"))
    db.session.commit()
    assert Example.query.count() == 1

def test_example_3(db, transaction):
    assert Example.query.count() == 0
