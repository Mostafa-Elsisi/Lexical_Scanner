import re
import csv

# 1 - Read the source code from an external file (code.cpp)
# This allows the scanner to process any C++ code saved in a text file.
# Make sure that the file "code.cpp" is in the same directory as this Python script.
with open("code.cpp", "r", encoding="utf-8") as f:
    code = f.read()

# 2 - Define the token specifications
# Each token type is described by a Regular Expression (regex) pattern.
# These patterns will be used to match parts of the code and classify them into categories.
token_specification = [
    # Reserved keywords used in the C++ language
    ('KEYWORD',        r'\b(for|while|if|else|return|int|float|char|double|void|endl)\b'),
    
    # Identifiers: variable names, function names, etc.
    # They start with a letter or underscore and can contain digits afterward.
    ('IDENTIFIER',     r'\b[A-Za-z_]\w*\b'),
    
    # Numeric constants: integers, floating-point numbers, or numbers in scientific notation (e.g., 3.4e+6)
    ('NUMERIC_CONST',  r'\b\d+(\.\d+)?(e[+-]?\d+)?\b'),
    
    # Character constants enclosed in single quotes (e.g., 'a')
    ('CHAR_CONST',     r"'.'"),
    
    # String literals enclosed in double quotes (e.g., "Hello World")
    ('STRING',         r'"[^"\n]*"'),
    
    # Operators: arithmetic, relational, assignment, and logical operators
    ('OPERATOR',       r'[+\-*/=<>!]+'),
    
    # Special characters: parentheses, braces, brackets, commas, and semicolons
    ('SPECIAL_CHAR',   r'[()[\]{};,]'),
    
    # Single-line comments starting with //
    ('COMMENT',        r'//.*'),
    
    # Multi-line comments enclosed within /* and */
    ('MULTI_COMMENT',  r'/\*[\s\S]*?\*/'),
    
    # Whitespace: spaces, tabs, or newlines (to be ignored during tokenization)
    ('WHITESPACE',     r'\s+'),
]

# 3 - Combine all token patterns into a single regex
# This step creates one large regular expression containing all possible token types.
# Using named groups (?P<NAME>...) allows us to easily identify which type of token was matched.
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

# This list will hold tuples of (lexeme, token_type)
tokens = []

# 4 - Tokenize the source code
# The re.finditer() function scans through the input code and finds all matches of the combined regex.
# Each match corresponds to a valid token in the source code.
for match in re.finditer(tok_regex, code):
    token_type = match.lastgroup       # The category name of the matched token
    lexeme = match.group(token_type)   # The actual text (lexeme) that was matched
    
    # Ignore whitespace and multi-line comments, as they don't contribute to syntax analysis
    if token_type not in ('WHITESPACE', 'MULTI_COMMENT'):
        tokens.append((lexeme, token_type))
        # Print the token neatly formatted
        print(f'{lexeme:<20} → {token_type}')

# 5 - Save the extracted tokens into a CSV file
# This step is helpful for later analysis, debugging, or feeding tokens into another compiler stage.
with open("tokens.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Write the CSV header
    writer.writerow(["Lexeme", "Token_Type"])
    # Write all tokens line by line
    writer.writerows(tokens)

# 6 - Final confirmation message
# After execution, you will find a new file "tokens.csv" in the same directory.
# It will contain two columns: the lexeme (actual code text) and its corresponding token type.
print("\n Tokens have been successfully extracted and saved to 'tokens.csv'.")

#  Notes:
# - You can modify the 'token_specification' list to include more patterns, such as preprocessor directives (#include),
#   boolean literals (true, false), or punctuation.
# - This scanner is simplified for educational purposes and works well for small C++ snippets.
# - In a real compiler, a lexer (scanner) also keeps track of line numbers and column positions
#   to provide precise error messages and debugging information.
# - If you want to process multiple C++ files, you can expand this script to loop through all .cpp files in a folder
#   and generate a separate CSV file for each one.
