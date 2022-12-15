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

#It recive the images and model to return the prediction

def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds

#-------------------------------------------------------------------

#Definition of the main page of the web and its model

def main():

    st.sidebar.markdown("")
    
    model=''

    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)

#Put a title in our web

    st.title('Crop recomendator :seedling:')
    st.write('With this simple website you can obtain a prediction of the best crop for the type of land you have')

#All the inputs to perform the calculation as defined variables (our ML algorithm identifies them from the user)

    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    N = st.text_input("Nitrogen:", placeholder="Ratio of Nitrogen content in soil")
    P = st.text_input("Phosphorous:", placeholder="Ratio of Phosphorous content in soil")
    K = st.text_input('Potassium:', placeholder="Ratio of Potassium content in soil")
    Temp = st.text_input("Temperature:", placeholder="Temperature in Celsius degrees")
    Hum = st.text_input("Relative humidity:", placeholder="Percentage of relative humidity")
    pH = st.text_input("pH:", placeholder="ph value of the soil")
    rain = st.text_input("Rain:", placeholder="Rainfall in mm")

#-------------------------------------------------------------------

#Define the "prediction" button to start the calculation procedure
    
    if st.button("Prediction:"):
#If loop to introduce a warning in case the input values are not in the stablished range
        if (0 <= int(N) <= 140) and (5 <= int(P) <= 145) and (5 <= int(K) <= 205) and (8.83 <= int(Temp) <= 43.7) and (14.3 <= int(Hum) <= 100) and (3.5 <= int(pH) <= 9.94) and (20.2 <= int(rain) <= 299):   
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
        else:
            st.write('There is a value which is out of range, try to change it! ⚠️')

#-------------------------------------------------------------------

#Definition of the second page of the web with its sidebar location

def page2():
    st.sidebar.markdown("")
    st.title('What can I plant? 🪴')
    st.text('')
    st.write('Different plantations from which we can choose:')
    st.text('')  

    st.subheader('Fruits:')

#Definition of the first block of images 

    columns = st.columns((1,1,1))
    
#Definition of each column with the images defined as variables

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

#Definition of the second block of images 

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

#Definition of the third block of images 

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

#Definition of the fourth block of images 

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

#-------------------------------------------------------------------

#Definition of the fifth block of images 
  
    columns = st.columns((1,1,1))

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

#Definition of the fourth page of the web with its sidebar location

#Location of two columns with an image and text

def page4():
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

#Definition of the third page of the web with its sidebar location

def page3():
    st.sidebar.markdown("")
    st.title('Calculation example 📝')
    st.text('')
    st.write('''
        Here we can see an example of how to enter the data belonging to each of the 
        required variables. We must take into account that the introduction of abnormal 
        data, will give error in the calculation of the algorithm.
    ''')
    st.subheader('Range of values:')

#Definition of the database for a table as a .csv file

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
    
#Video introduced as a variable

    st.subheader('Calculation example:')

    video_file = open('extra/video.mp4', 'rb')
    video= video_file.read()

    st.video(video)
    
#-------------------------------------------------------------------

def page5():
    st.sidebar.markdown("")
    st.title('Explanation of our web 🧠')

#Different text input explanations about the web and link inputs

    st.write('''
        A brief explanation of the different parts of the building process of the web is introduced
        here. The process of developing the app has been long, but at the end we think that the 
        result is quite good. 

        Thanks for using our app!
    ''')

    st.subheader('Data source and domain description:')
    st.write('''
        In this work a SVM support vector machine model has been generated to help recommend a type of 
        crop depending on the characteristics and climate of the area. The database used was created by 
        Atharva Ingle (Dev Expert at Weights and Biases (Pune, Maharashtra, India)), who made it public on 
        the Kaggle website. Thus, this dataset was build by augmenting datasets of rainfall, climate and 
        fertilizer data available for India. Its data entry goes up to about 2201 entries for different 
        types of crops (rice, pomegranate, bananas, chickpeas, ...). In this case, the same database, 
        which is a Microsoft Excel document (.csv), is divided into two groups referring to the training 
        data set (80%) and the test data set (20%) to ensure good performance.
    ''')

    st.write('You can see the information about the data base in [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?select=Crop_recommendation.csv)')    

    st.subheader('Initial investigations on the data sources:')
    st.write('''
        The database used was not very difficult to find, since from the Github platform, it was possible 
        to find a great variety of databases capable of being adapted to the algorithm found. 
        From the beginning, different databases were found to be implemented, but we were looking for a 
        database with enough variables (inputs) to be introduced to perform our calculation within 
        the algorithm. Different data sets were tested to see how they worked and how they had been trained 
        previously, but it was observed that they were not accurate enough, gave some kind of error or 
        did not follow the structure needed to perform a regression of the data.
    ''')

    st.subheader('App objective, problem statement and research questions:')
    st.write('''
        The app shown in this project started with the, already explained, investigation of different 
        pre-trained algorithms and a suitable database. It was possible to find a database which made 
        reference to what type of planting is more suitable for each type of soil and environment. 
        In this way, it was thought that it could be a good application, since, both in the countryside 
        and in the city itself, the population tries to make some small or large orchard. With this 
        application we try to provide the knowledge to be able to make a small or large plantation to any 
        person with internet access. On the other hand, the main problem that has been found in the project, 
        is due to the fact that the variables introduced in this algorithm, many times, may not be enough 
        to determine a sufficiently adequate crop, since data would be missing. We also know that we have 
        about 22 crops entered within our database, and that sometimes it cannot be adapted to what people 
        want in each region. Finally, we wonder how far this project can go, since the database used is 
        simple and can be easily expanded to increase the possibilities depending on the climate and terrain 
        variables.
    ''')

    st.subheader('Introduced fallbacks:')
    st.write('''
        As can be seen, the inputs used in our app are basically numerical values. In this way, the 
        fallback introduced to allow the correct functioning of the application has been referred to 
        the ranges of values of the variables that build the algorithm. In this case, an if loop has 
        been introduced to determine that if any of the values entered were outside the determined range, 
        a warning would be sent to the user so that he could change it and perform the calculation correctly. 
        Once the message is sent, the user can change the values that are not in accordance with the ranges 
        without stopping the web or stop working. Otherwise, no further fallbacks have been introduced 
        concerning the percentage efficiency of the algorithm, since as explained above the database used 
        comprises a large number of values for each of the plantations defined in it. However, it can be said 
        that the algorithm will always give a result because the parameters are delimited within an 
        established range.
    ''')

    st.subheader('Notes and main challenges faced during deployment phase:')
    st.write('''
        The created application has been generated correctly using Streamlit. On the other hand, it has been 
        necessary to put it on the Internet in order to make it available to all types of users who require its 
        services. To perform this task correctly, different platforms could be used (Heroku, Google Cloud, ...). 
        The free use of Heroku lasted until November 28th, due to some personal inconveniences the group 
        started to work after this date and could not use the platform explained. However we tried to use the 
        platform called Google Cloud, in this platform you must create a free user profile to work, but it 
        requires the introduction of personal bank details to perform the procedure which we do not agree to 
        deposit. We know the procedure to follow and, so that it does not seem that it has not been tried, we 
        wanted to explain the steps to follow to perform the procedure with Google Cloud:
                                           
        1️⃣  Activate [Google Cloud](https://cloud.google.com/gcp?utm_source=google&utm_medium=cpc&utm_campaign=emea-es-all-en-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_500236788684-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+~+GCP+~+General%23v1-KWID_43700060384861654-aud-606988878134:kwd-6458750523-userloc_1005431&utm_term=KW_google+cloud-NET_g-PLAC_&gclid=Cj0KCQiAqOucBhDrARIsAPCQL1b8L0cziKY5N797oufqX1xU_rqT4LlXFloraroIgODR3CxXbFYIaj4aAjScEALw_wcB&gclsrc=aw.ds&hl=ca)
                                                                                      
        2️⃣  Create a project in Google Cloud
                                             
        3️⃣  Install [GoogleCloudSDK](https://cloud.google.com/sdk/docs/install)

        4️⃣  Execute in the terminal:
                  
               gcloud init               
            gcloud app deploy app.yaml –project “Name of the project”

    ''')
    with st.expander("app.yaml"):
        st.write("""
            runtime: custom

            env: flex
        """)

#-------------------------------------------------------------------    

#Definition of each of the pages inside the web

page_names_to_funcs = {
    "Crop recomentador 🌱": main,
    "Different crops 🪴": page2,
    "Example 📝": page3,
    "Information about us 💡": page4,
    "Information about the web 🧠": page5    
}

#Function definition to select each page of the web in the sidebar

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

