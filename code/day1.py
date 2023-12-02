

with open(r'data\day1_puzzle.txt', 'r') as f:
    data = f.read()
lines = data.split('\n')
total = 0

for line in lines: 
    converted_line = list(line)
    process_line = [char for char in converted_line if not char.isalpha()]
    value = process_line[0] + process_line[-1]
    total += int(value)

print(total)
    
    