#make a file unique(remove duplicates ignoring some punctuations like ,.')
import sys
import re

#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

unique_dict = {}

for line in lines:
	if(line == ""):
		continue	

	#remove extra spaces
	line = re.sub(r'^ *',"", line, flags = re.MULTILINE)
	line = re.sub(r' *$',"", line, flags = re.MULTILINE)
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)

	line = re.sub(r'[,\'\.]', '', line, flags = re.MULTILINE)

	unique_dict[line] = 1


for key in unique_dict:
	print(key)