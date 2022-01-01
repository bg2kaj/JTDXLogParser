#JTDX Log Parser - BG2KAJ
#v 0.1
#2022 01 01 HNY!
#Feel free to modify and distribute, If you can see this line of comment.
#I create this script to dig a little bit deeper into JTDX logs so it's only for my own purpose.

import time
import json
import sys

def call_pfx_parse(input_callsign):
	num_detected=0
	for x in input_callsign:
		if(ord(x)-48>=0)and (ord(x)-48<=9):
			num_detected+=1
	return num_detected

def main():
#print titles
	print ("==================================================================")
	print ("JTDX Runtime Log parser By BG2KAJ")
	print ("This is a simple script to parse JTDX 20xxxx_ALL.txt file and generate several useful log summaries.")
	print ("Only used by radio amateurs. STILL UNDER DEVELOPMENT.")
	print ("==================================================================")
	print ("Copyright informations:")
	print ("BigCty file is a work of AD1C Jim Reisert.")
	print ("datparse.py is based on work of classabbyamp, Distribute with MIT licence.")
	print ("Inspired by PyHamTools and other WSJT-X / JTDX related tools.")
#init vars
#Continent counter
	cEU_counter=0
	cAS_counter=0
	cAF_counter=0
	cNA_counter=0
	cSA_counter=0
	cOC_counter=0
	cOther_counter=0

#Band counter
	bVLF=0
	b160=0
	b80=0
	b60=0
	b40=0
	b30=0
	b20=0
	b17=0
	b15=0
	b12=0
	b10=0
	b6=0

#date counter
	day_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#hour counter
	hour_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	line_read_in_counter=0
	last_day=1
	last_hour=0
	now_band=40
	

	print ("==================================================================")
	print (" ")
#open log file.
	try:
		input_log_file = open(str(sys.argv[1]))
	except:
		print("Input file name invalid or corrupted.")
		print("Usage: JLP.py <your log file name.txt>")
		sys.exit()
#open result file
	output_file_name="summary_of_"+input_log_file.name
	output_result_file=open(output_file_name,'w+')
	output_result_file.write("JTDX Log Parser Summary File\n")
	output_result_file.write("Result for file:"+input_log_file.name+"\n")
	process_time_start=time.time()
	localtime=time.asctime(time.localtime(time.time()))
	output_result_file.write("Task starts at :"+localtime+".\n")
	print ("Log file : "+input_log_file.name+" open successfully.")
	print ("Task starts at : "+localtime)
	output_result_file.write("\n")

#open database file created by datparse.py
	try:
		Lib_file=open("cty.json",'r')
		for line in Lib_file.readlines():
			json_data=json.loads(line)
	except:
		print("cty.json missing or corrupted. Run datparse.py to generate a new one from cty.dat.")
		sys.exit()

#read in a line and start parse
	line_present=input_log_file.readline()

	while line_present:
	#	print (line_present)
		line_read_in_counter=line_read_in_counter+1
		line_parsed=line_present.split(" ")
		print (line_parsed[0]+" ")

#check log entry time 
		date_time=line_parsed[0]
		date_time_parsed=date_time.split("_")
		year=int((date_time_parsed[0])[0:4])
		month=int((date_time_parsed[0])[4:6])
		day=int((date_time_parsed[0])[6:8])

#get log entry hour
		hour=int((date_time_parsed[1])[0:2])
		if(last_hour!=hour):
			output_result_file.write("Day %d-%d-%d Hour %d detailed report:\n" %(year,month,last_day,last_hour))
			output_result_file.write("AF: %d AS: %d EU: %d NA: %d SA: %d OC: %d \n" %(cAF_counter,cAS_counter,cEU_counter,cNA_counter,cSA_counter,cOC_counter))
			cEU_counter=0
			cAS_counter=0
			cAF_counter=0
			cNA_counter=0
			cSA_counter=0
			cOC_counter=0
			cOther_counter=0
			output_result_file.write("160m: %d 80m: %d 60m: %d 40m: %d 30m: %d 20m: %d 17m: %d 15m: %d 12m: %d 10m: %d 6m: %d \n" %(b160,b80,b60,b40,b30,b20,b17,b15,b12,b10,b6))
			bVLF=0
			b160=0
			b80=0
			b60=0
			b40=0
			b30=0
			b20=0
			b17=0
			b15=0
			b12=0
			b10=0
			b6=0
			last_hour=hour
#get log entry day
		if(last_day!=day):
			output_result_file.write("Day %d-%d-%d Daily detailed report:\n" %(year,month,last_day))
			output_result_file.write(str(hour_counter))
			output_result_file.write("\n")
			hour_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			last_day=day
			output_result_file.write("\n")

#parse log item
		if("CQ" in line_parsed): #CQ
			if("Transmitting" in line_parsed):
				print("CQ from Myself")#own CQ
			else:	#other's CQ
				if(len(line_parsed[(line_parsed.index("CQ")+1)])==2):
					print("CQ from "+line_parsed[(line_parsed.index("CQ")+2)])
					callsign_out=line_parsed[(line_parsed.index("CQ")+2)]
				else:
					print("CQ from "+line_parsed[(line_parsed.index("CQ")+1)])
					callsign_out=line_parsed[(line_parsed.index("CQ")+1)]
				try:
					sub_data=json.dumps(json_data[callsign_out[0:2]])
					sub_data_parsed=json.loads(sub_data)
					print ("Continent from :"+ sub_data_parsed['continent'])
					if(sub_data_parsed['continent']=="AS"):
						cAS_counter+=1
					elif(sub_data_parsed['continent']=="EU"):
						cEU_counter+=1
					elif(sub_data_parsed['continent']=="AF"):
						cAF_counter+=1
					elif(sub_data_parsed['continent']=="NA"):
						cNA_counter+=1
					elif(sub_data_parsed['continent']=="SA"):
						cSA_counter+=1
					elif(sub_data_parsed['continent']=="OC"):
						cOC_counter+=1
					elif(sub_data_parsed['continent']=="EU"):
						cEU_counter+=1
				except:
					try:
						sub_data=json.dumps(json_data[callsign_out[0:3]])
						sub_data_parsed=json.loads(sub_data)
						print ("Continent from :"+ sub_data_parsed['continent'])
						if(sub_data_parsed['continent']=="AS"):
							cAS_counter+=1
						elif(sub_data_parsed['continent']=="EU"):
							cEU_counter+=1
						elif(sub_data_parsed['continent']=="AF"):
							cAF_counter+=1
						elif(sub_data_parsed['continent']=="NA"):
							cNA_counter+=1
						elif(sub_data_parsed['continent']=="SA"):
							cSA_counter+=1
						elif(sub_data_parsed['continent']=="OC"):
							cOC_counter+=1
						elif(sub_data_parsed['continent']=="EU"):
							cEU_counter+=1
					except:
						try:
							sub_data=json.dumps(json_data[callsign_out])
							sub_data_parsed=json.loads(sub_data)
							print ("Continent from :"+ sub_data_parsed['continent'])
							if(sub_data_parsed['continent']=="AS"):
								cAS_counter+=1
							elif(sub_data_parsed['continent']=="EU"):
								cEU_counter+=1
							elif(sub_data_parsed['continent']=="AF"):
								cAF_counter+=1
							elif(sub_data_parsed['continent']=="NA"):
								cNA_counter+=1
							elif(sub_data_parsed['continent']=="SA"):
								cSA_counter+=1
							elif(sub_data_parsed['continent']=="OC"):
								cOC_counter+=1
							elif(sub_data_parsed['continent']=="EU"):
								cEU_counter+=1

						except:
							print("Callsign "+callsign_out+"look up failed.")

				if(now_band==160):
					b160+=1
				elif(now_band==80):
					b80+=1
				elif(now_band==60):
					b60+=1
				elif(now_band==40):
					b40+=1
				elif(now_band==30):
					b30+=1
				elif(now_band==20):
					b20+=1
				elif(now_band==17):
					b17+=1
				elif(now_band==15):
					b15+=1
				elif(now_band==12):
					b12+=1
				elif(now_band==10):
					b10+=1
				elif(now_band==6):
					b6+=1

				day_counter[day-1]+=1
				hour_counter[hour]+=1
				
		else:
			if(("MHz" in line_parsed) and (("FT8\n" in line_parsed) or ("JT65\n" in line_parsed))):	
#			if("MHz" in line_parsed):	#change band
				print ("Freq. changed to "+line_parsed[2])
				try:
					freq_parsed=float(line_parsed[2])
					if(freq_parsed>1.8)and(freq_parsed<2):
						now_band=160
					elif(freq_parsed>3.5)and(freq_parsed<4):
						now_band=80
					elif(freq_parsed>5)and(freq_parsed<5.5):
						now_band=60
					elif(freq_parsed>7)and(freq_parsed<7.3):
						now_band=40
					elif(freq_parsed>10.1)and(freq_parsed<10.15):
						now_band=30
					elif(freq_parsed>14)and(freq_parsed<14.4):
						now_band=20
					elif(freq_parsed>18)and(freq_parsed<18.2):
						now_band=17
					elif(freq_parsed>21)and(freq_parsed<21.5):
						now_band=15
					elif(freq_parsed>24.8)and(freq_parsed<24.9):
						now_band=12
					elif(freq_parsed>28)and(freq_parsed<30):
						now_band=10
					elif(freq_parsed>50)and(freq_parsed<54):
						now_band=6
				except:
					print("Band parse failed.")
			else:
				if("QSO" in line_parsed):
					print ("A QSO Logged.")
				else:
					if("loss" in line_parsed):
						print ("Audio loss detected.")
					else:
						try:	#other's QSO
							print("QSO: "+line_parsed[(line_parsed.index("~")+1)]+" <> "+line_parsed[(line_parsed.index("~")+2)])
							callsign_out=line_parsed[(line_parsed.index("~")+2)]
							try:
								sub_data=json.dumps(json_data[callsign_out[0:2]])
								sub_data_parsed=json.loads(sub_data)
								print ("Continent from :"+ sub_data_parsed['continent'])
								if(sub_data_parsed['continent']=="AS"):
									cAS_counter+=1
								elif(sub_data_parsed['continent']=="EU"):
									cEU_counter+=1
								elif(sub_data_parsed['continent']=="AF"):
									cAF_counter+=1
								elif(sub_data_parsed['continent']=="NA"):
									cNA_counter+=1
								elif(sub_data_parsed['continent']=="SA"):
									cSA_counter+=1
								elif(sub_data_parsed['continent']=="OC"):
									cOC_counter+=1
								elif(sub_data_parsed['continent']=="EU"):
									cEU_counter+=1

							except:
								try:
									sub_data=json.dumps(json_data[callsign_out[0:3]])
									sub_data_parsed=json.loads(sub_data)
									print ("Continent from :"+ sub_data_parsed['continent'])
									if(sub_data_parsed['continent']=="AS"):
										cAS_counter+=1
									elif(sub_data_parsed['continent']=="EU"):
										cEU_counter+=1
									elif(sub_data_parsed['continent']=="AF"):
										cAF_counter+=1
									elif(sub_data_parsed['continent']=="NA"):
										cNA_counter+=1
									elif(sub_data_parsed['continent']=="SA"):
										cSA_counter+=1
									elif(sub_data_parsed['continent']=="OC"):
										cOC_counter+=1
									elif(sub_data_parsed['continent']=="EU"):
										cEU_counter+=1

								except:
									try:
										sub_data=json.dumps(json_data[callsign_out])
										sub_data_parsed=json.loads(sub_data)
										print ("Continent from :"+ sub_data_parsed['continent'])
										if(sub_data_parsed['continent']=="AS"):
											cAS_counter+=1
										elif(sub_data_parsed['continent']=="EU"):
											cEU_counter+=1
										elif(sub_data_parsed['continent']=="AF"):
											cAF_counter+=1
										elif(sub_data_parsed['continent']=="NA"):
											cNA_counter+=1
										elif(sub_data_parsed['continent']=="SA"):
											cSA_counter+=1
										elif(sub_data_parsed['continent']=="OC"):
											cOC_counter+=1
										elif(sub_data_parsed['continent']=="EU"):
											cEU_counter+=1

									except:
										print("Callsign "+callsign_out+"look up failed.")
							day_counter[day-1]+=1
							hour_counter[hour]+=1
							if(now_band==160):
								b160+=1
							elif(now_band==80):
								b80+=1
							elif(now_band==60):
								b60+=1
							elif(now_band==40):
								b40+=1
							elif(now_band==30):
								b30+=1
							elif(now_band==20):
								b20+=1
							elif(now_band==17):
								b17+=1
							elif(now_band==15):
								b15+=1
							elif(now_band==12):
								b12+=1
							elif(now_band==10):
								b10+=1
							elif(now_band==6):
								b6+=1
						except:
							print("Line %d parsed failed." %line_read_in_counter)

		print (" ")
		line_present=input_log_file.readline()

	output_result_file.write("Day %d %d %d Hour %d detailed report:\n" %(year,month,last_day,last_hour))
	output_result_file.write("AF:%d AS:%d EU:%d NA:%d SA:%d OC:%d \n" %(cAF_counter,cAS_counter,cEU_counter,cNA_counter,cSA_counter,cOC_counter))
	cEU_counter=0
	cAS_counter=0
	cAF_counter=0
	cNA_counter=0
	cSA_counter=0
	cOC_counter=0
	cOther_counter=0
	output_result_file.write("160m: %d 80m: %d 60m: %d 40m: %d 30m: %d 20m: %d 17m: %d 15m: %d 12m: %d 10m: %d 6m: %d \n" %(b160,b80,b60,b40,b30,b20,b17,b15,b12,b10,b6))
	bVLF=0
	b160=0
	b80=0
	b60=0
	b40=0
	b30=0
	b20=0
	b17=0
	b15=0
	b12=0
	b10=0
	b6=0
#output a hour base output
	output_result_file.write("Day %d %d %d Hour detailed report:\n" %(year,month,last_day))
	output_result_file.write(str(hour_counter))
	output_result_file.write("\n")
	hour_counter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#output month base output
	output_result_file.write("\n")
	output_result_file.write("Month %d Total report:\n" %(month))
	output_result_file.write(str(day_counter))
#output last lines
	process_time_end=time.time()
	print ("File read in complete, in total %d records imported." %line_read_in_counter)
	output_result_file.write("\nProcess took %d seconds to complete.\n" %(process_time_end-process_time_start))
	output_result_file.write("In total %d lines of record were imported." %line_read_in_counter)
#close file
	input_log_file.close()
	output_result_file.close()
	sys.exit()


if __name__ == '__main__':
	main()