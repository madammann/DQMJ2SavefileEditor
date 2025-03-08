import json
from charset import bytes_to_sequence, int_to_char, sequence_to_bytes
from skills import Skill
from inventory import Weapon

MONSTER_TABLE = {}
with open('./monsters.json', 'r') as file:
    MONSTER_TABLE = json.load(file)

class Monster:
    LENGTH = 152
    START_IDX = 344

    def __init__(self, buffer : bytearray, slot : int):
        self._buffer = buffer
        self._idx = self.START_IDX + self.LENGTH * slot

    @property
    def name(self):
        return bytes_to_sequence(self._buffer[self._idx+0:self._idx+8])
    
    @name.setter
    def name(self, v : str | bytes):
        if isinstance(v, (bytes, bytearray)) and len(v) <= 8:
            self._buffer[self._idx:self._idx+8] = v
        elif isinstance(v, str):
            self._buffer[self._idx:self._idx+8] = sequence_to_bytes(v)

    @property
    def id(self):
        return int.from_bytes(self._buffer[self._idx+24:self._idx+24+2], byteorder='little')
    
    @id.setter
    def id(self, v):
        self._buffer[self._idx+24:self._idx+24+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def guest(self):
        return bool(int.from_bytes(self._buffer[self._idx+28:self._idx+28+1], byteorder='little'))
    
    @guest.setter
    def guest(self, v):
        self._buffer[self._idx+28:self._idx+28+1] = int(bool(v)).to_bytes(1, byteorder='little')
    
    @property
    def gender(self):
        return int.from_bytes(self._buffer[self._idx+26:self._idx+26+1], byteorder='little')
    
    @gender.setter
    def gender(self, v):
        self._buffer[self._idx+26:self._idx+26+1] = int(v).to_bytes(1, byteorder='little')
    
    @property
    def synthesis_cap(self):
        return int.from_bytes(self._buffer[self._idx+27:self._idx+27+1], byteorder='little')
    
    @synthesis_cap.setter
    def synthesis_cap(self, v):
        self._buffer[self._idx+27:self._idx+27+1] = int(v).to_bytes(1, byteorder='little')
    
    @property
    def tactic(self):
        return int.from_bytes(self._buffer[self._idx+49:self._idx+49+1], byteorder='little')
    
    @tactic.setter
    def tactic(self, v):
        self._buffer[self._idx+49:self._idx+49+1] = int(v).to_bytes(1, byteorder='little')
    
    @property
    def location(self):
        return None

    @property
    def scout_id(self):
        return int.from_bytes(self._buffer[self._idx+20:self._idx+20+4], byteorder='little') #may be longer 4/6/8
    
    @scout_id.setter
    def scout_id(self, v):
        self._buffer[self._idx+20:self._idx+20+2] = int(v).to_bytes(4, byteorder='little')
    
    @property
    def max_hp(self):
        return int.from_bytes(self._buffer[self._idx+32:self._idx+32+2], byteorder='little')
    
    @max_hp.setter
    def max_hp(self, v):
        self._buffer[self._idx+32:self._idx+32+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def max_mp(self):
        return int.from_bytes(self._buffer[self._idx+34:self._idx+34+2], byteorder='little')
    
    @max_mp.setter
    def max_mp(self, v):
        self._buffer[self._idx+34:self._idx+34+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def hp(self):
        return int.from_bytes(self._buffer[self._idx+36:self._idx+36+2], byteorder='little')
    
    @hp.setter
    def hp(self, v):
        self._buffer[self._idx+36:self._idx+36+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def mp(self):
        return int.from_bytes(self._buffer[self._idx+38:self._idx+38+2], byteorder='little')
    
    @mp.setter
    def mp(self, v):
        self._buffer[self._idx+38:self._idx+38+2] = int(v).to_bytes(2, byteorder='little')
        
    @property
    def attack(self):
        return int.from_bytes(self._buffer[self._idx+40:self._idx+40+2], byteorder='little')
    
    @attack.setter
    def attack(self, v):
        self._buffer[self._idx+40:self._idx+40+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def defense(self):
        return int.from_bytes(self._buffer[self._idx+42:self._idx+42+2], byteorder='little')
    
    @defense.setter
    def defense(self, v):
        self._buffer[self._idx+42:self._idx+42+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def agility(self):
        return int.from_bytes(self._buffer[self._idx+44:self._idx+44+2], byteorder='little')
    
    @agility.setter
    def agility(self, v):
        self._buffer[self._idx+44:self._idx+44+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def wisdom(self):
        return int.from_bytes(self._buffer[self._idx+46:self._idx+46+2], byteorder='little')
    
    @wisdom.setter
    def wisdom(self, v):
        self._buffer[self._idx+46:self._idx+46+2] = int(v).to_bytes(2, byteorder='little')
    
    @property
    def level(self):
        return int.from_bytes(self._buffer[self._idx+48:self._idx+48+1], byteorder='little')
    
    @level.setter
    def level(self, v):
        self._buffer[self._idx+48:self._idx+48+1] = int(v).to_bytes(1, byteorder='little')

    @property
    def experience(self):
        return int.from_bytes(self._buffer[self._idx+52:self._idx+52+8], byteorder='little')
    
    @experience.setter
    def experience(self, v):
        self._buffer[self._idx+52] = int(v).to_bytes(8, byteorder='little')

    @property
    def unspent_skillpoints(self):
        return int.from_bytes(self._buffer[self._idx+60:self._idx+60+2], byteorder='little')
    
    @unspent_skillpoints.setter
    def unspent_skillpoints(self, v):
        self._buffer[self._idx+60:self._idx+60+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def mother_id(self):
        return int.from_bytes(self._buffer[self._idx+90:self._idx+90+2], byteorder='little')
    
    @mother_id.setter
    def mother_id(self, v):
        self._buffer[self._idx+90:self._idx+90+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def father_id(self):
        return int.from_bytes(self._buffer[self._idx+68:self._idx+68+2], byteorder='little')
    
    @father_id.setter
    def father_id(self, v):
        self._buffer[self._idx+68:self._idx+68+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def parental_grandfather_id(self):
        return int.from_bytes(self._buffer[self._idx+112:self._idx+112+2], byteorder='little')
    
    @parental_grandfather_id.setter
    def parental_grandfather_id(self, v):
        self._buffer[self._idx+112:self._idx+112+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def parental_grandmother_id(self):
        return int.from_bytes(self._buffer[self._idx+116:self._idx+116+2], byteorder='little')
    
    @parental_grandmother_id.setter
    def parental_grandmother_id(self, v):
        self._buffer[self._idx+116:self._idx+116+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def maternal_grandfather_id(self):
        return int.from_bytes(self._buffer[self._idx+114:self._idx+114+2], byteorder='little')
    
    @maternal_grandfather_id.setter
    def maternal_grandfather_id(self, v):
        self._buffer[self._idx+114:self._idx+114+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def maternal_grandmother_id(self):
        return int.from_bytes(self._buffer[self._idx+118:self._idx+118+2], byteorder='little')
    
    @maternal_grandmother_id.setter
    def maternal_grandmother_id(self, v):
        self._buffer[self._idx+118:self._idx+118+2] = int(v).to_bytes(2, byteorder='little')

    @property
    def skills(self):
        skills = [Skill(self._buffer, self._idx+120+4*i) for i in range(5)]
        return skills
    
    def set_skill(self, i, v):
        skills = self.skills
        skills[i].id = v

    def set_skillpoints(self, i, v):
        skills = self.skills
        skills[i].skillpoints = v
    
    def get_skill(self, i):
        skills = self.skills
        return skills[i]
    
    @property
    def weapon(self):
        return int.from_bytes(self._buffer[self._idx+51:self._idx+51+1], byteorder='little') #may be longer
    
    @weapon.setter
    def weapon(self, v):
        self._buffer[self._idx+51:self._idx+51+1] = int(v).to_bytes(1, byteorder='little')

    @property
    def mother_name(self):
        return bytes_to_sequence(self._buffer[self._idx+92:self._idx+92+8]) #RED LEFT SIDE PARENT (MINUS)
    
    @mother_name.setter
    def mother_name(self, v : str | bytes):
        if isinstance(v, (bytes, bytearray)) and len(v) <= 8:
            self._buffer[self._idx+92:self._idx+92+8] = v
        elif isinstance(v, str):
            self._buffer[self._idx+92:self._idx+92+8] = sequence_to_bytes(v)

    @property
    def father_name(self):
        return bytes_to_sequence(self._buffer[self._idx+70:self._idx+70+8])
    
    @father_name.setter
    def father_name(self, v : str | bytes):
        if isinstance(v, (bytes, bytearray)) and len(v) <= 8:
            self._buffer[self._idx+70:self._idx+70+8] = v
        elif isinstance(v, str):
            self._buffer[self._idx+70:self._idx+70+8] = sequence_to_bytes(v)

    @property
    def level_cap(self):
        return int.from_bytes(self._buffer[self._idx+29:self._idx+29+1], byteorder='little')
    
    @level_cap.setter
    def level_cap(self, v):
        self._buffer[self._idx+29] = int(v).to_bytes(1, byteorder='little')

# Byte coverage:
# 0-7: name
# 8-19: UNMAPPED # original owner id?
# 20-23: scout_id (4 bytes?)
# 24-25: id
# 26: gender (0 = male, 1 = female, 2 = inter)
# 27: synthesis_cap
# 28: guest
# 29: level cap (0,1,2)
# 30-31: UNMAPPED INVISIBLE USEAGE
# 32-33: max_hp
# 34-35: max_mp
# 36-37: hp
# 38-39: mp
# 40-41: attack
# 42-43: defense
# 44-45: agility
# 46-47: wisdom
# 48: level
# 49: tactic (0=show no mercy ,1=mix it up, 2=focus on healing, 3=dont use magic skills)
# 51: weapon
# 52-59: experience (8 bytes)
# 60-61: unspent_skillpoints (2 bytes in use since <999)
# 62-67: UNMAPPED (seemingly unused, I think this may be a guest flag of parents)
# 68-69: father_id
# 70-77: father_name
# 90-91: mother_id
# 92-99: mother_name
# 112-113: parental_grandfather_id
# 114-115: maternal_grandfather_id
# 116-117: parental_grandmother_id
# 118-119: maternal_grandmother_id
# 120-139: skills (5 skills, 4 bytes each)
# 140-151: UNUSED (No idea what this could be, a few bytes may be the location of monster storage/team, possibly in mem battles only)