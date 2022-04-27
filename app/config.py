class Config:
  
  MOVIE_API_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
  
  pass

class DevConfig(Config):
  DEBUG=True
  
class ProdConfig(Config):
  pass