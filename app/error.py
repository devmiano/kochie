from flask import render_template
from app import app

@app.errorhandler(404)
def four_ow_four(error):
  '''Function to render a 404 error page '''
  return render_template('four_ow_four.html'),404