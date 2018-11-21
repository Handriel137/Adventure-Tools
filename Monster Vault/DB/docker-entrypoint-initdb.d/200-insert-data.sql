\connect postgres;

COPY monsters FROM '/sampledata/monsters.csv' CSV HEADER;
COPY actions FROM '/sampledata/actions.csv' CSV HEADER;
COPY reactions FROM '/sampledata/reactions.csv' CSV HEADER;
COPY special_abilities FROM '/sampledata/special_abilities.csv' CSV HEADER;
COPY legendary_actions FROM '/sampledata/legendary_actions.csv' CSV HEADER;
COPY monster_actions FROM '/sampledata/monster_actions.csv' CSV HEADER;
COPY monster_reactions FROM '/sampledata/monster_reactions.csv' CSV HEADER;
COPY monster_special_abilities FROM '/sampledata/monster_special_abilities.csv' CSV HEADER;
COPY monster_legendary_actions FROM '/sampledata/monster_legendary_actions.csv' CSV HEADER;
COPY npc_info FROM '/sampledata/npc_info.csv' CSV HEADER;