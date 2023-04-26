#! python3

import re, pyperclip


phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-)   # first separator
 \d\d\d     # first 3 digits
-          # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x)  # extension word-part (optional)
 (\d{2,5}))?       #extension number part (optional)
)
''', re.VERBOSE)


emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+


''', re.VERBOSE)

text = pyperclip.paste()

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print("Here's your extracted data. For your convenience it's already copied to your clipboard. " + '\n' + results) 


