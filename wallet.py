"this module contains main code"

import argparse
import database as db

def main():
	parser = argparse.ArgumentParser(description="SmartWallet - script "
	                                             "using database to manage "
	                                             "your costs")
	parser.add_argument("-s", "--supply", metavar='N', type=float,
	                    help="a float number of sum")
	parser.add_argument("-b", "--balance", action="store_true",
	                    help="get balance from wallet")
	parser.add_argument("-H", "--history", type=int, nargs='?', const=0,
	                    help="get history")
	parser.add_argument("-d", "--discard", nargs=2, metavar="data",
	                    help="set purchase")
	args = parser.parse_args()

if __name__ == "__main__":
	main()