# CompSoc, SSC

Code for The CompSoc, St. Stephen's College's website.

## Usage

You can try out the latest build using the following method:

1. Clone the repo to a suitable location using ```bash git clone <url>```.
2. Change permissions for setup.sh using ```bash chmod +x setup.sh```.
3. Run setup.sh ```bash ./setup.sh```.
4. You'll need to grab a client_secrets file from [here](console.developers.google.com) using the CompSoc Google login and place it in the root of the project.
5. Navigate to *localhost:8000/admin* and login with the credentials you set up.
6. Create some dummy data if you want to.
7. Head on to *localhost:8000* to use the website!

## Contribute

Below are the instructions for contributing to the compsocssc repo.

1. Create a new branch for the new feature or bugfix. Branch out from master.
2. Develop the feature on it's own branch until complete and stable.
3. Create a pull request to merge into the level_up. Think of this as a beta branch.
4. level_up will be merged into master at regular intervals.

The features currently under development are:

* Orfik Calendar event (add_to_calendar branch)
* Events overhaul (fix_events branch)

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


