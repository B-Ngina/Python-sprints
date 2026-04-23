# Python-sprints
A dedicated log of my daily technical problem-solving. This repository tracks my journey in mastering Python and SQL through consistent, daily challenges focused on algorithmic logic and data manipulation.

# Daily Analytical Logic Logs

| Day | Challenge | Core Concepts | Link |
| :--- | :--- | :--- | :--- |
| 01 | **Palindrome Middle** | String Slicing `[::-1]`, Integer Division `//`, Parity Logic | [View Code](./Python/01_palindrome_middle.py) |
| 02 | **FizzBuzz Validator** | `enumerate()`, Type Check, Modulo Math | [View Code](./Python/02_fizzbuzz_validator.py) |
| 03 | **Bingo Sequencer** | Dictionary Mapping, String Formatting | [View Code](./Python/03_bingo_sequencer.py) |
| 04 | **Spiral Matrix** | 2D Arrays, Boundary Management| [View Code](./Python/04_spiral_matrix.py) |
| 05 | **Name Initializer** |	String Splitting, List Joining, f-strings | [View Code](./Python/05_name_initializer.py) |
| 06 | **Alphabetical Max** |	max(key=str.lower) | [View Code](./Python/06_max_letter.py) |
| 07 | **Sort and Swap** | .sort() & Modulo | [View Code](./Python/07_sort_swap.py) |
| 08 | **String Math Parser** |	Regex \d+/\D+ & Gap-Parity Math |	[View Code](./Python/08_string_math.py) |
| 09 | **Vigenère Decoder** |	ASCII Mapping & Modular Wrap-around | [View Code](./Python/09_decoder.py) |
| 10 | **Acronym Resolver** |	Tokenization & Pattern Matching | [View Code](./Python/10_acronyms.py) |
| 11 | **Odd Word Filter** | String Length Parity & List Joins | [View Code](./Python/11_odd_words.py) |
| 12 | **Earth Day Cleanup** | State Tracking & Modular Math | [View Code](./Python/12_cleanup.py) |
| 13 | **Time Direction** | Minutes Normalization & Circular Modulo | [View Code](./Python/13_time_dir.py) |

#### [01] Palindrome Middle
**Problem:** Find the true center of a symmetric string.

**Logic:**
Symmetry Filter: Validates using `s[::-1]` (O(n) time).

Parity-Switch: Uses `% 2` to toggle between single-point median and cluster median.

Precision: Applied floor division `//` to avoid index floating errors.

#### [02] FizzBuzz Validator
**Problem:** Verify if a list follows FizzBuzz rules from any starting point.

**Logic:**
Sequence Anchoring: Finds the first integer to calculate the sequence's starting value.

Validation: Re-runs the FizzBuzz logic (modulo 3, 5, and 15) to ensure every list item matches the mathematical expectation.

#### [03] Bingo Sequencer
**Problem:** Find the next sequential Bingo number, handling column transitions and resetting at the end.

**Logic:**
Boundary Mapping: Uses a dictionary to define the upper limit for each letter (B=15, I=30, etc.).

Column Transition: If a number hits its limit, the `find()` method locates the next letter in "BINGO" to shift columns.

Hard Reset: Specifically checks for "O75" to wrap the sequence back to the starting "B1".

#### [04] Spiral Matrix
**Problem:** Convert a 2D matrix into a 1D array by traversing it in a clockwise spiral.

**Logic:**
Layer-by-Layer Shrinking: Sets four boundaries (Top, Bottom, Left, Right) and moves inward after each full side is traversed.

Directional Control: Uses four distinct for loops to handle the Right-Down-Left-Up movement pattern.

Overlap Prevention: Includes conditional checks within the loop to ensure rows or columns aren't processed twice as the boundaries meet in the center.

#### [05] Name Initializer
**Problem**: Convert a full name string into uppercase initials separated by dots.

**Logic**:

Tokenization: Uses .split() to break the string into individual names regardless of how many spaces are used.

Formatting: Extracts the character at index 0 for each name and applies .upper() to ensure consistency.

Reconstruction: Uses a loop and f-strings to append dots, then joins the list back into a single string.

#### [06] Alphabetical Max
**Problem**: Find the letter in a string that appears last in the alphabet while preserving its original casing.

**Logic**:

Character Filtering: Uses a list comprehension with .isalpha() to strip out numbers and symbols.

Case-Insensitive Comparison: Implements max(key=str.lower) to treat "W" and "w" equally during the search.

Originality: Returns the character in its original form (e.g., "W") rather than forcing it to lowercase.

#### [07] Sort and Swap
**Problem**: Sort an array ascendingly, then swap every element at a multiple-of-3 index with the item preceding it.

**Logic**:

Pre-sorting: Uses .sort() to establish a baseline order before any index manipulation occurs.

Index Multiples: Employs if i % 3 == 0 to pinpoint target indices while starting the loop at 1 to avoid a "before index 0" error.

Backward-Looking Swap: Uses arr[i], arr[i-1] for the swap. Because we look backward, we can safely iterate through the full len(arr) without skipping the final element.

#### [08] String Math Parser
**Problem**: Perform math on numbers hidden in a string based on the count of characters between them (Even = Add, Odd = Subtract).

**Logic**:

Regex Extraction: Uses re.findall to split the string into a list of numbers (\d+) and a list of separators (\D+).

Alignment: Employs gaps.pop(0) to remove leading non-digits, ensuring the first operator correctly corresponds to the space between the first and second numbers.

Cumulative Result: Iterates through the lists using a "look-back" index (i-1) to check the gap length while updating a running total.

#### [09] Vigenère-Style Decoder
**Problem**: Decode a message using a key derived from historical challenge titles (multiples of 25), applying a backward Caesar shift.

**Logic**:

Decodes a string using a repeating key and backward alphabetical shifts. 

Key Synchronization: A key_idx increments only for letters, skipping spaces so the key stays aligned with the message. 

1-26 Normalization: Converts characters to their alphabetical position ($A=1, Z=26$) to make the math intuitive.

Uses if decoded <= 0: + 26 to explicitly force the alphabet to loop from A back to Z.Re-encoding: Maps the calculated positions back to ASCII for the final output.

#### [10] Acronym Resolver
**Problem**: Match an acronym to its corresponding full organization name from a predefined list.

**Logic**:

String Tokenization: Uses .split() to break full names into individual word lists.

List Comprehension: Generates a temporary acronym by extracting the first character (word[0]) from each token.

Normalization: Applies .upper() to both the generated string and the input to ensure the match is case-insensitive.

Linear Search: Iterates through the list and returns the first name that yields a matching pattern.

#### [11] Odd Word Filter
**Problem**: Extract only words with an odd character count from a sentence and reassemble them.

**Logic**:

Tokenization: Splits the input string into a list using .split().

Parity Check: Uses len(word) % 2 != 0 to identify odd lengths (where the remainder after dividing by 2 is not zero).

Collection & Assembly: Collects matching strings into a list and uses " ".join() to restore the original sentence spacing format.

##### [12] Earth Day Cleanup Crew
**Problem**: Calculate a complex score based on base values, consecutive streaks, and recurring item multipliers.

**Logic**:

Type Checking: Uses isinstance() to differentiate between standard item strings and rare item lists.

State Tracking: Maintains streak_item and streak_bonus variables to increment points for consecutive duplicates.

Modular Multipliers: Applies i % 5 == 0 to trigger bonuses every fifth item, using floor division to scale the multiplier ($2\times, 3\times, 4\times$, etc.).

Lookup Efficiency: Utilizes a dictionary for $O(1)$ access to item base values.

#### [13] Time Direction Finder
**Problem**: Determine the shortest path (forward or backward) between two 24-hour timestamps.

**Logic**:

Time Normalization: Converts "HH:MM" strings into a single integer (total minutes from 00:00) using split and map.

Circular Distance Calculation: Employs the modulo operator (% 1440) to calculate distance on a 24-hour loop, automatically accounting for the midnight wrap-around.

Comparison Logic: Compares the forward and backward results to return the optimal direction.



