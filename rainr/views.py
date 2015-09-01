import flask as f

import parser as pr

from rainr import app


@app.route('/')
def home():
    parser = pr.Parser()
    data = parser.get_rain_data()
    f.g.parser = parser
    return f.render_template('home.html', data=data)
