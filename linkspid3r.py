from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
import lxml
import helper
import win_unicode_console , colorama
import pyfiglet

ascii_banner = pyfiglet.figlet_format("LinkSpid3r")
print(ascii_banner)
print("\t\t\t\t\tCreated by BugMania")
# Windows deserves coloring too :D
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\33[97m'  # white

try:
    pages = set()
    url = input("\nEnter the URL >> ")

    def getLinks(pageUrl):
        global pages
        clean = helper.clean(url)
        domain = helper.get_domain(clean)
        html = urlopen(clean)
        bsObj = BeautifulSoup(html, "lxml")
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                #We have encountered a new page
                    newPage = link.attrs['href']
                    if helper.valid(newPage, domain):
                        pages.add(newPage)
                        print("%sLink Founds >> %s"%(W,G), newPage)
                        getLinks(newPage)

    getLinks("")

except Exception as e:
    print("%s[-] Something gonna wrong! Please Restart the application."%(R))
