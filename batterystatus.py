import os
import time
import tkinter
import tkinter.messagebox


def main():
	while True:
		capacity = readCapacity()
		Charging = isCharging()
		if capacity < 40 and Charging==False:
			notify();
		time.sleep(1000)					


def readCapacity():
	searchValue="POWER_SUPPLY_CAPACITY" 
	with open("/sys/class/power_supply/BAT0/uevent") as status:
		for line in status:
			if line.split("=")[0]==searchValue:
				capacity = line.split("=")[1]				
		return int(capacity)


def isCharging():
	searchValue="POWER_SUPPLY_STATUS"
	with open("/sys/class/power_supply/BAT0/uevent") as status:
		for line in status:
			if line.split("=")[0]==searchValue:
				supplyStatus=line.split("=")[1]
	supplyStatus= supplyStatus.strip()			
	if supplyStatus=="Charging":
			return True		
	else:
		return False	


def notify():
	root=tkinter.Tk()
	root.withdraw()
	root.after(60000,suspend)
	tkinter.messagebox.showwarning("Warning", "Your computer is about to suspend")


def suspend():
	if isCharging()==False:
		os.system("systemctl suspend")

if __name__ == "__main__":
	main()