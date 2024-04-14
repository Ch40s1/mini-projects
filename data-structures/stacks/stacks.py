''' 
A real-world example of a stack could be the browser history feature in web browsers.

 When you visit a web page, the URL of that page is pushed onto a stack. If you click on a link to navigate to another page, 
 the URL of the current page is pushed onto the stack again. This process continues for each page you visit.

When you click the "Back" button in the browser, it pops the URL from the stack, effectively 
taking you back to the previously visited page. If you keep clicking "Back", it continues to pop URLs from the stack, 
effectively navigating you back through your browsing history.
'''


class Stack:
    def __init__(self):
        self.websites = []

    # stack.push(website) -> add a website to teh list
    def push(self, site):
        self.websites.append(site)
    # stack.peek() -> returns the top item from the stack without modifying the stack

    def peek(self):
        if len(self.websites) != 0:
            return self.websites[-1]
        else:
            print("Stack is empty")
    # stack.size() -> returns the number of items in the stack


stack = Stack()
stack.push("google.com")

print("Top of the stack", stack.peek())
