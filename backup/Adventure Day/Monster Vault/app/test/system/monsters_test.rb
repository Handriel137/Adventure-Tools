require "application_system_test_case"

class MonstersTest < ApplicationSystemTestCase
  setup do
    @monster = monsters(:one)
  end

  test "visiting the index" do
    visit monsters_url
    assert_selector "h1", text: "Monsters"
  end

  test "creating a Monster" do
    visit monsters_url
    click_on "New Monster"

    fill_in "Acrobatics", with: @monster.acrobatics
    fill_in "Actions", with: @monster.actions
    fill_in "Alignment", with: @monster.alignment
    fill_in "Arcana", with: @monster.arcana
    fill_in "Armor Class", with: @monster.armor_class
    fill_in "Athletics", with: @monster.athletics
    fill_in "Challenge Rating", with: @monster.challenge_rating
    fill_in "Charisma", with: @monster.charisma
    fill_in "Charisma Save", with: @monster.charisma_save
    fill_in "Condition Immunities", with: @monster.condition_immunities
    fill_in "Constitution", with: @monster.constitution
    fill_in "Constitution Save", with: @monster.constitution_save
    fill_in "Damage Immunities", with: @monster.damage_immunities
    fill_in "Damage Resistances", with: @monster.damage_resistances
    fill_in "Damage Vulnerabilities", with: @monster.damage_vulnerabilities
    fill_in "Deception", with: @monster.deception
    fill_in "Dexterity", with: @monster.dexterity
    fill_in "Dexterity Save", with: @monster.dexterity_save
    fill_in "History", with: @monster.history
    fill_in "Hit Dice", with: @monster.hit_dice
    fill_in "Hit Points", with: @monster.hit_points
    fill_in "Insight", with: @monster.insight
    fill_in "Intelligence", with: @monster.intelligence
    fill_in "Intelligence Save", with: @monster.intelligence_save
    fill_in "Intimidation", with: @monster.intimidation
    fill_in "Investigation", with: @monster.investigation
    fill_in "Languages", with: @monster.languages
    fill_in "Legendary Actions", with: @monster.legendary_actions
    fill_in "Medicine", with: @monster.medicine
    fill_in "Name", with: @monster.name
    fill_in "Nature", with: @monster.nature
    fill_in "Perception", with: @monster.perception
    fill_in "Performance", with: @monster.performance
    fill_in "Persuasion", with: @monster.persuasion
    fill_in "Race", with: @monster.race
    fill_in "Reactions", with: @monster.reactions
    fill_in "Religion", with: @monster.religion
    fill_in "Senses", with: @monster.senses
    fill_in "Size", with: @monster.size
    fill_in "Special Abilities", with: @monster.special_abilities
    fill_in "Speed", with: @monster.speed
    fill_in "Stealth", with: @monster.stealth
    fill_in "Strength", with: @monster.strength
    fill_in "Strength Save", with: @monster.strength_save
    fill_in "Subtype", with: @monster.subtype
    fill_in "Survival", with: @monster.survival
    fill_in "Wisdom", with: @monster.wisdom
    fill_in "Wisdom Save", with: @monster.wisdom_save
    click_on "Create Monster"

    assert_text "Monster was successfully created"
    click_on "Back"
  end

  test "updating a Monster" do
    visit monsters_url
    click_on "Edit", match: :first

    fill_in "Acrobatics", with: @monster.acrobatics
    fill_in "Actions", with: @monster.actions
    fill_in "Alignment", with: @monster.alignment
    fill_in "Arcana", with: @monster.arcana
    fill_in "Armor Class", with: @monster.armor_class
    fill_in "Athletics", with: @monster.athletics
    fill_in "Challenge Rating", with: @monster.challenge_rating
    fill_in "Charisma", with: @monster.charisma
    fill_in "Charisma Save", with: @monster.charisma_save
    fill_in "Condition Immunities", with: @monster.condition_immunities
    fill_in "Constitution", with: @monster.constitution
    fill_in "Constitution Save", with: @monster.constitution_save
    fill_in "Damage Immunities", with: @monster.damage_immunities
    fill_in "Damage Resistances", with: @monster.damage_resistances
    fill_in "Damage Vulnerabilities", with: @monster.damage_vulnerabilities
    fill_in "Deception", with: @monster.deception
    fill_in "Dexterity", with: @monster.dexterity
    fill_in "Dexterity Save", with: @monster.dexterity_save
    fill_in "History", with: @monster.history
    fill_in "Hit Dice", with: @monster.hit_dice
    fill_in "Hit Points", with: @monster.hit_points
    fill_in "Insight", with: @monster.insight
    fill_in "Intelligence", with: @monster.intelligence
    fill_in "Intelligence Save", with: @monster.intelligence_save
    fill_in "Intimidation", with: @monster.intimidation
    fill_in "Investigation", with: @monster.investigation
    fill_in "Languages", with: @monster.languages
    fill_in "Legendary Actions", with: @monster.legendary_actions
    fill_in "Medicine", with: @monster.medicine
    fill_in "Name", with: @monster.name
    fill_in "Nature", with: @monster.nature
    fill_in "Perception", with: @monster.perception
    fill_in "Performance", with: @monster.performance
    fill_in "Persuasion", with: @monster.persuasion
    fill_in "Race", with: @monster.race
    fill_in "Reactions", with: @monster.reactions
    fill_in "Religion", with: @monster.religion
    fill_in "Senses", with: @monster.senses
    fill_in "Size", with: @monster.size
    fill_in "Special Abilities", with: @monster.special_abilities
    fill_in "Speed", with: @monster.speed
    fill_in "Stealth", with: @monster.stealth
    fill_in "Strength", with: @monster.strength
    fill_in "Strength Save", with: @monster.strength_save
    fill_in "Subtype", with: @monster.subtype
    fill_in "Survival", with: @monster.survival
    fill_in "Wisdom", with: @monster.wisdom
    fill_in "Wisdom Save", with: @monster.wisdom_save
    click_on "Update Monster"

    assert_text "Monster was successfully updated"
    click_on "Back"
  end

  test "destroying a Monster" do
    visit monsters_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Monster was successfully destroyed"
  end
end
