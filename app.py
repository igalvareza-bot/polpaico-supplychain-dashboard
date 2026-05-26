import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ==========================================================
# CONFIGURACIÓN GENERAL
# ==========================================================

st.set_page_config(
    page_title="Polpaico Control Tower",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# ESTILO VISUAL PROFESIONAL
# ==========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fa;
    }

    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        border-left: 6px solid #C62828;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        color: #1E1E1E;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .executive-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    }

