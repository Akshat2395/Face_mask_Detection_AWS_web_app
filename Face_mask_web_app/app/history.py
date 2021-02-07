# -*- coding: utf-8 -*-
"""
DISPLAY HISTORY - PREVIOUSLY SEARCHED IMAGES

Categorize the images in 4 segments and display them.
"""

from app import app
from flask import render_template,redirect,url_for,request,session
import mysql.connector
from app.config import db_config


# Check sessions for the same username and display the HTML
@app.route('/history',methods=['GET'])
def history1():
    if 'username' not in session:    
        return redirect(url_for('login'))    
    else:
        uname=session["username"]
        return render_template('history1.html')


# Get details from the form submitted by the user
@app.route('/history',methods=['POST'])
def history():
    if 'username' not in session:    
        return redirect(url_for('login'))    
    else:
        uname=session["username"]
        cnx=mysql.connector.connect(user=db_config['user'],
                               password=db_config['password'],
                               host=db_config['host'],
                               database=db_config['database'],use_pure=True)
        
        cursor=cnx.cursor()
                
        # Get the set of images according to the conditions
        querry='SELECT img_addr,process_img From new_schema.history where username = %s and f_no=fm_no and f_no>0'
        querry1='SELECT img_addr,process_img From new_schema.history where username = %s and f_no= 0'
        querry2='SELECT img_addr,process_img From new_schema.history where username = %s and f_no>0 and fm_no=0'
        querry3='SELECT img_addr,process_img From new_schema.history where username = %s and fm_no>0 and f_no > fm_no'
        
        cursor.execute(querry,(uname,))
        row=cursor.fetchall()
        
        cursor.execute(querry1,(uname,))
        row1=cursor.fetchall()
        
        cursor.execute(querry2,(uname,))
        row2=cursor.fetchall()
        
        cursor.execute(querry3,(uname,))
        row3=cursor.fetchall()      
        
        cnx.close()
        
        opt=request.form.get('options',"")

        # Display images corresponding to each category
        if opt == "1":
            info='Images where all faces are wearing mask'
            return render_template('history.html',row=row, info=info)
        if opt== "2":
            info = 'Images with no face detected'
            return render_template('history.html',row=row1, info=info)
        if opt=="3":
            info = 'Images where all faces are not wearing mask'
            return render_template('history.html',row=row2, info=info)
        if opt=="4":
            info = 'Images with some face wearing mask'
            return render_template('history.html',row=row3, info=info)