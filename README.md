#### Requirements:
- [Python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

__Note:__ all commands are using `bash`. You may have to adjust some commands for other shell environments.


## Setup


### 1. Create a new virtualenv
```bash
mkvirtualenv -p /usr/local/bin/python3 pyar
# Your python3 may be installed in a different location.
# Use `which python3` to find out where it is located
```
You only have to do this once. Later, you can activate your environment using `workon pyar`, and you can quit your environment using `deactivate`.


### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a local_settings.py file (optional)
If you need to override any of the values in `settings.py` (namely for production), you'll have to create a `local_settings.py`.
```bash
touch local_settings.py
```
Then, the you can copy any settings from `settings.py` to `local_settings.py` to override the values.

### 4. Run the site
```bash
python app.py
```

### Done!
Visit [http://localhost:5000](http://localhost:5000) to test the site.
