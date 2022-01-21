#Russian and Korean alphabet trainer which mixes and matches latin alphabet to Korean and Russian alphabet to Korean.
#This trainer is for people who have already had a quick look at the letters before.

import datetime as dt
import time
fortsette = True

print("Hei! i dette programmet kan du lære både en liten miks av Russisk alfabet og Koreans alfabet med mest fokus på")
print("det Koreanske alfabet. OBS! Du må kunne det Russiske alfabetet fra før av.")
vlstrt = input("Vil du starte? y/n ").lower()

while fortsette:
    if vlstrt == "y":
        break
    elif (vlstrt == "n"): # gjør at alt dette funker
        print("Greit. Start gjerne opp programmet igjen om du vil prøve.")
        break
    else:
        print("Du tastet inn noe feil. Prøv igjen.") #fisk at den spammer omigjen

print("La oss starte:")
time.sleep(2)
print("Det er 24 bokstaver i det Koreanske alfabetet.")
time.sleep(2)

print("Selv om det ser avansert ut er ikke det det mest avanserte å lære.")
time.sleep(2)
print("Her er en liste med alle bokstavene og hva de betyr (Selvstuder):")
time.sleep(4)
print("ㄱ    er en G eller K ettersom hva som er før og etter i setningen.")
time.sleep(0.5)
print("ㄴ    er en N og er utrolig lik ㄱ, altså K/G men er opp ned.")
time.sleep(0.5)
print("ㄷ    er bare en D.")
time.sleep(0.5)
print("ㄹ    er ganske vanskelig å lære å lese. Det kan være en L eller R og uttales annerledes basert på bokstav før og etter.")
time.sleep(0.5)
print("ㅁ    er en standard M.")

input(" ")
input("Skriv hva som helst for å fortsette når du er klar ")
print("endofdemo")

