import os
import numpy as np

from flask import Flask, render_template

from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
