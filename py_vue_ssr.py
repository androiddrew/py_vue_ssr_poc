from py_mini_racer import py_mini_racer

def read_in_file(path):

	with open(path, mode='r') as f:
		return f.read()



def main():
	ctx = py_mini_racer.MiniRacer()
	ctx.eval('var process = { env: { VUE_ENV: "server", NODE_ENV: "production" }}; this.global = { process: process };')
	ctx.eval(read_in_file('./node_modules/vue/dist/vue.js'))
	ctx.eval(read_in_file('./node_modules/vue-server-renderer/basic.js'))
	ctx.eval(read_in_file('./ssr_example.js'))
	result = ctx.eval("result")

	print(result)


if __name__ == '__main__':
	main()
