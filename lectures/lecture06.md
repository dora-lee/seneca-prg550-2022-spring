<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lecture #6
Monday June 13, 2022

## Lecture Objective

- Gain expertise with using Jupyter Notebooks
- Introduction to Pandas
- Familiarity with Python regular expressions

## Pre-requisites

- Python version 3.9.9 installed on your computer and on Raspberry Pi
    check Python version with `python -V`

## Page Contents

- [Jupyter Notebooks](#Jupyter-Notebooks)
    - [Accessing Lecture Notebooks](#Accessing-Lecture-Notebooks)
    - [Overview of features for Jupyter Classic Notebook Interface](#Overview-of-features-for-Jupyter-Classic-Notebook-Interface)
- [Overview of Pandas](#Overview-of-Pandas)
    - [Additional Pandas References](#Additional-Pandas-References)
- [Regular Expressions in Python](#Regular-Expressions-in-Python)
- [Regular Expression Patterns](#Regular-Expression-Patterns)
- [The Python match/search Function](#The-Python-match/search-Function)
- [Searching and replacing text with Python](#Searching-and-replacing-text-with-Python)
- [Class Exercise A](#Class-Exercise-A)
- [Class Exercise B](#Class-Exercise-B)
- [Class Exercise C](#Class-Exercise-C)
- [Class Exercise D](#Class-Exercise-D)
- [Class Exercise E](#Class-Exercise-E)
- [Class Exercise F](#Class-Exercise-F)
- [Class Exercise G](#Class-Exercise-G)
- [Class Exercise H](#Class-Exercise-H)
- [Class Exercise I](#Class-Exercise-I)



----------------------------------

## Jupyter Notebooks

### Accessing Lecture Notebooks

Each week's Jupyter notebook course notes are located in course repository `seneca-prg550-2022-spring/lectures/*.ipynb`.  To update your local repo, use the steps below.

1. Make sure your Pi has internet access to update repo using `git pull`:
      ```
      cd /home/pi/seneca-prg550-2022-spring
      git pull
      ```
2. Copy the lecture notebook from the repo (`seneca-prg550-2022-spring/lectures/Lecture06-Jupyter-Notes.ipynb`) to your working directory (`/home/pi/workspace/lectures`)
      ```
      cd /home/pi/workspace/lectures # make the necessary directories if they do not exist
      cp ~/seneca-prg550-2022-spring/lectures/Lecture06-Jupyter-Notes.ipynb .
      ```
3. Start Jupyter notebook server from your workspace directory (beginning with step #2 [here](../setup/install-packages-for-ml.md#install-and-connect-to-jupyter-server-on-the-rasberry-pi-2))


4. Use the file browser tab and navigate to the `lectures` directory and open `Lecture06-Jupyter-Notes.ipynb`


### Overview of features for Jupyter Classic Notebook Interface

1. Briefly read through this introduction [Overview of features for Jupyter Classic Notebook interface](https://docs.jupyter.org/en/latest/start/index.html#try-the-classic-notebook-interface)

2. You can navigate and view the [Lecture 6 notebook notes](Lecture06-Jupyter-Notes.ipynb) within github but you cannot run it



### Overview of Pandas
1. [Overview of Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
    - [What kind of data does pandas handle](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
    - [Reading and Writing Data in Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
    - [Select subset of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)
    - [Create new columns of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
    - [Calculate summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
    - [Manipulating Text Data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html)

### Additional Pandas References

- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)


## Why Regular Expressions?

Regular expressions are a way programmatically describe the `string-pattern` you want to look for in a body of `text`.
For example:

- What if you want to search for a IP addresses having a specific subnet?
- What if you have a list of 1000 emails and you only want to find users who signed up with `yahoo` in North America  (ie keep `yahoo.ca` and `yahoo.com` but exclude `yahoo.co.uk`)?
- What if you need you have a list of emails like `test@domain.com` that you need to change to `test@my-domain.com` ?

How would you describe the string you want to find or the operation you want to make?  

Regular expressions (or "regex") are a way to parse and operate on strings in a compact manner.


## Regular Expressions in Python
[Regular expressions](https://docs.python.org/3/howto/regex.html) are search patterns. They are written using a
particular syntax and are compiled and then executed -- so regular
expressions are a computer language in their own right.
There are many different dialects of regular expressions in use,
however, the Perl version (PCRE) is one of the more powerful versions
in use today and has been implemented in Python!

A regular expression ("regex" or "regexp" for short) is compared
against input data to find matches. If there are several possible
matches in the input data, the rule is that the regular expression
engine will match the LEFTMOST and LONGEST possible match.

Regular expressions are created from some combinations of these components:

- Characters `A-Z a-z`
- Wildcards `* . + ?`
- Repetition ("quantifiers") `{n}`
- Anchors ("assertions") `^ &`
- Alternation `|`
- Grouping `()`

In Python, the module `re` provides full support for Perl-like regular
expressions. The `re` module raises the exception `re.error` if an error
occurs while compiling or using a regular expression.

## Regular Expression Patterns
Except for these meta characters: `+ ? . * ^ $ ( ) [ ] { } | \`
all characters match themselves. It is possible to escape a meta
character by preceding it with a backslash.

NOTE: In order to specify a regular expression pattern be used, the `r''`
notation may be employed in order to avoid any confusion when
dealing with regular expressions. So, the raw string syntax:
`r'expression'`
may be used in place of first compiling the regular expression and
then applying it to the search text for matching.

The following table lists the regular expression syntax available
in Python:
|       | Description |
|:-------|:------------|
|`^`|         Matches beginning of line.|
|`$`|         Matches end of line.|
|`.`|         Matches any single character except the newline. Using the m option allows it to match the newline as well.
|`[ ]`|       Matches any single character in a character class.|
|`[^]`|       Matches any single character not in character class|
|`*`|         Matches 0 or more occurrences of preceding expression.|
|`+`|         Matches 1 or more occurrence of preceding expression.|
|`?`|         Matches 0 or 1 occurrence of preceding expression.|
|`{n}`|       Matches exactly n number of occurrences of preceding expression.|
|`{n,}`|      Matches n or more occurrences of preceding expression.|
|`{n, m}`|    Matches at least n and at most m occurrences of preceding expression.|
|`\|`|     Matches either `a` or `b`.|
|`()`|       Groups regular expressions and organizes matched portions into groups.|
|`\w`|        Matches word characters.|
|`\W`|        Matches non-word characters.|
|`\s`|        Matches whitespace. Equivalent to [\t\n\r\f].|
|`\S`|        Matches non-whitespace.|
|`\d`|        Matches digits. Equivalent to [0-9].|
|`\D`|        Matches non-digits.|
|`\A`|        Matches beginning of string.|
|`\Z`|        Matches end of string. If a newline exists, it matches just before newline.|
|`\z`|        Matches end of string.|
|`\1..\9`|    Matches nth grouped subexpression.|

Examples:
```
r'1[abc]2'           - Matches between the `1` and `2`, either `a`, `b`, or `c` (ex: `1a2`, `1b2`, or `1c2`)
r'1[a-zA-Z0-9]2'     - Matches between `1` and `2`, any single char from (a to z) or (A to Z) or (0 to 9).
```

Anchors and assertions do not match specific characters, but
instead match specific locations or conditions.
`^` matches the beginning of the line
`$` matches the end of the line

Example:
```
r'^car$'  # matches "car" by itself but not "carrot"
r'^$'     # matches an empty line
```

Individual characters are called "atoms", or specific pieces of
text that need to be matched.
Any alphanumeric character matches itself: r'Hello' matches "Hello"

Any non-alphanumeric character will match itself if preceded by
a backslash: `r'\*\(foo\)'` matches `"*(foo)"`

Character classes may be specified using square-brackets `[ ]`.
A character class will match any one character listed in the
square-brackets; ranges may be specified with a dash. A carat
symbol `^` at the start of the class will invert the meaning of
the character class and cause it to match any character which is
NOT listed.

Example:
```
r'[12345]' # matches 1, 2, 3, 4, or 5
r'[1-5]' # matches 1,2,3, 4, or 5
r'[1-590]' # matches 1, 2, 3, 4, 5, 9, or 0
r'[^0-9]' # matches any character which is not a digit
r'[^:]' # matches any character which is not a colon
```
Alternation lets you write alternative text; either the text
before or after the alternation character `|` may be matched.
The alternation character may be used multiple times to specify
more than two alternate values.

Example:
```
r'Hello|Goodbye' # matches "Hello" or "Goodbye"
r'red|blue|green house' # matches "red house" or "blue house" or "green house"
```
The wildcard character `.` matches any one character.

Example:
```
r'l.ss' # matches "lass", "loss", "liss", "l9ss", ...
r'l...s' # matches "ladds", "likes", "loses", ...
```
A quantifier specifies how many times the preceding atom must be matched.
Quantifiers may take any of these forms:
- `{count}`
- `{minimum,}`
- `{minimum, maximum}`

These short forms are available:

- `?` same as `{0,1}`
- `+` same as `{1,}`
- `*` same as `{0,}`

Normally, a quantifier is 'greedy' -- it will match as many
characters as possible (because of the "leftmost and longest" rule).
You can reverse that to make a quantifier match as few characters
as possible by adding a question mark at the end:
```
{0,5}? # matches 0 to 5 of the preceeding atom, but ONLY as few as possible.
```

Examples:
```
r'a{5}'      # matches "aaaaa"
r'a{2,5}'    # matches "aa", "aaa", "aaaa", or "aaaaa"
r'a.*z'      # matches anything starting with a and ending with z
r'[a-z]{5,}' # matches 5 or more lowercase letters
```

## Regex `search`-ing and `match`-ing strings

The `search` function searches for the **first** occurrence of a regular
expression pattern ANYWHERE within the search text and may include
optional flags. The `match` function on the other hand ONLY matches
search text at the beginning of the text and NOT at other points within
the text.

Syntax:
```
re.search(pattern, string, flags=0)

re.match(pattern, string, flags=0)
```
where
|       |            |
|:------|:-----------|
|`pattern` | is the regular expression to be matched, |
|`string`  | is the variable holding the text to search, and |
|`flags`   | consist of one or more modifiers listed in the table below (which can be grouped by using the | (bitwise OR)operator|

`FLAGS`:
|       |            |
|:------|:-----------|
|`re.I` | Performs case-insensitive matching. |
|`re.L` | Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B). |
|`re.M` | Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string). |
|`re.S` | Makes a period (dot) match any character, including a newline.|
|`re.U` | Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.|
|`re.X` | Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker. |

Flags may be specified using bitwise OR (`|`) to include multiple flags

The `re.search` function returns a match object on success and `None` on
failure.
The `group(num)` or `groups()` function of the match object may be used to
access the matched expression.

|       |            |
|:------|:-----------|
| group(num=0) | This method returns entire match (or specific subgroup num) |
| groups()     | This method returns all matching subgroups in a tuple (empty if there weren't any) |

Example:
```
import re

regxList = [r'1a*2', r'2[a0-9]*6', r'[0-9].*[0-9]', r'[0-9].*?[0-9]']
string = "1aaaa2aaaa3aaaa4aaaa5aaaa6nnnn";
for pattern in regxList :
   match = re.search(pattern, string)
   if match :
      print("pattern:'%s' match found... start:%s end:%s match:%s\n"
      % (pattern, match.start(), match.end(), match.group()))
```


## Regex searching and replacing text with `sub`
One of the most important re methods that use regular expressions is sub.
Syntax:
```
re.sub(pattern, replace, string, max=0)
```
This method replaces all occurrences of the regular expression 'pattern'
within string with 'replace', substituting all occurrences unless a maximum
is provided. This method returns the modified string.

Example:
```
import re
result = re.sub(r'\sAND\s', ' $amp; ', 'Green Eggs AND Ham And Sam I Am!', flags=re.I)
print(result)
```

Regex resources
|                         |                         |
|:------------------------|:------------------------|
| [Awesome Regex](https://github.com/aloisdg/awesome-regex#awesome-regex) | A curated collection of awesome Regex libraries, tools, frameworks and software |
| [regex101.com](https://regex101.com) | A helpful website to help you test and understand regular expressions|
| [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) |Python Docs Regular Expression HOWTO |


## Class Exercise A

Work through all of [Pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html):
- [Reading and Writing Data in Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
- [Select subset of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)
- [Create new columns of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
- [Calculate summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
- [Manipulating Text Data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html)


## Class Exercise B

1. Read `aapl_stock.json` into a Pandas dataframe
1. Convert the `date` field from `string` to `datetime` object
1. Create a `month` column derived from `date` field
1. Create a `year` column derived from `date` field
1. Create a `day-of-week` column derived from `date` field
1. Calculate the average volume for each day of the week

## Class Exercise C
Write the Python regular expressions (regexp) which will do the following:
If any of the conditions are encountered, print the message `Exception Found...` to the screen.

    a)    Tests to see if a string contains any NON-alphanumeric data
          (i.e. contains something other than digits or alphabetic
          characters).
    b)    Makes sure that a string contains only UPPER case alphabetic
          characters.
    c)    Makes sure that a field (string) contains a single positive
          whole number value.
    d)    Tests to see if a string contains 2 or more whitespace
          (' ', '\t', '\n') characters.
    e)    Makes sure that a field contains at least 1 NON-whitespace
          character.

## Class Exercise D
Explain each of the following regular expressions:

    a)    r'(\w+)$'
    b)    r'^#'
    c)    re.sub(r'#{2,}', '#', text)
    d)    r'^[0-9]+$'
    e)    r'((^[0-9]+\.?)$)|((\.[0-9][0-9]*)$)'

## Class Exercise E

Replace every occurrence of the character `s` (upper or lowercase),
      in the string `She sells sea shells by the sea shore.`, with
      the character `T`.

## Class Exercise F
Write a complete Python program which opens a plain text file
      and replaces every occurence of the word `he` with the
      word `she`.

## Class Exercise G
Write the regular expression that validates a Canadian POSTAL CODE
      in the form `LetterNumberLetter (embedded space or - permitted) NumberLetterNumber`

## Class Exercise H
Write the regular expression that validates a North American telephone number in the form

        xxx (optional space or `-`) yyy (optional space or `-` ) zzzz
    
    Such that `x`, `y`, `z` are digit characters ONLY.

## Class Exercise I

Write the regular expression that validates an email address in the form `username@host.domain`
such that:

      username: MUST contain at least 2 alphabetic characters and may contain
                special characters - and . but MAY NOT end with a - or .
      host:     MUST contain at least 2 alphabetic characters and may contain
                special characters - and . but MAY NOT end with a - and MUST end with a .
      domain:   MUST contain at least 2 alphabetic characters, but no more than 4.
