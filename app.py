from flask import Flask, request, jsonify
from modules import username_checker, email_breach_checker, whois_lookup, metadata_extractor
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to OSINT Toolkit API"})

@app.route('/api/username-check', methods=['POST'])
def username_check():
    data = request.jsonpy 
    username = data.get('username')
    if not username:
        return jsonify({"error": "username required"}), 400
    result = username_checker.check_username(username)
    return jsonify(result)

@app.route('/api/email-breach', methods=['POST'])
def email_breach():
    data = request.json
    email = data.get('email')
    api_key = data.get('api_key')
    if not email or not api_key:
        return jsonify({"error": "email and api_key required"}), 400
    result = email_breach_checker.check_breach(email, api_key)
    return jsonify(result)

@app.route('/api/whois', methods=['POST'])
def whois_lookup_route():
    data = request.json
    domain = data.get('domain')
    shodan_key = data.get('shodan_key')
    result = {}
    try:
        result['whois'] = whois_lookup.whois_domain(domain)
    except Exception as e:
        result['whois'] = f"Error: {str(e)}"
    if shodan_key:
        try:
            result['shodan'] = whois_lookup.geo_ip(domain, shodan_key)
        except Exception as e:
            result['shodan'] = f"Error: {str(e)}"
    return jsonify(result)

@app.route('/api/metadata-extract', methods=['POST'])
def metadata_extract():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    result = metadata_extractor.extract_metadata(filepath)
    return jsonify({"metadata": result})

if __name__ == '__main__':
    app.run(debug=True)
