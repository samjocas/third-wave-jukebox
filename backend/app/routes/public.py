from flask import Blueprint, jsonify, render_template, request, redirect, flash, url_for
from ..models import Review
from ..services.db import db

bp = Blueprint("public", __name__)


@bp.route("/")
def home():
    reviews = Review.query.order_by(Review.created_at.desc()).all()
    return render_template("index.html", reviews=reviews)


@bp.route("/api/reviews")
def list_reviews():
    reviews = Review.query.order_by(Review.created_at.desc()).all()
    return jsonify([r.to_dict() for r in reviews])


@bp.route("/api/seed")
def seed():
    """Dev-only helper: seeds a couple of reviews if table is empty."""
    if Review.query.count() == 0:
        demo = [
            Review(
                artist="Radiohead",
                album="Kid A",
                rating=9.5,
                cover_url="https://upload.wikimedia.org/wikipedia/en/0/02/Radiohead.kid.a.albumart.jpg",
                body="A chilly, beautiful left-turn that still feels like the future.",
            ),
            Review(
                artist="Kendrick Lamar",
                album="To Pimp a Butterfly",
                rating=10.0,
                cover_url="https://upload.wikimedia.org/wikipedia/en/9/92/To_Pimp_a_Butterfly_cover.png",
                body="Explosive, intricate, and brutally honest—an instant classic.",
            ),
        ]
        db.session.add_all(demo)
        db.session.commit()
    return jsonify({"ok": True, "count": Review.query.count()})


@bp.route('/submit_review', methods=['POST'])
def submit_review():
    title = request.form.get('title')
    artist = request.form.get('artist')
    rating = request.form.get('rating')
    review_text = request.form.get('review')

    # Basic validation
    if not title or not artist or not rating or not review_text:
        flash('All fields are required.', 'error')
        return redirect(url_for('public.index'))

    # TODO: Save review to database here

    flash('Review submitted successfully!', 'success')
    return redirect(url_for('public.index'))


@bp.route('/review/<int:review_id>')
def review_detail(review_id):
    review = Review.query.get_or_404(review_id)
    return render_template('review_detail.html', review=review)