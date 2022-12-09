import streamlit as st
import random


def password_generator():
    length = st.sidebar.slider("Password length", 12, 18)
    btn = st.sidebar.button("Calculate")
    def generator():
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 +-:|~!@#$%^&*?\/"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        num = "1234567890"
        special = " +-:|~!@#$%^&*?\/"
        upper_count = 0
        lower_count = 0
        num_count = 0
        special_count = 0
        password = ""
        for i in range(length):
            char = random.choice(a)
            password += char
        for j in password:
            if j in upper:
                upper_count += 1
            if j in lower:
                lower_count += 1
            if j in num:
                num_count += 1
            if j in special:
                special_count += 1
        if upper_count >= 4 and lower_count >= 4 and num_count >= 1 and special_count >= 1:
            p="The Password is: "+password
            st.success(p)
            #st.header("The Password is:  {}".format(password))
            st.markdown("***")
            st.write("Developed by:")
            st.write("*Amit Kumar* :sunglasses:")
        else:
            generator()
    if btn:
        generator()


st.title("Password Generator")
st.image("./Strong Password Generator.jpg",width=360)
password_generator()
