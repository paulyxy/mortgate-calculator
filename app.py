# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:09:42 2023

@author: pyan
"""

import numpy as np
import streamlit as st
from matplotlib import pyplot as plt

st.set_page_config(layout="wide")
st.title("Mortgage calculator") 
st.write("By Dr. Yan, v1.0, 2/18/2023")

a1=f" ##### Input a set of values: house price, % down payment, mortgage rate, and loan term (the number of years)."
a2=f" ##### this mortgage calculator will calculate 1) the monthly payment, and 2) draw a nice pie chart."
a3=f" #####  Buy a house in Costa Rica? https://www.youtube.com/@TropicalGlowCostaRica"

with st.expander("Click here to see (or hide) a simple explanation."):
    st.write(a1)
    st.write(a2)
    st.write(a3)

col1, col2,col3 =st.columns([1.2,1,1])

price=col1.number_input("Step 1: Input the price of a house (the default value is $100,000):",value=100_000)
  
pct= col1.number_input("Step 2: Input % of the house price as a down payment (the default value is 0.2, i.e., 20%):",value=0.20)

with col1.expander("Step 2B: Click here to see (or hide) the down payment"):
    downpayment=pct*price
    st.write(round(downpayment,2))

rate= col1.number_input("Step 3: Input an annual interest rate (the default value is 0.056, i.e., 5.6%):",value=0.056,format="%0.5f")

year = col1.selectbox(
    "Step 4: Choose a loan term, i.e., the nubmer of years (the default value is 30):", (30, 20, 15, 10,5))

R_monthly=rate/12
loan=(1-pct)*price   

with col2.expander("Step 5: Click here to see the Effective Monthly Rate"):
     st.write(round(R_monthly,6))
     
with col2.expander("Step 6: Click here to see the loan amount."):
    st.write(loan)
     
monthlyPayment=loan*rate/12/(1-1/(1+rate/12)**(year*12))
  
with col2.expander("Step 7: Click here to see the monthly mortgage payment:"):
    st.write(round(monthlyPayment,2))
    
    
tax= col2.number_input("Step 8 (optional): enter the property tax (monthly payment)",value=150)    

insurance= col2.number_input("Step 9 (optional): insutrance (monthly payment)",value=100)    

HOAmonthlyFee=col2.number_input("Step 10 (optional): HOA (Home Owner Association) monthly payment",value=200)    
    
total=monthlyPayment+tax+insurance+HOAmonthlyFee

with col3.expander("Step 11: Click here to see the total monthly payment:"):
    st.write(round(total,2))

with col3.expander("Step 12: show (or hide) a nice pie chart"):
    #names=['Monthly Mortgage Payment','Tax','Insurance','HOA']    
    #data = [monthlyPayment, tax,insurance,HOAmonthlyFee]
    #fig = plt.figure(figsize =(10, 7))
    #plt.pie(data, labels = names)
    #plt.show()
    #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    labels = 'Tax (monthly)','Monthly Mortgage Payment','Insurance (monthly)','HOA (monthly)'    
    #sizes = [15, 30, 45, 10]
    sizes= [tax, monthlyPayment,insurance,HOAmonthlyFee]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

     

    
