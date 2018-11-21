\connect postgres;

create TABLE monsters(
    name text PRIMARY KEY,
    size text,
    type text,
    subtype text,
    alignment text,
    armor_class text,
    hit_points text,
    hit_dice text,
    speed text,
    strength text,
    dexterity text,
    constitution text,
    intelligence text,
    wisdom text,
    charisma text,
    wisdom_save text,
    damage_vulnerabilities text,
    damage_resistances text,
    damage_immunities text,
    condition_immunities text,
    senses text,
    languages text,
    challenge_rating text,
    special_abilities text,
    actions text,
    constitution_save text,
    perception text,
    history text,
    legendary_actions text,
    intelligence_save text,
    religion text,
    medicine text,
    stealth text,
    dexterity_save text,
    charisma_save text,
    persuasion text,
    insight text,
    deception text,
    athletics text,
    arcana text,
    nature text,
    acrobatics text,
    strength_save text,
    reactions text[],
    survival text,
    investigation text,
    intimidation text,
    performance text,
    arctic boolean,
    coast boolean,
    desert boolean,
    forest boolean,
    grassland boolean,
    hill boolean,
    mountain boolean,
    swamp boolean,
    underdark boolean,
    underwater boolean,
    urban boolean
);

create TABLE actions(
    action_id serial PRIMARY KEY,
    name text NOT NULL,
    description text NOT NULL,
    attack_bonus integer,
    damage_dice text,
    damage_bonus text
);

create TABLE monster_actions(
    monster_name text REFERENCES monsters(name),
    monster_action_id integer REFERENCES actions(action_id)
);

create TABLE reactions(
    reaction_id serial PRIMARY KEY,
    name text NOT NULL,
    description text NOT NULL,
    attack_bonus integer

);

create TABLE monster_reactions(
    monster_name text REFERENCES monsters(name),
    monster_reaction_id integer REFERENCES reactions(reaction_id)
);

create TABLE special_abilities(
    special_abilities_id serial PRIMARY KEY,
    name text NOT NULL,
    description text NOT NULL,
    attack_bonus integer,
    damage_dice text
);

create TABLE monster_special_abilities(
    monster_name text REFERENCES monsters(name),
    monster_special_ability_id integer REFERENCES special_abilities(special_abilities_id)
);

create TABLE legendary_actions(
	legendary_action_id serial PRIMARY KEY,
	name text NOT NULL,
	description text NOT NULL,
	attack_bonus integer,
	damage_dice text
);

create TABLE monster_legendary_actions(
    monster_name text REFERENCES monsters(name),
    monster_legendary_actions_id integer REFERENCES legendary_actions(legendary_action_id)
);

create TABLE npc_info(
    appearance text,
    personality text,
    quirk text
);