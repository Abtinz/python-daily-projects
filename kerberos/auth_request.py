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