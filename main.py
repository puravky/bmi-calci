import streamlit as st

st.title("BMI Calculator App 💪")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", value=20, min_value=5, max_value=95)
if name:
    st.write(f"Hello!👋 {name}, Ready to calculate your BMI?")

wt = st.number_input("Enter your weight (kgs):", value=60 ,min_value=10)
height = st.number_input("Enter your height (cms):", value=150, min_value=50)
ht = height / 100

if st.button("Calculate BMI"):
    BMI = wt / (ht * ht)
    bmi = float(BMI)
    st.write(f"Your BMI value is {bmi:.1f}")

    if bmi < 18:
        st.warning("You are underweight. Put on some weight!")
    elif 18 <= bmi < 25:
        st.success(f"Congrats!🎉 {name}, you are healthy and fit!")
        st.balloons()
    elif 25 <= bmi < 30:
        st.error(f"You are overweight {name}. Consider losing some weight by eating healthy and doing exercise.")
    else:
        st.error(f"You are obese! {name}, Eat less food man!")

    st.write("Thanks for using this App made by @puravky")
