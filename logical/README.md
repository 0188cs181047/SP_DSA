# Logical / Aptitude Problems

This folder is a catch-all for classic **logic and number-puzzle** style
questions — the kind used as warm-up questions in interviews, or as the
"logical reasoning + coding" round at service companies (TCS, Infosys,
Wipro, Capgemini). They don't need a dedicated data structure the way a
tree or graph problem does; the challenge is usually spotting a math
trick, a digit-manipulation pattern, or a small recursive relation.

## Interview Roadmap (Basic → Advanced)

Every problem below has its own runnable `.py` file with a problem statement,
the approach, and time/space complexity in its docstring. Work through them
top to bottom — each section builds on the one before it.

| # | Folder | Problem | File | Pattern | Difficulty | Asked At |
|---|---|---|---|---|---|---|
| 1 | [01_basics](01_basics) | FizzBuzz | [fizzbuzz.py](01_basics/fizzbuzz.py) | Modulo Check | Easy | TCS, Infosys, Amazon, Wipro |
| 2 | [01_basics](01_basics) | Check if a Number is Prime | [check_prime_number.py](01_basics/check_prime_number.py) | Trial Division up to √n | Easy | TCS, Infosys, Wipro |
| 3 | [01_basics](01_basics) | Factorial (Iterative & Recursive) | [factorial.py](01_basics/factorial.py) | Iteration / Recursion | Easy | TCS, Infosys, Amazon |
| 4 | [01_basics](01_basics) | Print the First N Fibonacci Numbers | [fibonacci_series.py](01_basics/fibonacci_series.py) | Iterative Sequence Building | Easy | TCS, Infosys, Adobe |
| 5 | [02_number_theory](02_number_theory) | Reverse a Number & Check Palindrome Number | [reverse_and_palindrome_number.py](02_number_theory/reverse_and_palindrome_number.py) | Digit Extraction (% and //) | Easy | TCS, Wipro, Amazon |
| 6 | [02_number_theory](02_number_theory) | Check Armstrong Number | [armstrong_number.py](02_number_theory/armstrong_number.py) | Digit Extraction + Power Sum | Easy | TCS, Infosys |
| 7 | [02_number_theory](02_number_theory) | GCD and LCM of Two Numbers | [gcd_lcm.py](02_number_theory/gcd_lcm.py) | Euclidean Algorithm | Easy | TCS, Infosys, Amazon |
| 8 | [02_number_theory](02_number_theory) | Swap Two Numbers Without a Temp Variable | [swap_without_temp.py](02_number_theory/swap_without_temp.py) | Arithmetic Trick / XOR Trick | Easy | TCS, Wipro, Capgemini |
| 9 | [03_strings_bits](03_strings_bits) | Check String Palindrome & Anagram of Two Strings | [string_palindrome_anagram.py](03_strings_bits/string_palindrome_anagram.py) | Two Pointers / Char Count | Easy | TCS, Amazon, Microsoft |
| 10 | [03_strings_bits](03_strings_bits) | Count Set Bits (1s) in an Integer | [count_set_bits.py](03_strings_bits/count_set_bits.py) | Brian Kernighan's Bit Trick | Easy/Medium | Amazon, Microsoft, Nvidia |
| 11 | [03_strings_bits](03_strings_bits) | Power of a Number (Fast Exponentiation) | [power_fast_exponentiation.py](03_strings_bits/power_fast_exponentiation.py) | Binary Exponentiation | Medium | Amazon, Google, Microsoft |
| 12 | [03_strings_bits](03_strings_bits) | Find the Missing Number in an Array (1 to N) | [missing_number.py](03_strings_bits/missing_number.py) | Sum Formula / XOR | Easy/Medium | Amazon, Microsoft, TCS |
| 13 | [../hash_table](../hash_table) | Two Sum | [two_sum.py](two_sum.py) | HashMap | Easy | Amazon, Google, Microsoft, Meta, Adobe |
| 14 | [04_advanced](04_advanced) | Print All Permutations of a String | [permutations_of_string.py](04_advanced/permutations_of_string.py) | Backtracking (swap-based) | Medium | Amazon, Microsoft, Google |
| 15 | [04_advanced](04_advanced) | Roman Numeral ↔ Integer Conversion | [roman_integer_conversion.py](04_advanced/roman_integer_conversion.py) | Greedy + Lookup Table | Medium | Amazon, Microsoft, Adobe |
| 16 | [04_advanced](04_advanced) | The Josephus Problem | [josephus_problem.py](04_advanced/josephus_problem.py) | Recursion / Circular Elimination | Hard | Amazon, Google, Directi |

## How to Pick the Right Pattern in an Interview

- Number → digits, need to reverse/sum/compare them? → **Digit extraction** with `% 10` and `// 10`
- Two numbers, need a common factor/multiple? → **Euclidean Algorithm** (GCD, then LCM = a*b/GCD)
- Need to test every bit, or count/toggle bits? → **Bit manipulation** (`n & (n-1)`, `^`, `<<`/`>>`)
- Need every arrangement of a small set/string? → **Backtracking** (swap or "choose next" recursion)
- Elements arranged in a circle with periodic elimination? → **Recursive relation** (Josephus-style)
- Doesn't fit a DS category at all, just "compute this value"? → Trial division / greedy / simulation — whichever is simplest to reason about correctly under interview pressure

## Folder Structure

```
logical/
├── README.md
├── two_sum.py            # classic HashMap warm-up (see also ../hash_table)
├── 01_basics/             # FizzBuzz, Prime Check, Factorial, Fibonacci Series
├── 02_number_theory/      # Reverse/Palindrome Number, Armstrong, GCD/LCM, Swap Without Temp
├── 03_strings_bits/       # String Palindrome/Anagram, Set Bits, Fast Power, Missing Number
└── 04_advanced/            # Permutations, Roman Numeral Conversion, Josephus Problem
```

Run any file directly to see it work, e.g.:

```bash
python 04_advanced/josephus_problem.py
```
