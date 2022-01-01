import ctyparser
import time

print (" ")
print ("datparse.py")
print ("===========")
print ("Starting BigCty Database conversion...")
print ("Please make sure the BigCty file (cty.dat) is up to date.")
print ("Download latest file at https://www.country-files.com/category/big-cty/ ")
print ("This is a part of JTDXLogParser, Make sure run this program first if no cty.json file is present.")
print ("Based on cytparser by classabbyamp, 0x5c. Distribute with MIT licence.")
print (" ")

time.sleep(5)

cty=ctyparser.BigCty()
try:
	cty.import_dat("cty.dat")
except IOError:
	print ("Missing cty.dat file. Program aborted.")
else:
	print ("Generating cty.json files, Stand by.")
	cty.dump("cty.json")
	print ("cty.json file created. Program now will exit.")
	time.sleep(5)
	exit()