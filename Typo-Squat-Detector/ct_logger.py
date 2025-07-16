import io

import requests

url = "https://crt.sh/json?q=com"
session = requests.session()


def get_ct_logs():
    logs = session.get(url)
    return logs.json()


def log_domains(crt_log_data: dict):
    file_obj = io.StringIO()
    domains = []

    for data in crt_log_data:
        domain = data.get('common_name')
        file_obj.write(f"{domain}\n")
        domains.append(domain)

    return domains, file_obj
