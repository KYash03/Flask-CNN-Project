import numpy as np

from flask import Flask, render_template, request

from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img


app = Flask(__name__)
model = load_model("static/x-ray_best_model.keras")


@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def main_page_predict():
    image_file = request.files['image-file']
    image_path = "./images/" + image_file.filename
    image_file.save(image_path)

    image = load_img(image_path,
                     target_size=(64, 64))
    image_array = img_to_array(image)
    image_array = image_array.reshape((1, ) + image_array.shape)
    image_array = image_array / 255.0
    prediction = model.predict(image_array)
    class_names = ["normal", "pneumonia"]
    return render_template("index.html", prediction=class_names[np.argmax(prediction[0])].capitalize() + "; " + str(round(prediction[0][np.argmax(prediction[0])] * 100, 2)) + "%")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
