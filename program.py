import random
from random import choice
import logging
from pathlib import Path
import datetime



# checks entries for error
def err_check(dataset):
    log_object = logging.getLogger('error')
    path = logging.FileHandler('error.log')

    format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    path.setFormatter(format)
    log_object.addHandler(path)
    log_object.setLevel(logging.ERROR)
    c = 1
    for entry in dataset:
        if type(entry) is str and  entry == "err":

            log_object.error('The Sensor ' + str(c) + ' returning a error.')
        else:
            pass
        c += 1


# generate dummy data-set
def gen_good_dataSet():
    data = []

    # generates a single set of data
    def gen_asset_reading():
        randArray = []
        for p in range(1,17):
            randArray.append(round(random.uniform(0, 1), 2))
        return randArray

    for n in range(32):
        data.append(gen_asset_reading())

    q = 1
    for entry in data:
        print("Sensor " + str(q) + ": " + str(entry))
        q+=1
    return data


# generate corrupt dummy data-set
def gen_corrupt_dataSet():
    data = []
    random_corrupt_asset = 0

    # generates a single set of data
    def gen_asset_reading():
        randArray = []
        for p in range(1,17):
            randArray.append(round(random.uniform(0, 1), 2))
        return randArray

    for n in range(32):
        random_corrupt_asset = random.randint(0,32)
        if n == random_corrupt_asset:
            data.append("err")
            continue

        data.append(gen_asset_reading())
    q = 1
    for entry in data:
        print("Sensor " + str(q) + ": " + str(entry))
        q += 1
    return data


if __name__ == "__main__":

    dataSet = []

    # stores a data-set into a variable
    functions = [gen_good_dataSet, gen_corrupt_dataSet]

    dataSet = choice(functions)() # randomly selects between generating a good and corrupt data-set

    # checks (variable) data-set for error
    err_check(dataSet)

    # checks if storage file already exists
    file = Path("data-set.csv")

    name_of_file = "data-set.csv"
    # if storage file exist, it adds new data-set without named column title row
    if file.is_file():
        # stores and exports data-set to csv file
        csv = open(name_of_file, "a")
        c = 1
        for key in dataSet:
            name = c
            reading = key
            if type(key) is str and key == "err":  # replaces error string "err" with 9.9999 which is to be uniquely identified as the error.
                row = str(name) + "," + str(9.9999) + "," + ",,,,,,,,,,,,,,," + str(datetime.date.today()) + "," + str(datetime.datetime.now().time()) + "\n"
            else:
                row = str(name) + "," + str(reading)[1:-1] + "," + str(datetime.date.today()) + "," + str(datetime.datetime.now().time()) + "\n"
            csv.write(row)
            c += 1

    # if storage file does not exist, it adds new data-set with named column title row
    else:
        csv = open(name_of_file, "a")
        columnTitleRow = "#, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, Date, Time \n"
        csv.write(columnTitleRow)

        c = 1
        for key in dataSet:
            name = c
            reading = key
            if type(key) is str and key == "err":  # replaces error string "err" with 9.9999 which is to be uniquely identified as the error.
                row = str(name) + "," + str(9.9999) + "," + ",,,,,,,,,,,,,,," + str(datetime.date.today()) + "," + str(datetime.datetime.now().time()) + "\n"
            else:
                row = str(name) + "," + str(reading)[1:-1] + "," +  str(datetime.date.today()) + "," + str(datetime.datetime.now().time()) + "\n"
            csv.write(row)
            c += 1