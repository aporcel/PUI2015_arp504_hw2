import json
import sys
import urllib2
    
def main(key,busN):
    urlData = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (key,busN)
    #key = 42252389-44d7-48d7-8c7e-749b6c84c0e2
    webUrl = urllib2.urlopen(urlData)
    data = webUrl.read()
    jsonData = json.loads(data)
    vehicData = jsonData["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    print "Bus Line : %s" % (busN)
    print "Number of active buses : %s" % (str(len(vehicData)))
    cont = 0
    for v in vehicData:
        buslon = v["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"] 
        buslat = v["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        print "Bus %s is at latitude %s and longitude %s" % (str(cont),str(buslat),str(buslon))
        cont += 1

if __name__ == "__main__":
    main(str(sys.argv[1]),str(sys.argv[2]))   