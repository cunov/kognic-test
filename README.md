# kognic-solution-engineer-test

Tested using Python 3.11

## Package usage
First, create and activate a virtual environment.

To install the package run `pip install annotation_converter/` from the main directory.

The only thing that is designed to be used by the user is the `convert()` function. You can simply import it like `from annotation_converter import convert`.

The default parameters are set, but you can update things like the host, port, and template file if you want to run it from somewhere else. Simply run `annotation_converter.module.host = HOST`, for example.

## Starting the service
Start the service by navigating to `application/` and executing `flask run`. You may need to set the environment variable `FLASK_APP=app.py`.

## Converting the annotation
Run `demo.py` to convert the provided file and print to file and screen.

## Bbox conversion
According to OpenLABEL's JSON schema, "A 2D bounding box is defined as a 4-dimensional vector `[x, y, w, h]`, where `[x, y]` is the center of the bounding box and `[w, h]` represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively." Since we are provided 4 points, each containing an extrema, we can find the `min_x, max_x, min_y, max_y` and then compute `[x, y, w, h]` as:

`x = min_x + (max_x - min_x) / 2`

`w = max_x - min_x`

and similarly for `y` and `h`.
