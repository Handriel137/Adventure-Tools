# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2018_10_10_011555) do

  create_table "attacks", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "damage_dice"
    t.integer "damage_bonus"
  end

  create_table "attacks_monsters", id: false, force: :cascade do |t|
    t.integer "monster_id", null: false
    t.integer "attack_id", null: false
    t.integer "monsters_id"
    t.integer "attacks_id"
    t.index ["attacks_id"], name: "index_attacks_monsters_on_attacks_id"
    t.index ["monsters_id"], name: "index_attacks_monsters_on_monsters_id"
  end

  create_table "legendary_actions", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.integer "attack_bonus"
    t.string "damage_dice"
  end

  create_table "legendary_actions_monsters", id: false, force: :cascade do |t|
    t.integer "monster_id", null: false
    t.integer "legendary_action_id", null: false
    t.integer "monsters_id"
    t.integer "legendary_actions_id"
    t.index ["legendary_actions_id"], name: "index_legendary_actions_monsters_on_legendary_actions_id"
    t.index ["monsters_id"], name: "index_legendary_actions_monsters_on_monsters_id"
  end

  create_table "monsters", force: :cascade do |t|
    t.string "name", null: false
    t.string "size"
    t.string "race"
    t.string "subtype"
    t.string "alignment"
    t.string "armor_class"
    t.string "hit_points"
    t.string "hit_dice"
    t.string "speed"
    t.string "strength"
    t.string "dexterity"
    t.string "constitution"
    t.string "intelligence"
    t.string "wisdom"
    t.string "charisma"
    t.string "wisdom_save"
    t.string "damage_vulnerabilities"
    t.string "damage_resistances"
    t.string "damage_immunities"
    t.string "condition_immunities"
    t.string "senses"
    t.string "languages"
    t.string "challenge_rating"
    t.string "constitution_save"
    t.string "perception"
    t.string "history"
    t.string "intelligence_save"
    t.string "religion"
    t.string "medicine"
    t.string "stealth"
    t.string "dexterity_save"
    t.string "charisma_save"
    t.string "persuasion"
    t.string "insight"
    t.string "deception"
    t.string "athletics"
    t.string "arcana"
    t.string "nature"
    t.string "acrobatics"
    t.string "strength_save"
    t.string "survival"
    t.string "investigation"
    t.string "intimidation"
    t.string "performance"
  end

  create_table "monsters_reactions", id: false, force: :cascade do |t|
    t.integer "monster_id", null: false
    t.integer "reaction_id", null: false
    t.integer "monsters_id"
    t.integer "reactions_id"
    t.index ["monsters_id"], name: "index_monsters_reactions_on_monsters_id"
    t.index ["reactions_id"], name: "index_monsters_reactions_on_reactions_id"
  end

  create_table "monsters_special_abilities", id: false, force: :cascade do |t|
    t.integer "monster_id", null: false
    t.integer "special_ability_id", null: false
    t.integer "monsters_id"
    t.integer "special_abilities_id"
    t.index ["monsters_id"], name: "index_monsters_special_abilities_on_monsters_id"
    t.index ["special_abilities_id"], name: "index_monsters_special_abilities_on_special_abilities_id"
  end

  create_table "reactions", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.integer "attack_bonus"
  end

  create_table "special_abilities", force: :cascade do |t|
    t.string "name", null: false
    t.string "description"
    t.integer "attack_bonus"
    t.string "damage_dice"
  end

end
