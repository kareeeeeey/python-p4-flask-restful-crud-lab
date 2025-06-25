from server.app import app
from server.models import db, Plant

with app.app_context():
    print("🌱 Seeding data...")

    db.drop_all()
    db.create_all()

    plants = [
        Plant(name="Aloe Vera", image="https://tinyurl.com/2p9zzc8p", price=10.99),
        Plant(name="Peace Lily", image="https://tinyurl.com/ymz8rsbj", price=12.50),
        Plant(name="Spider Plant", image="https://tinyurl.com/mr2h8x6b", price=8.75),
    ]

    db.session.add_all(plants)
    db.session.commit()

    print("✅ Done seeding!")




