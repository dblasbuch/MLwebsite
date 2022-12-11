#Import dependencies (libraries)

import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st
from PIL import Image
import pandas as pd

#-------------------------------------------------------------------

#Path of the pretrained model

MODEL_PATH = 'models/pickle_model.pkl'

#-------------------------------------------------------------------

# Se recibe la imagen y el modelo, devuelve la predicción

def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds

#-------------------------------------------------------------------

def main():

    st.sidebar.markdown("")
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)

#put a title in our web

    st.title('Crop recomendator :seedling:')
    st.write('With this simple website you can obtain a prediction of the best crop for the type of land you have')

#afegim entrades de text per posar la informació "features/variables que identifica el nostre ML" de l'usuari (textinput = que posi una dada, slider=linea de coses,...)

    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    N = st.text_input("Nitrogen:", placeholder="Ratio of Nitrogen content in soil")
    P = st.text_input("Phosphorous:", placeholder="Ratio of Phosphorous content in soil")
    K = st.text_input('Potassium:', placeholder="Ratio of Potassium content in soil")
    Temp = st.text_input("Temperature:", placeholder="Temperature in Celsius degrees")
    Hum = st.text_input("Relative humidity:", placeholder="Percentage of relative humidity")
    pH = st.text_input("pH:", placeholder="ph value of the soil")
    rain = st.text_input("Rain:", placeholder="Rainfall in mm")

#-------------------------------------------------------------------

# El botón predicción se usa para iniciar el procesamiento
    
    if st.button("Prediction:"):
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(N.title()),
                    np.float_(P.title()),
                    np.float_(K.title()),
                    np.float_(Temp.title()),
                    np.float_(Hum.title()),
                    np.float_(pH.title()),
                    np.float_(rain.title())]
        predictS = model_prediction(x_in, model)
        st.success('The recommended crop is: {}'.format(predictS[0]).upper())

#-------------------------------------------------------------------

def page2():
    st.sidebar.markdown("")
    st.title('What can I plant? 🪴')
    st.text('')
    st.write('Different plantations from which we can choose:')
    st.text('')  

    st.subheader('Fruits:')

    columns = st.columns((1,1,1))
    
    with columns[0]:
        pomegranate = Image.open('plants/fruits/pomegranate.jpg')
        apple = Image.open('plants/fruits/apple.jpg')
        bananas = Image.open('plants/fruits/bananas.jpg')
     
        st.image(pomegranate, use_column_width=True)
        with st.expander("pomegranate"):
            st.write("""
                "A several-celled reddish berry that is about the size of an orange 
                with a thick leathery skin and many seeds with pulpy crimson arils 
                of tart flavor"
            """)
        
        st.image(apple, use_column_width=True)
        with st.expander("apple"):
            st.write("""
                "The fleshy, usually rounded red, yellow, or green edible pome
                fruit of a usually cultivated tree (genus Malus) of the rose family"
            """)

        st.image(bananas, use_column_width=True)
        with st.expander("banana"):
            st.write("""
                "An elongated usually tapering tropical fruit with soft pulpy
                flesh enclosed in a soft usually yellow rind"
            """)

    st.subheader('Legumes:')

    with columns[1]:
        coconut = Image.open('plants/fruits/coconut.jpg')
        mango = Image.open('plants/fruits/mango.jpg')
        muskmelon = Image.open('plants/fruits/muskmelon.jpg')

        st.image(coconut, use_column_width=True)
        with st.expander("coconut"):
            st.write("""
                "The drupaceous fruit of the coconut palm whose outer fibrous husk
                yields coir and whose nut contains thick edible meat and,
                in the fresh fruit, a clear liquid"
            """)

        st.image(mango, use_column_width=True)
        with st.expander("mango"):
            st.write("""
                "A tropical usually large ovoid or oblong fruit with a firm
                yellowish-red skin, hard central stone, and juicy aromatic pulp"
            """)

        st.image(muskmelon, use_column_width=True)
        with st.expander("muskmelon"):
            st.write("""
                "A usually sweet edible melon that is the fruit of an annual trailing
                or climbing Asian vine (Cucumis melo) of the gourd family"
            """)

    with columns[2]:
        orange = Image.open('plants/fruits/orange.jpg')
        papaya = Image.open('plants/fruits/papaya.jpg')
        watermelon = Image.open('plants/fruits/watermelon.jpg')

        st.image(orange, use_column_width=True)
        with st.expander("orange"):
            st.write("""
                "A globose berry with a yellowish to reddish-orange
                rind and a sweet edible pulp"
            """)

        st.image(papaya, use_column_width=True)
        with st.expander("papaya"):
            st.write("""
                "A tropical American tree (Carica papaya of the family Caricaceae,
                the papaya family) having an oblong to globose yellow edible fruit
                with numerous black seeds in a central cavity"
            """)

        st.image(watermelon, use_column_width=True)
        with st.expander("watermelon"):
            st.write("""
                "A large oblong or roundish fruit with a hard green or white rind often
                striped or variegated, a sweet watery pink, yellowish, or red pulp, and
                usually many seeds"
            """)

#-------------------------------------------------------------------

    columns = st.columns((1,1,1))

    with columns[0]:        
        blackgram = Image.open('plants/legumes/blackgram.jpg')
        chickpea = Image.open('plants/legumes/chickpea.jpg')
        kidneybeans = Image.open('plants/legumes/kidneybeans.jpg')
    
        st.image(blackgram, use_column_width=True)
        with st.expander("blackgram"):
            st.write("""
                "A twining herb (Dolichos biflorus) of the tropics of the Old World 
                that is cultivated in India for fodder with the seeds being used as food"
            """)

        st.image(chickpea, use_column_width=True)
        with st.expander("chickpeas"):
            st.write("""
                "An Asian herb (Cicer arietinum) of the legume family cultivated 
                for its short pods with one or two seeds"
            """)

        st.image(kidneybeans, use_column_width=True)
        with st.expander("kidneybeans"):
            st.write("""
                "An edible and nutritious usually kidney-shaped seed of any of various 
                cultivated beans of the common species (Phaseolus vulgaris)"
            """)
       
    st.subheader('Tropical crops:')

    with columns[1]:

        lentils = Image.open('plants/legumes/lentils.jpg')
        mothbeans = Image.open('plants/legumes/mothbeans.jpg')

        st.image(lentils, use_column_width=True)
        with st.expander("lentils"):
            st.write("""
                "A widely cultivated Eurasian annual leguminous plant (Lens culinaris)
                with flattened edible seeds and leafy stalks used as fodder"
            """)

        st.image(mothbeans, use_column_width=True)
        with st.expander("mothbeans"):
            st.write("""
                "A legume (Vigna acontifolia or Phaseolus aconitifolius) cultivated
                especially in India for its edible cylindrical pods and small seeds"
            """)


    with columns[2]:
        pigeonpeas = Image.open('plants/legumes/pigeonpeas.jpg')
        mungbeans = Image.open('plants/legumes/mungbeans.jpg')

        st.image(pigeonpeas, use_column_width=True)
        with st.expander("pigeonpeas"):
            st.write("""
                "A leguminous shrubby herb (Cajanus cajan) with trifoliate leaves, yellow
                flowers, and flattened pods that is much cultivated especially
                in the tropics"
            """)

        st.image(mungbeans, use_column_width=True)
        with st.expander("mungbeans"):
            st.write("""
               "An erect bushy annual bean (Vigna radiata synonym Phaseolus aureus) that
                is widely cultivated in warm regions for its edible usually green or yellow
                seeds, for forage, and as the chief source of bean sprouts"
            """)

#-------------------------------------------------------------------

    columns = st.columns((1,1,1))

    with columns[0]:
        coffee = Image.open('plants/tropical_crops/coffee.jpg')
        cotton = Image.open('plants/tropical_crops/cotton.jpg')

        st.image(coffee, use_column_width=True)
        with st.expander("coffee"):
            st.write("""
                "Any of several Old World tropical plants (genus Coffea and 
                especially C. arabica and C. canephora) of the madder family 
                that are widely cultivated in warm regions for their seeds 
                from which coffee is prepared"
            """)

        st.image(cotton, use_column_width=True)
        with st.expander("cotton"):
            st.write("""
                "The tropical and subtropical plant that is commercially grown to make 
                cotton fabric and thread. Oil and a protein-rich flour are also 
                obtained from the seeds"
            """)
    
    st.subheader('Vineyards:')
    
    with columns[1]:

        jute = Image.open('plants/tropical_crops/jute.jpg')

        st.image(jute, use_column_width=True)
        with st.expander("jute"):
            st.write("""
                "The glossy fiber of either of two Asian plants (Corchorus olitorius and 
                C. capsularis) of the linden family used chiefly for sacking, burlap, 
                and twine"
            """)

    with columns[2]:

        rice = Image.open('plants/tropical_crops/rice.jpg')

        st.image(rice, use_column_width=True)
        with st.expander("rice"):
            st.write("""
                "The starchy seeds of an annual southeast Asian cereal grass
                (Oryza sativa) that are cooked and used for food"
            """)

#-------------------------------------------------------------------

    columns = st.columns((1,1,1))

    with columns[0]:

        grapes = Image.open('plants/vineyards/grapes.jpg')

        st.image(grapes, use_column_width=True)
        with st.expander("grapes"):
            st.write("""
                "A smooth-skinned juicy light green or deep red to purplish black
                berry eaten dried or fresh as a fruit or fermented to produce wine"
            """)

    st.subheader('Cereals:')

    columns = st.columns((1,1,1))

#-------------------------------------------------------------------

    with columns[0]:

        maize = Image.open('plants/cereals/maize.jpg')

        st.image(maize, use_column_width=True)
        with st.expander("maize"):
            st.write("""
                "A tall annual cereal grass (Zea mays) originally
                domesticated in Mexico and widely grown for its
                large elongated ears of starchy seeds"
            """)

#-------------------------------------------------------------------

def page3():
    st.sidebar.markdown("")
    st.title('Information of the group 💡')
    st.text('')

    columns = st.columns((1,1))

    with columns[0]:

        image = Image.open('extra/dani.jpg')

        st.image(image, use_column_width=True)

        st.write('')
        st.subheader('Github repository')
        st.write("Check out our [Github repository](https://github.com/dblasbuch/MLwebsite)")

        st.subheader('Instagram')
        st.write('Check out our [Instagram profile](https://www.instagram.com/dblasbuch_/)')

    with columns[1]:

        st.write('''
            My name is Dani Blas Buch. I'm 24 years old and I'm currently studying 
            the TCCM master at the University of Barcelona (UB). I have created this 
            website using a pre-trained algorithm in order to help some people who 
            don't know what can be the best thing to plant in their farmland. 
            It is just for a work of this master but it has been a good learning process.
           
            In case you have used the web and got this far, thank you very much for
            your trust and enjoy!
        ''')  

        firma = Image.open('extra/firma.png')

        st.image(firma)

#-------------------------------------------------------------------

def page4():
    st.sidebar.markdown("")
    st.title('Calculation example 📝')
    st.text('')
    st.write('''
        Here we can see an example of how to enter the data belonging to each of the 
        required variables. We must take into account that the introduction of abnormal 
        data, will give error in the calculation of the algorithm.
    ''')
    st.subheader('Range of values:')
    
    df = pd.read_csv('table/table.csv')

#CSS to inject contained in a string

    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

#Inject CSS with Markdown

    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(df)
    
    st.subheader('Calculation example:')

    video_file = open('extra/video.mp4', 'rb')
    video= video_file.read()

    st.video(video)
    
#-------------------------------------------------------------------
    
page_names_to_funcs = {
    "Crop recomentador": main,
    "Different crops": page2,
    "Information about us": page3,
    "Example": page4    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

