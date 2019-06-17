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
mycursor.execute('select * from country order by Name')
hasil = mycursor.fetchall()


query = 'select * from country order by Name'
df = pd.read_sql(query, con = mydb)

x = df['Name'][df['Region'] == 'Southeast Asia']

y = df['Population'][df['Region'] == 'Southeast Asia']

colour = ['green', 'yellow', 'black', 'red', 'blue', 'cyan', 'grey', 'pink', 'brown', 'lightgreen', 'lightblue']

plt.pie(y, labels=x,
    colors = colour,
    autopct='%1.1f%%', textprops={'color': 'grey'}
)

plt.title('Persentase Penduduk ASEAN')

plt.show()