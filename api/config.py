# PUBLIC_DATA_SERVICE_KEY
PUBLIC_DATA_SERVICE_KEY = "Your-Public-Data-Service-Key"
PUBLIC_DATA_REQUEST_URL = "Your-data-request-url"
# Air Pollution
STATION = "Station-name"
# Google Drive API, credentials
import os
# Google Drive API, credentials
GOOGLE_SERVICE_KEY=os.path.abspath(os.path.dirname(__file__))+'/instance/pubapi.json'#다운받은 구글키 json 파일

GOOGLE_SPREADSHEET_NAME = 'publicdata' # 생성한 스프레드시트 파일 이름
GOOGLE_WORKSHEET = 'Sheet'#시트 이름

#FLASK MAIL
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "gmail id"
MAIL_PASSWORD = "gmail app password"

MAIL_SUBJECT_PREFIX = 'AirBOUT'
MAIL_SENDER = "sender@email.com"
ADMIN = 'admin@email.com'
SECRET_KEY='SECRET_KEY'

#Celery
CELERY_BROKER_URL="redis://localhost:6379"
# Simulation Parameter
SIMULATION_MODE = 'REAL_TIME'
CRAWLING_TIME = 5
TIME_DENSITY=1