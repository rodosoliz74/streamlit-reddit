import streamlit as st
from google.cloud import firestore
import datetime
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
from datetime import timezone
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
# With:
import json

#key_dict = json.loads(st.secrets["textkey"])
keyfile_data = json.loads(st.secrets["textkey"])
#creds = ServiceAccountCredentials.from_json_keyfile_name(key-to-toml, scope)
#creds = ServiceAccountCredentials.from_json_keyfile_name(key_dict)
#creds = service_account.Credentials.from_service_account_info(key-to-toml, scope)
#creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_data)
#db = firestore.Client(credentials=creds, project="streamlit-reddit")

db = firestore.Client.from_service_account_json("firestore-key.json")
#SUBIR
DX1 = 3.1
DX2 = 3.2
DX3 = 3.4
DX4 = 3.4
DX5 = 3.3

DY1 = 5.0
DY2 = 5.4
DY3 = 5.3
DY4 = 5.2
DY5 = 5.5
Numero = st.text_input("Numero")
Fecha = st.text_input("Fecha")
submit = st.button("Nuevo")
# Once the user has submitted, upload it to the database
if Numero and Fecha and submit:
	doc_ref = db.collection("Admin").document(Numero)
	doc_ref.set({
		"Numero": Numero,
		"Fecha": Fecha
})
	frank_ref = db.collection('Admin').document(Numero)
	frank_ref.set({
        	'Tabla 1': {
            		'Dato 1': {
                		'dateExample': datetime.datetime.now(timezone.utc),
                		'x_coordinate': 4,
                		'y_coordinate': 1,
                		'distance_setpoint': 5.1,
           		 },
            		'Dato 2': {
                		'dateExample': datetime.datetime.now(timezone.utc),
                		'x_coordinate': 5,
               			'y_coordinate': 2,
               			'distance_setpoint': 5.1,
            		},
            		'Dato 3': {
               			'dateExample': datetime.datetime.now(timezone.utc),
                		'x_coordinate': 6,
                		'y_coordinate': 3,
                		'distance_setpoint': 5.1,
            		},

       		 },

        

})
#BAJAR
posts_ref = db.collection("Admin")
for doc in posts_ref.stream():
	post = doc.to_dict()
	#Numero = post["Numero"]
	#Fecha = post["Fecha"]
st.subheader(f": {Numero}")
st.subheader(f": {Fecha}")
st.write(": ", doc.id)
st.write(": ", doc.to_dict())
        #st.subheader(f"Admin: {Numero de Laboratorio}")
	#st.write(f":link: [{url}]({url})")


st.write("Tabla 1")
st.write(pd.DataFrame({
    'Cordenada x': [DX1, DX2, DX3, DX4,DX5],
    'Cordenada y': [DY1, DY2, DY3, DY4,DY5]
}))

