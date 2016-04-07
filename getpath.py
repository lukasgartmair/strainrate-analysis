from string import *
from numpy import *
import os


# *************************************************
# ********** function definitions ****************
# *************************************************


def get_path():

    # Requiring inputs from user

    # the list id composed of all the text files located in the directory
    measurement_files = [elem for elem in os.listdir(
        ".") if elem[-3:] == "txt" and elem[-11:] != "summary.txt"]
    print("\nFatigue measurement files available for processing :")
    print('')
    if measurement_files != []:
        for i in range(len(measurement_files)):
            # text from type number : file
            print("  %-2i : %s" % (i, measurement_files[i]))
    print('')
    num_file_measurement = int(
        input("Index of the file that you want to use = "))
    file_name = measurement_files[num_file_measurement]

    try:
        measurement_file_tmp = str(file_name)
        print('')
        print("  -> File %s opened" % file_name)

    except IOError:
        print('')
        print("  -> File %s not found. Please check the spelling and try again" % file_name)

    return measurement_file_tmp
