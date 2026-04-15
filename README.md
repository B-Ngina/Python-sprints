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

#### [01] Palindrome Middle
**Problem:** Find the true center of a symmetric string.
**Logic:**
- Symmetry Filter: Validates using `s[::-1]` (O(n) time).
- Parity-Switch: Uses `% 2` to toggle between single-point median and cluster median.
- Precision: Applied floor division `//` to avoid index floating errors.

#### [02] FizzBuzz Validator
**Problem:** Verify if a list follows FizzBuzz rules from any starting point.
**Logic:**
- Sequence Anchoring: Finds the first integer to calculate the sequence's starting value.
- Validation: Re-runs the FizzBuzz logic (modulo 3, 5, and 15) to ensure every list item matches the mathematical expectation.

#### [03] Bingo Sequencer
**Problem:** Find the next sequential Bingo number, handling column transitions and resetting at the end.
**Logic:**
- Boundary Mapping: Uses a dictionary to define the upper limit for each letter (B=15, I=30, etc.).
- Column Transition: If a number hits its limit, the `find()` method locates the next letter in "BINGO" to shift columns.
- Hard Reset: Specifically checks for "O75" to wrap the sequence back to the starting "B1".

#### [04] Spiral Matrix
**Problem:** Convert a 2D matrix into a 1D array by traversing it in a clockwise spiral.
**Logic:**
- Layer-by-Layer Shrinking: Sets four boundaries (Top, Bottom, Left, Right) and moves inward after each full side is traversed.
- Directional Control: Uses four distinct for loops to handle the Right-Down-Left-Up movement pattern.
- Overlap Prevention: Includes conditional checks within the loop to ensure rows or columns aren't processed twice as the boundaries meet in the center.

#### [05] Name Initializer
**Problem**: Convert a full name string into uppercase initials separated by dots.

**Logic**:

-Tokenization: Uses .split() to break the string into individual names regardless of how many spaces are used.

-Formatting: Extracts the character at index 0 for each name and applies .upper() to ensure consistency.

-Reconstruction: Uses a loop and f-strings to append dots, then joins the list back into a single string.

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
