# Primero importamos las librerías a utilizar 
import pandas as pd
import streamlit as st
import numpy as np
import codecs 

#Colocamos el título de nuestro sitio web
st.title('Análisis de deserción de empleados')
st.header("Esta aplicación realiza un análisis de los datos de los empleados para ofrecer mayor entendimiento del fenómeno de la deserción")

# Cargamos nuestra base de datos
data_emp = ('Employees.csv')

#Hacemos una función para mostrar los datos primeros 500
@st.cache
def load_data(nrows):
    data = pd.read_csv(data_emp, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    #data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Datos por empleado")
#st.dataframe(data)

#Creamos un sidebar que nos permita mostrar u ocultar nuestro data frame
agree = st.sidebar.checkbox("Mostrar todos los datos ")
if agree:
  st.dataframe(data)

#Buscador de empleados por Employee_ID
#Se trabaja en el slidebar 
sidebar = st.sidebar
sidebar.title("Buscador de empleados.")
sidebar.write("Por Employee_ID, Hometown o Unit.")

@st.cache
def search_data(Employee_ID) : 
    doc = codecs.open('Employees.csv')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_filme = data[data['Employee_ID'].str.upper().str.contains(str.upper(Employee_ID))]

    return filtered_data_filme
  

myname = st.sidebar.text_input( "Buscador de empleados:")
btnmov = st.sidebar.button("Por Employee_ID")
if (myname): 
     filterbyname = search_data(myname)
     count_row = filterbyname.shape[0] #Número columnas
     st.write(f"Total names :  {count_row}")

if (btnmov): 
    st.dataframe(filterbyname)

@st.cache
def search_data(Hometown) : 
    doc = codecs.open('Employees.csv')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_filme1 = data[data['Hometown'].str.upper().str.contains(str.upper(Hometown))]

    return filtered_data_filme1


myname1 = st.sidebar.text_input( "Buscador de Hometown:")
btnmov1 = st.sidebar.button("Hometown")
if (myname1): 
     filterbyname1 = search_data(myname1)
     count_row1 = filterbyname1.shape[0] #Número columnas
     st.write(f"Total names :  {count_row1}")

if (btnmov1): 
    st.dataframe(filterbyname1)

@st.cache
def search_data(Unit) : 
    doc = codecs.open('Employees.csv')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_filme = data[data['Unit'].str.upper().str.contains(str.upper(Unit))]

    return filtered_data_filme

myname2 = st.sidebar.text_input( "Buscador de unit:")
btnmov2 = st.sidebar.button("Unit")
if (myname2): 
     filterbyname2 = search_data(myname2)
     count_row2 = filterbyname2.shape[0] #Número columnas
     st.write(f"Total names :  {count_row2}")

if (btnmov2): 
    st.dataframe(filterbyname2)


@st.cache
def load_data():
    data = pd.read_csv(data_emp)
    return data

@st.cache
def search_data(Education_Level) : 
    doc = codecs.open('Employees.csv')
    data = pd.read_csv(doc)
    filtered_data_nivel = data[data["Education_Level"] == Education_Level]

    return filtered_data_nivel

data = load_data()
selected_edu = st.sidebar.selectbox("Education Level", data ["Education_Level"].unique())
btnFilterbylevel = st.sidebar.button("Education Level")

if (btnFilterbylevel):
    filterbylevel = search_data(selected_edu)
    count_row = filterbylevel.shape[0] 
    st.write(f"Total items: {count_row}")

    
    st.dataframe(filterbylevel)


@st.cache
def load_data():
    data = pd.read_csv(data_emp)
    return data

@st.cache
def search_data(Hometown) : 
    doc = codecs.open('Employees.csv')
    data = pd.read_csv(doc)
    filtered_data_ciudad = data[data["Hometown"] == Hometown]

    return filtered_data_ciudad

data = load_data()
selected_ciu = st.sidebar.selectbox("Ciudad", data ["Hometown"].unique())
btnFilterbyciu = st.sidebar.button("Ciudad")

if (btnFilterbylevel):
    filterbyciudad = search_data(selected_ciu)
    count_row = filterbyciudad.shape[0] 
    st.write(f"Total items: {count_row}")

    
    st.dataframe(filterbyciudad)


@st.cache
def load_data():
    data = pd.read_csv(data_emp)
    return data

@st.cache
def search_data(Unit) : 
    doc = codecs.open('Employees.csv')
    data = pd.read_csv(doc)
    filtered_data_unit = data[data["Unit"] == Unit]

    return filtered_data_unit

data = load_data()
selected_unit = st.sidebar.selectbox("Unit", data ["Unit"].unique())
btnFilterbyunit = st.sidebar.button("Unit_1")

if (btnFilterbyunit):
    filterbyunit = search_data(selected_unit)
    count_row = filterbyunit.shape[0] 
    st.write(f"Total items: {count_row}")


    st.dataframe(filterbyunit)
    

#DATE_COLUMN = 'started_at'
#LAT = 'start_lat'
#LON = 'start_lng'

#@st.cache
#def load_data(Age):
    #doc = codecs.open('Employees.csv')
    #data = pd.read_csv(doc, Age=Age)
    #lowercase = lambda x: str(x).lower()
    #data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    #return data

#data_load_state = st.text('Loading data...')
#data = load_data(500)
#data_load_state.text("Done! (using st.cache)")
#st.dataframe(data)

if st.sidebar.checkbox("Edad empleados "):
    st.subheader("Empleados agrupados por edad")
    Age = data["Age"]

    hist_values = np.histogram(data[Age], bins = 24, range = (0, 24)) [0]
    st.bar_chart(hist_values)
    