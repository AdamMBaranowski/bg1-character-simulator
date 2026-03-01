from character_generator import *

# Define your Power Builds
POWER_BUILDS = {
        
    "Paladin": {
        "classes": (Human, Paladin),
        "build": {
            "exceptional_strength": 00,
            "strength": 18,
            "dexterity": 6,
            "constitution": 18,
            "intelligence": 3,
            "wisdom": 13,
            "charisma": 18
        }
    },
    
    "Halfelf Bard": {
        "classes": (Halfelf, Bard),
        "build": {
            "strength": 8,
            "dexterity": 18,
            "constitution": 16,
            "intelligence": 18,
            "wisdom": 3,
            "charisma": 18
        }
    },
    
    "Halfelf Druid" : {
        "classes": (Halfelf, Druid),
        "build": {
            "strength": 8,
            "dexterity": 15,
            "constitution": 16,
            "intelligence": 4,
            "wisdom": 18,
            "charisma": 18
        }
    },

    "Halfelf Fighter/Druid (PC)" : {
        "classes": (Halfelf, Fighter, Druid),
        "build": {
            "strength": 15,
            "dexterity": 6,
            "constitution": 18,
            "intelligence": 4,
            "wisdom": 18,
            "charisma": 18
        }
    },

    "Halfelf Fighter/Druid (ID)" : {
        "classes": (Halfelf, Fighter, Druid),
        "build": {
            "exceptional_strength": 00,
            "strength": 18,
            "dexterity": 6,
            "constitution": 18,
            "intelligence": 4,
            "wisdom": 18,
            "charisma": 15
        }
    },

    "Halfelf Ranger/Cleric (ID)": {
        "classes": (Halfelf, Ranger, Cleric),
        "build": {
            "exceptional_strength": 00,
            "strength": 18,
            "dexterity": 18,
            "constitution": 18,
            "intelligence": 4,
            "wisdom": 18,
            "charisma": 3
        }
    },

    #Elf Rangers have their mins. so high that they re-roll quickly enabling more powerful builds
    "Elf Ranger": {
        "classes": (Elf, Ranger),
        "build": {
            "exceptional_strength": 25,
            "strength": 18,
            "dexterity": 19,
            "constitution": 17,
            "intelligence": 8,
            "wisdom": 14,
            "charisma": 8
        }
    },

    "Elf Fighter/Thief": {
        "classes": (Elf, Fighter, Thief),
        "build": {
            #"exceptional_strength": 50,
            "strength": 9,
            "dexterity": 19,
            "constitution": 17,
            "intelligence": 8,
            "wisdom": 3,
            "charisma": 18
        }
    },

    "Elf Enchanter (Challenge)": {
        "classes": (Elf, Enchanter),
        "build": {
            "strength": 6,
            "dexterity": 19,
            "constitution": 16,
            "intelligence": 18,
            "wisdom": 3,
            "charisma": 18
        }
    },
      
    "Dwarf Fighter/Cleric": {
        "classes": (Dwarf, Fighter, Cleric),
        "build": {
            "exceptional_strength": 00,
            "strength": 18,
            "dexterity": 17,
            "constitution": 19,
            "intelligence": 3,
            "wisdom": 18,
            "charisma": 1
        }
    },

    "Dwarf Fighter/Thief (Challenge)": {
        "classes": (Dwarf, Fighter, Thief),
        "build": {
            "exceptional_strength": 00,
            "strength": 18,
            "dexterity": 17,
            "constitution": 19,
            "intelligence": 3,
            "wisdom": 3,
            "charisma": 16
        }
    },

    "Gnome Illusionist/Thief": {
        "classes": (Gnome, Illusionist, Thief),
        "build": {
            "strength": 8,
            "dexterity": 18,
            "constitution": 18,
            "intelligence": 19,
            "wisdom": 2,
            "charisma": 16
        }
    },

    "Gnome Cleric/Thief (Challenge)": {
        "classes": (Gnome, Cleric, Thief),
        "build": {
            "strength": 18,
            "dexterity": 18,
            "constitution": 18,
            "intelligence": 7,
            "wisdom": 16,
            "charisma": 3
        }
    },

    "Halfling Fighter/Thief": {
        "classes": (Halfling, Fighter, Thief),
        "build": {
            "strength": 9,
            "dexterity": 19,
            "constitution": 18,
            "intelligence": 6,
            "wisdom": 2,
            "charisma": 18
        }
    },
        
}
