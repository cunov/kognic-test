# kognic-solution-engineer-test

Tested using Python 3.11

## Package usage
To install the package run `pip install annotation_converter/ --use-pep517` from the main directory. Neglecting the `--use-pep517` 

The only thing that is designed to be used by the package is `convert`

## Running it
You can either start the process on your own from the terminal by navigating to

`annotation_converter/annotation_converter/application`

setting the environment variable `FLASK_APP=app.py` and running

`flask run`

or just let the package thread the service for you.

Run `demo.py` to convert the provided file and print to screen.

## Bbox conversion
According to OpenLABEL's JSON schema, "A 2D bounding box is defined as a 4-dimensional vector `[x, y, w, h]`, where `[x, y]` is the center of the bounding box and `[w, h]` represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively." Since we are provided 4 points, each containing an extrema, we can find the `min_x, max_x, min_y, max_y` and then compute `[x, y, w, h]` as:

`x = min_x + (max_x - min_x) / 2`

`w = max_x - min_x`

and similarly for `y` and `h`.
