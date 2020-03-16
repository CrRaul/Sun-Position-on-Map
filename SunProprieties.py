from datetime import datetime, date
from pysolar.solar import *
import geocoder
import astral


class SunProprieties():
	def __init__(self):
		self.__location = None
		self.__sunDet = []

	def getSunProp(self):
		return self.__sunDet

	def setLocation(self):
		# get my location
		g = geocoder.ip('me')
		latitude = g.latlng[0]
		longitude = g.latlng[1]

		self.__location = [longitude,latitude]

	# get details about the sun(azimuth,altitude,time) at sunset, sunrise, noon, dusk, dawn
	def sunProprieties(self):
		sunDet = []

		loc = astral.Location(('altcv', 'cv', self.__location[0], self.__location[1], 'Europe/Bucharest', 510))
		for event, time in loc.sun(date.today()).items():
			altitude = get_altitude(self.__location[0],self.__location[1], time)
			azimuth = get_azimuth(self.__location[0], self.__location[1], time)
			sunDet.append([event,altitude,azimuth,time])
		
		sortedSunDet = sorted(
		sunDet,
    	key=lambda x: datetime.datetime.strptime(str(x[3]), '%Y-%m-%d %H:%M:%S+02:00'), reverse=False
		)
		self.__sunDet = sortedSunDet
