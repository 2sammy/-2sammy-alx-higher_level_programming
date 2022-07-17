#lists are mutable
gradeDict ={"sam":90,"san":98,"manoah":97,"sharleen":80}
print(gradeDict)
print(gradeDict["sam"])
gradeDict["sam"] = 92
print(gradeDict)
gradeDict["noah"] = 86
del gradeDict['sharleen']

gradeDict ={"sam":[90,89],"san":[98,99],"manoah":[97,99],"sharleen":[80,90]}