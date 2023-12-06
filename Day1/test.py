number_words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

# Example usage
mapping = [('two', [5]), ('three', [8]), ('eight', [1])]
input_string = 'eightwothree'
output_string = input_string

for word, indices in mapping:
        for index in indices:
            output_string = output_string.replace(word, number_words[word])

print(output_string)  # This will print the expected output