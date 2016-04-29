# CompSoc, SSC

Code for The CompSoc, St. Stephen's College's website. *Still under development...*

## Try

You can try out the latest build using the following method:

1. Clone the repo to a suitable location using ```bash git clone <url>```.
2. Set up a virtualenv by running ```bash virtualenv -p python3 <env_name>```.
3. After activing the virtualenv, install the dependancies using ```bash pip install -r requirements.txt```.
4. Navigate to website/settings and add a file called 'local.py'.
5. **cd** to the root of the project (where manage.py lives) and run the following commands :

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```

6. Navigate to *localhost:8000/admin* and login with the credentials you set up.
7. Create some dummy data if you want to.
8. Head on to *localhost:8000* to use the website!

## Styling

The project uses Sass for the styles. All the Sass lives in (HA!) /static/sass. If editing the Sass, make sure you only compile main.scss in the Sass folder and nothing else. We recommend either CodeKit to watch for changes to the Sass and JavaScript but the Sass gem's watch method should work as well.

## License

```text

The MIT License (MIT)

Copyright (c) 2014-15 The CompSoc, St. Stephen's College

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
