import os


input_directory = input("Please specify the full path to a directory containing DLC-based pose estimation csv files?")

output_list = []

for filename in os.listdir(input_directory):
    print(filename)
