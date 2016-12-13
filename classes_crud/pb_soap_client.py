from pysimplesoap.client import SoapClient

client = SoapClient(
    location='http://127.0.0.1:8000',
    trace=True
)

print client.Add(a=1, b=2).res


"""

curl -X POST -H "Content-type: text/xml; charset='UTF-8'" -d '<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soap:Header/><soap:Body><Add xmlns="None"><a>1</a><b>2</b></Add></soap:Body></soap:Envelope>' http://127.0.0.1:8000

"""