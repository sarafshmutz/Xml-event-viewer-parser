#!/usr/bin/env python3 
#import xml.dom.minidom as XP
from bs4 import BeautifulSoup

def xml_parse(file):
  string=""
  dict1={}
  count=0
  for line in file.readlines():
    string+=line
    if "</Event>" in line:
       #print(string)
       
       soup = BeautifulSoup(string, 'xml')
       data = soup.find_all('Data')
       for tag_name in data:
         dict1[tag_name.get('Name')]=tag_name.text
       #print(dict1)
       if 'SourceIp' in dict1.keys():
        # print(dict1)
         count+=1
         print(str(count)+"."+"ip src: "+dict1['SourceIp']+" ip dst: "+dict1['DestinationIp']+" user: "+dict1['User']+" host_dest: "+ dict1['DestinationHostname'] +" host_src: "+ dict1['SourceHostname'])
       dict1={}
       string=" "   
 # print(dict1)
       

  
def main():

  with open("./1.xml") as file:
    xml_parse(file)

main()
