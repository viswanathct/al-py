from ffffffff import flow, feed

# Helpers
def x(x):
	print(x)

# Main
feed([1, 2], flow(
		x
	)
)
