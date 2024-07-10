# Written by Jamie Sinclair-Eagle
import csv
with open("book1.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    f = open("new.csv", 'a')
    for row in csv_reader:
        # Get day and date for row
        dayDate = row[0].split()
        day = dayDate[0]
        date = dayDate[1]

        # Find out duty, name, service, team, reason
        for i in range(1, len(row)):
            if row[i] != "":
                temp = row[i].split(" - ")
                # Find duty
                if temp[0] == 'L':
                    duty = "ld"
                    temp = temp[1:]
                elif temp[0] == "N":
                    duty = "2200-0800"
                    temp = temp[1:]
                else:
                    duty = "0800-1600"
                
                # Find name                
                name = temp[0]
                # Find service, team and reason
                setr = temp[1].split()
                service = setr[0]
                team = ""
                if len(setr) == 2:
                    team = ""
                    reason = setr[1]
                elif len(setr) == 3:
                    team = setr[1]
                    reason = setr[2]
                
                # Change GM to General Medicine
                if service.upper() == "GM" or service.upper() == "GEN MED":
                    service = "General Medicine"
                elif service.upper() == "SPINAL":
                    service = "Spinal Rehab"
                    team = ""
                elif service.upper() == "AT&R":
                    service = "AT&R"
                # Change day to full name
                if day.upper() == "MON":
                    day = "Monday"
                elif day.upper() == "TUE":
                    day = "Tuesday"
                elif day.upper() == "WED":
                    day = "Wednesday"
                elif day.upper() == "THU":
                    day = "Thursday"
                elif day.upper() == "FRI":
                    day = "Friday"
                elif day.upper() == "SAT":
                    day = "Saturday"
                elif day.upper() == "SUN":
                    day = "Sunday"
                # Change Reason
                if reason == "(RDO)":
                    reason = "Roster Vacancy-RDO"
                elif reason == "(NR)":
                    reason = "Roster Vacancy-NR"
                elif reason == "(AL)":
                    reason = "Uncovered AL"
                elif reason == "(STIL)":
                    reason = "Uncovered STIL"

                if duty != "ld":
                    output = date + "," + day + "," + service + ","+ team + ",HO,no,"+duty + ","+name+","+ reason +",NA\n"
                else:
                    output = date + "," + day + "," + service + ","+ team + ",HO,no,"+ "0800-1600" + ","+name+","+ reason +",NA\n"
                    f.write(output)
                    output = date + "," + day + "," + service + ","+ team + ",HO,no,"+ "1600-2200" + ","+name+","+ reason +",NA\n"
                f.write(output)
f.write("\n")                
f.close()
csvfile.close()
    
                
            
        