# Cannon Distance Calculator
## Overview
**This program calculates the distance traveled by a cannonball in three different scenarios based on user inputs. It utilizes physics principles and trigonometry to determine how far the cannonball will travel, given its speed, angle, and height. This is a useful tool for understanding projectile motion in various contexts.**

## 🚀 Features
- **Scenario 1:** Horizontal Cannon: Calculate the distance traveled by a cannonball fired horizontally from a given height.
- **Scenario 2:** Angled Cannon at the Same Level: Calculate the distance traveled by a cannonball fired at an angle when the cannon and target are at the same height.
- **Scenario 3:** Angled Cannon at a Lower Level: Calculate the distance traveled by a cannonball fired at an angle when the cannon is at a height above the target.
## 🛠️ How to Use
- **Run the Program:** Start the script to begin the calculations.
- **Choose a Scenario:** Select one of the three scenarios.
- **Enter Parameters:**
  - For **Scenario 1**, provide the speed of the cannonball and the height of the cannon.
  - For **Scenario 2**, provide the speed of the cannonball and the angle at which it is fired.
  - For **Scenario 3**, provide the speed of the cannonball, the height of the cannon, and the angle at which it is fired.
- **View Results:** The program will calculate and display the distance the cannonball will travel based on the chosen scenario.
- **Retry or Exit:** Choose to perform another calculation or exit the program.
## 📜 Code Breakdown
**cannon Class**
- **Constructor (__init__):** Initializes the cannonball parameters (speed, angle, height) and the scenario choice.

- **Method (shooter):** Performs the calculation based on the selected scenario:

    - **Scenario 1:** Calculates the distance using horizontal motion equations.
    - **Scenario 2:** Uses projectile motion equations to calculate the distance.
    - **Scenario 3:** Accounts for an initial height and calculates the distance using projectile motion equations.
