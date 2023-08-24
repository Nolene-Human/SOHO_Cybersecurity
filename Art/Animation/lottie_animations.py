import json

import streamlit as lit
import requests # to be able to load animation from website

from streamlit_lottie import st_lottie

def load_animation(filepath:str):
    with open(filepath, "r") as f:
        return json.load(f)
    

# importing animation lottie
from streamlit_lottie import st_lottie

        #OWN FUNCTION CALLS
import Art.Animation.lottie_animations