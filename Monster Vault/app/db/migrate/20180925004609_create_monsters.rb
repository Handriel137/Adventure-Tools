class CreateMonsters < ActiveRecord::Migration[5.2]
  def change
    create_table :monsters do |t|
      t.text :name
      t.text :size
      t.text :race
      t.text :subtype
      t.text :alignment
      t.text :armor_class
      t.text :hit_points
      t.text :hit_dice
      t.text :speed
      t.text :strength
      t.text :dexterity
      t.text :constitution
      t.text :intelligence
      t.text :wisdom
      t.text :charisma
      t.text :wisdom_save
      t.text :damage_vulnerabilities
      t.text :damage_resistances
      t.text :damage_immunities
      t.text :condition_immunities
      t.text :senses
      t.text :languages
      t.text :challenge_rating
      t.text :special_abilities
      t.text :actions
      t.text :constitution_save
      t.text :perception
      t.text :history
      t.text :legendary_actions
      t.text :intelligence_save
      t.text :religion
      t.text :medicine
      t.text :stealth
      t.text :dexterity_save
      t.text :charisma_save
      t.text :persuasion
      t.text :insight
      t.text :deception
      t.text :athletics
      t.text :arcana
      t.text :nature
      t.text :acrobatics
      t.text :strength_save
      t.text :reactions
      t.text :survival
      t.text :investigation
      t.text :intimidation
      t.text :performance

      t.timestamps
    end
  end
end
