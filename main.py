import streamlit as st
from openai import OpenAI

API_KEY = st.secrets["API_KEY"]

modelo_ia = OpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


#Titulo
st.write("Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

#Input
txt_user = st.chat_input("Digite sua mensagem...")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if txt_user:
    print(txt_user)
    st.chat_message("user").write(txt_user)
    mensagem_user =  {"role": "user", "content": txt_user}
    st.session_state["lista_mensagens"].append(mensagem_user)

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-3.8-flash"
    )
    txt_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(txt_resposta_ia)
    mensagem_ia =  {"role": "assistant", "content": txt_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

print(st.session_state["lista_mensagens"])