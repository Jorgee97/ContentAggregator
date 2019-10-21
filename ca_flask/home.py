from .models import Articles
from flask import (
    Blueprint, flash, g, render_template, request, url_for, redirect, jsonify
)
from datetime import datetime

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    articles = Articles.objects()
    sources = set([s.source for s in articles]) 
    return render_template('base.html', title="Content Aggregator", sources = sources, articles = articles)
