num = []

for i in range(1,11):
    num.append(i)

print("Original list: ", num)
extract = num[:5]
print("Extracted first five elements:", extract)
revextract = list(reversed(extract))
print("Reversed extracted elements:",revextract)