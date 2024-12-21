#copyright and documentation stem from: 
#   source: https://gist.github.com/krzysztofantczak/92094ea4eaf499a948d900c30411fc6f
#   source author:  Krzysztof Antczak 
# this code is just aim in learn and train py-kerb(no commercial use)
#pip install  pykerberos --user   

import requests
import pykerberos

##specifications and initial information will be saved in this class
class Kerb_Information():
    def __init__(self,url,username,password,realm,spn):
        self.url = url
        self.username = username
        self.password = password
        self.realm = realm
        self.spn = spn

kerb_Information = Kerb_Information(
    url= 'http:/ABTINZADNI81.org',
    username= 'abtinam',
    password = 'zandiam',
    realm = "abtin@REALM",
    spn = 'HTTP/ABTINZADNI81.org@REALM'
)    

kerberos_ticket = pykerberos.authGSSClientInit(kerb_Information.span)
kerberos_ticket = pykerberos.authGSSClientStep(kerberos_ticket, kerb_Information.username)
kerberos_ticket = pykerberos.authGSSClientStep(kerberos_ticket, kerb_Information.password)
kerberos_ticket = pykerberos.authGSSClientUnwrap(kerberos_ticket, '')

headers = {
    'Authorization': 'Negotiate ' + kerberos_ticket
}

try:

    response = requests.get(
    url=kerb_Information.url, 
    headers=headers
    )

    if response.status_code == 200:
        print("200! KCD message:", response.text)
    else:
        print("error occurred! Given code and error message:", response.status_code , response.text)

except Exception as error:
        print("500! Internal service error:", error)

