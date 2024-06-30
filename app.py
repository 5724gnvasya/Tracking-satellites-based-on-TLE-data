import pandas as pd
from flask import Flask, request, render_template, send_file, flash
import threading
from func import fetch_tle_data, make_other, add_id, remove_id, remove_all_ids, assign_colours, initialize_csv
from main import endless_loop
import datetime

app = Flask(__name__)

# app.secret_key = 'd75724d7loveS01FedG10OOprivet_menya_zovyt_aALLa_i_mne_hochetsya_et0_opyblickovat_'
# Initialize CSV file
initialize_csv()

# Create a thread for the endless loop
thread = threading.Thread(target=endless_loop)
thread.start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select_satellites", methods=["GET", "POST"])
def select_satellites():
    if request.method == "POST":
        selected_satellites = request.form.getlist("satellites")
        remove_all_ids() 
        df = pd.read_csv("curr.csv")
        current_satellites = df["Satellite"].tolist()
        for sat in current_satellites:
            if sat not in selected_satellites:
                remove_id(sat)
        for sat in selected_satellites:
            add_id(sat)
        assign_colours()
        make_other()
        # error_message = make_other()
        # if error_message:
        #     return render_template("trajectory.html", error_message=error_message)
        # if error_message == None:
        #     return render_template("trajectory.html")

        # error_message = make_other()
        # if error_message:
        #     return render_template('trajectory.html', error_message=error_message)
        # else:
        #     return render_template('trajectory.html')
        return render_template("trajectory.html")
        # return render_template("trajectory.html", error_message=error_message)
        #return render_template('trajectory.html', error_message=error_message)
    else:
        df = pd.read_csv("test_tle.csv")
        satellites = df["Satellite"].tolist()
        return render_template("select_satellites.html", satellites=satellites)

   
@app.route("/trajectory")
def trajectory():
    return render_template("trajectory.html")


@app.route('/satellites.png')
def serve_satellites_png():
    return send_file('satellites.png', mimetype='image/png', last_modified=datetime.datetime.utcnow())

if __name__ == "__main__":
    app.run(debug=True)