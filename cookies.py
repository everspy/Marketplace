import os
import pickle

def saveCookies(browser, creds):
    cookies = browser.get_cookies()

    badFileChars = ['//', '*', '|', '?', '*']
    fileName = creds[0]
    for char in badFileChars:
        fileName.replace(char, '')

    path = os.getcwd() + "/cookies"
    if not os.path.isdir(path):
        os.mkdir(path)

    pickle.dump(cookies, open("cookies/%s.pkl" % fileName, "wb"))

def loadCookies(creds):
    badFileChars = ['//', '*', '|', '?', '*']
    fileName = creds[0]
    for char in badFileChars:
        fileName.replace(char, '')
  
    try:
        cookies = pickle.load(open("cookies/%s.pkl" % fileName, "rb"))
    except:
        cookies = []
        print("Failed to load cookies for %s" % creds[0])

    return cookies 
