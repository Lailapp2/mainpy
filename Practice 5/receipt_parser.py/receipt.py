#string that has 'a' followed by zero or more 'b'
import re
pattern = r"ab*"
text = "abbb a ab abb"
matches = re.findall(pattern, text)
print(matches)

#string that has 'a' followed by 2–3 'b'
import re
pattern = r"ab{2,3}"
text = "ab abb abbb abbbb"
matches = re.findall(pattern, text)
print(matches)

#sequences of lowercase letters joined with underscore
import re
pattern = r"[a-z]+_[a-z]+"
text = "hello_world test_value Hello_World another_example"
matches = re.findall(pattern, text)
print(matches)

#sequences of one uppercase letter followed by lowercase letters
import re
pattern = r"[A-Z][a-z]+"
text = "Hello World TEST Python Regex"
matches = re.findall(pattern, text)
print(matches)

#string that has 'a' followed by anything, ending in 'b'
import re
pattern = r"a.*b"
text = "acccb axxxb ab a123b"
matches = re.findall(pattern, text)
print(matches)

#Replace space, comma, or dot with colon
import re
text = "Hello, world. Python is fun"
result = re.sub(r"[ ,\.]", ":", text)
print(result)

#Convert snake_case → camelCase
def snake_to_camel(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
text = "hello_world_python"
print(snake_to_camel(text))

#Split a string at uppercase letters
import re
text = "HelloWorldPython"
result = re.findall(r'[A-Z][^A-Z]*', text)
print(result)

#Insert spaces between words starting with capital letters
import re
text = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)

#Convert camelCase → snake_case
import re
def camel_to_snake(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')
text = "helloWorldPython"
print(camel_to_snake(text))