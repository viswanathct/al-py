# Helpers
from time import sleep

# State
logs = []

def runExamples(examples, speed=200):
	global logs
	exampleNames = filter(lambda name: 'ex_' in name, list(examples.__dict__.keys()))
	exampleNames.sort()
	examples = examples()

	for exampleName in exampleNames:
		logs += [exampleName]
		getattr(examples, exampleName)()
		logs += ['']

	for line in logs:
		sleep(speed / 1000.0)
		print(line)

def log(x):
	global logs
	logs += ['\t%s' % x]
