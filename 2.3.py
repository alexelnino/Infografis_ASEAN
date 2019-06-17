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

y = df['GNP'][df['Region'] == 'Southeast Asia']

colour = ['green', 'yellow', 'black', 'red', 'blue', 'cyan', 'grey', 'pink', 'brown', 'lightgreen', 'lightblue']
plt.style.use('ggplot')
plt.bar(x, y, color=colour)

plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xlabel('Negara')
plt.ylabel('Gross National Product(US$)')
plt.xticks(rotation = 45)
plt.subplots_adjust(
    left=0.20, bottom=0.20, right=0.80, top=0.90,
    wspace=.2, hspace=.2
    )
plt.show()