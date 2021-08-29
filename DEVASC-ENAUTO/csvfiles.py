import csv

print("Please add a new router to the list")
hostname = input("What is the hostname? ")
ip = input("What is the IP? ")
location = input("What is the location? ")

router = [hostname, ip, location]

print(router)


with open("routerlist.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)


with open("routerlist.csv") as data:
    csv_list = csv.reader(data)

    for row in csv_list:
        try:
            device = row[0]
            location = row[2]
            ip = row[1]
        except:
            continue

        print(f"{device} is in {location.rstrip()} and has IP {ip}.")
