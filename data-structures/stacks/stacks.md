# Stacks

## what is a stack?
A Stack is an abstract data type that serves as a collection of elements. It uses LIFO ( last in first out).
It can store any data.

## What it has?

* stack.push(item) -> places a new item on top of the stack
* stack.pop() -> removes the top item from the stack and returns it
* stack.peek() -> returns the top item from the stack without modifying the stack
* stack.size() -> returns the number of items in the stack

## Notes
I visualize them as a stack of plates. We grab from the top downward. The time complexity of the push, pop, peek and size methods
is O(1). The time complexity to remove the last item is O(n) because we would need to remove all the items on top and work
our way downward.



