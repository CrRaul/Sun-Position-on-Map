from math import *
from SunProprieties import *
import numpy as np
import cv2
from prettytable import PrettyTable


H,W = 500,500

# rotate the line((0,0),(0,R)) with angle in clockwise
def rotateLine(angle, R):
	y = -R
	xp = -y * sin(deg2rad(angle)) + H//2
	yp = y * cos(deg2rad(angle)) + H//2

	return [xp,yp]

def deg2rad(deg):
	return (deg*pi)/180
 

def drawSunriseSunset(sunProp, image):
	for i in range(len(sunProp)):
		if sunProp[i][0]=='sunrise' or sunProp[i][0] == 'sunset':
			point = rotateLine(sunProp[i][2],200)
			cv2.line(image,(int(point[0]),int(point[1])),(W//2,H//2),(0,255,255),2)

	return image


def drawAng(image):

	for i in range(0,360,10):
		point = rotateLine(i,200)
		cv2.line(image,(int(point[0]),int(point[1])),(W//2,H//2),(190,190,190),1)

		point = rotateLine(i,220)
		image = cv2.putText(image, str(i), (int(point[0])-10,int(point[1])), cv2.FONT_HERSHEY_SIMPLEX ,  0.5, (255,0,0), 1, cv2.LINE_AA) 

	return image


def main():
	s = SunProprieties()
	s.setLocation()
	s.sunProprieties()


	sunProp = s.getSunProp()

	t = PrettyTable(['event', 'altitude', 'azimuth','date'])
	for i in range(len(sunProp)):
		t.add_row([sunProp[i][0], sunProp[i][1], sunProp[i][2], sunProp[i][3]])
	print(t)


	image = cv2.imread("testImg.png")

	image = drawSunriseSunset(sunProp,image)
	image = drawAng(image)

	cv2.imshow("s", image)
	cv2.waitKey(0)


main()

'''



def createMap(myLoc, sunDet):
	# declare the center of the map, and how much we want the map zoomed in
	latitude = myLoc[0]
	longitude = myLoc[1]

	gmap = gmplot.GoogleMapPlotter(latitude, longitude, 10)

	ang = sunDet[0][2]
	
	latitude_list = [latitude,lat,latitude,]
	longitude_list = [longitude,lng,longitude,]

	gmap.plot(latitude_list, longitude_list,  
	           'cornflowerblue', edge_width = 5.5) 

	#Your Google_API_Key
	gmap.apikey = "AIzaSyA5bIGtytfmsQut59BDVUZI3-unyaD14SM"
	# save it to html
	gmap.draw(r"map.html")
'''




#mai bine striga 
#ion fara de tara
#mizantrop 
#structura nucleu evolutie
#glossa