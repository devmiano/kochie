from flask import render_template
from app import app
from .request import get_movies,get_movie


@app.route('/')

def index():
  popular_movies = get_movies('popular')
  upcoming_movies = get_movies('upcoming')
  now_showing_movie = get_movies('now_playing')
  print(popular_movies)
  message = 'Hello Flask!'
  title = 'Home - Welcome to The best Movie Review Website Online'
  return render_template('index.html', message=message, title=title, popular=popular_movies, upcoming=upcoming_movies, now_showing=now_showing_movie)

@app.route('/movie/<int:id>')
def movie(id):
  movie  = get_movie(id)
  title = f'{movie.title}'
  
  return render_template('movie.html', title = title, movie = movie)
