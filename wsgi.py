from flask import Flask, render_template
from flask_mysqldb import MySQL
application = Flask(__name__)
application.config['MYSQL_HOST'] = 'custom-mysql.gamification.svc.cluster.local'
application.config['MYSQL_USER'] = 'xxuser'
application.config['MYSQL_PASSWORD'] = 'welcome1'
application.config['MYSQL_DB']= 'sampledb'
mysql = MySQL(application)
@app.route('/')
def employees():
    try:
        cur = mysql.connection.cursor()
        print(cur)
        res = cur.execute("SELECT ITEM_NUMBER, DESCRIPTION, LONG_DESCRIPTION FROM sampledb.XXIBM_PRODUCT_STYLE LIMIT 10")
        print(res)
        if res > 0:
            userDetails = cur.fetchall()
            return render_template('employee.html',userDetails=userDetails)
        cur.close()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    application.run()
