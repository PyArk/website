from datetime import datetime

from flask import Flask, render_template
from flask_assets import Environment, Bundle

import settings


app = Flask(__name__)
assets = Environment(app)
app.config['ASSETS_DEBUG'] = True


js = Bundle('js/app.js', filters='babel', output='dist/app.js')
css = Bundle('scss/*.scss', filters='scss', output='dist/app.css')
assets.register('js_all', js)
assets.register('css_all', css)


@app.context_processor
def global_context():
    return {
        'site_name': settings.SITE_NAME,
        'now': datetime.utcnow()
    }

@app.route('/', methods=['GET'])
def index_route():
    return render_template('pages/index.html', page_title='Home')

@app.route('/about/', methods=['GET'])
def about_route():
    return render_template('pages/about.html', page_title='About')

@app.route('/about/meetups/', methods=['GET'])
def about_meetups_route():
    return render_template('pages/about_meetups.html')

@app.errorhandler(404)
def error_handler_404(error):
    return render_template('pages/error_404.html'), 404


if __name__ == '__main__':
    app.run()
