#Lex Bosch
#06-02-2018

def main():
    RawSpells = open("Spells.txt", "r").readlines()
    SpellList = FullList(RawSpells)
    WriteSpells(SpellList)
    
def FullList(RawSpells):
    SpellList = []
    TempSpells = []
    level = 1
    for i in RawSpells:
        if str(level) in i:
            SpellList.append(TempSpells)
            TempSpells = []
            level += 1
        elif "0" in i or "Spell Name" in i or "Back to Top" in i or "Unviversal" in i or "Abjuration" in i or "Conjuration" in i or "Divination" in i or "Enchantment" in i or "Evocation" in i or "Illusion" in i or "Necromancy" in i:
            pass
        else:
            TempSpells.append(i.replace("\n",""))
    SpellList.append(TempSpells)
    return SpellList

def WriteSpells(SpellList):
    SpellString = ""
    for level in SpellList:
        for spell in level:
            SpellString += spell + "\n"
        SpellString += "\n"
    open("SpellList.txt", "w").write(SpellString)

    
main()
