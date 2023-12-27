import csv
import sys

# this program should take exactly two command-line arguments: names of csv files(existing and new - to be written)

def main():
    try:
        l = len(sys.argv)
        if l < 3:
            sys.exit("Too few command-line arguments")
        elif l > 3:
            sys.exit("Too many command-line arguments")
        else:
            scourgify(sys.argv[1],sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


# this function reads a CSV file of students fullnames and houses in each row & Converts it to a new CSV file of same info in columns: first, last, and house
def scourgify(old, new):
    splitted_names = []
    with open(old) as file:
        reader = csv.DictReader(file)

        #splitting fullnames; note that names in each row are in order - last , first
        for row in reader:
            last, first = row["name"].split(", ")

            # adding dicts, with each student's firstname, lastname and house, in a list
            splitted_names.append({"first": first, "last": last, "house": row["house"]})

    with open(new, "w") as new_csv:
        writer = csv.DictWriter(new_csv, fieldnames=["first","last", "house"])
        writer.writeheader()
        for element in splitted_names:
            writer.writerow(element)

if __name__ == "__main__":
    main()