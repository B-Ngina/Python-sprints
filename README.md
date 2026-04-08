# Python-sprints
A dedicated log of my daily technical problem-solving. This repository tracks my journey in mastering Python and SQL through consistent, daily challenges focused on algorithmic logic and data manipulation.

# Daily Analytical Logic Logs

| Day | Challenge | Core Concepts | Link |
| :--- | :--- | :--- | :--- |
| 01 | **Palindrome Middle** | String Slicing `[::-1]`, Integer Division `//`, Parity Logic | [View Code](./Python/01_palindrome_middle.py) |
| 02 | **FizzBuzz Validator** | `enumerate()`, Type Check, Modulo Math | [View Code](./Python/02_fizzbuzz_validator.py) |

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
