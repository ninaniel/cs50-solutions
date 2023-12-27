from PIL import Image, ImageOps
import sys
import os

# program should take exactly two command-line arguments to treat first as input and other - as output
def main():
    l = len(sys.argv)
    if l < 3:
        sys.exit("Too few command-line arguments")
    elif l > 3:
        sys.exit("Too many command-line arguments")
    else:
        inpt, outpt = get_valid_args()
        shirtify(inpt, outpt)

# when received 2 c-l args, the function checks the pathes to be jpg, jpeg, png and returns them
def get_valid_args():
    extensions = [".jpg", ".jpeg", ".png"]

    #while splitext returns tuple of root and ext, we save only ext
    path1 = os.path.splitext(sys.argv[1])[1]
    path2 = os.path.splitext(sys.argv[2])[1]

    try:
        if path1 and path2 in extensions:
            if path1 == path2:
                muppet = Image.open(sys.argv[1]) #open img here in Try block to catch error if occured
                return muppet, sys.argv[2]
            
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

# this function takes as input img & path; outputs img with inputed path, overlayed by cs50 shirt
def shirtify(muppet, p_shirted):
    shirt = Image.open("shirt.png")

    edited = ImageOps.fit(muppet, (600,600)) # cropped to fit shirt measurements
    edited.paste(shirt,(0,0),shirt)
    edited.save(p_shirted)

if __name__ == "__main__":
    main()