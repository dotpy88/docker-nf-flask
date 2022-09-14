import os, requests
from flask import Flask, request, abort, render_template
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

load_dotenv()

app = Flask(__name__)

@app.route('/lookup-nfsen-host', methods=['GET'])
def nflookup():
    username = os.getenv('nde_username')
    password = os.getenv('nde_password')
    nde_api_url = os.getenv('nde_url')
    lookup = request.args.get('lookup')
    error = "Error returned from API"
    if not lookup: abort(404)
    try:
        response = requests.request('GET', nde_api_url + lookup, auth=HTTPBasicAuth(username,password),verify=False)
        resp = response.json().get('data')
        api_type = resp.get('api_type')
        if not api_type: return error
        return render_template(f'template-{api_type}.html',resp=resp)
    except Exception as e:
        return str(e)
 
if __name__ == '__main__':
   app.run()