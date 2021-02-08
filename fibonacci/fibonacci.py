import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", type=int,
                    help="display nth fibonacci")
parser.add_argument("-m", "--method", type= int,
                    help="method for fibonacci calcualtion", choices=[0, 1, 2])

args = parser.parse_args()


def iterativefib(n):
	'''iterative fibonacci'''

	if n <1:
		return -1
	elif n ==1:
		return 0
	elif n==2:
		return 1

	a, b, c = 0, 1 , 0

	for i in range(3, n+1):
		c = a + b
		a, b = b, c
	return c

def recursivefib(n):
	'''recursive fibonnacci calculation'''
	if n <1:
		return -1
	elif n ==1:
		return 0
	elif n==2:
		return 1

	return recursivefib(n-1) + recursivefib(n-2)


def memofib(n, mdict = {1:0, 2: 1}):

	if n in mdict:
		return mdict[n]
	else:
		mdict[n] = memofib(n-1, mdict) + memofib(n-2, mdict)
		return mdict[n]

if args.method== 0:
	print(f"Recursive {args.number}th fibonacci is {recursivefib(args.number)}.")
elif args.method ==1:
	print(f"Iterative {args.number}th fibonacci is {iterativefib(args.number)}.")
else:
	print(f"Dynamic fib {args.number}th fibonacci is {memofib(args.number)}.")
