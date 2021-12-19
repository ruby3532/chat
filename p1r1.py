
# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換格式
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen' # 存下來的話，就可以用
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 如果 person 有值，才繼續執行
			new.append(person + ': ' + line)	
	return new

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')	
	lines = convert(lines)
	write_file('output1.txt', lines)	

main()





