require 'test_helper'

class MonstersControllerTest < ActionDispatch::IntegrationTest
  setup do
    @monster = monsters(:one)
  end

  test "should get index" do
    get monsters_url
    assert_response :success
  end

  test "should get new" do
    get new_monster_url
    assert_response :success
  end

  test "should create monster" do
    assert_difference('Monster.count') do
      post monsters_url, params: { monster: { acrobatics: @monster.acrobatics, actions: @monster.actions, alignment: @monster.alignment, arcana: @monster.arcana, armor_class: @monster.armor_class, athletics: @monster.athletics, challenge_rating: @monster.challenge_rating, charisma: @monster.charisma, charisma_save: @monster.charisma_save, condition_immunities: @monster.condition_immunities, constitution: @monster.constitution, constitution_save: @monster.constitution_save, damage_immunities: @monster.damage_immunities, damage_resistances: @monster.damage_resistances, damage_vulnerabilities: @monster.damage_vulnerabilities, deception: @monster.deception, dexterity: @monster.dexterity, dexterity_save: @monster.dexterity_save, history: @monster.history, hit_dice: @monster.hit_dice, hit_points: @monster.hit_points, insight: @monster.insight, intelligence: @monster.intelligence, intelligence_save: @monster.intelligence_save, intimidation: @monster.intimidation, investigation: @monster.investigation, languages: @monster.languages, legendary_actions: @monster.legendary_actions, medicine: @monster.medicine, name: @monster.name, nature: @monster.nature, perception: @monster.perception, performance: @monster.performance, persuasion: @monster.persuasion, race: @monster.race, reactions: @monster.reactions, religion: @monster.religion, senses: @monster.senses, size: @monster.size, special_abilities: @monster.special_abilities, speed: @monster.speed, stealth: @monster.stealth, strength: @monster.strength, strength_save: @monster.strength_save, subtype: @monster.subtype, survival: @monster.survival, wisdom: @monster.wisdom, wisdom_save: @monster.wisdom_save } }
    end

    assert_redirected_to monster_url(Monster.last)
  end

  test "should show monster" do
    get monster_url(@monster)
    assert_response :success
  end

  test "should get edit" do
    get edit_monster_url(@monster)
    assert_response :success
  end

  test "should update monster" do
    patch monster_url(@monster), params: { monster: { acrobatics: @monster.acrobatics, actions: @monster.actions, alignment: @monster.alignment, arcana: @monster.arcana, armor_class: @monster.armor_class, athletics: @monster.athletics, challenge_rating: @monster.challenge_rating, charisma: @monster.charisma, charisma_save: @monster.charisma_save, condition_immunities: @monster.condition_immunities, constitution: @monster.constitution, constitution_save: @monster.constitution_save, damage_immunities: @monster.damage_immunities, damage_resistances: @monster.damage_resistances, damage_vulnerabilities: @monster.damage_vulnerabilities, deception: @monster.deception, dexterity: @monster.dexterity, dexterity_save: @monster.dexterity_save, history: @monster.history, hit_dice: @monster.hit_dice, hit_points: @monster.hit_points, insight: @monster.insight, intelligence: @monster.intelligence, intelligence_save: @monster.intelligence_save, intimidation: @monster.intimidation, investigation: @monster.investigation, languages: @monster.languages, legendary_actions: @monster.legendary_actions, medicine: @monster.medicine, name: @monster.name, nature: @monster.nature, perception: @monster.perception, performance: @monster.performance, persuasion: @monster.persuasion, race: @monster.race, reactions: @monster.reactions, religion: @monster.religion, senses: @monster.senses, size: @monster.size, special_abilities: @monster.special_abilities, speed: @monster.speed, stealth: @monster.stealth, strength: @monster.strength, strength_save: @monster.strength_save, subtype: @monster.subtype, survival: @monster.survival, wisdom: @monster.wisdom, wisdom_save: @monster.wisdom_save } }
    assert_redirected_to monster_url(@monster)
  end

  test "should destroy monster" do
    assert_difference('Monster.count', -1) do
      delete monster_url(@monster)
    end

    assert_redirected_to monsters_url
  end
end
