import requests
import time
import pytz
from datetime import datetime, timezone

from flask import Flask, render_template
from flask_assets import Environment, Bundle
from werkzeug.exceptions import HTTPException

import settings

app = Flask(__name__)
assets = Environment(app)
app.config['ASSETS_DEBUG'] = settings.ASSETS_DEBUG


js = Bundle('js/app.js', filters='babel', output='dist/app.js')
css = Bundle('scss/*.scss', filters='scss', output='dist/app.css')
assets.register('js_all', js)
assets.register('css_all', css)


@app.context_processor
def global_context():
    meetup_url = 'https://www.meetup.com/{}/'.format(settings.MEETUP_SLUG)
    return {
        'site_name': settings.SITE_NAME,
        'meetup_url': meetup_url,
        'meetup_events_url': '{}events/'.format(meetup_url),
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
    r = None
    try:
        r = requests.get('http://api.meetup.com/{}/events'.format(settings.MEETUP_SLUG))
    except requests.exceptions.ConnectionError:
        pass
    events = None
    success = False
    if r and r.status_code == 200:
        success = True
        events = r.json()
        for event in events:
            t = time.localtime((event['time'] / 1000) - (5 * 60 * 60))
            dt = datetime.utcfromtimestamp(time.mktime(t))
            tz = pytz.timezone('America/Chicago')
            event['date'] = tz.localize(dt)
    return render_template('pages/getinvolved_meetups.html',
                           events=events,
                           success=success)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    message = ('Oh, no! Something happened during that request. Please try again later or email '
               '<a href="mailto:{email}">{email}</a>'
                    .format(email=settings.ERROR_EMAIL))
    return message, code

@app.errorhandler(404)
def error_handler_404(error):
    return render_template('pages/error_404.html'), 404


if __name__ == '__main__':
    app.run(host=settings.FLASK_HOST, debug=settings.FLASK_DEBUG, port=settings.FLASK_PORT)
