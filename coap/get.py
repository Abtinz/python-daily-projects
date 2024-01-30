from coapthon.client.helperclient import HelperClient
from coapthon.resources.resource import Resource

host = "127.0.0.1"
port = 5683
path ="basic"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())

client.post(path, "Posted resource")
response = client.get(path)
print(response.pretty_print())

client.stop()
