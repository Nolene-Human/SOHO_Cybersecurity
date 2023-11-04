   ## ------------------------------------Features used by Unregisted users -------------------------------------------------##
 ## -------------------------- Called from Launch.py when user select any of the tabs ------------------------------------##

import streamlit as lit
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import html



def learn():
## ______________________________________________________________________________________________________________________##
# - NO FUTURE DEVELOPMENT PLANNED - #
## ______________________________________________________________________________________________________________________##
   

    lit.header("Monitor your Network")
    lit.write("In this section you will aquire the basic knowledge to understand the threat on a HomeOffice network")
    
    lit.markdown("---")

# ---------- Key Terminology ---------------#
       
    
    lit.text("CYBERSECURITY TERMINOLOGY : ")
    col2,col3= lit.columns(2) 
    
    
    col2.write("""
            - Cyber Threats
            - Cyber Attacks
            - Attack Surface
            - Gateway
            - IP Address
            - Mac Addresses
               
            """)

    col3.write(""" 
        - Internet devices
        - Network        
        - Ports
        - Integrity
        - Availability
        - Confidentiality"""
    )

    lit.markdown("---")

# ---------- Key Ideas ---------------#  
   

    lit.subheader("Why would ANYONE want to attack you?")

    lit.write("""In the book [The Art of Attack](https://www.amazon.com/Art-Attack-Attacker-Security-Professionals/dp/1119805465) by Maxi Reynolds, a very successful social engineering in CyberSecurity states it well""")
                    
    lit.markdown("#### Your information, or the information you have access too, is crucial for cybercriminals.")

    lit.markdown("---")



    lit.subheader("What is a Network and Why Should I care?")
    lit.markdown("""
    You are connecting to the internet via a DEVICE through a PORT.
     The DEVICE connecting you to the internet is called a WIFI ROUTER. 
    The Port is like a DOOR to and from the Internet World. 
    Your Wifi Router is also commonly refered to as your GATEWAY.""",)
    lit.write("Each device will have a DOOR -> connected to your GATEWAY -> leading to the World Wide Web and all the hackers that live there.")
    lit.markdown("#### Securing your network and the access to your resources is one of the best ways to secure you and your home business")
    lit.markdown("---")

    lit.subheader("How is this done?")
    lit.markdown("""
    Your Gateway will assign each device on your network an address to identify and communicate with, this is called an IP ADDRESS. 
    Each device will have a unique IP ADDRESS and a MAC ADDRESS""")
    
    lit.markdown("The router assign a devices and IP address and a Manufacturer assigns the Mac Address")
    lit.markdown("""
    Through these unique numbers hackers can identify the devices on your network (inlcuding its known vulnerabilites and uses).""") 

    lit.markdown("""
    Hackers can without your consent, connect, communicate or monitor your NETWORK.  
    Once in your network, they can disguise themselves, reroute your internet activities to their servers in turn see your activities. This will include accounts, usernamesand password.""")
    
    lit.markdown("#### These malicious activities are called CYBER THREATS.")

    lit.markdown("---")
    lit.markdown("""
    With Fang your Home Business network will follow and monitor the most common SOHO cyber threats, securing your business and 
                 partners agains cyberattacks. With our comprehensive protection, you business and home can browse, work, and communicate in 
                 cohesion with the utmost confidence :medal: """)


def test():
## ______________________________________________________________________________________________________________________##
# - Link each threat to a solution which will either be the TIPS or the SCANNER page 
## ______________________________________________________________________________________________________________________##

   lit.header("Identify your risks:")

    # -- tick box for users input -- #
   social_Engineering = lit.checkbox('Do you use Emails?')
   thirdparty_Exposure = lit.checkbox('Do you work from home on other business data?')
   configuration = lit.checkbox('Are you nervous doing any configuration on your devices?')
   hygiene = lit.checkbox("You don't have any network protection processes in place?")
   cloud = lit.checkbox("Do you use any websites or access data through an online connection?")
   mobile= lit.checkbox("Do use any online applications?")
   things=lit.checkbox("Do you have any smart devices that connect to the network or you control through an application (tv's , lights, poweradaptors)?") 
   ransomeware=lit.checkbox("Do you work with sensitive or private data, that can't be seen by other except those it is intended?")
   data =lit.checkbox("Do you share data or any information over the internet?")
   procedures=lit.checkbox("You don't do any checks on your system?")

   lit.markdown("---")
   
    # -- if a tick box is checked the vulnerability is shown -- #
   if social_Engineering:
      lit.write("**Social Engineering**: this relies on you making a mistake by giving away your information (phishing and email impersonation)")
    
   if thirdparty_Exposure:
      lit.write("""**Third-party Exposure**: You are working outside of a protected network, working from home as an employee or contractors.
                 This is making you a weak link in the network for the organisations you are working for""")
      
   if configuration:
      lit.write("""**Configuration Mistakes** : Not ensuring all your devices connected to the internet meets the minimum security configuration is a huge risk""")
    
   if hygiene:
      lit.write("""**Poor Cyber Hygiene** : Poor password, unprotected home networks makes for an easy target""")

   if cloud:
      lit.write("""**Cloud Vulnerabilities** : Web Application and Cloud Service breaches are increasing, default security settings were exposed, exposing ways for application and services
         to be hacked, with insufficient access control such as Multifactor Authentication (MFA) and casual trust between environments is making your devices easier to hack""")

   if mobile:
      lit.write("""**Mobile Device Vulnerabilities** : Malicious mobile application, coming sometimes from the organisations you are working with can cause a risk in you network""")

   if things:
      lit.write("""**Internet of Things** : Malicious mobile application, coming sometimes from the organisations you working with can cause a risk in you network""")
      
   if ransomeware:
      lit.write("""**Ransomware** : Through malicious software sent to you by an attacker data can be held for ransom, blocking you from accessing it until you have paid, or could provide details
      on how they have hacked your system and threat to release this to your clients.""")
    
   if data:
      lit.write("""**Poor Data Management** : Your or the companies you work for, data can be exploited for financial gain- this is different from ransomeware as the data is sold to a third party without your
      knowledge.""")

   if procedures:
      lit.write("""**Inadequate Post-Attack Procedures** : Not having a system or process in place to recover from any of these attacks could close your business or destroy your reputation.""")

   lit.markdown("---")

def tips():
## ______________________________________________________________________________________________________________________##
# - FUTURE DEVELOPMENT - #
# - Add questionnaire so user are able to relate better to the treats 
# - Link each threat to a solution which will either be the TIPS or the SCANNER page 
## ______________________________________________________________________________________________________________________##

    lit.header("Good CyberHygiene Tecniques + Tips")
    select = lit.selectbox("Select a topic from the dropdown list",(" ","Maintain good password hygiene","Update systems and software","Multi Factor Authentication","Keep up-to-date on phishing/security training and awareness","Implement 'Zero Trust'","Anti-Virus"))

    if select == "Maintain good password hygiene":
        lit.markdown("FANG can help you manage all those passwords, ensure they are strong and enable features that can protect your account from attackers")
        lit.subheader("Some reason why you should")
        lit.markdown("- Block Web and Email Threats")
        lit.markdown("- Keep Hackers of your PC")
        lit.markdown("- Protect you from Snoops")
        lit.markdown("- Shop and Bank saver")        
        lit.subheader("How to:")
        lit.write("Use Password Management Tools")
        lit.markdown("Consider Passphrase or Random common words for your password")

    elif select =="Update systems and software":
        lit.subheader("Some reason why you should")
        lit.markdown("- Enhance Security")
        lit.markdown("- Enhance Performance")
        lit.markdown("- Avoid Hardware Problems")
        lit.markdown("- Avoid losing features")
        lit.markdown("- Avoid Data loss")
        lit.subheader("How to:")
        lit.write("""Visit the software or device company website to see if there is any updates. If you have an application installed see if you have any notifications to update. 
        Some apps or devices will notify you through settings.""")
        lit.write("❗ Don't forget to do this for all devices connected to the internet.")

    elif select == "Multi Factor Authentication (MFA)":
        lit.subheader("Some reason why you should")
        lit.markdown("- Reduce the chances of a data breach")
        lit.markdown("- Secure Against Identity Theft Via Stolen Passwords")
        lit.markdown("- Enable Your Other Security Measures To Do Their Job Properly")
        lit.markdown("- Stay compliant")
        lit.subheader("What it Does")
        lit.write("MFA provides more than one way to verify your login, hackers are unable to access your accounts without knowing all three keys at the time you log in")
        lit.subheader("Link to explain MFA")
        lit.markdown("[Multi Factor Authentication](https://www.youtube.com/watch?v=nc7fpGJsE1g)")
        lit.subheader("Link to tools that can be used for all types of accounts")
        lit.markdown("[Microsoft Multi Factor Authenticator](https://www.microsoft.com/en-nz/p/microsoft-authenticator/9nblgggzmcj6")
        lit.markdown("[Twilio](https://authy.com/guides/twilio/)")
        lit.markdown("[LastPass](https://www.lastpass.com/)")
    
    elif select == "Keep up-to-date with phishing/security training and awareness":
        lit.subheader("Some reason why you should")
        lit.markdown("- Protecting your personal and financial information")
        lit.markdown("- Protecting your business")
        lit.markdown("- Staying ahead of evolving threats")
        lit.markdown("- Will help you stay compliant with regulations and standards")
        lit.subheader("Register to a newsletter")
        lit.markdown("[Cloudflare]https://blog.cloudflare.com/)")

    elif select == "Anti-Virus":
        lit.subheader("Some reason why you should")
        lit.write("Detect and remove computer Virus and anti-malware from your device")
        lit.markdown("- Malware & Virus Protection")
        lit.markdown("- Defence Against Data Thieves")
        lit.markdown("- Increases Your Computer’s Lifetime")
        lit.markdown("- Comprehensive Threat Protection")
        lit.subheader("What it Does")
        lit.markdown("- Stop threats in Real time")
        lit.markdown("- Block Web and Email Threats")
        lit.markdown("- Keep Hackers of your PC")
        lit.markdown("- Protect you from Snoops")
        lit.markdown("- Shop and Bank saver")
        lit.markdown("- Alerts and Reports")
        lit.subheader("Link's to some of the top Anti-Virus Software")
        lit.write("[AVG](https://www.avg.com/en-ww/homepage#pc)")
        lit.write("[Kaspersky](https://www.kaspersky.com.au/)")
        lit.write("[McAfee](https://nz.norton.com/store)")
        lit.write("[Norton](https://nz.norton.com/store)")
        lit.write("[Bitdefender](https://www.bitdefender.com/)")

    else:
        lit.write("Starting somewhere is better than nowhere")

def what():
## ______________________________________________________________________________________________________________________##
# - NO FUTURE DEVELOPMENT PLANNED - #
## ______________________________________________________________________________________________________________________##

    lit.header("Cybersecurity Specialist")
    lit.markdown("**for Home Offices and Web Application Developers**")

    col1, col2 = lit.columns(2)
    col2.markdown('**Application Security**')
    col2.write("""Recognizing that every application is unique, we adopt a tailored approach to cybersecurity. 
            Our solutions are never one-size-fits-all; instead, join you on your journey where you need us.
               From start to finish, code audits to penetration testing, we leave no stone unturned in your pursuit of comprehensive security.    
      """)
    
    col2.markdown(""" * Before Development Begins\n
* During Definition and Design \n
* During Development \n
* During Deployment \n
* During Maintenance and Operations""")
  
    col1.markdown('**Home Office Security**')
    col1.write(""" Recognizing that every SOHO network has its unique footprint, we adopt a bespoke approach to security. 
               Our solutions are never off-the-shelf; rather, they are meticulously crafted to address your specific 
               network architecture and devices.  
               Our commitment to your security goes beyond the immediate horizon. As you evolve, we evolve with you, 
               adapting our strategies to match your growth and changing threat landscapes. 
                Embark on a journey where security meets innovation.Explore our services, meet our specialists
               , and get ready to elevate your network security to unprecedented heights.""")
    
    col1.markdown(""" * Pre-engagement Interactions\n
* Intelligence Gathering \n
* Threat Modeling \n
* Vulnerability Analysis \n
* Exploitation / Post Exploitation""")
    lit.write ("\n\n\n ")
    lit.markdown('**Scroll through our FREE basic training resources**')

def who():
   lit.header("Cybersecurity Specialist")
   with lit.form('contact', clear_on_submit=True):
      lit.write('Contact us for an assessement and quote')
      form_name=lit.text_input('Name')
      form_email=lit.text_input('Email address')
      form_number=lit.text_input('Contact Number')
      contact_form=lit.form_submit_button('Submit')
   if contact_form:
      FROM ='onlyforshowhacks@gmail.com'
      email_password=os.environ.get('admin_gmail')
      TO = 'onlyforshowhacks@gmail.com'
          
      subject=f"message from new client {html.escape(form_name)}"
      content =f"Please contact {html.escape(form_name)} on {html.escape(form_email)},on {html.escape(form_email)}"
      em = MIMEMultipart()
      em['From']=FROM
      em['To']=TO
      em['Subject']=subject
      body=MIMEText(content,'plain')
      em.attach(body)
          
      context = ssl.create_default_context()
      
      try:
         with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login('onlyforshowhack@gmail.com',email_password)
            smtp.sendmail('onlyforshowhack@gmail.com',TO,em.as_string())
            lit.write("Thank you for contacting us, we will be in touch soon!"
      
      except Exception as e:
         lit.write('unable to send email')

   
