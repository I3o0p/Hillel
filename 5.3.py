import string

examples = [
    'Python Community',
    'i like python community!',
    'Should, I. subscribe? Yes!'
]

for example in examples:
    example = example.translate(str.maketrans('', '', string.punctuation))

    words = example.split()

    hashtag = '#' + ''.join(word.capitalize() for word in words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    print(hashtag)
