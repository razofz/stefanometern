import os
from flask import Flask, render_template, session
app = Flask(__name__,
            static_url_path='', 
            static_folder='examples',
            template_folder='examples')

@app.route("/")
def stefanometern():
    return render_template('index.html', fullpage_license_key = os.environ.get('LICENSE_KEY'))

