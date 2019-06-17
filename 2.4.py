import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost' ,
        user = 'nino',
        passwd = 'mvplover',
        database = 'world'
    )

mycursor = mydb.cursor()
mycursor.execute('select * from country')
hasil = mycursor.fetchall()

query = 'select * from country'
df = pd.read_sql(query, con = mydb)

x = df['Name'][df['Region'] == 'Southeast Asia']

y = df['SurfaceArea'][df['Region'] == 'Southeast Asia']

plt.pie(y, labels=x,
    autopct='%1.1f%%', textprops={'color': 'black'}
)
plt.title('Persentase Luas Daratan ASEAN')


plt.show()