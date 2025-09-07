from datetime import datetime
from .services.db import db

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(120), nullable=False)
    album = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)  # 0–10
    cover_url = db.Column(db.String(500), nullable=True)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "artist": self.artist,
            "album": self.album,
            "rating": self.rating,
            "cover_url": self.cover_url,
            "body": self.body,
            "created_at": self.created_at.isoformat(),
        }