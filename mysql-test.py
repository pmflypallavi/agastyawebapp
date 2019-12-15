from flask import Flask, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'custom-mysql.gamification.svc.cluster.local:3306'
app.config['MYSQL_USER'] = 'xxuser'
app.config['MYSQL_PASSWORD'] = 'welcome1'
app.config['MYSQL_DB']= 'sampledb'
mysql = MySQL(app)
@app.route('/input')
def employees():
    try:
        cur = mysql.connection.cursor()
        print(cur)
        res = cur.execute("SELECT ITEM_NUMBER, DESCRIPTION, LONG_DESCRIPTION FROM XXIBM_PRODUCT_STYLE LIMIT 10")
        print(res)
        if res > 0:
            userDetails = cur.fetchall()
            return render_template('employee.html',userDetails=userDetails)
        cur.close()
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    app.run()
