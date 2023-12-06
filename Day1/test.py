def decode_string(mapping_dict, input_string):
  result = ""
  i = 0
  while i < len(input_string):
    for key, value in mapping_dict.items(): # iterate over dictionary items
      if input_string.startswith(key, i):
        result += str(value[0])
        i += len(key)
        break
  return result


mapping = [("two", [5]), ("three", [8]), ("eight", [1])]
mapping_dict = dict(mapping) # create a dictionary from the list

input_string = "eightwothree"

output = decode_string(mapping_dict, input_string)
print(f"Expected output: {output}")
