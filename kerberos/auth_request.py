import requests
from requests_kerberos import HTTPKerberosAuth
r = requests.get("https://krbhost.example.com/krb", auth=HTTPKerberosAuth())

##Password Authentication
import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED
kerberos_auth = HTTPKerberosAuth(
        principal="abtin@REALM",
        password="14785487963/*/*/ccc",
    )
r = requests.get("http://example.org", auth=kerberos_auth)
