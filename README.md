# Python FFmpeg bindings


[![pypi](https://img.shields.io/pypi/v/pyffmpeg.svg)](https://pypi.python.org/pypi/pyffmpeg)
[![Travis](https://img.shields.io/travis/hmaarrfk/pyffmpeg.svg)](https://travis-ci.org/hmaarrfk/pyffmpeg)
[![Docs](https://readthedocs.org/projects/pyffmpeg/badge/?version=latest)](https://pyffmpeg.readthedocs.io/en/latest/?badge=latest)


Python FFmpeg bindings for fast video encoding and decoding

The advantage of using this library over calling `ffmpeg` as a subprocess
is that `FFmpeg` now has access to all your python memory. This means that you
avoid a full copy of your data back and forth when encoding/decoding.

While this specific project is licensed under an MIT license, the compiled
binary packages of ffmpeg might have a different license.

Features
--------

* TODO

Credits
-------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[hmaarrfk/cookiecutter-pypackage](https://github.com/hmaarrfk/cookiecutter-pypackage)
project template.
