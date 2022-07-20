import sys

def main():
	speed = sys.argv[1]
	size = sys.argv[2]
	flag = sys.argv[3]
	# result = '{"speed": "' + str(speed) +'", "size": "' + str(size) + '", "flag": "' + str(flag) + '"}'
	result = '{"count": "' + str(5000) +'"}';
	print (result)
	sys.stdout.flush()

if __name__ == '__main__':
	main()