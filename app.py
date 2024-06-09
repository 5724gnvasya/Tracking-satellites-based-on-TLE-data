from flask import Flask, request, render_template, send_file
# from flask_session import Session
from gevent.pywsgi import WSGIServer
# from main import api_shp, make_png
import api_shp
import make_png
from datetime import date
# import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    sat_id = int(request.form['id'])
    step = int(request.form['step'])
    date_str = request.form['date']
    year, month, day = map(int, date_str.split('-'))
   
    api_shp.create_orbital_track_shapefile_for_day(sat_id, date(year, month, day), step)
    make_png.make_png(sat_id)

    return send_file(f'{sat_id}.png', mimetype='image/png')

 

    # Pass the values as arguments to the main.py script
    # subprocess.run(['python', 'main.py', str(id), str(year), str(month), str(day), str(step)])

    # # Return the generated image
    # image_path = 'sat_id.png'
    # return send_file(image_path, mimetype='image/png')

    
    # make_png(sat_id)
    # return make_png(sat_id)
    # return send_file(f'{sat_id}.png', mimetype='image/png')



if __name__ == '__main__':
    http_server = WSGIServer(('', 8000), app)
    http_server.serve_forever()





 # sat_id = request.form['id']
    # if sat_id:
    #     sat_id = int(sat_id)
    # else:
    #     return "Error: ID is reqired"

    # step = request.form['step']
    # if step:
    #     step = int(step)
    # else:
    #     return "Error: Step is required"

    # date_str = request.form['date']
    # if date_str:
    #     year, month, day = map(int, date_str.split('-'))
    # else:
    #     return "Error: Date is required"


