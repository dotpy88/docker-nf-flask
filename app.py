import os, requests
from flask import Flask, request, abort
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

load_dotenv()

app = Flask(__name__)

@app.route('/lookup-nfsen-host', methods=['GET'])
def nflookup():
    username = os.getenv('nde_username')
    password = os.getenv('nde_password')
    nde_api_url = 'https://nde.its.vanderbilt.edu/api/lookup-nfsen-host.py?ipaddress='
    lookup = request.args.get('lookup')
    if not lookup: abort(404)
    try:
        response = requests.request('GET', nde_api_url + lookup, auth=HTTPBasicAuth(username,password),verify=False)
        return response.json()
    except Exception as e:
        return str(e)
 
if __name__ == '__main__':
   app.run()