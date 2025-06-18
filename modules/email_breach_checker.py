import requests

def check_breach(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": api_key, "user-agent": "osint-toolkit"}
    r = requests.get(url, headers=headers)
    return r.json() if r.status_code == 200 else "No breach found."
