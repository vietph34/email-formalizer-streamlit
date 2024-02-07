import streamlit as st
from langchain import PromptTemplate
from langchain_openai import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.  

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: I headed straight for the produce section to grab some fresh vegetables, like bell peppers and zucchini. After that, I made my way to the meat department to pick up some chicken breasts.
    - British: Well, I popped down to the local shop just the other day to pick up a few bits and bobs. As I was perusing the aisles, I noticed that they were fresh out of biscuits, which was a bit of a disappointment, as I do love a good cuppa with a biscuit or two.

    Please start the email with a warm introduction. Add the introduction if you need to.
    
    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR {dialect} RESPONSE:
"""
prompt = PromptTemplate(input_variables=["tone", "dialect", "email"], template=template)

def load_llm():
    llm = OpenAI(temperature=0.5)
    return llm
llm = load_llm()
st.set_page_config(page_title="Globalize Text", page_icon="🦃")
st.header("Email Formalizer 📧")

col1, col2 = st.columns(2)

with col1:
    st.write("This tool will help you improve your email skill by converting your email into a more professional format. This tool is powered by Langchain.")
with col2:
    st.image(image="./images.png")


col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox("Which tone woudl you like your email to have?",
                               ("Formal", "Informal"))
with col2:
    option_dialect = st.selectbox("Which English Dialect would you like?", 
                                  ("American English", "British English"))

def get_text():
    input_text = st.text_area(label="", placeholder="Your Email...", key="email_input")
    return input_text

st.markdown("## Enter Your Email To Convert")
email_input = get_text()
st.markdown("### Your Converted Email")
if email_input:
    model_input = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    formated_email = llm(model_input)
    st.write(formated_email)

