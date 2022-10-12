from app import create_app, db
from app.models import User, Post, PostLikes

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'PostLikes': PostLikes}

