#!/usr/bin/env python3

import glob
import ntpath
import os

geteld = glob.glob("./character_*.png")
skins = glob.glob("./*.png")

if len(skins) == len(geteld):
  print("Niets nieuws. Je hebt nog steeds " + str(len(skins)) + " skins ... ")
  exit()

teller = len(geteld) + 1

nieuweskins = [ skin for skin in skins if skin not in geteld ]

for nieuweskin in nieuweskins:
  inkomendenaam = ntpath.basename(nieuweskin)
  uiteindelijkenaam = "./" + "character_" + str(teller) + ".png"
  metadatabestandsnaam = "../meta/" + "character_" + str(teller) + ".txt"
  metadatainhoud = '''Name ="''' + inkomendenaam + '''",
Author = "Unknown",
Description = "",
Comment = ""
  '''
  print(uiteindelijkenaam)
  print(metadatainhoud)
  print(metadatabestandsnaam)
  metabestand = open(metadatabestandsnaam, "w")
  print(metadatainhoud, file=metabestand)
  metabestand.close()

  os.rename(nieuweskin,uiteindelijkenaam)
  teller += 1


print("Ik heb " + str(len(nieuweskins)) + " nieuwe skins toegevoegd")
print(nieuweskins)

