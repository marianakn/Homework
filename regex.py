
import re


text = """"
Hello! My name is Mariana Knyazyan. You can contact me at knyazyan.mariana@gmail.com or mariana.knyazyan@ysu.am.

My phone numbers are:
+374-91-123456
(010) 456-789
+1 (555) 987-6543

Here are some dates:
15/07/2025
2025-07-11
05.06.24

A few other names: Aram, Mariam, Davit, Emma, and their teacher Mrs. Sargsyan.

The class email is: python_course2025@gmail.com
"""



emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print("Emails:", emails)

phones = re.findall(r'(\+\d{1,3}[-\s]?\(?\d+\)?[-\s]?\d{3}[-\s]?\d{3,4})', text)
print("Phone Numbers:", phones)

dates = re.findall(r'\b(?:\d{1,2}[\/.-]\d{1,2}[\/.-]\d{2,4}|\d{4}-\d{2}-\d{2})\b', text)
print("Dates:", dates)

capitalized_words = re.findall(r'\b[A-Z][a-z]+\b', text)
print("Capitalized Words:", capitalized_words)