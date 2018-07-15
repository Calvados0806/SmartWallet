#!/usr/bin/env python3
"this module contains main code"

import argparse
import database as db

def main():
	parser = argparse.ArgumentParser(description="SmartWallet - script "
	                                             "using database to manage "
	                                             "your costs")
	parser.add_argument("-s", "--supply", metavar='N', type=int,
	                    help="a float number of sum")
	parser.add_argument("-b", "--balance", action="store_true",
	                    help="get balance from wallet")
	parser.add_argument("-H", "--history", type=int, nargs='?', const=0,
	                    help="get history")
	parser.add_argument("-d", "--discard", nargs=2, metavar="data",
	                    help="set purchase")
	args = parser.parse_args()
	if args.supply:
		db.supply(db.cursor, args.supply)
		print("Successful supplying!")
	elif args.balance:
		bal = db.get_balance(db.cursor)
		print("You have {0} UAN".format(bal))
	elif args.history or args.history == 0:
		res = db.get_history(db.cursor, args.history)
		if res:
			for i in res:
				print("{1} := {2}".format(*i))
		else:
			print("There is no info yet")
	elif args.discard:
		try:
			n = int(args.discard[0])
		except ValueError:
			print("N is not a number")
			exit(1)
		db.discard(db.cursor, n, args.discard[1])
		print("Successful discarding!")
	else:
		print("Print `--help` or `-h` to find out arguments")

if __name__ == "__main__":
	main()
