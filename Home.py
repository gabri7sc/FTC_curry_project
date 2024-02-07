# Imports

import streamlit as st
from PIL import Image


st.set_page_config( page_title='Home', page_icon='👽' )

# mage_path = 'C:/Users/gabre/DS IN PROGRESS/DS_2023/Ciclo_Basico/FTC Analisando dados com Python/FTC_pycharm/'
# image_filename = 'environmental_data science.jpg'
# full_image_path = image_path + image_filename
# image = Image.open( full_image_path )
image = Image.open( 'company_curry.png' )

st.sidebar.image( image, width=250, use_column_width=True )

st.sidebar.markdown( '# Curry Company' )
st.sidebar.markdown( '## Fastest Delivery in Town' )
st.sidebar.markdown( """___""" )

st.write( '# Curry Company Growth Dashboard' )

st.markdown(
    '''
    Growth Dashboard was created to follow the growth metrics from Deliverymen and Restaurants.
    ### How to use it?
    - Company's View:
        - Management View: General behavior metrics.
        - Tactic View: Weekly growth indicator.
        - Geographic View: Geological insights.
    - Deliveryman's View:
        - Weekly growth indicator
    - Restaurants' View:
        - Weekly growth indicator
    ### Ask for help
    - Data Science Team on Discord
        - @gabri7sc
''' )
