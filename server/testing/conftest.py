import pytest
from server.app import app, db
from server.models import Plant

@pytest.fixture(scope="function")
def test_app():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with app.app_context():
        db.create_all()

        plant = Plant(
            name="Test Plant",
            image="https://example.com/plant.jpg",
            price=19.99,
            is_in_stock=True
        )
        db.session.add(plant)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()

