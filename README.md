# Python-sprints
A dedicated log of my daily technical problem-solving. This repository tracks my journey in mastering Python and SQL through consistent, daily challenges focused on algorithmic logic and data manipulation.

# Daily Analytical Logic Logs

| Day | Challenge | Core Concepts | Link |
| :--- | :--- | :--- | :--- |
| 01 | **Palindrome Middle** | String Slicing `[::-1]`, Integer Division `//`, Parity Logic | [View Code](./Python/01_palindrome_middle.py) |
| 02 | **FizzBuzz Validator** | `enumerate()`, Type Check, Modulo Math | [View Code](./Python/02_fizzbuzz_validator.py) |
| 03 | **Bingo Sequencer** | Dictionary Mapping, String Formatting | [View Code](./Python/03_bingo_sequencer.py) |
---

#### [01] Palindrome Middle
**Problem:** Find the true center of a symmetric string.
**Logic:**
- **Symmetry Filter:** Validates using `s[::-1]` (O(n) time).
- **Parity-Switch:** Uses `% 2` to toggle between single-point median and cluster median.
- **Precision:** Applied floor division `//` to avoid index floating errors.

#### [02] FizzBuzz Validator
**Problem:** Verify if a list follows FizzBuzz rules from any starting point.
**Logic:**
- **Sequence Anchoring:** Finds the first integer to calculate the sequence's starting value.
- **Validation:** Re-runs the FizzBuzz logic (modulo 3, 5, and 15) to ensure every list item matches the mathematical expectation.

#### [03] Bingo Sequencer
**Problem:** Find the next sequential Bingo number, handling column transitions and resetting at the end.
**Logic:**
- **Boundary Mapping:** Uses a dictionary to define the upper limit for each letter (B=15, I=30, etc.).
- **Column Transition:** If a number hits its limit, the `find()` method locates the next letter in "BINGO" to shift columns.
- **Hard Reset:** Specifically checks for "O75" to wrap the sequence back to the starting "B1".
