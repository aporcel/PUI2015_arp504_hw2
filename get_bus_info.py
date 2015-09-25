import json
import sys
import urllib2
import csv 
   
def main(key,busNo,fileNm):
    urlData = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (key,busNo)
    #key = 42252389-44d7-48d7-8c7e-749b6c84c0e2
    webUrl = urllib2.urlopen(urlData)
    data = webUrl.read()
    jsonData = json.loads(data)
    vehicData = jsonData["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    with open(fileNm, 'wb') as outBus:
        wBus = csv.writer(outBus)
        wBus.writerow(["Latitude","Longitude","Stop Name","Stop Status"])    
        for v in vehicData:
            buslon = v["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"] 
            buslat = v["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
            bussts = "N/A"
            busstn = "N/A"
            contst = 0
            for StopData in v["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]:
                bussts = StopData["Extensions"]["Distances"]["PresentableDistance"]
                busstn = StopData["StopPointName"] 
                if bussts == "approaching" or bussts == "1 stop away" or bussts == "< 1 stop away" or bussts == "at stop":
                    wBus.writerow([buslat,buslon,busstn,bussts])
                    contst += 1
            if contst == 0:
                bussts = "N/A"
                busstn = "N/A"
                wBus.writerow([buslat,buslon,busstn,bussts])

if __name__ == "__main__":
    main(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))   