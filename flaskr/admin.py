from flask import Blueprint
from flask import flash
from flask import g 
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint("admin",__name__)


@bp.route('/admin')
@login_required
def index():
    """Show all the posts, most recent first."""
    userscount = get_user_count()
    postcount = get_post_count()
    total_likes = get_total_likes()
    print(f"userscount= {userscount[0]} , length: {len(userscount)}")
    print(f"postcount= {postcount[0]} , length: {len(postcount)}")
    print(f"totallikes= {total_likes[0]} , length: {len(total_likes)}")

    return render_template('admin/index.html',
                           userscount=userscount,
                           postcount=postcount,
                           totallikes=total_likes)


def get_user_count():
    """ Returns the count of users registered in app"""
    db = get_db()
    usercount = db.execute(
        "SELECT COUNT(*) FROM user"
    ).fetchone()
    
    return usercount


def get_post_count():
    """ Returns the count of posts in app"""
    db = get_db()
    postcount = db.execute(
        "SELECT COUNT(*) FROM post"
    ).fetchone()
    
    return postcount


def get_total_likes():
    """ Returns the sum of likes in posts"""
    db = get_db()
    likes = db.execute(
        "SELECT SUM(likes) FROM post"
    ).fetchone()

    return likes


def get_post(id, check_author=True):

    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, likes, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/create',methods=('GET','POST'))
@login_required
def create():
    """Create a new post for the current user."""    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, likes, author_id) VALUES (?,?,?,?)",
                (title, body, 0, g.user['id']),
            )
            db.commit()
            return redirect(url_for('blog.index'))
    
    return render_template('blog/create.html')


@bp.route('/<int:id>/like', methods=('GET',))
@login_required
def like(id):


    if request.method == 'GET':
        error = None
        # check_author flag was set to False to permit
        # that every logged in user can like a post.
        post = get_post(id, check_author=False)
        
        if not post:
            error = 'Post id is not valid'
        
        if error is not None:
            flash(error)
        else:
            #update likes in post.
            likes = post["likes"] + 1
            
            db = get_db()
            db.execute(
                "UPDATE post SET likes = ? WHERE id = ?",(likes, id)
            )
            db.commit()

    return redirect(url_for('blog.index'))


@bp.route('/<int:id>/update',methods=('GET','POST'))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)
    

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, body = ? WHERE id = ?",(title,body,id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
        
    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete',methods=('POST',))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?",(id,))
    db.commit()
    return redirect(url_for('blog.index'))
    