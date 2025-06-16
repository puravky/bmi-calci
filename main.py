import streamlit as st

st.title("BMI Calculator App")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}, ready to calculate your BMI?")

wt = st.number_input("Enter your weight (kgs):", value=60.0 ,min_value=10.0, step=0.1)
height = st.number_input("Enter your height (cms):", value=150.0, min_value=50.0, step=1.0)
ht = height / 100

if st.button("Calculate BMI"):
    BMI = wt / (ht * ht)
    bmi = float(BMI)
    st.write(f"Your BMI value is {bmi:.1f}")

    if bmi < 18:
        st.warning("You are underweight. Put on some weight!")
    elif 18 <= bmi < 25:
        st.success("You are healthy. Keep it up!")
        st.balloons()
    elif 25 <= bmi < 30:
        st.warning("You are overweight. Consider a balanced diet and exercise.")
    else:
        st.error("You are obese. Eat less food man!")

    st.write("Thanks for using this App made by @puravky")

