from app import app, db, cli
from app.models import User, Post


@app.shell_context_processor
def make_hell_context():
    return {'db': db, 'User': User, 'Post': Post}
