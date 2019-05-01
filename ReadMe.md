# Assembly Line a.k.a. ffffffff

	A simple set of utilities, to help with building assembly-lines in Python.

## The `Why`

* Assembly lines help in implementing complex flows, in a manner -- easy to comprehend and maintain.
* Considerably improves readability.
* Allows for a hybrid-approach, by bringing together concepts from FP and Non-FP patterns.

## Installation
```sh
$ pip install ffffffff
```

## Use Cases

* Data pipelines.

* Asset pipelines.

* Complex and ever-changing business flows.

## Keys

* Simple functions are stiched together to compose complex flows.

* The same object is passed to all the functions in a flow, as the only argument.

* Returning false from a function, affects the flow of the all downstream functions. Utility functions help in deciding on, how the flow is affected.

## Notes

* The name flow, is a delibarate choice, to prevent confusing them with traditional pipes.

* Assembly lines are similar to unix pipes, builder pattern and the pipe-filter pattern from functional languages. Yet, there are some key differentiators:

	* Assembly lines feed the same entity to all the functions in a flow. They do not feed their return values downstream (like pipes / pipes-and-filters).

	* Builder pattern has a specific purpose, building a complex object; where as assembly lines are meant to be a generic pattern in managing complex flows, which might include the building of complex objects.

* When a flow looks complex, break it into sub-flows.

* The library doesn't have any dependencies.

* The package name **ffffffff** represents the primary utilitiy functions of the library. The lack of availability of the name -- **assemblyline, alpy and their likes** -- with PyPI played a part in choosing such an odd name. There are a few more reasons to the name:

	* ***False** plays a key role in controling the flow.*

	* The lib is all about functions.

	* All the key functions start with the letter, **F**.

	* *And **ffffffff** is also the hex code of white.*

# Development

## ToDo

* Bring in the cheatsheet example from al-js.

* Write tests.

* Write some examples and include a few of them in the ReadMe.

* Add some example bots. Especially, a batcher, a timer and an apiFetcher.

* Document the API.
