##copyright and documentation are stem from: https://pypi.org/project/requests-kerberos/
##request kerberos essential codes

import requests
from requests_kerberos import HTTPKerberosAuth
r = requests.get("https://abtinzandi81.org", auth=HTTPKerberosAuth())

##Password Authentication
import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
kerberos_auth = HTTPKerberosAuth(
        principal="abtin@REALM",
        password="14785487963/*/*/ccc",
    )
r = requests.get("http://abtinzandi81.org", auth=kerberos_auth)


##Delegation
import requests
from requests_kerberos import HTTPKerberosAuth
r = requests.get("http://abtinzandi81.org", auth=HTTPKerberosAuth(delegate=True))


__, krb_context = kerberos.authGSSClientInit("HTTP@krbhost.example.com")

kerberos.authGSSClientStep(krb_context, "")


negotiate_details = kerberos.authGSSClientResponse(krb_context)

headers = {"Authorization": "Negotiate " + negotiate_details}

r = requests.get("https://krbhost.example.com/krb/", headers=headers)

print(r.status_code , r.json)

