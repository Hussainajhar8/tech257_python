double_quotes_str = "Look! Double quotes!"
single_quotes_str = 'Look! Single quotes!'
triple_quotes_str = '''Look! Triple quotes!
'''

print(double_quotes_str)
print(single_quotes_str)
print(triple_quotes_str)

test_str = 'I said \'Wow!\''
print(test_str)
test_str = "I said 'Wow!'"
print(test_str)

hello_str = "      hello my name is      "
print(len(hello_str))
hello_stripped = " hello my name is ".strip()
print(len(hello_stripped))


example_str = "Here's some text with lots of text"
print(example_str)
print(type(example_str.count("text")))