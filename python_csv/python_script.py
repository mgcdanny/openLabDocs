#this exercise takes two csv files and makes one long one
#we need to use some helpful modules
import csv
import os

#we are going to create a file called big_csv_file.csv
#so first, lets delete it if it already exists

try:
    os.remove("big_csv_file.csv")
except OSError:
    pass


file_list = []

#this will put all the fils in the current directory
#into the the_file list
for the_file in os.listdir('.'):
    if os.path.isfile(the_file):
        file_list.append(the_file)

#lets see what is in there
print(file_list)

#but we only want the .csv files
#lets cheat and just remove it by index
del file_list[2]
print(file_list)

#question 1
#try to figure a better way to get only the csv files into the list


#open a csv file, and call the opened file open_file
open_file = open("feb_purchases.csv", "rb")

#we can see the contents like this:
print(open_file.read())
#close the open file
open_file.close()

#ok lets just make the big file already:
big_csv_file = open("big_csv_file.csv","wb")
writer = csv.writer(big_csv_file)
is_first = True
for open_file in file_list:
    reader = csv.reader(open(open_file, 'rb'))
    if is_first:
        is_first = False
        for row in reader:
            writer.writerow(row)
    else:
        next(reader, None) #skip the header
        for row in reader:
            writer.writerow(row)
            
#close out the file we wrote to
big_csv_file.close()

