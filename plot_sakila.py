# plot_sakila.py

import matplotlib.pyplot as plt
import argparse
import pymysql

ap = argparse.ArgumentParser()
ap.add_argument("-y", "--year", required = True, help = "Year to be plotted.")
args = vars(ap.parse_args())


db = pymysql.connect("192.168.121.14", "python", "axtelpython", "sakila")
cursor = db.cursor()


sql = """SELECT SUM(amount), MONTHNAME(payment_date), YEAR(payment_date)
FROM payment
WHERE YEAR(payment_date) = {}
GROUP BY 2, 3
ORDER BY 3, 2 DESC;
""".format(args["year"])

cursor.execute(sql)
data = cursor.fetchall()
db.close()

for row in data:
	print("Year: {:5}   Month:{:2}   Profit: {:10}".format(row[2], row[1], row[0]))


months = []
profit = []
for row in data:
	months.append(row[1])
	profit.append(row[0])

bar = plt.bar(months, profit, color = 'r')
plt.show()