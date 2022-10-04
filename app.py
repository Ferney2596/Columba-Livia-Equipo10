from app import create_app, db
from app.models import User, Post, PostLikes

app = create_app()


@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'PostLikes': PostLikes}
