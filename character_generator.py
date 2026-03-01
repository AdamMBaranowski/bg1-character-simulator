###Original Baldur's Gate character generator in Python, complete with:
#Ability score rolling (including exceptional strength!)
#Race and class modifiers
#Multiclass inheritance and validation 
#Assembly character creation
#Defensive checks for rules enforcement
#Display output
#Extendable design
###

import random

#Utility classes
class AbilityScores:
    def __init__(self):
        self.strength = self.roll()
        self.dexterity = self.roll()
        self.constitution = self.roll()
        self.intelligence = self.roll()
        self.wisdom = self.roll()
        self.charisma = self.roll()
        
    def roll(self):
        """
        Roll 4d6, sort results in a list, slice off the lowest result and return the sum of the list.
    
        This is a common method in tabletop RPGs to generate ability scores.
        It results in values between 3 and 18, with a higher average than 3d6.
        """
        #Might be using cheaty dice for testing check randint range
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])
        

class WarriorAbilityScores(AbilityScores):
    def __init__(self):
        super().__init__()
        
        self.exceptional_strength = random.choice([25, 50, 75, 100])
        print(f"ex str suffix: {self.exceptional_strength}")


    def display_strength(self):
        if self.strength == 18:
            suffix = "00" if self.exceptional_strength == 100 else str(self.exceptional_strength)
            return f"18/{suffix}"
        else:
            return str(self.strength)


class CharacterAssembly:
    """Base for combining race and class(es) into a full character."""
    def __init__(self):
        super().__init__()

        seen_classes = set()

        for cls in self.__class__.mro():
            if cls is object or cls in seen_classes:
                continue
            seen_classes.add(cls)

            # Only apply modifiers defined in that exact class
            if getattr(cls, 'is_class', False) and 'apply_class_modifiers' in cls.__dict__:
                print(f"Calling class modifiers from: {cls.__name__}")
                cls.apply_class_modifiers(self)

            if getattr(cls, 'is_race', False) and 'apply_race_modifiers' in cls.__dict__:
                print(f"Calling race modifiers from: {cls.__name__}")
                cls.apply_race_modifiers(self)


    
#WarriorClasses: Fighter, Ranger, Paladin
class Fighter(WarriorAbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Fighter modifiers")
        """
        Warrior classes have additional STR roll: 18/25, 18/50, 18/75, 18/00.
        Fighter has minimal score STR9
        """
        #Ensure strength is not below 9
        if self.strength < 9:
            print("Fighter strength too low — raising to minimum of 9.")
            self.strength = 9


class Paladin(WarriorAbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Paladin modifiers")
        """
        Warrior classes have additional STR roll: 18/25, 18/50, 18/75, 18/00.
        Paladin has minimal scores: STR12, DEX9, CON13, WIS17
        """
        #Ensure strenth is not below 12
        if self.strength < 12:
            print("Paladin strength too low — raising to minimum of 12.")
            self.strength = 12
        
        #Ensure constitution is not below 9
        if self.constitution < 9:
            print("Paladin constitution too low — raising to minimum of 9.")
            self.constitution = 9

        #Ensure wisdom is not below 13
        if self.wisdom < 13:
            print("Paladin wisdom too low — raising to minimum of 13.")
            self.wisdom = 13

        #Ensure charisma is not below 17
        if self.charisma < 17:
            print("Paladin charisma too low — raising to minimum of 17.")
            self.charisma = 17


class Ranger(WarriorAbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Ranger modifiers")
        """
        Warrior classes have additional STR roll: 18/25, 18/50, 18/75, 18/00.
        Ranger has minimal scores: STR13, DEX13, CON14, WIS14
        """
        #Ensure strenth is not below 13
        if self.strength < 13:
            print("Ranger strength too low — raising to minimum of 13.")
            self.strength = 13
        
        #Ensure dexterity is not below 13
        if self.dexterity < 13:
            print("Ranger dexterity too low — raising to minimum of 13.")
            self.dexterity = 13
            
        #Ensure constitution is not below 14
        if self.constitution < 14:
            print("Ranger constitution too low — raising to minimum of 14.")
            self.constitution = 14

        #Ensure wisdom is not below 14
        if self.wisdom < 14:
            print("Ranger wisdom too low — raising to minimum of 14.")
            self.wisdom = 14


#Cleric classes
class Cleric(AbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Cleric modifiers")
        """
        Cleric has minimal scores: WIS
        """
        #Ensure wisdom is not below 9
        if self.wisdom < 9:
            print("Cleric wisdom too low — raising to minimum of 9.")
            self.wisdom = 9


class Druid(AbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Druid modifiers")
        """
        Druid has minimal scores: WIS12, CHA15
        """
        #Ensure wisdom is not below 12
        if self.wisdom < 12:
            print("Paladin wisdom too low — raising to minimum of 12.")
            self.wisdom = 12

        #Ensure charisma is not below 15
        if self.charisma < 15:
            print("Paladin wisdom too low — raising to minimum of 15.")
            self.charisma = 15


#Arcane caster classes
class Bard(AbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Bard modifiers")
        """
        Bard has minimal scores: DEX12, INT13, CHA15
        """
        #Ensure dexterity is not below 12
        if self.dexterity < 12:
            print("Bard dexterity too low - raising to minimum 12")
            self.dexterity = 12
        #Ensure intelligence is not below 13
        if self.intelligence < 13:
            print("Bard intelligence too low - raising to minimum 13")
            self.intelligence = 13
        #Ensure charisma is not below 15
        if self.charisma < 15:
            print("Bard charisma too low - raising to minimum 15")
            self.charisma = 15


class Mage(AbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Mage modifiers")
        """
        Mage has minimal scores: INT9
        """
        #Ensure intelligence is not below 9
        if self.intelligence < 9:
            print("Mage intelligence too low - raising to minimum 9")
            self.intelligence = 9


#Mage specialist kits (see Race restrictions)
class Abjurer(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Abjurer modifiers")
        """
        Abjurer has minimal scores: WIS15
        """
        #Ensure wisdom is not below 15
        if self.wisdom < 15:
            print("Abjurer wisdom too low - raising to minimum 15")
            self.wisdom = 15


class Conjurer(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Conjurer modifiers")
        """
        Conjurer has minimal scores: CON15
        """
        #Ensure constitution is not below 15
        if self.constitution < 15:
            print("Conjurer intelligence too low - raising to minimum 15")
            self.constitution = 15


class Diviner(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Diviner modifiers")
        """
        Diviner has minimal scores: WIS16
        """
        #Ensure wisdom is not below 16
        if self.wisdom < 16:
            print("Diviner wisdom too low - raising to minimum 16")
            self.wisdom = 16


class Enchanter(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Enchanter modifiers")
        """
        Enchanter has minimal scores: CHA16
        """
        #Ensure charisma is not below 16
        if self.charisma < 16:
            print("Enchanter charisma too low - raising to minimum 16")
            self.charisma = 16 


class Illusionist(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Illusionist modifiers")
        """
        Mage has minimal scores: DEX16
        """
        #Ensure dexterity is not below 16
        if self.dexterity < 16:
            print("Illusionist dexterity too low - raising to minimum 16")
            self.dexterity = 16 


class Invoker(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Invoker modifiers")
        """
        Invoker has minimal scores: CON16
        """
        #Ensure contitution is not below 16
        if self.intelligence < 16:
            print("Invoker constitution too low - raising to minimum 16")
            self.intelligence = 16 


class Necromancer(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Necromancer modifiers")
        """
        Necromancer has minimal scores: WIS16
        """
        #Ensure wisdom is not below 16
        if self.intelligence < 16:
            print("Necromancer wisdom too low - raising to minimum 16")
            self.intelligence = 16


class Transmuter(Mage):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Transmuter modifiers")
        """
        Transmuter has minimal scores: DEX15
        """
        #Ensure dexterity is not below 15
        if self.dexterity < 15:
            print("Transmuter dexterity too low - raising to minimum 15")
            self.dexterity = 15 


#Rogue class
class Thief(AbilityScores):
    is_class = True
    
    def __init__(self):
        super().__init__()
    def apply_class_modifiers(self):
        print("Applying Thief modifiers")

        """
        Thief has minimal scores: DEX9
        """
        #Ensure dexterity is not below 9
        if self.dexterity < 9:
            print("Thief dexterity too low - raising to minimum 9")
            self.dexterity = 9
            

#Races
class Human:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Human modifiers")
        """
        Humans have no ability score modifiers in BG1.
        """
        pass


class Halforc:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Half-Orc modifiers")
        """
        Halforcs get +1STR, +1CON and -2INT
        They have minimal scores: STR4, CON4 and INT1
        They have Human thieving skills.
        """
        print("Applying Halforc bonuses: +1 Strength, +1 Constitution, -2 Intelligence")
        self.strength += 1
        self.constitution += 1
        self.intelligence -= 2


#Elves
class Elf:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Elf modifiers")
        """
        Elves get +1DEX and -1CON.
        They have minimal scores: DEX7, CON6, INT8, CHA8."
        """
        print("Applying Elf bonuses: +2 Dexterity, -1 Constitution")
        self.dexterity += 1
        self.constitution -= 1
        
        #Ensure dexterity is not below 7
        if self.dexterity < 7:
            print("Elf dexterity too low — raising to minimum of 7.")
            self.dexterity = 7
            
        #Ensure constitution is not below 6
        if self.constitution < 6:
            print("Elf constitution too low — raising to minimum of 6.")
            self.constitution = 6

        #Ensure intelligence is not below 8
        if self.intelligence < 8:
            print("Elf intelligence too low — raising to minimum of 8.")
            self.intelligence = 8

        #Ensure charisma is not below 8
        if self.charisma < 8:
            print("Elf charisma too low — raising to minimum of 8.")
            self.charisma = 8


class Halfelf:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Half-Elf modifiers")
        """
        Halfelves have some class restrictions.
        They have minimal scores: DEX6, CON6, INT4,
        """
        #Ensure dexterity is not below 6
        if self.dexterity < 6:
            print("Halfelf dexterity too low — raising to minimum of 6.")
            self.dexterity = 6
            
        #Ensure constitution is not below 6
        if self.constitution < 6:
            print("Halfelf constitution too low — raising to minimum of 6.")
            self.constitution = 6

        #Ensure intelligence is not below 4
        if self.intelligence < 4:
            print("Halfelf intelligence too low — raising to minimum of 4.")
            self.intelligence = 4


#Shorty races
class Dwarf:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Dwarf modifiers")
        """
        Dwarves get +1CON, -1DEX, -2CHA.
        They have minimal scores: STR8, DEX2, CON12, CHA1. This is after EE fix
        """
        print("Applying Dwarf bonuses: +1 Constitution, -1 Dexterity, -2 Charisma")
        self.constitution += 1
        self.dexterity -= 1
        self.charisma -= 2
    
        #Ensure strength is not below 8
        if self.strength < 8:
            print("Dwarf strength is too low — raising to minimum of 8.")
            self.strength = 8
        
        #Ensure constitution is not below 12
        if self.constitution < 12:
            print("Dwarf constitution too low — raising to minimum of 12.")
            self.constitution = 12


class Gnome:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Gnome modifiers")
        """
        Gnomes get +1INT and -1WIS.
        They have minimal scores: STR6, CON8, INT7.
        """
        print("Applying Gnome bonuses: +1 Intelligence, -1 Wisdom")
        self.intelligence += 1
        self.wisdom -= 1
        
        #Ensure strength is not below 6
        if self.strength < 6:
            print("Gnome strength is too low — raising to minimum of 6.")
            self.strength = 6
        
        #Ensure constitution is not below 8
        if self.constitution < 8:
            print("Gnome constitution too low — raising to minimum of 8.")
            self.constitution = 8
        
        #Ensure intelligence is not below 7
        if self.intelligence < 7:
            print("Gnome intelligence too low — raising to minimum of 7.")
            self.intelligence = 7
    
    
class Halfling:
    is_race = True
    
    def __init__(self):
        super().__init__()
    def apply_race_modifiers(self):
        print("Applying Halfling modifiers")
        """
        Halflings get +1DEX, -1STR and -1WIS.
        They have minimal scores: STR6, DEX8, CON10, INT6, WIS2
        """
        print("Applying Halfling bonuses: +1 Dexterity, -1 Strength, -1 Wisdom")
        self.dexterity += 1
        self.strength -= 1
        self.wisdom -= 1
    
        #Ensure strenth is not below 6
        if self.strength < 6:
            print("Halfling strength too low — raising to minimum of 6.")
            self.strength = 6
        
        #Ensure dexterity is not below 8
        if self.dexterity < 8:
            print("Halfling dexterity too low — raising to minimum of 8.")
            self.dexterity = 8
            
        #Ensure constitution is not below 10
        if self.constitution < 10:
            print("Halfling constitution too low — raising to minimum of 10.")
            self.constitution = 10

        #Ensure intelligence is not below 6
        if self.intelligence < 6:
            print("Halfling intelligence too low — raising to minimum of 6.")
            self.intelligence = 6


#Valid class combinations by race
VALID_CLASSES = {
    Human: [
        (Fighter,),
        (Ranger,),
        (Paladin,),
        (Cleric,),
        (Druid,),
        (Bard,),
        (Mage,),
        (Abjurer,),
        (Conjurer,),
        (Diviner,),
        (Enchanter,),
        (Illusionist,),
        (Invoker,),
        (Necromancer,),
        (Transmuter,),
        (Thief,),
        (Ranger, Cleric),
        (Fighter, Druid),
        (Cleric, Thief),
        (Thief, Enchanter)
    ],
    Halforc: [
        (Fighter,),
        (Cleric,),
        (Thief,),
        (Fighter, Cleric),
        (Cleric, Thief),
        (Fighter, Thief)
    ],
    Halfelf: [
        (Fighter,),
        (Ranger,),
        (Cleric,),
        (Druid,),
        (Bard,),
        (Mage,),
        (Conjurer,),
        (Diviner,),
        (Enchanter,),
        (Transmuter,),
        (Thief,),
        (Fighter, Cleric),
        (Fighter, Druid),
        (Fighter, Mage),
        (Fighter, Thief),
        (Ranger, Cleric),
        (Fighter, Cleric, Mage)
    ],
    Elf: [
        (Fighter,),
        (Ranger,),
        (Cleric,),
        (Mage,),
        (Diviner,),
        (Enchanter,),
        (Thief,),
        (Fighter, Mage),
        (Fighter, Thief),
        (Mage, Thief)
    ],
    Dwarf: [
        (Fighter,),
        (Cleric,),
        (Thief,),
        (Fighter, Cleric),
        (Fighter, Thief)
    ],
    Gnome: [
        (Fighter,),
        (Cleric,),
        (Illusionist,),
        (Thief,),
        (Fighter, Cleric),
        (Fighter, Thief),
        (Fighter, Illusionist),
        (Cleric, Illusionist),
        (Thief, Illusionist),
        (Cleric, Thief)
    ],
    Halfling: [
        (Fighter,),
        (Cleric,),
        (Thief,),
        (Fighter, Thief),
    ]
}


"""
class Gnome_Thief_Illusionist(MulticlassCharacter, Thief, Illusionist, Gnome):
    def __init__(self):
        super().__init__()  # Triggers all modifier calls

    def display(self):
        print(f"Strength: {self.display_strength() if hasattr(self, 'display_strength') else self.strength}")
        for attr in ['dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            print(f"{attr.capitalize()}: {getattr(self, attr)}")
"""

#Character creation function
def create_character(*bases, name="Unnamed Hero"):
    # Extract race and class candidates
    races = [b for b in bases if getattr(b, 'is_race', False)]
    classes = [b for b in bases if getattr(b, 'is_class', False)]

    # ❗ Enforce exactly one race
    if len(races) != 1:
        race_names = ', '.join(cls.__name__ for cls in races)
        raise ValueError(f"A character must have exactly one race. Found: {race_names or 'none'}.")

    race = races[0]
    classes_sorted = tuple(sorted(classes, key=lambda x: x.__name__))

    # Validate class combo
    legal_combos = VALID_CLASSES.get(race, [])
    legal_combos_sorted = [tuple(sorted(combo, key=lambda x: x.__name__)) for combo in legal_combos]

    if classes_sorted not in legal_combos_sorted:
        raise ValueError(
            f"Invalid class combo: {', '.join(cls.__name__ for cls in classes_sorted)} for race {race.__name__}"
        )

    # Dynamic character class
    class CustomCharacter(CharacterAssembly, race, *classes):
        def __init__(self):
            self.name = name
            super().__init__()

        def display(self):
            print(f"\n{name}'s Ability Scores:")
            print(f"Strength: {self.display_strength() if hasattr(self, 'display_strength') else self.strength}")
            for attr in ['dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
                print(f"{attr.capitalize()}: {getattr(self, attr)}")

    return CustomCharacter()

#I want to export some things with *
__all__ = [
    "create_character",
    "Human", "Halforc", "Elf", "Halfelf", "Dwarf", "Gnome", "Halfling",
    "Fighter", "Paladin", "Ranger",
    "Cleric", "Druid",
    "Bard", "Mage", "Abjurer", "Conjurer", "Diviner", "Enchanter", "Illusionist", "Invoker", "Necromancer", "Transmuter",
    "Thief"
    ]

if __name__ == "__main__":
    character = create_character(Elf, Ranger, name="Chuck")
    character.display()
    #print(character.__class__.mro())
#consider swaping print() to logger later