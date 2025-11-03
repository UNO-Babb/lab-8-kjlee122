#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  def makeID(first, last, idNum):
    idLen = len(idNum)
    while len(last) < 5:
      last = last + "X"
    id = first[0] + last + idNum[idLen - 3: ]
    #print(id)
    return id
  def getMajor(major):
    majorAbrv = major[0:3]
    return majorAbrv
  def getYear(year):
    if year == "Freshman":
      yearAbrv = "FR"
    elif year == "Sophomore":
      yearAbrv = "SO"
    elif year == "Junior":
      yearAbrv = "JR"
    else:
      yearAbrv = "SR"
    return yearAbrv





  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]
    #print(data)
    student_id = makeID(first, last, idNum)
    student_major = getMajor(major)
    student_year = getYear(year)
    output = last + "," + first + "," + student_id + "," + student_major + "-" + student_year + "\n"
    outFile.write(output)
  




  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
