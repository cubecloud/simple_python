# Example of w+ and ^ Expression
import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)
print (r1)

# Example of \s expression in re.split function
import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+", xx)
phrase=('we are splitting the words')
phrase1 = ('2011-08-01 18:03:34,338 - exampleApp - INFO - Program started\n')
print (re.split(r'\s', phrase))
print (re.split(r'\s[-]\s|\n', phrase1))

# print (re.split(r's','split the words'))
#
# # Using re.findall for text
# import re
#
# list = ["guru99 get", "guru99 give", "guru Selenium"]
# for element in list:
#     z = re.match("(g\w+)\W(g\w+)", element)
# if z:
#     print(z.groups())
#
# patterns = ['software testing', 'guru99']
# text = 'software testing is fun?'
# for pattern in patterns:
#     print ('Looking for "%s" in "%s" ->' % (pattern, text),)
#     if re.search(pattern, text):
#         print ('found a match!')
# else:
#     print ('no match')
# abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
# emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
# for email in emails:
#     print (email)
#
# # Example of re.M or Multiline Flags
# import re
# xx = """guru99
# careerguru99
# selenium"""
# k1 = re.findall(r"^\w", xx)
# k2 = re.findall(r"^\w", xx, re.MULTILINE)
# print (k1)
# print (k2)