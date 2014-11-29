import os
import sys
import subprocess
def get_immediate_subdirectories(a_dir):
	return [name for name in os.listdir(a_dir)
		if os.path.isdir(os.path.join(a_dir, name))]

if __name__ == "__main__":
	dirs = get_immediate_subdirectories(sys.argv[1])
	print  sys.argv[2]
	if sys.argv[2].strip() == "2":
		bash = "./plotPhase2.sh"
	elif sys.argv[2].strip() == "1":
		bash = "./plotPhase1.sh"
	for di in dirs:
		cmd = [ bash, os.path.join(sys.argv[1], di)]
		subprocess.call(cmd)
