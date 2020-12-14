from django.shortcuts import render
# Create your views here.
import requests
import geopy.distance
import datetime
import json
from .forms import NearEarthObjects,GetLocation,GetDate
from . import nearbody

def home(request):

	return render(request,'nasa/landingpage.html')




def optionspage(request):

	return render(request,'nasa/optionspage.html')


def pictureoftheday(request):
	URL="https://api.nasa.gov/planetary/apod"
	datetimenow=datetime.datetime.now()
	day=datetimenow.strftime("%Y-%m-%d")
	PARAMS={'date':day,'hd':True,'api_key':'krjUmgl08IstU9xpSasgbqXuAkJMagbYz3Mve9U7'}

	response=requests.get(URL,PARAMS)
	data = response.json()
	print(data)
	code=data['code']
	if(code==404):
		return render(request,'nasa/nasapictureofthedayfail.html')
	else:
		displaydate=data['date']
		picture=data['url']
		explanation=data['explanation']
		return render(request,'nasa/pictureoftheday.html',{'displaydate':displaydate,'picture':picture,'explanation':explanation})




def nearearthobjects(request):
	form=NearEarthObjects()
	return render(request,'nasa/nearearthobjects.html',{'form':form})



def allmeteorlandings(request):
	URL="https://data.nasa.gov/resource/gh4g-9sfh.json"
	response=requests.get(URL)
	data = response.json()

	return render(request,'nasa/allmeteorlandings.html',{'data':data})


def getlocnearmeteor(request):
	form=GetLocation()
	return render(request,'nasa/getlocnearmeteor.html',{'form':form})


def marsroverpics(request):
	form=GetDate()

	return render(request,'nasa/marsroverpics.html',{'form':form})




def nearearthobjectsdisplay(request):

	if request.method=='POST':
		data = request.POST
		start_date=data['start_date']
		end_date=data['end_date']

		url="https://api.nasa.gov/neo/rest/v1/feed?start_date="+start_date+"&end_date="+end_date+"&api_key=krjUmgl08IstU9xpSasgbqXuAkJMagbYz3Mve9U7"

		response=requests.get(url)
		alldata=response.json()['near_earth_objects']
	
		kkeys=list(alldata.keys())
		kkeys.sort()
		b=[]
		for i in kkeys:
			for j in alldata[i]:
				b.append({'name':j['name'],'magnitude':j['absolute_magnitude_h'],'is_hazardous':j['is_potentially_hazardous_asteroid']})



		return render(request,'nasa/nearearthobjectsdisplayinfo.html',{'b':b})




def getlocationgivedata(request):
	if request.method=='POST':
		data1=request.POST
		latitude=float(data1['latitude'])
		longitude=float(data1['longitude'])
		URL="https://data.nasa.gov/resource/gh4g-9sfh.json"
		response=requests.get(URL)
		data = response.json()
		c=[]

		for i in nearbody.nearbodydata:
			c.append([i[0],geopy.distance.distance((latitude,longitude),(float(i[1]),float(i[2]))).km,i[-1],i[1],i[2]])
		d=sorted(c,key=lambda x:x[1])
		e=[]
		for i in range(5):
			e.append({'id':d[i][0],'name':d[i][2],'latitude':d[i][3],'longitude':d[i][4],'kms':d[i][1]})

		return render(request,'nasa/getlocationgivedata.html',{'data':e})



def getroverpics(request):
	if request.method=='POST':
		data=request.POST
		date=data['date']
		url="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="+date+"&api_key=krjUmgl08IstU9xpSasgbqXuAkJMagbYz3Mve9U7"
		response=requests.get(url)
		data=response.json()
		fulldata=data['photos']
		return render(request,'nasa/getroverpics.html',{'data':fulldata})