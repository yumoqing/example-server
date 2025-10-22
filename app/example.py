from ahserver.serverenv import ServerEnv
from ahserver.webapp import webapp
from bricks_for_python.init import load_pybricks

def get_module_dbname(module_name):
	return 'test'

def init():
	env = ServerEnv()
	env.get_module_dbname = get_module_dbname
	load_pybricks()

if __name__ == '__main__':
	webapp(init)
