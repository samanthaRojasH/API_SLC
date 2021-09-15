from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'uxhfzmaewjqzxbrj'
app.config['MYSQL_DATABASE_PASSWORD'] = 'GBn0L8UIFXxRYooyhJIE'
app.config['MYSQL_DATABASE_DB'] = 'billfrqpmswhgyydyxcv'
app.config['MYSQL_DATABASE_HOST'] = 'billfrqpmswhgyydyxcv-mysql.services.clever-cloud.com'
mysql.init_app(app)