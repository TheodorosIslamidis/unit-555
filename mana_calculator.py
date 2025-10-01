import streamlit as st
import pandas as pd

def calculate_modifier(score: int) -> int:
    """Calculates the ability modifier for a given score."""
    return (score - 10) // 2

def get_bonus_spells(modifier: int, max_spell_level: int, has_divine_feat: bool = False) -> list[int]:
    """
    Calculates the bonus spells per day for each spell level.
    
    Args:
        modifier: The ability modifier.
        max_spell_level: The highest spell level to calculate for.
        has_divine_feat: If True, calculates bonus spells for levels 10-25.
        
    Returns:
        A list of integers representing the bonus spells for each level.
    """
    if modifier <= 0:
        return [0] * max_spell_level
    
    bonus_spells = []
    for spell_level in range(1, max_spell_level + 1):
        if modifier >= spell_level:
            # Use divine formula for levels 10+ only if the feat is enabled
            if has_divine_feat and spell_level >= 10:
                # Formula for Divine Spellcasting feat (levels 10+)
                spells = (modifier - spell_level) // 4 + 2
            elif spell_level < 10:
                # Standard formula for spell levels 1-9
                spells = (modifier - spell_level) // 4 + 1
            else:
                # No bonus spells for levels 10+ without the feat
                spells = 0
            bonus_spells.append(spells)
        else:
            bonus_spells.append(0)
            
    return bonus_spells

st.set_page_config(page_title="Bonus Spell Calculator", layout="centered")

st.title("🔮 Bonus Spell Calculator")

st.write(
    "This tool calculates the number of bonus spells per day a character "
    "receives based on their primary spellcasting ability score (e.g., Intelligence, "
    "Wisdom, or Charisma)."
)

# --- System Selection ---
system_choice = st.radio(
    "Select your calculation system:",
    ('D&D 3.5e / Pathfinder', 'Final Fantasy Mana System'),
    help="Choose the rule system to calculate your bonus spells or mana."
)

has_divine_feat = st.checkbox(
    "Character has the Divine Spellcasting feat (or equivalent)?",
    help="Check this if you are using rules for epic/divine spells beyond 9th level."
)

# --- User Input ---
ability_score = st.number_input(
    "Enter your character's ability score:",
    min_value=1,
    value=10,
    step=1,
    help="Enter the score for your character's spellcasting ability (e.g., 18)."
)

max_spell_level_input = st.number_input(
    "What is your character's highest spell level?",
    min_value=1,
    value=9,
    step=1,
    help="Enter the highest level of spell your character can cast (e.g., 9 for a 17th-level wizard)."
)

# --- Calculations ---
modifier = calculate_modifier(ability_score)
bonus_spells_list = get_bonus_spells(modifier, max_spell_level_input, has_divine_feat)

# --- Display Results ---
st.header("Results")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Ability Score", value=ability_score)
with col2:
    st.metric(label="Ability Modifier", value=f"{modifier:+}")


if system_choice == 'D&D 3.5e / Pathfinder':
    if ability_score < 12:
        st.info("An ability score of 11 or lower does not grant any bonus spells.")
    else:
        st.write("### Bonus Spells per Day")
        
        # Create a DataFrame for better table display
        num_levels = len(bonus_spells_list)
        spell_levels = []
        for i in range(num_levels):
            level = i + 1
            suffix = "th" if 11 <= level <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(level % 10, "th")
            spell_levels.append(f"{level}{suffix}")

        
        df = pd.DataFrame({
            'Spell Level': spell_levels,
            'Bonus Spells': bonus_spells_list
        })
        
        # Filter out rows where there are no bonus spells to keep the table clean
        df_display = df[df['Bonus Spells'] > 0].set_index('Spell Level')
        
        if not df_display.empty:
            st.table(df_display)
        else:
            st.info("No bonus spells are granted at this ability score.")

elif system_choice == 'Final Fantasy Mana System':
    if ability_score < 12:
        st.info("An ability score of 11 or lower does not grant any bonus mana.")
        st.metric(label="Total Bonus Mana", value=0)
    else:
        # Calculate total mana: sum of (spell_level * bonus_spells_for_that_level)
        total_mana = sum((i + 1) * spells for i, spells in enumerate(bonus_spells_list))
        
        st.metric(label="Total Bonus Mana", value=total_mana)
        
        if total_mana > 0:
            st.write("#### Mana Calculation Breakdown")
            st.caption("Each bonus spell slot contributes its spell level to the total mana pool.")
            # We can reuse the DataFrame logic to show the breakdown
            num_levels = len(bonus_spells_list)
            spell_levels = [i + 1 for i in range(num_levels)]
            df = pd.DataFrame({'Spell Level': spell_levels, 'Bonus Spells': bonus_spells_list[:num_levels]})
            df['Mana Value'] = df['Spell Level'] * df['Bonus Spells']
            st.table(df[df['Bonus Spells'] > 0].set_index('Spell Level'))

st.markdown("---")
st.caption("This calculator is based on the rules for bonus spells found in games like D&D 3.5e and Pathfinder 1e.")
