import streamlit as st
import json
from bs4 import BeautifulSoup
import base64
from PIL import Image
import io

with open('data.json') as f:
    jobj = json.load(f)
def updateUsers(data):
    with open('users.json') as f:
        users = json.load(f)
    users['tests'].append(data)
    with open('users.json', 'w') as f:
        json.dump(users, f)

def finishTest(test):
    score = 0
    failed_q = []
    for i,r  in enumerate(st.session_state.attempt["respuestas"]):
        if test["preguntas"][i]["opciones"][r]["respuestaSN"]==-1:
            score+=1
        else:
            failed_q.append(i)
    data = {"id":st.session_state.attempt["test"],"score":score,"failed_q":failed_q}
    updateUsers(data)    
    placeholder.empty()
    with placeholder.container():
        st.title("Test Finalizado")
        st.write("Has terminado el test "+str(st.session_state.attempt["test"]+1))
        st.write("Respuestas correctas: "+str(score))
        for q in failed_q:
            question = BeautifulSoup(test["preguntas"][q]["pregunta"],"lxml").text
            st.header("Pregunta "+str(q+1))
            st.subheader(question)
            base64_img = test["preguntas"][q]["foto64"]
            if base64_img !="0":
                image_bytes = base64.b64decode(base64_img)
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image,width=300)
            for o in test["preguntas"][q]["opciones"]:
                if o["respuestaSN"]==-1:
                    correct_option = BeautifulSoup(o["respuesta"],"lxml").text
                    st.write("Respuesta correcta: "+correct_option)
            selected = st.session_state.attempt["respuestas"][q]
            bad_option = BeautifulSoup(test["preguntas"][q]["opciones"][selected]["respuesta"],"lxml").text
            st.write("Respuesta seleccionada: "+bad_option)
    del st.session_state.attempt
    del st.session_state.q
def nextQuestion(option,test):
    st.session_state.attempt["respuestas"][st.session_state.q]= option
    st.session_state.q += 1
    if st.session_state.q < len(test["preguntas"]):
        renderQuestion(test)
    else:
        finishTest(test)
def renderQuestion(test):
    placeholder.empty()
    with placeholder.container():
        st.title("Pregunta "+ str(st.session_state.q+1))
        question = BeautifulSoup(test["preguntas"][st.session_state.q]["pregunta"],"lxml").text
        st.write(question)
        base64_img = test["preguntas"][st.session_state.q]["foto64"]
        if base64_img =="0" or base64_img =="NO Existe el fichero ":
            pass
        else:
            image_bytes = base64.b64decode(base64_img)
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image,width=300)
        for i in range(len(test["preguntas"][st.session_state.q]["opciones"])):
            option = BeautifulSoup(test["preguntas"][st.session_state.q]["opciones"][i]["respuesta"],"lxml").text
            st.button(option,on_click=nextQuestion,args=[i,test])

def createTest(i):
    global placeholder
    placeholder=st.empty()
    test = jobj[i]
    if 'attempt' not in st.session_state:
        st.session_state.attempt = {"test":i,"respuestas":[None]*len(test['preguntas'])}
    if 'q' not in st.session_state:
        st.session_state.q = 0
    st.button("Start Test "+str(i+1),on_click=renderQuestion,args=[test])
    
col =st.sidebar.columns(3)
i = 0
while i < len(jobj):
    col[0].button("Test " + str(i+1), key=i,on_click=createTest,args=[i])
    i+=1
    col[1].button("Test " + str(i+1), key=i,on_click=createTest,args=[i])
    i+=1
    col[2].button("Test " + str(i+1), key=i,on_click=createTest,args=[i])
    i+=1
#import json file as object
#json_file = open('data.json') 
#place buttons on sidebar all together in the same line