import whois
import shodan

def whois_domain(domain):
    return whois.whois(domain)

def geo_ip(ip, shodan_api_key):
    api = shodan.Shodan(shodan_api_key)
    return api.host(ip)
