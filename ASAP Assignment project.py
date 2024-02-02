#!/usr/bin/env python
# coding: utf-8

# # Regulor Expressions

# # Answer 1

# In[1]:


def replace_with_colon(text):
    # Define the characters to be replaced
    replace_chars = [' ', ',', '.']

    # Replace each character with a colon
    for char in replace_chars:
        text = text.replace(char, ':')

    return text

# Sample Text
sample_text = 'Python Exercises, PHP exercises.'

# Call the function and print the output
result = replace_with_colon(sample_text)
print("Expected Output:", result)


#  # Answer 2

# In[2]:


import pandas as pd

# Dictionary
data = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}

# Create DataFrame
df = pd.DataFrame(data)

# Remove unwanted characters from the 'SUMMARY' column
df['SUMMARY'] = df['SUMMARY'].str.replace('[^a-zA-Z\s]', '', regex=True)

# Display the DataFrame
print("Expected Output:")
print(df)


# # Answer 3

# In[3]:


import re

def find_long_words(input_string):
    # Define a regular expression pattern to match words of at least 4 characters
    pattern = re.compile(r'\b\w{4,}\b')

    # Use findall to get all matches in the input string
    long_words = pattern.findall(input_string)

    return long_words

# Example usage
input_text = "This is a sample text with words of various lengths, such as apple, banana, orange, and python."

# Call the function and print the result
result = find_long_words(input_text)
print("Words with at least 4 characters:", result)


# # Answer 4

# In[4]:


def find_words_by_length(input_string):
    # Define a regular expression pattern to match words of length 3, 4, and 5
    pattern = re.compile(r'\b\w{3,5}\b')

    # Use findall to get all matches in the input string
    matched_words = pattern.findall(input_string)

    return matched_words

# Example usage
input_text = "This is a sample text with words of various lengths, such as apple, banana, orange, and python."

# Call the function and print the result
result = find_words_by_length(input_text)
print("Words with lengths 3, 4, and 5:", result)


# # Answer 5

# In[5]:


import re

def remove_parentheses(strings):
    # Compile a regular expression pattern for matching parentheses
    pattern = re.compile(r'\((.*?)\)')

    # Remove parentheses from each string in the list
    cleaned_strings = [re.sub(pattern, '', text) for text in strings]

    return cleaned_strings

# Sample Text
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# Get the cleaned output
cleaned_output = remove_parentheses(sample_text)

# Print the cleaned output
for text in cleaned_output:
    print(text)


# # Data Scientist

# # Answer 6

# In[6]:


import re

# Write the sample text to a text file
with open("sample_text.txt", "w") as file:
    file.write('["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]')

# Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Define the regular expression pattern for matching text within parentheses
parenthesis_pattern = r'\([^)]*\)'

# Use the sub() function to remove the text within parentheses
cleaned_text = re.sub(parenthesis_pattern, '', text)

# Print the cleaned text
print("Expected Output:", cleaned_text)


# # Answer 7

# In[7]:


import re

# Sample text
sample_text = "ImportanceOfRegularExpressionsInPython"

# Define a regular expression pattern to match uppercase letters
pattern = re.compile(r'[A-Z][a-z]*')

# Use findall to get all matches in the sample text
result = pattern.findall(sample_text)

# Print the result
print("Expected Output:", result)








# # Answer 8

# In[8]:


import re

# Sample text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

# Define a regular expression pattern to match uppercase letters and numbers
pattern = re.compile(r'[A-Z][a-z]*|\d+')

# Use findall to get all matches in the sample text
result = pattern.findall(sample_text)

# Print the result
print("Expected Output:", result)


# # Answer 9

# In[9]:


import re

def insert_spaces(input_string):
    # Define a regular expression pattern to match uppercase letters and numbers
    pattern = re.compile(r'([A-Z][a-z]*|\d+)')

    # Use sub to insert a space before each match
    modified_text = pattern.sub(r' \1', input_string)

    return modified_text.strip()

# Sample Text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

# Call the function and print the result
result = insert_spaces(sample_text)
print("Expected Output:", result)


# # Answer 10

# In[10]:


import pandas as pd

# GitHub link to the dataset
github_link = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"

# Read the data into a DataFrame
df = pd.read_csv(github_link)


# In[11]:


df


# In[12]:


# Extract the first 6 letters of each country and store in a new column
df['first_five_letters'] = df['Country'].str[:6]

# Display the DataFrame with the new column
print(df.head())


# # Answer 11

# In[13]:


import re

def is_valid_string(input_string):
    # Define a regular expression pattern for valid strings
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')

    # Use match to check if the entire string matches the pattern
    match = pattern.match(input_string)

    return match is not None

# Example usage
test_string1 = "Valid_String123"
test_string2 = "Invalid_String@456"

# Check if the strings are valid
print(f'Is "{test_string1}" valid? {is_valid_string(test_string1)}')
print(f'Is "{test_string2}" valid? {is_valid_string(test_string2)}')


# # Answer 12

# In[14]:


def starts_with_number(input_string, specified_number):
    return input_string.startswith(str(specified_number))

# Example usage
test_string1 = "123abc"
test_string2 = "456def"
specified_number = 123

# Check if the strings start with the specified number
print(f'Does "{test_string1}" start with {specified_number}? {starts_with_number(test_string1, specified_number)}')
print(f'Does "{test_string2}" start with {specified_number}? {starts_with_number(test_string2, specified_number)}')


# # Answer 13

# In[15]:


import ipaddress

def remove_leading_zeros(ip_address_str):
    try:
        # Parse the IP address
        ip_address = ipaddress.IPv4Address(ip_address_str)

        # Convert the IP address back to a string without leading zeros
        cleaned_ip = str(ip_address)

        return cleaned_ip
    except ipaddress.AddressValueError:
        # Handle the case where the input is not a valid IP address
        print("Invalid IP address")

# Example usage
ip_with_zeros = "192.001.002.003"
ip_without_zeros = remove_leading_zeros(ip_with_zeros)

print(f'Original IP address: {ip_with_zeros}')
print(f'IP address without leading zeros: {ip_without_zeros}')


# # Answer 14

# In[16]:


import re

# Write the sample text to a text file
with open("sample_text.txt", "w") as file:
    file.write('On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.')

# Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Define the regular expression pattern
date_pattern = r'(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b)'

# Search for the pattern in the text
match = re.search(date_pattern, text)

# Extract and print the matched date string
if match:
    date_string = match.group(1)
    print("Expected Output:", date_string)
else:
    print("Date not found in the specified format.")


# # Answer 15

# In[17]:


sample_text = 'The quick brown fox jumps over the lazy dog.'

# List of literals to search for
search_literals = ['quick', 'fox', 'lazy', 'cat']

# Using the 'in' operator
for literal in search_literals:
    if literal in sample_text:
        print(f'"{literal}" found in the text.')
    else:
        print(f'"{literal}" not found in the text.')

# Using the 'find()' method
for literal in search_literals:
    index = sample_text.find(literal)
    if index != -1:
        print(f'"{literal}" found at index {index} in the text.')
    else:
        print(f'"{literal}" not found in the text.')


# # Answer 16

# In[18]:


sample_text = 'The quick brown fox jumps over the lazy dog.'
search_word = 'fox'

# Using the 'find()' method
index = sample_text.find(search_word)

if index != -1:
    print(f'"{search_word}" found at index {index} in the text.')
else:
    print(f'"{search_word}" not found in the text.')


# # Answer 17

# In[19]:


sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

# Find all occurrences of the pattern
start_index = sample_text.find(pattern)

while start_index != -1:
    print(f'Found at index {start_index}: "{sample_text[start_index:start_index + len(pattern)]}"')
    start_index = sample_text.find(pattern, start_index + 1)


# # Answer 18

# In[20]:


def find_occurrences_positions(text, pattern):
    occurrences = 0
    positions = []

    start_index = text.find(pattern)

    while start_index != -1:
        occurrences += 1
        positions.append(start_index)
        start_index = text.find(pattern, start_index + 1)

    return occurrences, positions


sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern_to_find = 'exercises'

occurrences, positions = find_occurrences_positions(sample_text, pattern_to_find)

if occurrences > 0:
    print(f'Total occurrences of "{pattern_to_find}": {occurrences}')
    print(f'Positions: {positions}')
else:
    print(f'No occurrences of "{pattern_to_find}" found in the text.')


# # Answer 19

# In[21]:


from datetime import datetime

def convert_date_format(input_date):
    try:
        # Parse the input date in yyyy-mm-dd format
        date_object = datetime.strptime(input_date, '%Y-%m-%d')

        # Format the date in dd-mm-yyyy format
        output_date = date_object.strftime('%d-%m-%Y')

        return output_date

    except ValueError:
        # Handle the case where the input date is not in the expected format
        return 'Invalid date format'

# Example usage
input_date = '2022-01-29'
output_date = convert_date_format(input_date)

print(f'Input date: {input_date}')
print(f'Converted date: {output_date}')


# # Answer 20

# In[22]:


import re

def find_decimal_numbers(text):
    # Define a regex pattern for finding decimal numbers with precision of 1 or 2
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')

    # Use findall to extract all matches from the text
    decimal_numbers = pattern.findall(text)

    return decimal_numbers

# Example usage
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
result = find_decimal_numbers(sample_text)

print("Sample Text:", sample_text)
print("Output:", result)


# # Answer 21

# In[23]:


import re

def separate_and_print_numbers(text):
    # Define a regex pattern to find numbers
    number_pattern = re.compile(r'\b\d+\b')

    # Use finditer to get an iterator of match objects
    matches = number_pattern.finditer(text)

    # Iterate through matches and print numbers along with their positions
    for match in matches:
        number = match.group()
        start_position = match.start()
        end_position = match.end()

        print(f'Number: {number}, Position: {start_position}-{end_position}')

# Example usage
sample_text = "There are 42 apples and 17 oranges in the basket."
separate_and_print_numbers(sample_text)


# # Answer 22

# In[24]:


import re

def extract_maximum_numeric_value(text):
    # Define a regex pattern to find all numeric values
    numeric_pattern = re.compile(r'\b\d+\b')

    # Use findall to extract all numeric values
    numeric_values = list(map(int, numeric_pattern.findall(text)))

    # Check if there are any numeric values
    if numeric_values:
        max_numeric_value = max(numeric_values)
        return max_numeric_value
    else:
        return None

# Example usage
sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
result = extract_maximum_numeric_value(sample_text)

if result is not None:
    print(f'Maximum numeric value: {result}')
else:
    print('No numeric values found in the text.')


# # Answer 23

# In[25]:


import re

def insert_spaces(text):
    # Use a regular expression to find words starting with capital letters
    pattern = re.compile(r'([a-z])([A-Z])')
    
    # Use sub to insert space between the lowercase letter and the uppercase letter
    result = pattern.sub(r'\1 \2', text)
    
    # Add space before the first capital letter
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', result)

    return result

# Example usage
sample_text = "RegularExpressionIsAnImportantTopicInPython"
result = insert_spaces(sample_text)

print("Sample Text:", sample_text)
print("Output:", result)


# # Answer 24

# In[26]:


import re

def find_uppercase_followed_by_lowercase(text):
    pattern = re.compile(r'([A-Z][a-z]+)')

    matches = pattern.findall(text)

    return matches

# Example usage
sample_text = "The Quick Brown Fox Jumps Over The Lazy Dog"
result = find_uppercase_followed_by_lowercase(sample_text)

print("Sample Text:", sample_text)
print("Output:", result)


#  # Answer 25

# In[27]:


import re

def remove_continuous_duplicates(sentence):
    # Use a regular expression to find continuous duplicate words
    pattern = re.compile(r'\b(\w+)(\s+\1)+\b', flags=re.IGNORECASE)

    # Use sub to remove continuous duplicate words
    result = pattern.sub(r'\1', sentence)

    return result

# Example usage
sample_text = "Hello hello world world"
result = remove_continuous_duplicates(sample_text)

print("Sample Text:", sample_text)
print("Output:", result)


# # Answer 26

# In[28]:


import re

def ends_with_alphanumeric(input_string):
    pattern = re.compile(r'\w$')

    if pattern.search(input_string):
        return True
    else:
        return False

# Example usage
sample_string1 = "Hello123"
sample_string2 = "World!"

result1 = ends_with_alphanumeric(sample_string1)
result2 = ends_with_alphanumeric(sample_string2)

print(f"Input: {sample_string1}, Ends with Alphanumeric: {result1}")
print(f"Input: {sample_string2}, Ends with Alphanumeric: {result2}")


# # Answer 27

# In[29]:


import re

def extract_hashtags(text):
    pattern = re.compile(r'#\w+')

    hashtags = pattern.findall(text)

    return hashtags

# Example usage
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
result = extract_hashtags(sample_text)

print("Sample Text:", sample_text)
print("Output:", result)


# # Answer 28

# In[30]:


import re

def remove_u_plus_symbols(text):
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')

    result = pattern.sub('', text)

    return result

# Example usage
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
result = remove_u_plus_symbols(sample_text)

print("Sample Text:", sample_text)
print("Output:", result)


# # Answer 29

# In[31]:


import re

# Write the sample text to a text file
with open("sample_text.txt", "w") as file:
    file.write('Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.')

# Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Define the regular expression pattern for matching dates in DD-MM-YYYY format
date_pattern = r'\b\d{2}-\d{2}-\d{4}\b'

# Find all occurrences of the pattern in the text
matched_dates = re.findall(date_pattern, text)

# Print the extracted dates
print("Extracted Dates:", matched_dates)


# # Answer 30

# In[32]:


import re

def remove_words_between_lengths(text):
    # Define a regular expression for matching words of length 2 to 4
    word_pattern = re.compile(r'\b\w{2,4}\b')

    # Replace matched words with an empty string
    result_text = word_pattern.sub('', text)

    return result_text

if __name__ == "__main__":
    sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

    modified_text = remove_words_between_lengths(sample_text)

    print("Original Text:")
    print(sample_text)
    print("\nModified Text:")
    print(modified_text)


# In[ ]:




