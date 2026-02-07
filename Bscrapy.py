import requests
import string
import time
import csv
from bs4 import BeautifulSoup

#Create CSV file
filename = "nfl_players.csv"
f = open(filename, "w", newline="", encoding="utf-8")
writer = csv.writer(f)

# Write the headers first
writer.writerow(["ID_number", "Player Name", "Position", "Team"])

# Identify as not a bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print("Starting scrape... saving to tableB.csv")
count = 0

#Loop through names by letter
for letter in string.ascii_uppercase:
    url = f"https://www.footballdb.com/players/index.html?letter={letter}"
    
    try:
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, "html.parser")
        
        table = soup.find("table", class_="statistics")
        if table:
            rows = table.find("tbody").find_all("tr")
            
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 3:
                    name = cols[0].get_text(strip=True)
                    pos = cols[1].get_text(strip=True)
                    team = cols[2].get_text(strip=True)
                    
                    # Write to file
                    writer.writerow([count, name, pos, team])
                    count += 1
        
        # Pause
        time.sleep(3)

    except Exception as e:
        print(f"Error on {letter}: {e}")

#close file
f.close()
print(f"Ended Scrapping {count}. player tuples in '{filename}'.")