import argparse

def parse_args():
	parser = argparse.ArgumentParser(description='描述信息')
	parser.add_argument(
		'-O', '--output', type=str, nargs='+', help='解释-o描述'
		)
	parser.add_argument(
		'-V', '--version', action='version', version='v1.0', help="print the production version number and exit."
		)
	parser.add_argument('config', default=None, help='train config file path')
	args = parser.parse_args()
	return args


if __name__ == "__main__":
	args = parse_args()
	print(args)
	print(args.config)
	print(args.output)
