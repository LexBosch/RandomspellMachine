#Lex Bosch
#6-2-2018
import random

def main():
    Spells = AmountSpells()
    AllSpells = OpenSpells()
    AvSpells = RanSpells(Spells, AllSpells)
    Output(AvSpells)

def AmountSpells():
    lvl = True
    while lvl:
        Level = int(input("How many sorcerer levels are you?"))
        if Level >= 1 and Level <= 20:
            lvl = False
        else:
            print("Please select a level between 1 and 20")
    Spells = ""
    SpellLevel = open("LevelSpells.txt","r").readlines()
    for Layer in SpellLevel:
        if str(Level) in str(Layer[0:2]):
            Spells = filter(None,Layer.replace("\x97","").replace("\n","").split("\t")[1:])
            break
    return(Spells)


def OpenSpells():
    SpellList = []
    TempSpellList = []
    AllSpells = open("SpellList.txt", "r").read()
    for i in AllSpells.split("\n"):
        if i:
            TempSpellList.append(i)
        else:
            SpellList.append(TempSpellList)
            TempSpellList = []
    return(SpellList)

def RanSpells(AmSpells, AllSpells):
    SpellLevel = 0
    AvSpells = []
    LevelSpell = []
    for L in AmSpells:
        for i in range(0, int(L)):
            succeed = False
            while succeed == False:
                RanSpell = random.randint(0,len(AllSpells[SpellLevel]))
                if not AllSpells[SpellLevel][RanSpell - 1] in LevelSpell:
                    LevelSpell.append(AllSpells[SpellLevel][RanSpell - 1])
                    succeed = True
        AvSpells.append(LevelSpell)
        LevelSpell = []
        SpellLevel += 1
    return(AvSpells)

def Output(Spells):
    LVLcount = 0
    print("="*80)
    print("These are the spell you will be able to cast today")
    print("="*80)
    for level in Spells:
        print("-"*80)
        print("These are your ", LVLcount,"th level spells")
        print("-"*80)
        for Spell in level:
            print(Spell)
        LVLcount += 1


main()
