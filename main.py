#Russian and Korean alphabet trainer which mixes and matches latin alphabet to Korean and Russian alphabet to Korean.
#This trainer is for people who have already had a quick look at the letters before.

import datetime as dt
import time
import random as rand
fortsette = True

print("Hei! i dette programmet kan du lære Koreans alfabet.")
print("det Koreanske alfabet. OBS! Du må kunne det Russiske alfabetet fra før av.")
vlstrt = str(input("Vil du starte? y/n ")).lower()

while fortsette:
    if vlstrt == ("y" or "yes" or "ja"):
        print('')
        break
    elif vlstrt == ("n" or "no" or "nei"): # gjør at alt dette funker
        print("Greit. Start gjerne opp programmet igjen om du vil prøve.")
        time.sleep(3)
    else:
        print("Du tastet inn noe feil. Prøv igjen.") # fisk at den spammer omigjen
        time.sleep(3)



print("La oss starte:")
time.sleep(3)
print("Det er 24 bokstaver i det Koreanske alfabetet.")
time.sleep(3)

print("Selv om det ser avansert ut er ikke det det mest avanserte å lære.")
time.sleep(3)
print("Her er en liste med alle bokstavene og hva de betyr (Selvstudér):")
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
time.sleep(0.5)
print("ㅂ    er en standard p eller b avhengig av plassering.")
time.sleep(0.5)
print("ㅅ    er en standard s.")
time.sleep(0.5)
print("ㅇ    er ng om den ligger på slutten av hver klump.")
time.sleep(0.5)
print("ㅈ    er en standard j.")
time.sleep(0.5)
print("ㅊ    er  ch.")
time.sleep(0.5)
print("ㅋ    er en standard k.")
time.sleep(0.5)
print("ㅌ    er en standard t.")
time.sleep(0.5)
print("ㅎ    er en standard h.")
time.sleep(0.5)
print("ㅏ    er en standard a.")
time.sleep(0.5)
print("ㅑ    er en  ya og uttales ja.")
time.sleep(0.5)
print("ㅓ    er en eo og uttales å.")
time.sleep(0.5)
print("ㅕ    er en  yeo og uttales yå.")
time.sleep(0.5)
print("ㅗ    er en standard o.")
time.sleep(0.5)
print("ㅁ    er en yo og uttales jo.")
time.sleep(0.5)
print("ㅜ    er en standard u.")
time.sleep(0.5)
print("ㅠ    er en  yu.")
time.sleep(0.5)
print("ㅡ    er en eu og uttales u.")
time.sleep(0.5)
print("ㅣ    er en standard i.")
time.sleep(0.5)

input("")
input("Skriv hva som helst for å fortsette når du er klar ")
print("endofdemo")

