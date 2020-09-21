import requests
import requests_ntlm
from lxml import html
import json

#URL = "http://velocity/"
URL = "http://velocity/review.asp?action=review&WorkOrder=35999&PartID=&QC=&PONum=&POLine="

def main():
    response = requests.get(URL, auth=requests_ntlm.HttpNtlmAuth('roberthartshorn', 'LaylaClapton3'))
    print(response.status_code)
   # print(response.content)
    
    doc = html.fromstring(response.content)
    # resultSet = doc.xpath('//head/title/table[@class="top"')
    resultSet = doc.xpath("//body//table[@class='toptab']//table//tr")
    print(resultSet)
  #/tr/tdtd/table
  
    #html.open_in_browser(doc) 
    #responseJSON = json.dumps(response.text)
    #print(responseJSON)

if __name__ == "__main__":
    main()
