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
        'admin_email': settings.ADMIN_EMAIL,
        'now': datetime.utcnow(),
    }

@app.route('/', methods=['GET'])
def index_route():
    return render_template('pages/index.html', page_title='Home')

@app.route('/get-involved/', methods=['GET'])
def getinvolved_route():
    return render_template('pages/getinvolved.html', page_title='Get Involved')

@app.route('/get-involved/meetups/', methods=['GET'])
def getinvolved_meetups_route():
    return render_template('pages/getinvolved_meetups.html')

@app.route('/contact/', methods=['GET'])
def contact_route():
    return render_template('pages/contact.html', page_title='Contact Us')

@app.errorhandler(404)
def error_handler_404(error):
    return render_template('pages/error_404.html'), 404


if __name__ == '__main__':
    app.run()
