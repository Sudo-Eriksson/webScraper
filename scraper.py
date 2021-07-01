import requests
from bs4 import BeautifulSoup
from time import sleep
from playsound import playsound

for i in range(0, 10):
    URL = "https://www.vgregion.se/ov/vaccinationstider/bokningsbara-tider/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="wrapper")

    job_elements = results.find_all("div", class_="media-body")

    counter = 0

    for item in job_elements:
        item_str = str(item).lower()
        if "göteborg" in item_str or "mölndal" in item_str:
            print(item)
            counter += 1

    if counter == 0:
        print("Inga bokningar möjliga i Göteborg :(")
    else:
        for timer in range(2):
            playsound('alarm.wav')

    sleep(60)