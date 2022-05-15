# Snakes Cafe

## Features: 
1. Intro message
   - Run one time with menu
   - Put in *variable* in case something is to change
2. Menu
   - Appetizers
   - Entrees
   - Desserts
   - Beverages

    ### Run conditions
   - Run one time with Intro message
   - Create individual variables for each category to help with future changes
3. Acknowledgement of order
  - Variable for user input to track what was ordered
  - Check dictionary to see if previously ordered and add one to existing qty
4. Option to exit (use 'quit')
  - Check user input variable to see if 'quit' was entered
5. Track quantity of items ordered (e.g., 2 Wings orders)
  - Use dictionary
    - Entry should be *Item: qty*
    - Start all items at qty 0 *or*
    - Only add to dictionary when an item is ordered

Need 6 variables and a dictionary

## Changes realized during coding
The single most significant change realized during the coding was that the 
code was going to be repetitive by having the menu listed and then creating 
lists to handle the orders.  This was refactored by using dictionaries instead.

Unfortunately, due to time constraints, refactoring of the if/elif 
statements into a single set of the statements was not able to be done.