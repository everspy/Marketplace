import os

# This will get the username and password from a text file
# Supports multiple logins, line separated
# Returns list of username,password
def getCredentials():

    # Open/read the file
    file = open("login.txt")
    file = file.read().splitlines()
    creds = []
    for credentials in file:
        credentials = credentials.split(", ")
        creds.append([credentials[0], credentials[1]])
    return creds

# This will retrieve the relevant info for the ad posting
# Returns title, price, description
def getAdInformation(directory):

    title, price, description = open("ad/"+directory+"/Ad.txt").read().split("\n", 2)
    return title, price, description

# This will return the absolute path to all images
# Returns a list of absolute paths to images
def getAdImagePaths(directory):
    ads = os.getcwd() + "/ads/" + directory
    files = os.listdir(ads)

    # We will go through this list and remove the hidden files as well as Ad.txt
    # This will assume all remaining files are images so make sure they are!
    # Otherwise bad things might happen
    images = []
    for file in files:
        if file[0] != "." and file != "Ad.txt":
            images.append(ads + "/" + file)
    return images

# This retrieves the directory name of each ad
# Returns list of ad folder names
def getAds():
    ads = os.getcwd() + "/ads/"
    ads = os.listdir(ads)
    return ads