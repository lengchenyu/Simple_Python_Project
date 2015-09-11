#encoding=utf-8
def lines(file):
	for line in file:
		yield line
	yield '\n' #思考：为什么要加这一行？  答：为了取回最后一个block


def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []