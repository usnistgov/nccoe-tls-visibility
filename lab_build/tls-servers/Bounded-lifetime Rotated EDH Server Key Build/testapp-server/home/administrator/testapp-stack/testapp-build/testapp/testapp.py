from flask import Flask
from flask_oidc import OpenIDConnect
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import session, request, redirect, url_for
import urllib
import os
import sys
import mysql.connector as db
from datetime import *
import random

app = Flask(__name__)
app.secret_key=b"<<sanitized>>"
print("Current python directory: %s" % os.getcwd() )
config={}
config['OIDC_CLIENT_SECRETS'] = './oidc-client-secret.txt'
config['SECRET_KEY'] = '<<sanitized>>'
config['OVERWRITE_REDIRECT_URI'] = "https://rk-testapp.visibility.nccoe.org/authorize"
config['OIDC_SCOPES'] = ['openid','profile','email']
app.config.update(config)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=2, x_host=2, x_proto=2)
oidc = OpenIDConnect(app)

db_config={}
db_config['DATABASE_SERVER'] = 'rk-mariadb.visibility.nccoe.org'
db_config['DATABASE_USER'] = 'testappuser'
db_config['DATABASE_PASSWORD'] = '<<sanitized>>'
db_config['DATABASE_NAME'] = 'testapp'

#SUPPORTED_CONTENT_TYPES = ['text/html','application/xhtml+xml','application/xml;q=0.9','image/avif','image/webp','image/apng','*/*;q=0.8','application/signed-exchange;v=b3;q=0.7']

#@app.before_request
#def check_accept_header():
#    if 'Accept' in request.headers:
#        accept_header = request.headers['Accept']
#        print(f"Accept header: {accept_header}")
#
#        #Split the accept header values by commas
#        accept_values = [value.strip() for value in accept_header.split(',')]
#
#        #Add the values to supported content types if not already present
#        for value in accept_values:
#            if value not in SUPPORTED_CONTENT_TYPES:
#                SUPPORTED_CONTENT_TYPES.append(value)
#                print(value)
#        #Check if any of the accept header values are unsupported
#        if not any(value in SUPPORTED_CONTENT_TYPES for value in accept_values):
#            return "Not Acceptable", 406

@app.route('/')
def index():
  if oidc.user_loggedin:
    info = oidc.user_getfield('given_name')
    return "Hello " + info + ", <a href='/signout'>sign out here</a><p><a href='/database'>Dashboard</a>"
  return "Hello anonymous, <a href='/login'>login</a>!"

@app.route('/login')
@oidc.require_login
def login():
  sys.exit()
  print("logged in...")
  return "Login achieved."

@app.route('/signout')
@oidc.require_login
def logout():
  print("logging out...")
  oidc.logout()
  #do something here to actually expire the session on keycloakcorp as well
  return "You have been logged out."

def get_db_connection():
  return db.connect( user = db_config['DATABASE_USER'],
                     password = db_config['DATABASE_PASSWORD'],
                     host = db_config['DATABASE_SERVER'],
                     database = db_config['DATABASE_NAME'],
                     tls_versions = ['TLSv1.3'])


@app.get('/database')
@oidc.require_login
def view_database():
  dbconn = get_db_connection()

  dbcursor = dbconn.cursor(buffered=True)

  insert_query = "INSERT INTO events (event, timestamp, ipaddress, username, random) values (%s, %s, %s, %s, %s)"
  data = ("AUTOLOG",
          datetime.now(timezone.utc),		#time of this request in UTC
          request.remote_addr,		    	#IP address of client
          oidc.user_getfield('given_name'),	#user name that they entered into keycloak
          random.randint(0,999) )		#just create some random number for no reason

  dbcursor.execute(insert_query, data)
  dbcursor.close()
  dbconn.commit()

  select_query = "SELECT event, ipaddress, username, count(*) as count FROM events GROUP BY event, ipaddress, username"

  dbcursor = dbconn.cursor(buffered=True)
  dbcursor.execute( select_query )
  dbcursor.close()
  dbconn.close()

  query_result_text = "<table><tr><td>Event</td><td>IP Address</td><td>User Name</td><td>Count</td></tr>"

  for (event, ipaddress, username, count) in dbcursor:
    query_result_text += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (event, ipaddress, username, str(count) )

  query_result_text += "</table>"

  query_result_text += "<br/><form action='/database' method='GET'><button>Refresh</button></form>"
  query_result_text += "<form action='/database' method='POST'><button>Manual Log</button></form>"

  return query_result_text

@app.post('/database')
@oidc.require_login
def update_database():
  dbconn = get_db_connection()
  dbcursor = dbconn.cursor(buffered=True)

  insert_query = "INSERT INTO events (event, timestamp, ipaddress, username, random) values (%s, %s, %s, %s, %s)"

  data = ("MANUALLOG",
          datetime.now(timezone.utc),		#time of this request in UTC
          request.remote_addr,		    	#IP address of client
          oidc.user_getfield('given_name'),	#user name that they entered into keycloak
          random.randint(0,999) )		#just create some random number for no reason

  dbcursor.execute(insert_query, data)
  dbcursor.close()
  dbconn.commit()
  dbconn.close()


  return "Your manual log request has been successful.  Return to the dashboard <a href='/database'>here</a>"

@app.post('/cnc')
def cnc():
    return 'eyJoc3pBIjoiS2FqSnpnPT0ifQ=='
#    return '{"hszA":"KajJzg=="}'

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)






