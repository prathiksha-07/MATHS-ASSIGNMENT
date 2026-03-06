import streamlit as st
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Interpolation Calculator", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928DAB);
        color: white;
    }
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #ff4b2b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }

    /* Make all input labels white */
    label {
        color: white !important;
        font-weight: 500;
    }

    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">✨ Interpolation Calculator ✨</div>', unsafe_allow_html=True)
st.write("---")

# ---------------- FUNCTIONS ----------------

def lagrange_with_steps(x, y, value, round_digits):
    n = len(x)
    steps = []

    steps.append(r"L(x) = \sum_{i=0}^{n} y_i \prod_{j=0, j \ne i}^{n} \frac{(x - x_j)}{(x_i - x_j)}")

    result = 0

    for i in range(n):
        term = y[i]
        num_parts = []
        den_parts = []

        for j in range(n):
            if j != i:
                num_parts.append(f"({value} - {x[j]})")
                den_parts.append(f"({x[i]} - {x[j]})")
                term *= (value - x[j]) / (x[i] - x[j])

        numerator = "".join(num_parts)
        denominator = "".join(den_parts)

        latex_line = rf"Term_{{{i}}} = {y[i]} \times \frac{{{numerator}}}{{{denominator}}}"
        steps.append(latex_line)

        result += term

    result = round(result, round_digits)
    steps.append(rf"\text{{Final Answer}} = {result}")

    return result, steps

# ---------------- USER INPUT ----------------
st.sidebar.header("Enter Data Points")

n = st.sidebar.number_input("Number of data points", min_value=2, step=1)
round_digits = st.sidebar.number_input("Decimal places", min_value=0, max_value=10, value=3)

x = []
y = []

st.sidebar.subheader("X Values")
for i in range(n):
    val = st.sidebar.number_input(f"x{i}", key=f"x{i}")
    x.append(round(val, round_digits))

st.sidebar.subheader("Y Values")
for i in range(n):
    val = st.sidebar.number_input(f"y{i}", key=f"y{i}")
    y.append(round(val, round_digits))

value = st.number_input("Enter value to interpolate")
value = round(value, round_digits)

method = st.selectbox("Choose Method", ("Lagrange Interpolation",))

# ---------------- CALCULATION ----------------
if st.button("Calculate"):
    st.write("---")
    st.subheader("Step-by-Step Solution")

    result, steps = lagrange_with_steps(x, y, value, round_digits)

    for step in steps:
        st.latex(step)

    st.markdown(f"<h3 style='color:white;'>Interpolated Value = {result}</h3>", unsafe_allow_html=True)