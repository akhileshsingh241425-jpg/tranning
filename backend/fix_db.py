from app import app, db

with app.app_context():
    db.create_all()
    print("Database tables created/updated!")

    from app import SiteSettings
    existing = SiteSettings.query.first()
    if not existing:
        settings = SiteSettings()
        db.session.add(settings)
        db.session.commit()
        print("SiteSettings created!")
    else:
        print("SiteSettings already exists")