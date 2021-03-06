# 55 page done
import requests, zipfile, io
from bs4 import BeautifulSoup
home = "https://yts-subs.com"

# included
start_page = 301
end_page = 310
end_page += 1

print(f"starting program for page {start_page} to {end_page} ")

page_link = []
for j, i in enumerate(range(start_page, end_page)):

    link=f"https://yts-subs.com/language/english?page={i}"

    source=requests.get(link).text
    soup = BeautifulSoup(source, "lxml")


    # find names of movie.
    name = soup.findAll("h3", class_="media-heading")
    name = [i.text for i in name]
    
    with open("name of all movies subtitle downloaded.txt", "a") as write_name:
        write_name.write("\n"+", ".join(name))

    print(f"movie names are {name} \n written")
    

    page_link_block = soup.findAll("li", class_="media")
    for k in page_link_block:
        page_link.append(home + k.div.a["href"])


    print(f"{i} th page found")


length = len(page_link)
# input(f"\ntotal links = {length} \nshould be go for it ")


link_for_english = []

try:  # if english didn't found
    for j, i in enumerate(page_link):

        source=requests.get(i).text
        soup = BeautifulSoup(source, "lxml")
        all_language = soup.findAll("span", class_="sub-lang")

        for index, word in enumerate(all_language):
            if word.text=="English":
                index_for_english = index
                break

        all_language_link = soup.findAll("a", class_="subtitle-download")
        link_for_english.append(home + all_language_link[index_for_english]["href"])
        
        print(f"{j+1} out of {length} English subtitle page link found")
except:
    pass

zip_link = []
for j, i in enumerate(link_for_english):
    source=requests.get(i).text
    soup = BeautifulSoup(source, "lxml")

    zip_link.append(soup.find("a", class_="download-subtitle")["href"])

    print(f"{j+1} out of {length} File found")

err=0
for j, i in enumerate(zip_link):

    try:
        r = requests.get(i)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("D:\Coding\Python\words\scripted download after 200")
        print(f"{j+1} out of {length} file saved")
    except:
        # input("we got an error")
        err+=1

print("All Done")
print("eror = ",err)


