#importing module for api 

import json
import requests
#defining country info to get the information about country and simultaneously printing the information 

def country_info(country_name):
	api_url=f"https://restcountries.com/v3.1/name/{country_name}"
	get_country_info=requests.get(api_url)
	data=get_country_info.json()
	#creating a loop to read data from the dictionary we have get in "data" 
	
	for country in data:
		if country.get("name",{}).get("common")==country_name:
			name=country ["name"]["common"]
			capital =country.get("capital",["N/A"])[0]
			region =country.get("region","N/A")
			latlng=country.get("latlng",[0,0])
			latitude=latlng[0]
			longitude=latlng[1]
			print("\n---COUNTRY INFORMATION---")
			print(f"Country : {name}")
			print(f"Capital : {capital}")
			print(f"Region : {region}")
			dashboard()
#defining weather to get the country real time temp and wind speed using api 

def weather(latitude,longitude,country_name):
	api_url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
	get_country_weather=requests.get(api_url)
	data=get_country_weather.json()
	temp=data["current_weather"]["temperature"]
	wind_speed=data["current_weather"]["windspeed"]
	print("\n---WEATHER REPORT---")
	print(f"Country : {country_name}")
	print(f"Temperature : {temp}°C")
	print(f"Wind Speed : {wind_speed}")
#defining exit to exit from the smart CLI Dashboard 

def exit():
	print("exiting dashboard...")
	print("Smart CLI Dashboard exited successfully ✅")
	print("Thanks  for Choosing Us🙏")
#defining dashboard to get user choice 

def dashboard():
	print("---SMART CLI DASHBOARD---")
	print("1. Country Information ")
	print('2. Country Weather')
	print("3. Exit")
	user_choice=int(input("Choose Option(1-3) : "))
	if user_choice==1:
		country_name=input("Enter country name : ")
		api_url=f"https://restcountries.com/v3.1/name/{country_name}"
		get_country_info=requests.get(api_url)
		data=get_country_info.json()
		for country in data:
			if country.get("name",{}).get("common")==country_name:
				latlng =country.get("latlng",[0,0])
				latitude =latlng[0]
				longitude =latlng[1]
			country_info(country_name)
	elif user_choice==2:
		country_name=input("Enter country name : ")
		api_url=f"https://restcountries.com/v3.1/name/{country_name}"
		get_country_info=requests.get(api_url)
		data=get_country_info.json()
		for country in data:
			if country.get("name",{}).get("common")==country_name:
				latlng =country.get("latlng",[0,0])
				latitude =latlng[0]
				longitude =latlng[1]
		weather(latitude,longitude,country_name)
	elif user_choice==3:
		exit()
	else:
		print("❌ No such Options available ")
		print("\ntry again")
		dashboard()
#calling the function dashboard	

dashboard()
