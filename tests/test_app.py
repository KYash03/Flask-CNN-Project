# python3 -m pytest -W ignore::DeprecationWarning

from io import BytesIO
from main import app


def test_main_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b'<!DOCTYPE html>\n<html lang="en">\n\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Pneumonia Detector</title>\n    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet"\n        integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">\n</head>\n\n<body>\n    \n\n<div class="container">\n    <h2 class="mt-4">Pneumonia Detector</h2>\n\n    <form action="/" method="post" enctype="multipart/form-data">\n        <div class="mb-3">\n            <input type="file" name="image-file" class="form-control">\n        </div>\n        <input type="submit" value="Predict Image" class="btn btn-primary">\n    </form>\n\n    \n</div>\n\n\n</body>\n\n</html>'


def test_main_page_predict():
    with open("test_images/test_image_pneumonia.jpeg", "rb") as image_file:
        image_data = image_file.read()

    response = app.test_client().post("/", data={"image-file": (BytesIO(image_data),
                                                                "test_image.jpeg")}, content_type="multipart/form-data")

    assert response.status_code == 200
    assert response.data == b'<!DOCTYPE html>\n<html lang="en">\n\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Pneumonia Detector</title>\n    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet"\n        integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">\n</head>\n\n<body>\n    \n\n<div class="container">\n    <h2 class="mt-4">Pneumonia Detector</h2>\n\n    <form action="/" method="post" enctype="multipart/form-data">\n        <div class="mb-3">\n            <input type="file" name="image-file" class="form-control">\n        </div>\n        <input type="submit" value="Predict Image" class="btn btn-primary">\n    </form>\n\n    \n    <p class="mt-4">Result: Pneumonia, 84.38%</p>\n    \n</div>\n\n\n</body>\n\n</html>'


test_main_page()
