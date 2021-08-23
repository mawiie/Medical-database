import json
import time
DEFAULT = 'patients.json'

"""
Filename: cip_project.py
-----------------------------
Code to implement a medical dictionary
"""


def main():
    """
    Code for a medical not-so-hand book
    Code in three sections:
    1. To create a new file (for your very first entry)
    2. To update an already existing file
    3. To retrieve previous entries
    parameters: None
    return: None
    """
    run_down()
    while True:
        user_input = input("What would you like to do? Input 1 to create, 2 to update and 3 to retrieve: ")
        if user_input == '1':
            create_new_file()
        elif user_input == '2':
            update_entry()
        elif user_input == '3':
            retrieve_entry()
        elif user_input == "":
            break
        else:
            print("Please enter either 1, 2, or 3 or hit enter to terminate program")


def retrieve_entry():
    filename = input("What is the name of your file (Hit Enter for default name): ")
    if filename == "":
        filename = DEFAULT
    print("If there are multiple entries with the same name value, all such entries would be printed out")
    name = input("What is the name of the patient whose record you want to retrieve?: ")
    count = 0
    with open(filename) as f:
        data = json.load(f)
    for item in data:
        if item["Name"] == name:
            print("")
            print(item)
            count += 1
    if count < 1:
        print("There is no entry with such name. Please check your spelling, case and/or punctuation")


def update_entry():
    """
    update entry has two sections. 1. add a new entry to an already existing file 2. correct a previously existing entry
    :return:
    """
    filename = input("What is the name of your file (Hit Enter for default name): ")
    if filename == "":
        filename = DEFAULT
    with open(filename) as f:
        data = json.load(f)

    while True:
        user_input = input("Enter 1 to add a new entry or 2 to correct an existing entry(press enter to terminate): ")
        if user_input == "1":
            entry_loop(data, filename)
        elif user_input == "2":
            correct_entry(filename)
        elif user_input == "":
            break
        else:
            print("Please enter either 1, 2 or hit enter to terminate program")


def correct_entry(filename):
    name = input("What is the name (unique_value) of the patient whose record you want to correct?: ")
    correction = input('What would you like to correct? Name, Age, Address, Diagnosis, or Drugs? ')
    count = 0
    with open(filename) as f:
        data = json.load(f)
    for item in data:
        if item["Name"] == name:
            count += 1
            print("")
            if correction == 'Drugs':

                item[correction]['Name'] = input("What is the correct drug name: ")
                item[correction]["Dosage"] = input("What is the correct drug dosage: ")
            elif correction == 'Name' or correction == 'Address' or correction == 'Diagnosis' or correction == 'Age':
                item[correction] = input("What is the correct " + str(correction) + " ")
            else:
                print("Check that spelling🌚")
                pass
            print(data[data.index(item)])
        else:
            pass

    if count < 1:
        print("There is no entry with such name. Please check your spelling, case and/or punctuation")

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def entry_loop(data, filename):
    while True:
        next_time = input("Type 'yes' if you wish to input another entry, else hit enter: ")
        if next_time == 'yes':
            data.append(new_entry())
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        elif next_time == "":
            return
        else:
            print("Incorrect value. Please enter yes in lower case or hit enter")


def create_new_file():
    filename = input("What would you like to name your file (Hit Enter for default name): ")
    if filename == "":
        filename = DEFAULT
    data = [new_entry()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    entry_loop(data, filename)


def new_entry():
    """
    :parameter: filename
    :return: a dict of details entered
    """
    details = {
        "Name": input("What is your patient's name?: "),
        "Age": input("How old is your patient?: "),
        "Address": input("What is your patient's address?: "),
        "Diagnosis": input("What is your patient's diagnosis?: "),
        "Drugs": drugs()
    }
    return details


def drugs():
    """
    :return: a list of drugs prescribed for patients
    """
    drugs_details = {"Name": input("Enter a drug prescribed for the patient: "), "Dosage": input("Enter the dosage for drug entered above: ")}
    drug = [drugs_details]
    while True:
        next_time = input("Type 'yes' if you wish to enter another drug prescription, else hit enter ")
        if next_time == 'yes':
            drugs_details = {"Name": input("Enter a drug prescribed for the patient: "), "Dosage": input("Enter the dosage for drug entered above: ")}
            drug.append(drugs_details)
        elif next_time == "":
            return drug
        else:
            print("Incorrect value. Please enter yes in lower case or hit enter")


def run_down():
    print("This is a brief run down on a code to implement a digital medical handbook")
    time.sleep(1.5)
    print("There are three functions of this program: 1. Create, 2. Update and 3. Retrieve")
    time.sleep(1.5)
    print("You will soon be prompted to choose what function you will be using.")
    time.sleep(1.5)
    print("Enter 1 if you wish to create a new file i.e you haven't previously entered any value or you wish to start all over again")
    time.sleep(1.5)
    print("Enter 2 if you wish to update a file that already has at least one entry")
    time.sleep(1.5)
    print("Enter 3 if you wish to retrieve a patient's info")
    time.sleep(1.5)
    print("After any function you may terminate the program by hitting the enter button")


if __name__ == "__main__":
    main()
