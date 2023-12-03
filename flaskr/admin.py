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
    users = get_usernames()

    return render_template('admin/index.html',
                           userscount=userscount,
                           postcount=postcount,
                           totallikes=total_likes,
                           users=users)


def get_user_count():
    """ Returns the count of users registered in app"""
    db = get_db()
    usercount = db.execute(
        "SELECT COUNT(*) FROM user"
    ).fetchone()
    
    return usercount[0]


def get_post_count():
    """ Returns the count of posts in app"""
    db = get_db()
    postcount = db.execute(
        "SELECT COUNT(*) FROM post"
    ).fetchone()
    
    return postcount[0]


def get_total_likes():
    """ Returns the sum of likes in posts"""
    db = get_db()
    likes = db.execute(
        "SELECT SUM(likes) FROM post"
    ).fetchone()

    return likes[0]


def get_usernames():
    """Get Users list """
    db = get_db()
    users = db.execute(
        "SELECT username FROM user ORDER BY id ASC"
    ).fetchall()

    return users
