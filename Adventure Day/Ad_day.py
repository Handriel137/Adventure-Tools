
#!/usr/bin/python
# import nltk
import json_lines
import json
import re
import psycopg2
import mistune
import random
import string


# REGEX
re_title = re.compile("^#{1,3}([\\w\\s']+)\\n")
re_tags = re.compile("\\*{2}([\\w\\s]+)\\*{2}")
re_sceneOutline = re.compile("\\n+([^=#]+)")
dictionary = re.compile("==\n+([\\w\\W\\s]+) \\Z")
re_level = re.compile("^([1-9]{1,2})[\\w]{1,2}")

def locationQuery(location):
    conn = None
    try:

        # connect to the PostgreSQL server
        print('executing query for location...')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Running a query
        cur.execute('SELECT name FROM monsters where (%s) is TRUE;' % location)
        data = cur.fetchall()
        print(data)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def monsterQuery (monsterName):
    conn = None
    try:

        # connect to the PostgreSQL server
        print(f'************************************')
        print(f'executing query for {monsterName}...')
        print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        

        # print(monsterName)
        #Running a query
        cur.execute(f"SELECT row_to_json(monsters) from monsters where name = \'{monsterName}\';")
        data = cur.fetchall()
        # print(data[0][0])

        #strips the list and touple format
        return data[0][0]
        
 
        # display the PostgreSQL database server version
        # execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')

def npcQuery():
    conn = None
    try:

        # connect to the PostgreSQL server
        print(f'************************************')
        print(f'Getting NPC info...')
        print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Running a query for NPC traits

       	cur.execute("SELECT row_to_json(t)from (select appearance from npc_info) t OFFSET floor(random()* (SELECT COUNT(*) from npc_info)) LIMIT 1;")
        appearance = cur.fetchall()
        appearance = appearance[0][0]
        # print(appearance)
        cur.execute("SELECT row_to_json(t)from (select personality from npc_info) t OFFSET floor(random()* (SELECT COUNT(*) from npc_info)) LIMIT 1;")
        personality = cur.fetchall()
        personality = personality[0][0]
        # print(type(personality)) 
        cur.execute("SELECT row_to_json(t)from (select quirks from npc_info) t OFFSET floor(random()* (SELECT COUNT(*) from npc_info)) LIMIT 1;")
        quirks = cur.fetchall()
        quirks = quirks[0][0]
        # print(type(quirks))
        
        dicts = {**appearance, **personality, **quirks}
        # print(dicts)
        
        return dicts
        
 
        # display the PostgreSQL database server version
        # execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')
 
def actionQuery (actionName):
    conn = None
    try:

        # connect to the PostgreSQL server
        # print(f'************************************')
        # print(f'executing query for monster with {actionName}...')
        # print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Fetch a random monster from the DB that has the desired ability.
        cur.execute(f"SELECT row_to_json(t) from (SELECT monsters.* FROM monsters INNER JOIN monster_actions m2 on monsters.name = m2.monster_name INNER JOIN actions sa on sa.action_id = m2.monster_action_id WHERE lower(sa.name) LIKE lower(\'%{actionName}%\') ORDER BY random() LIMIT 1) t")
        data = cur.fetchall()
        # print(data[0][0])
        data = data[0][0]
        print(data['name'])
        #strips the list and touple format
        return data
        
 
        # display the PostgreSQL database server version
        # execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')

def getActions (monsterName):
    conn = None
    try:

        # connect to the PostgreSQL server
        # print(f'************************************')
        # print(f'getting info for {monsterName}...')
        # print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Fetch a random monster from the DB that has the desired ability.
        cur.execute(f"SELECT row_to_json(t) from (SELECT actions.* FROM actions INNER JOIN monster_actions m2 on actions.action_id = m2.monster_action_id AND monster_name = '{monsterName}') t")
        data = cur.fetchall()
        actions = []
        for item in data:
            # print(item[0])
            actions.append(item[0])
        
        # print(actions)
        return actions
        

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')  

def getSpecAbs (monsterName):
    conn = None
    try:

        # connect to the PostgreSQL server
        # print(f'************************************')
        # print(f'getting abilities for {monsterName}...')
        # print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Fetch a random monster from the DB that has the desired ability.
        cur.execute(f"SELECT row_to_json(t) from (SELECT special_abilities.* FROM special_abilities INNER JOIN monster_special_abilities m2 on special_abilities.special_abilities_id = m2.monster_special_ability_id AND monster_name = '{monsterName}') t")
        data = cur.fetchall()
        abilities = []
        for item in data:
            # print(item[0])
            abilities.append(item[0])
        
        # print(abilities)
        return abilities
        

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')

def getLegendActs (monsterName):
    conn = None
    try:

        # connect to the PostgreSQL server
        # print(f'************************************')
        # print(f'getting info for {monsterName}...')
        # print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Fetch a random monster from the DB that has the desired ability.
        cur.execute(f"SELECT row_to_json(t) from (SELECT legendary_actions.* FROM legendary_actions INNER JOIN monster_legendary_actions m2 on legendary_actions.legendary_action_id = m2.monster_legendary_actions_id AND monster_name = '{monsterName}') t")
        data = cur.fetchall()
        legends = []
        for item in data:
            # print(item[0])
            legends.append(item[0])
        
        print(legends)
        return legends
        

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')    

def specialAbilityQuery (abilityName):
    conn = None
    try:

        # connect to the PostgreSQL server
        # print(f'************************************')
        # print(f'executing query for monster with {abilityName}...')
        # print(f'************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Fetch a random monster from the DB that has the desired ability.
        cur.execute(f"SELECT row_to_json(t) from(SELECT monsters.* FROM monsters INNER JOIN monster_special_abilities m2 on monsters.name = m2.monster_name	INNER JOIN special_abilities sa on sa.special_abilities_id = m2.monster_special_ability_id WHERE lower(sa.name) LIKE lower(\'% {abilityName}%\') ORDER BY random() LIMIT 1) t")
        data = cur.fetchall()
        # print(data[0][0])
        data = data[0][0]
        # print(data['name'])
        #strips the list and touple format
        return data
        
 
        # display the PostgreSQL database server version
        # execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')

def getDictionary(string):
    #gets the dictionary from bottom of file
    dict_contents = re.findall(dictionary,string)
    dict_contents = ''.join(dict_contents)
    dict_contents = dict_contents.splitlines()
    # print(dict_contents)

    return dict_contents

def getSceneInfo(string):
    sceneOutline = re.findall(re_sceneOutline, string)
    sceneOutline = ''.join(sceneOutline)
    sceneOutline = sceneOutline.splitlines()
    # print('printing scenes')

    sceneOutput = []
    for scene in sceneOutline:
        
        if scene is '':
            pass

        elif '{' in scene:
            # print(scene)
            pass

        else:
            sceneOutput.append(scene)

    # for scene in sceneOutput:
    #     print(f'{sceneOutput.index(scene)} - {scene}') 
    return sceneOutput

def getTags(lines):
    highlights = []
    for line in lines:
        if re.findall(re_tags,line):
            highlights.extend(re.findall(re_tags,line))

    return highlights

def getLevel(highlight):
    if(re.match(re_level, highlight) is not None):
            adventure_level = re.findall(re_level, highlight)
            adventure_level = adventure_level[0]
            print(adventure_level)

def encounterQuery(CR, location):
    conn = None
    try:

        monster_list = []

        # connect to the PostgreSQL server
        # print(f'****************************************************')
        # print(f'creating an encounter for Level {CR} Adventurers...')
        # print(f'****************************************************\n')
        
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "postgres")
 
        # create a cursor
        cur = conn.cursor()
        
        #Running a query
        cur.execute(f" SELECT row_to_json(monsters) from monsters where challenge_rating <= {CR} AND {location} = true")
        data = cur.fetchall()
        

        i=0
                
        while i < len(data):
            # print(type(data[i][0]))

            # monster_list.update()
            monster = data[i][0]
            # print(monster['name'])
            monster_list.append(monster)
            i += 1

        # printing all of the monster names found.
        # for key in monster_list.keys():
        #     print(monster_list[key]['name'])

        return monster_list
        #strips the list and touple format
        # return data[0]
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')

def buildEasyEncounter(level, players, location):
    
    if(type(level) is not int):
        print("changing to integer")
        level = int(level)

    easy_xp = [0,25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
    medium_xp = [0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900]
    hard_xp = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
    deadly_xp = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]

    encounter_mulitplier = {'1':1, '2': 1.5, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2.5, '8': 2.5,  '9': 2.5,  '10': 2.5,  '11': 3, '12': 3, '13': 3,  '14': 3, '15': 4, '16':4, '17': 4}

    # determine easy XP threshold
    easy_xp_allotment = players * easy_xp[level]
    medium_xp_allotment = players * medium_xp[level]
    hard_xp_allotment = players * hard_xp[level]
    deadly_xp_allotment = players * deadly_xp[level]    
    print(easy_xp_allotment)
    easy_monsters = encounterQuery(level, location)

    # building an encounter
    encounter_xp = 0
    encounter_roster = []
    easy_encounter_monsters = easy_monsters.copy()
    while encounter_xp < easy_xp_allotment or encounter_xp <= medium_xp_allotment:
        
        #limits the number of different monsters
        if(len(encounter_roster) > 4):
            easy_encounter_monsters = encounter_roster

        # Picks a monster
        encounter_monster = random.choice(list(easy_encounter_monsters))
        xp = encounter_monster['experience']

        #monster xp is 80% of allotment and xp left in allotment
        if(xp <= (medium_xp_allotment/2) and xp <= medium_xp_allotment - encounter_xp):
            
            encounter_roster.append(encounter_monster)
            # print(f"added {encounter_monster['name']}")
            # print(f"{encounter_monster['experience']}")
            # print(len(encounter_roster))
            
            encounter_xp = 0
            
            #adds monster to the list for the encounter
            for monster in encounter_roster:
                encounter_xp += monster['experience']

            #calculates the experience multiplier based on # of monsters
            encounter_xp = encounter_xp * encounter_mulitplier[f'{len(encounter_roster)}']
        
        #if between the easy and medium range stop looking for monsters to add
        if(encounter_xp in range(easy_xp_allotment, medium_xp_allotment)):
            break

    # print("Encounter Roster\n")
    # for monster in encounter_roster:
    #     print(monster['name'])

    # print("encounter xp")
    # print(encounter_xp)
    return encounter_roster
    # print(easy_monsters)
    # for key in easy_monsters.keys():
    #     print(f"{easy_monsters[key]['name']} - {easy_monsters[key]['experience']}")
  
def buildMediumEncounter(level, players, location):
    
    if(type(level) is not int):
        print("changing to integer")
        level = int(level)

    easy_xp = [0,25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
    medium_xp = [0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900]
    hard_xp = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
    deadly_xp = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]

    encounter_mulitplier = {'1':1, '2': 1.5, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2.5, '8': 2.5,  '9': 2.5,  '10': 2.5,  '11': 3, '12': 3, '13': 3,  '14': 3, '15': 4, '16':4, '17': 4}

    # determine easy XP threshold
    easy_xp_allotment = players * easy_xp[level]
    medium_xp_allotment = players * medium_xp[level]
    hard_xp_allotment = players * hard_xp[level]
    deadly_xp_allotment = players * deadly_xp[level]    
    print(easy_xp_allotment)
    easy_monsters = encounterQuery(level, location)

    # building an encounter
    encounter_xp = 0
    encounter_roster = []
    easy_encounter_monsters = easy_monsters.copy()
    while encounter_xp < medium_xp_allotment or encounter_xp <= hard_xp_allotment:
        
        #limits the number of different monsters
        if(len(encounter_roster) > 4):
            easy_encounter_monsters = encounter_roster

        # Picks a monster
        encounter_monster = random.choice(list(easy_encounter_monsters))
        xp = encounter_monster['experience']

        #monster xp is 80% of allotment and xp left in allotment
        if(xp <= hard_xp_allotment /2 and xp <= hard_xp_allotment - encounter_xp):
            
            encounter_roster.append(encounter_monster)
            # print(f"added {encounter_monster['name']}")
            # print(f"{encounter_monster['experience']}")
            # print(len(encounter_roster))
            
            encounter_xp = 0
            
            #adds monster to the list for the encounter
            for monster in encounter_roster:
                encounter_xp += monster['experience']

            #calculates the experience multiplier based on # of monsters
            encounter_xp = encounter_xp * encounter_mulitplier[f'{len(encounter_roster)}']
        
        #if between the easy and medium range stop looking for monsters to add
        if(encounter_xp in range(medium_xp_allotment, hard_xp_allotment)):
            break

    # print("Encounter Roster\n")
    # for monster in encounter_roster:
    #     print(f"{monster['name']} - {monster['experience']}")

    # print("encounter xp")
    # print(encounter_xp)
    return encounter_roster
    # print(easy_monsters)
    # for key in easy_monsters.keys():
    #     print(f"{easy_monsters[key]['name']} - {easy_monsters[key]['experience']}")
    # print(medium_xp_allotment)
    # print(hard_xp_allotment)
    # print(deadly_xp_allotment)

def buildHardEncounter(level, players, location):
    
    if(type(level) is not int):
        print("changing to integer")
        level = int(level)

    easy_xp = [0,25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
    medium_xp = [0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900]
    hard_xp = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
    deadly_xp = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]

    encounter_mulitplier = {'1':1, '2': 1.5, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2.5, '8': 2.5,  '9': 2.5,  '10': 2.5,  '11': 3, '12': 3, '13': 3,  '14': 3, '15': 4, '16':4, '17': 4}

    # determine easy XP threshold
    easy_xp_allotment = players * easy_xp[level]
    medium_xp_allotment = players * medium_xp[level]
    hard_xp_allotment = players * hard_xp[level]
    deadly_xp_allotment = players * deadly_xp[level]    
    print(easy_xp_allotment)
    easy_monsters = encounterQuery(level, location)

    # building an encounter
    encounter_xp = 0
    encounter_roster = []
    easy_encounter_monsters = easy_monsters.copy()
    while encounter_xp < hard_xp_allotment or encounter_xp <= deadly_xp_allotment:
        
        #limits the number of different monsters
        if(len(encounter_roster) > 4):
            easy_encounter_monsters = encounter_roster

            

        # Picks a monster
        encounter_monster = random.choice(list(easy_encounter_monsters))
        xp = encounter_monster['experience']
        
        print(len(encounter_roster))

        while(len(encounter_roster) is 0 and encounter_monster['challenge_rating'] < level / 2):
            encounter_monster = random.choice(list(easy_encounter_monsters))
            xp = encounter_monster['experience']
            print("changed monster")
        
        #monster xp is 80% of allotment and xp left in allotment
        if(xp <= (deadly_xp_allotment*.8) and xp <= deadly_xp_allotment - encounter_xp):
            
            encounter_roster.append(encounter_monster)
            # print(f"added {encounter_monster['name']}")
            # print(f"{encounter_monster['experience']}")
            # print(len(encounter_roster))
            
            encounter_xp = 0
            
            #adds monster to the list for the encounter
            for monster in encounter_roster:
                encounter_xp += monster['experience']

            #calculates the experience multiplier based on # of monsters
            encounter_xp = encounter_xp * encounter_mulitplier[f'{len(encounter_roster)}']
        
        #if between the easy and medium range stop looking for monsters to add
        if(encounter_xp in range(hard_xp_allotment, deadly_xp_allotment)):
            break

    # print("Encounter Roster\n")
    # for monster in encounter_roster:
    #     print(f"{monster['name']} - {monster['experience']}")

    # print("encounter xp")
    # print(encounter_xp)
    return encounter_roster
    # print(easy_monsters)
    # for key in easy_monsters.keys():
    #     print(f"{easy_monsters[key]['name']} - {easy_monsters[key]['experience']}")
    # print(medium_xp_allotment)
    # print(hard_xp_allotment)
    # print(deadly_xp_allotment)

def buildDeadlyEncounter(level, players, location):
    
    if(type(level) is not int):
        level = int(level)

    easy_xp = [0,25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
    medium_xp = [0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900]
    hard_xp = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
    deadly_xp = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]

    encounter_mulitplier = {'1':1, '2': 1.5, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2.5, '8': 2.5,  '9': 2.5,  '10': 2.5,  '11': 3, '12': 3, '13': 3,  '14': 3, '15': 4, '16':4, '17': 4}

    # determine easy XP threshold
    easy_xp_allotment = players * easy_xp[level]
    medium_xp_allotment = players * medium_xp[level]
    hard_xp_allotment = players * hard_xp[level]
    deadly_xp_allotment = players * deadly_xp[level]    
    easy_monsters = encounterQuery(level, location)

    # building an encounter
    encounter_xp = 0
    encounter_roster = []
    easy_encounter_monsters = easy_monsters.copy()
    while encounter_xp <= deadly_xp_allotment:
        
        #limits the number of different monsters
        if(len(encounter_roster) > 4):
            easy_encounter_monsters = encounter_roster

        # Picks a monster
        encounter_monster = random.choice(list(easy_encounter_monsters))
        xp = encounter_monster['experience']

        while(len(encounter_roster) is 0 and encounter_monster['challenge_rating'] < level-2):
            encounter_monster = random.choice(list(easy_encounter_monsters))
            xp = encounter_monster['experience']
            # print(f"{encounter_monster['name']} - {encounter_monster['experience']}")

        #monster xp is 80% of allotment and xp left in allotment
        if(xp <= (deadly_xp_allotment/2) and xp <= deadly_xp_allotment - encounter_xp):
            
            encounter_roster.append(encounter_monster)
            # print(f"added {encounter_monster['name']}")
            # print(f"{encounter_monster['experience']}")
            # print(len(encounter_roster))
            
            encounter_xp = 0
            
            #adds monster to the list for the encounter
            for monster in encounter_roster:
                encounter_xp += monster['experience']

            #calculates the experience multiplier based on # of monsters
            encounter_xp = encounter_xp * encounter_mulitplier[f'{len(encounter_roster)}']
        
        #if between the easy and medium range stop looking for monsters to add
        if(encounter_xp in range(deadly_xp_allotment, (deadly_xp_allotment*2))):
            break

    # print("Encounter Roster\n")
    # for monster in encounter_roster:
    #     print(monster['name'])

    # print("encounter xp")
    # print(encounter_xp)
    return encounter_roster
    # print(easy_monsters)
    # for key in easy_monsters.keys():
    #     print(f"{easy_monsters[key]['name']} - {easy_monsters[key]['experience']}")
    # print(medium_xp_allotment)
    # print(hard_xp_allotment)
    # print(deadly_xp_allotment)

# TODO create template for monster in markdown
def monsterMarkdown(monster):
    t = f'''___
>## {monster['name']}
>*{monster['type']}, {monster['alignment']}*
> ___
> - **Armor Class** {monster['armor_class']}
> - **Hit Points** {monster['hit_points']} ({monster['hit_dice']})
> - **Speed** {monster['speed']}
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|{monster['strength']} ({monster['strength']}) |{monster['dexterity']} ({monster['dexterity']}) |{monster['constitution']} ({monster['constitution']}) |{monster['intelligence']} ({monster['intelligence']}) |{monster['wisdom']} ({monster['wisdom']}) |{monster['charisma']} ({monster['charisma']}) |
>___
> - **Damage Vulnerabilities** {monster['damage_vulnerabilities']}
> - **Damage Resistances** {monster['damage_resistances']}
> - **Damage Immunities** {monster['damage_immunities']}
> - **Condition Immunities** {monster['condition_immunities']}
> - **Senses** {monster['senses']}
> - **Languages** {monster['languages']}
> - **Challenge Rating** {monster['challenge_rating']}
>___
>'''
    # if there are no actions do nothing
    abilities = getSpecAbs(monster['name'])
    actions = getActions(monster['name'])

    # if there are no abilities do nothing
    if not abilities:
        pass
    else:
        ability_string = ''
        for ability in abilities:
            if("\n" in ability['description']):
                # print('before')
                # print(ability['description'])
                line = ability['description'].replace('\n', "")
                # print('after')
                # print(line)
            else:
                line = ability['description']
                # print(line) 
            ability_string = ability_string + f"\n> **{ability['name']}**: \n>"+line+ "\n>" 
        t += ability_string


    # if there are no actions do nothing
    if not actions:
        pass
    else:
        action_string = f'''
> ### Actions
>\n'''
        for action in actions:
            action_string = action_string + f'''> **{action['name']}**: \n>{action['description']}\n>\n''' 
        t+= action_string
    if(len(actions)+len(abilities) >=4):
        t = "___\n" + t

    # print(t)
    return t

def npcMarkdown(npc):
    text = f'''
<div class='descriptive'>
##### NPC: {npc['name']}
_{npc['description']}_
- **appearance**: {npc['appearance']}
- **personality**: {npc['personality']}
- **quirks**: {npc['quirks']}
</div>'''

    return text

if __name__ == '__main__':
    # Estimated difficulty of adventure
    adventure_level = 1
    #number of PC's for encounter building / balance
    players = 4
    # the adventure line by line
    lines = open("Sample_Adventure.txt", encoding = 'utf8').readlines()
    # The text of the adventure
    text = open("Sample_Adventure.txt", encoding = 'utf8').read()
    
    #containers for output into markdown.
    monsters = {}
    npcs = {}
    encounters = {}
    titles = {}
    
    #get the tags found in the text file.
    tags = getTags(lines)
    # print(tags)
    
    #get the scene outlines for each heading.
    scenes = getSceneInfo(text)

    #get the contents of the dictionary in json form
    contents = getDictionary(text)
    # print(contents)

    # Makes a list of monsters from dictionary compare to tags
    entry_list = []
    json_1 = json_lines.reader(contents) 
    for x in json_1:
        entry_list.append(x['name'])

    # compares dictionary entries to tags and queries for monster if not found.
    for tag in tags:

        # look for level of adventure here and 
        if(re.match(re_level, tag) is not None):
            adventure_level = re.findall(re_level, tag)
            #set to the desired level.
            adventure_level = adventure_level[0]
            # print(adventure_level)
            # print("Building an encounter")
            # buildDeadlyEncounter(adventure_level, players, 'dungeon')

        if(tag not in entry_list):
            result = monsterQuery(tag)
            if not(isinstance(result, IndexError)):
                monsters[result['name']] = result
                # print(f"added {result['name']}\n")

    json_contents = json_lines.reader(contents)

    # for all the tags in the dictionary get their results from the DB.
    for item in json_contents:
        
        NAME = item['name'].upper()
        # print(item['name'])
        
            # if(item['name'] in tags):
            #     print(f"{item['name']} - not found")
            # else:
            #     print(f"{item['name']} - Found!")

        #check if it contains a type
        if('type' in item):
            TYPE = item['type'].upper()
            #check if it is a Monster and modify if necessary
            if(TYPE == 'MONSTER'):

                if(item['type'] == 'monster'):
                    #do a query here for the monster
                    monster = monsterQuery(item['name'])
                    print(f"Name: {monster['name']}")

                    if('CR' in item):
                        # print("change the CR")
                        adjustment = item['CR']
                        

                        #upgrading monster
                        if(adjustment >= 1):
                            # print(monster['hit_points'])
                            monster['hit_points'] = str(int(monster['hit_points']) + (10 * int(adjustment)))
                            monster['challenge_rating'] = str(int(monster['challenge_rating'])+(int(adjustment)))
                            monsters[monster['name']] = monster
                            print(f"Added: {monster['name']} at CR {monster['challenge_rating']}")
                            # print(monster['challenge_rating'])
                            # print(monster['hit_points'])
                        
                        #downgrading monster
                        if(adjustment < 0):
                            # print(monster['hit_points'])
                            monster['hit_points'] = str(int(monster['hit_points']) + (10 * int(adjustment)))
                            monster['challenge_rating'] = str(int(monster['challenge_rating'])+(int(adjustment)))
                            monsters[monster['name']] = monster
                            print(f"Added: {monster['name']} at CR {monster['challenge_rating']}")

            if (TYPE == 'NPC'):
                print(f"{item['name']}")
            	#get an appearance, quirk and personality for the NPC
                npc = npcQuery()
                npc.update({'name':item['name']})

                if 'description' in item.keys():
                    npc.update({'description':item['description']})

                print(npc['name'])
                npcs[npc['name']] = npc 

        elif('ability' in item):
            #TODO a query to find all monsters that have the action and name specified.
            # print(f"{item['ability']}")
            monster = specialAbilityQuery(item['ability'])
            monsters[monster['name']] = monster
                    

        elif('action' in item):
            # TODO create query for actions
            monster = actionQuery(item['action'])
            monsters[monster['name']] = monster
    
    f= open("MARKDOWN.txt","a+")
    for key, value in monsters.items():
        monsterMD = monsterMarkdown(value) 
        f.write(f"{monsterMD}")

    for key, value in npcs.items():
        # print(value)
        npcMD = npcMarkdown(value)
        # print(npcMD)
        f.write(f"{npcMD}")    
    # monsterMarkdown(value)


## get rid of this stuff below here

    # append monster statistics
    # markdown = mistune.Markdown()
    # f.write(markdown(text))
    # with open('sample_dictionary.jsonl', 'rb') as json_data:
    # 	for item in json_lines.reader(json_data):
    # 		print(item)
    		# print(f"Name: {item['name']}")

    # for entry in entries:
    #     # print(entry)
    #     for content in contents:
    #         # print(content)
    #         if content.find(entry):
    #             print(entry)
    #             break
         
    # for line in lines:
    #     if re.findall(re_header, line):
    #         print(re.findall(re_header, line))

