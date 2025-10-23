# 🧩 Lexical Scanner (C++ Tokenizer)

This project implements a simple **Lexical Scanner** (also known as a *Lexer*) using **Python**.  
It reads a C++ source file (`code.cpp`), analyzes its contents, and extracts **tokens** such as keywords, identifiers, constants, operators, and comments.  
Finally, it saves the tokenized output into a CSV file named **`tokens.csv`**.

---

## 🚀 Features

- Reads code automatically from `code.cpp`
- Detects and classifies:
  - **Keywords** (e.g., `for`, `if`, `int`, `return`)
  - **Identifiers** (variable and function names)
  - **Numeric constants** (including scientific notation)
  - **Character and string literals**
  - **Operators** (+, -, =, *, /, <, >, etc.)
  - **Special symbols** ((), {}, [], ;, ,)
  - **Comments** (single and multi-line)
- Ignores unnecessary whitespace
- Saves all tokens in a **structured CSV file** for analysis

---

## 🧠 How It Works

1. **Read the Source File**  
   The scanner loads the contents of `code.cpp`.

2. **Define Token Patterns**  
   Each token type (keyword, identifier, etc.) is defined using **regular expressions (regex)**.

3. **Tokenization**  
   The program scans the file and matches all patterns, identifying the corresponding token types.

4. **Export Tokens**  
   The extracted tokens are printed in the terminal and saved to a CSV file called `tokens.csv`.

---

## 👨‍💻 Designed & Created By

This project was designed and implemented by:

Mostafa Alaa Bahnasi El-Sisi

Mohamed Abd Elhamed Elbahshene

Faculty of  Electronics Engineering,
Department of Computer & science Engineering.
