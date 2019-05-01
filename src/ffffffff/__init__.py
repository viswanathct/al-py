def flow(*flows): # Returns a flow with the given sub-flows.
	flowCount = len(flows)

	def fn(data):
		i = 0
		lastReturnValue = None

		while lastReturnValue != False and i < flowCount:
			lastReturnValue = flows[i](data)
			i += 1

		return lastReturnValue

	return fn

def forgive(*flows): # Helps in continuing the flow with further elements in the input, even when an element blocks the flow.
	return lambda data: flow(*flows)(data) or None

def flip(*flows): # Expects a failure to coninue the flow. Helps in incorporating external helpers.
	return lambda data: False if flow(*flows)(data) == False else None

def fail(): # Syntactic sugar, used to signify a break in the flow.
	return False

def fork(forkFn, defaultFlow, forkedFlow): # Helps in altering between two flows.
	return lambda data: (forkedFlow if forkFn(data) == False else defaultFlow)(data)

def fix(fn, *flows): # Helps in intiiating recovery flows when a flow fails.
	return lambda data: flow(*flows)(data) if fn(data) == False else None

def follow(director): # Helps to switch to one among many flows, on the fly.
	return lambda data: director(data)(data)

def feed(items, *flows): # Helps in passing a list of items through a flow.
	i = 0
	l = len(items)
	lastReturnValue = None

	while i < l and lastReturnValue != False:
		lastReturnValue = flow(*flows)(items[i])
		i += 1

	return lastReturnValue
