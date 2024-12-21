##copyright and documentation are stem from: https://pypi.org/project/requests-kerberos/
##request kerberos essential codes

import requests
from requests_kerberos import HTTPKerberosAuth

##HTTPKerberosAuth
r = requests.get("https://abtinzandi81.org", auth=HTTPKerberosAuth())

##Password Authentication
kerberos_auth = HTTPKerberosAuth(
        principal="abtin@REALM",
        password="14785487963/*/*/ccc",
    )
r = requests.get("http://abtinzandi81.org", auth=kerberos_auth)


##Delegation
r = requests.get("http://abtinzandi81.org", auth=HTTPKerberosAuth(delegate=True))