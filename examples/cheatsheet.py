# The cheatsheet, example.

from ffffffff import *
from helpers import log, runExamples

# Data
orders = [
	{
		'product': 'shoes',
		'price': 10,
		'quantity': 1,
	},
	{
		'product': 'apples',
		'price': 20,
		'quantity': 10,
	},
]
reversedOrders = orders[:]
reversedOrders.reverse()
stock = {
	'shoes': 10,
	'apples': 5,
}

# Flows
def verifyStock(order):
	isInStock = stock[order['product']] >= order['quantity']
	log('%s %s stock!' % (order['product'],
		'in' if isInStock else'out of')
	)
	return isInStock

def procureProduct(order):
	log('Procuring {quantity} {product}.'.format(**order))

def calculateTotal(order):
	log('Calculating total...')
	order['total'] = order['quantity'] * order['price']

def dispatchProduct(order):
	log('Dispatching {quantity} {product}.'.format(**order))

def doNothing(order):
	log('Doing nothing!')

# Examples
class examples:
	def ex_01_simple_flow(self):
		feed(orders, flow(
			calculateTotal,
			dispatchProduct,
		))

	def ex_02_simple_flow_with_validation(self):
		feed(orders, flow(
			verifyStock, # The flow breaks when validation fails.
			calculateTotal,
			dispatchProduct,
		))

	def ex_03_flow_with_forgive(self):
		feed(orders, flow(
			forgive(verifyStock), # Forgive helps in continuing the flow, despite failure.
			calculateTotal,
			dispatchProduct,
		))

	def ex_04_flow_with_fix(self):
		feed(orders, flow(
			fix(verifyStock, procureProduct), #procureProduct is called only when verifyStock fails.
			calculateTotal,
			dispatchProduct,
		))

	def ex_05_flow_with_fork(self):
		completeDispatch = flow(calculateTotal, dispatchProduct) #NOTE: Flows could be combined.

		feed(orders, flow(
			fork(verifyStock,
				completeDispatch, # The pass case.
				procureProduct # The fail case.
			),
		))

	def ex_06_flow_with_flip(self):
		feed(reversedOrders, flow(
			flip(verifyStock), #Fix expects a failure to proceed. This is partly due to to help while leveraging third-party functions.
			procureProduct,
		))

	def ex_07_flow_with_fail(self):
		feed(reversedOrders, flow(
			fix(verifyStock, procureProduct, fail), # Fails stops the flow. The fucntion is a syntactic-sugar, as well as an aid to improve readability.
			calculateTotal,
			dispatchProduct,
		))

	def ex_08_flow_with_follow(self):
		feed(orders, flow(
			follow(
				lambda order: procureProduct if verifyStock(order) else doNothing # Choose a path to follow, on the fly.
			),
			calculateTotal,
			dispatchProduct,
		))

# Main
runExamples(examples)
