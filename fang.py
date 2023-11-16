## ----------------------------------------THIS IS 'MAIN' ----------------------------------------------- ##
## ----------Launced when application start and is the only 'page' in this application------------------##
## --------All other 'pages' are called functions displayed when conditions have been met-------------##

## ______________________________________________________________________________________________________________________##

## Importing Front-end tool Streamlit (https://streamlit.io/)
import streamlit as lit

import requests
headers ={'X-Frame-Option:DENY'}
r=requests.post('https://httpbin.org/post',headers=headers)

## ______________________________________________________________________________________________________________________##

## Import applications Login and Registration Functions ##
import launch_pages.launch


## ______________________________________________________________________________________________________________________##

## Page UI / UX
#lit.set_page_config(page_title="FANG",page_icon="🚀")

## ______________________________________________________________________________________________________________________##


launch_pages.launch.launch()  

        
