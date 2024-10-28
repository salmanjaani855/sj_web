import streamlit as st



name =st.text_input("Enter Your Name")
Fname =st.text_input("Enter Your Father Name")
adrr =st.text_area("Enter Your Text: ")
classdata =st.selectbox("Enter Your Class",(1,2,3,4,5))

button =st.button("Submit")

if button:
      st.markdown(f"""
      Name : {name}
      Father Name : {Fname}
      Address : {adrr}
      Class : {classdata} """)