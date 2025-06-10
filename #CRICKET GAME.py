#CRICKET GAME
import google.generativeai as genai
import random
import csv
import os
Flag=True
def playingXI():#accept playing XI from the user
    XI=input("Enter the playing XI for the given CONDITIONS :").split(",")
    response = model.generate_content(f"Given the list of cricketers {XI}, correct any spelling errors and remove any unnecessary spaces. Return only the corrected list in a clean format as a Python list. Do not include any additional text or explanation. Only output the final list of names.")
    lister=response.text
    return lister
def leaderboard(name, score, condition, Format, Players):
    filename = f"{condition} {Format}.csv"
    file_empty = not os.path.exists(filename) or os.stat(filename).st_size == 0
    
    with open(filename, "a", newline="") as f:
        w = csv.writer(f)
        if file_empty:
            w.writerow(["NAME", "SCORE", "TEAM"])
        w.writerow([name, score, Players])
#main program
genai.configure(api_key="AIzaSyD8tNAQBZxz25MoURndw1VhMi0PHJl3e8A")
model = genai.GenerativeModel("gemini-1.5-flash")
'''conditions_list=["Green","Dry","Flat","Hard","Slow"]
Overs_list=["T20","ODI","Test"]'''
conditions_list=["flat"]
Overs_list=["T20"]

name=input("Enter the player name: ")
condition=conditions_list[random.randint(0,len(conditions_list)-1)]
Format=Overs_list[random.randint(0,len(Overs_list)-1)]
print(f"The PITCH CONDITION : {condition}")
print(f"The Format of the match : {Format}")
Players=playingXI()
response=model.generate_content(f'''Based on the following players, pitch conditions, and match format, analyze the ideal selection fit of this team for the conditions provided. Use recent player performance, form, and historical data on similar pitch types to generate a winning suitability score (in percentage) specifically for this lineup in the given conditions.

Output only the ideal team suitability percentage as a single float value, without any additional text or explanation.

Players: {Players}
Pitch Condition: {condition}
Match Format: {Format}''')
score=response.text
print(Players)
print(score)