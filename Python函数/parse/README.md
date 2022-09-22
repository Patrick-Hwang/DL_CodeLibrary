```python
import argparse
def parse_args():
	parser = argparse.ArgumentParser(description='描述信息')
	parser.add_argument(# nargs 表示多个值输入
		'-O', '--output', type=str, nargs='+', help='解释-o描述'
		)
	parser.add_argument(	# action，不能用print(args.version)，只能在终端输出版本号：python funname.py -V
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
```

输入`python funname.py -h`课得到当前parse函数的帮助信息，返回如下：

```shell
usage: parse_fun.py [-h] [-O OUTPUT [OUTPUT ...]] [-V] config

描述信息
positional arguments:
  config                train config file path

optional arguments:
  -h, --help            show this help message and exit
  -O OUTPUT [OUTPUT ...], --output OUTPUT [OUTPUT ...]
                        解释-o描述
  -V, --version         print the production version number and exit.
```

`config`参数是位置参数，即在终端输入时必须有该值的输入。

`-参数`或`--参数`是可选参数，即输入时候可以选择是否输入。



**参考:**

[Python Parser的用法_python_脚本之家 (jb51.net)](https://www.jb51.net/article/212035.htm)



