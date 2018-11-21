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

ActiveRecord::Schema.define(version: 2018_09_25_004609) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "monsters", force: :cascade do |t|
    t.text "name"
    t.text "size"
    t.text "race"
    t.text "subtype"
    t.text "alignment"
    t.text "armor_class"
    t.text "hit_points"
    t.text "hit_dice"
    t.text "speed"
    t.text "strength"
    t.text "dexterity"
    t.text "constitution"
    t.text "intelligence"
    t.text "wisdom"
    t.text "charisma"
    t.text "wisdom_save"
    t.text "damage_vulnerabilities"
    t.text "damage_resistances"
    t.text "damage_immunities"
    t.text "condition_immunities"
    t.text "senses"
    t.text "languages"
    t.text "challenge_rating"
    t.text "special_abilities"
    t.text "actions"
    t.text "constitution_save"
    t.text "perception"
    t.text "history"
    t.text "legendary_actions"
    t.text "intelligence_save"
    t.text "religion"
    t.text "medicine"
    t.text "stealth"
    t.text "dexterity_save"
    t.text "charisma_save"
    t.text "persuasion"
    t.text "insight"
    t.text "deception"
    t.text "athletics"
    t.text "arcana"
    t.text "nature"
    t.text "acrobatics"
    t.text "strength_save"
    t.text "reactions"
    t.text "survival"
    t.text "investigation"
    t.text "intimidation"
    t.text "performance"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
