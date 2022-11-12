import os
import csv

read_from = "./kitti_train.csv"

with open(read_from, 'r') as read:
    csvreader = csv.reader(read)
    for row in csvreader:
        img_exist = os.path.exists(row[1])
        depth_exist = os.path.exists(row[2])
        if not img_exist:
            print("[ERROR] IMAGE DOES NOT EXIST {}".format(row[1]))
        if not depth_exist:
            print("[ERROR] DEPTH DOES NOT EXIST {}".format(row[2]))