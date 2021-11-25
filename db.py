from app import app
from flaskext.mysql import MySQL
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'uxhfzmaewjqzxbrj'
#configMY['DEFAULT_MYSQL']['MYSQL_DATABASE_USER_DB']
app.config['MYSQL_DATABASE_PASSWORD'] = 'GBn0L8UIFXxRYooyhJIE'
#configMY['DEFAULT_MYSQL']['MYSQL_DATABASE_PASSWORD_DB']
app.config['MYSQL_DATABASE_DB'] = 'billfrqpmswhgyydyxcv'
#configMY['DEFAULT_MYSQL']['MYSQL_DATABASE_DB_DB']
app.config['MYSQL_DATABASE_HOST'] = 'billfrqpmswhgyydyxcv-mysql.services.clever-cloud.com'
#configMY['DEFAULT_MYSQL']['MYSQL_DATABASE_HOST_DB']
mysql.init_app(app)