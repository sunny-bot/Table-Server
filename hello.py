import csv
import random

alphabeticalList = ['Ahmad, Daanish']

# read the namelist.csv
with open('/Users/sunnyzhao/Desktop/StudentList.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
            #add alphabeticalList entries
            alphabeticalList.append(f'{row["Ahmad"]}, {row["Daanish"]}')

#convert list of strings to a list of objects
listOfNames = list()
for i in alphabeticalList:
    listOfNames.append(i)

#shuffle any given list using a shallow copy to keep the objects the same
def shuffleObjects(copiedList):
    shuffledObjects = copiedList.copy()
    random.shuffle(shuffledObjects)
    return shuffledObjects

shuffledNames = shuffleObjects(listOfNames)

kitchenStaff = list()
waiters = list()
tableList = list()

for i in range(0,7):
    kitchenStaff.append(shuffledNames.pop(0))

for i in range(0,31):
    waiters.append(shuffledNames.pop(0))

for i in range(0,4):
    tableList.append(list())
    for x in range(0,9):
        tableList[i].append(shuffledNames.pop(0))

for i in range(0,27):
    tableList.append(list())
    for x in range(0,8):
        tableList[i+4].append(shuffledNames.pop(0))

print(shuffledNames)

#!/usr/bin/python3
# Framework for Simple http service with JSON reply
# John MacFarlane (2020)

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        requestPath = self.path

        #Log to us
        print(f'\n----- GET Request Start ----->\n')
        print(f'Request path: {requestPath}')
        print(f'Request headers:\n')
        for line in self.headers:
            print(f'  > {line}: {self.headers[line]}')
        print(f'\n<----- GET Request End -----\n')

        #Answer 200 => OK Status
        self.send_response(200)

        #Add Headers if any needed
        #self.send_header("Set-Cookie", "cate=true")
        self.end_headers()

        #Body of reply
        json_reply = json.dumps({'kitchenStaff':kitchenStaff, 'waiters':waiters, 'table1':tableList[0], 'table2':tableList[1], 'table3':tableList[2], 'table4':tableList[3], 'table5':tableList[4], 'table6':tableList[5], 'table7':tableList[6], 'table8':tableList[7], 'table9':tableList[8], 'table10':tableList[9], 'table11':tableList[10], 'table12':tableList[11], 'table13':tableList[12], 'table14':tableList[13], 'table15':tableList[14], 'table16':tableList[15], 'table17':tableList[16], 'table18':tableList[17], 'table19':tableList[18], 'table20':tableList[19], 'table21':tableList[20], 'table22':tableList[21], 'table23':tableList[22], 'table24':tableList[23], 'table25':tableList[24], 'table26':tableList[25], 'table27':tableList[26], 'table28':tableList[27], 'table29':tableList[28], 'table30':tableList[29], 'table31':tableList[30],})
        self.wfile.write(json_reply.encode(encoding='utf_8'))

# Listen on Port 80
port = 80
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
server.serve_forever()
