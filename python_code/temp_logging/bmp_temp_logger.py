#!/usr/bin/python
#!/usr/bin/env

import smbus, time, os, urllib, urllib2
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()
thinkKey = 'AddKeyHere' # ---- Add your api key here ----
thinkUrl = 'https://api.thingspeak.com/update'

def sendData(url,key,field1,temp):

    values = {'key' : key,'field1' : temp}

    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)

    log = time.strftime("%d-%m-%Y\n%H:%M:%S\n")
    log = log + "{:.1f}C\n".format(temp)

    try:
        # Send data to Thingspeak
        response = urllib2.urlopen(req, None, 5)
        html_string = response.read()
        response.close()
        log = log + 'Update ' + html_string

    except urllib2.HTTPError, e:
        log = log + 'Server could not fulfill the request. Error code: ' + e.code
    except urllib2.URLError, e:
        log = log + 'Failed to reach server. Reason: ' + e.reason
    except:
        log = log + 'Unknown error'

    print log

if __name__=="__main__":
    temperature = sensor.read_temperature()
    sendData(thinkUrl,thinkKey,'field1',temperature)
    print "Inside temp - %0.1fC" % sensor.read_temperature()
