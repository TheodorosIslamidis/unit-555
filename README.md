# 🔮 Mana & Bonus Spell Calculator

A simple yet powerful Streamlit web application designed for tabletop RPG players to calculate bonus spells or a mana pool based on their character's ability scores. This tool is primarily based on the rules found in **Dungeons & Dragons 3.5e** and **Pathfinder 1e**, with flexible options for homebrew systems.

## ✨ Features

- **Dual System Calculation**: Choose between two different calculation methods:
  - **D&D 3.5e / Pathfinder**: Displays the number of bonus spell slots gained for each spell level (1-9).
  - **Final Fantasy Mana System**: Calculates a total mana pool where each bonus spell slot contributes its spell level to the total (e.g., a 3rd-level slot is worth 3 mana).
- **Epic & Divine Spell Support**: Includes an option for characters with feats like "Divine Spellcasting," extending the calculation to support spell levels from 10th and higher levels.
- **Uncapped Ability Scores**: Enter any ability score, no matter how high, to support epic-level and mythic characters.
- **Clean & Interactive UI**: A straightforward and easy-to-use interface built with Streamlit.
- **Detailed Breakdown**: For the mana system, the app provides a clear table showing how the total mana pool is calculated from the bonus spell slots.

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

You need to have Python 3.7+ installed on your system.

### Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory in your terminal.

3. Install the required Python packages using pip:
   ```sh
   pip install streamlit pandas
   ```

### Running the Application

1. In your terminal, run the following command from the project's root directory:
   ```sh
   streamlit run mana_calculator.py
   ```

2. Your default web browser will open with the application running locally.

## 📖 How to Use

1.  **Select your calculation system**:
    - Choose `D&D 3.5e / Pathfinder` to see a list of bonus spell slots per level.
    - Choose `Final Fantasy Mana System` to see a total bonus mana pool.

2.  **Enable Divine Spellcasting (Optional)**:
    - Check the box if your character has a feat or ability that grants bonus spells for levels 10 and higher. This option works for both calculation systems.

3.  **Enter your ability score**:
    - Input your character's primary spellcasting ability score (e.g., Intelligence, Wisdom, or Charisma).

4.  **View the Results**:
    - The application will instantly display your ability modifier and the calculated bonus spells or mana based on your selections.

---

*This tool is based on the SRD (System Reference Document) rules for D&D 3.5e and is adaptable for similar d20 systems.*