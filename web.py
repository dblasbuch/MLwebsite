import streamlit as st

import numpy as np
import pandas as pd
import joblib 

from prep import PP, columns

model = joblib.load('xgbpipe.joblib')

st.title('An ML-website by Dani Blas Buch :robot:')

