import requests
import requests_ntlm
import os
from lxml import html
import json
import time

#URL = "http://velocity/"
jobURL = "http://velocity/review.asp?action=review&WorkOrder="
inspURL = "http://velocity/review.asp?action=review&QC="
dest = "/Users/roberthartshorn/Desktop/Inspection Exports/"
#jobsFile = dest + "jobslist.txt"
jobsFile = "/Users/roberthartshorn/Desktop/jobslist.txt"

def main():
  os.chdir(dest)

  with open(jobsFile, "r") as f:
    jobs = f.read()  

  for job in jobs.split(","): 
    resultSet = []
    print(job)
    response = requests.get(jobURL + job, auth=requests_ntlm.HttpNtlmAuth('inspectionmigrator', 'inspectionmigrator'))
    print(job)
    print(response.status_code)
    
    try:
      doc = html.fromstring(response.content)
      resultSet = doc.xpath("//body//table[@class='toptab']//table//tr//td/a")
    except:
      with open("log.txt", "a") as f:
        f.write(job + "\n")

    for count, x in enumerate(resultSet):
      resp = requests.get(inspURL + x.text, auth=requests_ntlm.HttpNtlmAuth('inspectionmigrator', 'inspectionmigrator'))
      filename = job + "." + str(count) + ".html"
      with open(filename, "wb") as f:
        f.write(resp.content)

    time.sleep(3)

if __name__ == "__main__":
    main()
