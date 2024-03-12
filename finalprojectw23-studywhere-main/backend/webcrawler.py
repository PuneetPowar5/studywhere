import math
import requests
from bs4 import BeautifulSoup
import json

# OPTIONS request
options_url = "https://api.easi.utoronto.ca/ttb/getPageableCourses"
options_header = {
    "Host": "api.easi.utoronto.ca",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Access-Control-Request-Method": "POST",
    "Access-Control-Request-Headers": "content-type",
    "Referer": "https://ttb.utoronto.ca/",
    "Origin": "https://ttb.utoronto.ca",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site"
}

options_response = requests.options(options_url, headers=options_header)

# POST request
post_url = "https://api.easi.utoronto.ca/ttb/getPageableCourses"
post_header = {
    "Host": "api.easi.utoronto.ca",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Content-Length": "360",
    "Origin": "https://ttb.utoronto.ca",
    "Connection": "keep-alive",
    "Referer": "https://ttb.utoronto.ca/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site"
}


post_data = {"courseCodeAndTitleProps":{"courseCode":"","courseTitle":"","courseSectionCode":""},"departmentProps":[],"campuses":[],"sessions":["20229","20231","20229-20231"],"requirementProps":[],"instructor":"","courseLevels":[],"deliveryModes":[],"dayPreferences":[],"timePreferences":[],"divisions":["ERIN"],"creditWeights":[],"page":1,"pageSize":10,"direction":"asc"}
post_response = requests.post(post_url, headers=post_header, json=post_data, stream=True)

data = post_response.json() 

numCourses = data['payload']['pageableCourse']['total']
pageSize = data['payload']['pageableCourse']['pageSize']

output = {}

for inc in range(numCourses):
    print(f"{inc}/{numCourses}")
    post_data = {"courseCodeAndTitleProps":{"courseCode":"","courseTitle":"","courseSectionCode":""},"departmentProps":[],"campuses":[],"sessions":["20229","20231","20229-20231"],"requirementProps":[],"instructor":"","courseLevels":[],"deliveryModes":[],"dayPreferences":[],"timePreferences":[],"divisions":["ERIN"],"creditWeights":[],"page":inc,"pageSize":1,"direction":"asc"}
    post_response = requests.post(post_url, headers=post_header, json=post_data)
    
    courses = (post_response.json())['payload']['pageableCourse']['courses']
    for c in courses:
        for i in c["sections"]:
            for j in i["meetingTimes"]:
                name = c["name"]
                code = c["code"]
                b = j["building"]
                building_code = b['buildingCode']
                room_num = b['buildingRoomNumber']
                day = j['start']['day']
                start_time = j['start']['millisofday'] / 3600000
                end_time = j['end']['millisofday'] / 3600000
                
                if inc not in output:
                    output[inc] = {}
                    output[inc]['BuildingName'] = ''
                    output[inc]['RoomNumber'] = ''
                    output[inc]['classCode'] = ''
                    output[inc]['Day'] = 0
                    output[inc]['Time'] = ()
                
                if building_code not in output[inc]['BuildingName']:
                    output[inc]['BuildingName'] = building_code
                    
                if room_num not in output[inc]['RoomNumber']:
                    output[inc]['RoomNumber'] = room_num
                
                if code not in output[inc]['classCode']:
                    output[inc]['classCode'] = code
                    print(code)
                    
                if day != output[inc]['Day']:
                    output[inc]['Day'] = day
                
                timeframe = (start_time, end_time)
                if timeframe not in output[inc]['Time']:
                    output[inc]['Time'] = timeframe
                
                
                # check if building in dict
                #if building_code not in output:
                    #output[building_code] = {}
                
                # check if room number in building_code
                #if room_num not in output[building_code]:
                   #output[building_code][room_num] = {}
                
    
                # check if day in building_code->room_num
                #if day not in output[building_code][room_num]:
                    #output[building_code][room_num][day] = {}
                    
                #code_with_name = name + "-" + code 
                #check if course code in building_Code ->room_num->day
                #if code_with_name not in output[building_code][room_num][day]:
                    #output[building_code][room_num][day][code_with_name]=[]
                
                # time in use for building_code->room_num->day->course code->time
                #timeslot = (start_time, end_time)
                #if timeslot not in output[building_code][room_num][day][code_with_name]:
                    #output[building_code][room_num][day][code_with_name].append(timeslot)

with open("out.json", "w+") as outfile:
    json.dump(output, outfile)
 