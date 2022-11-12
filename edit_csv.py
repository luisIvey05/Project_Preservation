import csv

read_from = "./kitti_train.csv"
write_to  = "./kitti_trai.csv"

with open(read_from, 'r') as read:
    with open(write_to, 'w') as write:
        csvreader = csv.reader(read)
        csvwriter = csv.writer(write)
        for row in csvreader:
            path_header = "/projectnb/ece601/Project_Preservation/Project_Preservation/data/"
            row[1] = path_header + "data_image/" + row[1][9:]
            row[2] = path_header + "data_depth/" + row[1][45:]
            csvwriter.writerow(row)