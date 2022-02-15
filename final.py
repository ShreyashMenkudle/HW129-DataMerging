import csv

dataset_1 = []
dataset_2 = []

with open ("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)

    for read_row in csv_reader:
        dataset_1.append(read_row)

with open ("brown_dwarfs_sorted.csv", "r") as f:
    csv_reader = csv.reader(f)

    for read_row in csv_reader:
        dataset_2.append(read_row)

headers_1 = dataset_1[1]
star_data_1 = dataset_1[1:]

headers_2 = dataset_2[1]
star_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
star_data = [] 

for index, data_row in enumerate(star_data_1): 
    star_data.append(star_data_1[index] + star_data_2[index])

with open("lastfinal.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(star_data)