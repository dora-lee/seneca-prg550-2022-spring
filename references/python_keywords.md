The following list below contains a list of Keywords (reserved words) in the
Python programming language (as of python 3.6)

```
False
None
True
and
as
assert
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
```

# Python program to display a list of current keywords

```
#!/usr/bin/python3
# keywords.py

import sys
import keyword

print("Python version: ", sys.version_info)
print("Python keywords: ", keyword.kwlist)
```

# Rules for writing identifiers:

Identifiers can consist of a combination of lower and uppercase letters (a to z), (A to Z),
digits (0 to 9), or an underscore (_). Examples of valid identifiers are: `var1`, `speed_of_light`, `_my_object`, `input_file`, etc.

An identifier may NOT begin with a digit and may NOT be the same as an existing Keyword.
Also, please note that Python is a case-sensitive language. Thus identifiers such as `Apple`,
`APPLE`, and `appLE`, are all considered unique names.