import requests
import string
import csv
import time
import bs4
from bs4 import BeautifulSoup

#Create csv file
filename = "tableA.csv"
f = open(filename, "w", newline="", encoding="utf-8")
writer = csv.writer(f)

# Headers
writer.writerow(["ID_number", "Player Name", "Position", "Team"])

#Identify not a bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
#Loop through positions 

#Url PosID mapping
position_mapping = {
10: "QB", 
20: "RB", 
30: "WR", 
40: "TE", 
80: "K", 
99: "DEF", 
50: "DL", 
60: "LB", 
70: "DB"
}

count = 0
print("Starting Scrape...")

for pos_id, pos_name in position_mapping.items():
    page_count = 0
    previous_first_player = None
    
    #Loop through pages until no more pages
    while True:
        url = f"https://www.fftoday.com/stats/playerstats.php?Season=2025&GameWeek=Season&PosID={pos_id}&cur_page={page_count}"
        print(f"Scraping {pos_name}, page {page_count}")
        
        try:
            req = requests.get(url, headers=headers)
            soup = BeautifulSoup(req.content, "html.parser")
            
            all_rows = soup.find_all("tr")
            player_page_count = 0
            begin_with_player = None
            f = open(filename, "a", newline="", encoding="utf-8")
            writer = csv.writer(f)
                
            for row in all_rows:
                cols = row.find_all("td", class_="sort1")
                if 2 <= len(cols) < 30 and cols[0].find("a"):
                    player_tag = cols[0].find("a")
                    Player_name = player_tag.get_text(strip=True)
                    Team = cols[1].get_text(strip=True)
                   
                    if begin_with_player is None:
                        begin_with_player = Player_name
                    
                    # Write to file
                    writer.writerow([count, Player_name, pos_name, Team])
                    count += 1
                    player_page_count += 1
            
            #Loop Check
            if begin_with_player == previous_first_player:
                print(f"  -> Duplicate page detected. Stop Looping. {pos_name}.")
                break
            
            # Reset memory loop check
            previous_first_player = begin_with_player
                    
            # Break the loop if end of players
            if player_page_count == 0:
                break   
           
            page_count += 1 
                            
            # Pause
            time.sleep(3)

        except Exception as e:
            print(f"Error on {pos_name}: {e}")

#close file
f.close()
print(f"Ended Scrapping. {count} player tuples in '{filename}'.")