## ----------------------------------------THIS IS 'LAUNCH PAGE LAYOUT' ---------------------------------------------##


import streamlit as lit #front-end

## ______________________________________________________________________________________________________________________##

# Each function accessable under a different TAB by unregistered users

import launch_pages.launch_tabs.unregistered_user

## ______________________________________________________________________________________________________________________##

## This is the launch page Layout - each tab calls a different function displaying the various features
def launch():
    
        tab1, tab2, tab3, tab4, tab5 = lit.tabs(["What is FANG","|  CyberSecurity Tips","|  Learn about Cybersecurity ","|  Take the Vulnerability Test", "| Contact Us"])



        with tab1: # What is FANG
                launch_pages.launch_tabs.unregistered_user.what()

        with tab2: # Displaying tips and tricks on good cyberhygiene
                launch_pages.launch_tabs.unregistered_user.tips()        
                
        with tab3: # Displaying educational topics for users on networking and cybersecurity           
                launch_pages.launch_tabs.unregistered_user.learn()

        with tab4: # Displaying a test for users to show their vulnerabilties
                launch_pages.launch_tabs.unregistered_user.test()
        
        with tab5: # What is FANG
                launch_pages.launch_tabs.unregistered_user.who()
