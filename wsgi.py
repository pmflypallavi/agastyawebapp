from flask import Flask, render_template,request
from flask_mysqldb import MySQL
application = Flask(__name__)

application.config['MYSQL_HOST'] = 'custom-mysql.gamification.svc.cluster.local'
application.config['MYSQL_USER'] = 'xxuser'
application.config['MYSQL_PASSWORD'] = 'welcome1'
application.config['MYSQL_DB']= 'sampledb'
mysql = MySQL(application)

@application.route('/')
def home():
    return render_template("home.html")

@application.route("/about", methods=['GET', 'POST'])
def about():
    try:
        cur = mysql.connection.cursor()
        res = cur.execute("SELECT DESCRIPTION FROM sampledb.XXIBM_PRODUCT_STYLE LIMIT 10")
        if res > 0:

            userDetails = cur.fetchall()
            product = list()
            Listprice = list()
            for i in range(len(userDetails)):
                product.append(userDetails[i][0])
            if request.method == 'POST':
                description = request.form.get('userDetails')
                price = cur.execute("select List_Price from sampledb.XXIBM_PRODUCT_PRICING where Item_Number in (select Item_Number  from sampledb.XXIBM_PRODUCT_SKU where Description=%s) and In_stock ='Yes' order by Price_Effective_Date desc limit 1",(description,))
                if price > 0:
                    Price = cur.fetchall()
                    Listprice = Price[0][0]

            return render_template('about.html', userDetails=product, Listprice=Listprice)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    application.run()
