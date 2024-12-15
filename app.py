from flask import Flask, render_template, request
from queue_link_list import Queue
from input_restricted_deque import InputRestrictedDeque
from output_restricted_deque import OutputRestrictedDeque
from stack import infix_to_postfix

app = Flask(__name__)

# Initialize a simple linked list as a global list for demonstration
linked_list_data = []
postfix_steps = []
queue = Queue()
inputrestricted = InputRestrictedDeque()
outputrestricted = OutputRestrictedDeque()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/linked_list', methods=['GET', 'POST'])
def linked_list():
    global linked_list_data

    message = None  # Message to display feedback

    if request.method == 'POST':
        action = request.form['action']
        value = request.form.get('value', '').strip()

        if action == 'insert_beginning':
            linked_list_data.insert(0, value)
        elif action == 'insert_end':
            linked_list_data.append(value)
        elif action == 'search':
            # Searching for the value in the linked list
            if value in linked_list_data:
                message = f'Value "{value}" found at index {
                    linked_list_data.index(value)}.'
            else:
                message = f'Value "{value}" not found in the list.'
        elif action == 'delete_beginning' and linked_list_data:
            linked_list_data.pop(0)
        elif action == 'delete_end' and linked_list_data:
            linked_list_data.pop()
        elif action == 'delete_at':
            try:
                index = int(value)
                if 0 <= index < len(linked_list_data):
                    linked_list_data.pop(index)
                else:
                    message = f'Invalid index: {index}.'
            except ValueError:
                message = 'Please enter a valid index.'

    return render_template('linked_list.html', linked_list=linked_list_data, message=message)

@app.route("/stack", methods=["GET", "POST"])
def stack():
    global postfix_steps
    output = None
    message = None  # Initialize message to avoid UnboundLocalError

    if request.method == "POST":
        action = request.form.get("action")

        if action == "push":
            infix_expression = request.form.get("infix", "").strip()
            if infix_expression:  # Only process if infix_expression is not empty
                postfix_steps = infix_to_postfix(infix_expression)
                output = "\n".join(postfix_steps)
                message = "Conversion successful!"  # Inform user of successful conversion
            else:
                message = "Please enter a valid infix expression."
        elif action == "clear":
            # Clear the result and reset steps
            postfix_steps = []
            output = None
            message = "Stack cleared."

    return render_template("stack.html", output=output, message=message)



@app.route('/queue_file', methods=['GET', 'POST'])
def queue_operations():
    message = None

    if request.method == 'POST':
        action = request.form['action']
        value = request.form.get('value', '').strip()

        if action == 'enqueue':
            if value:
                queue.enqueue(value)
                message = f'"{value}" enqueued.'
            else:
                message = 'Please provide a value to enqueue.'
        elif action == 'dequeue':
            dequeued_value = queue.dequeue()
            if dequeued_value:
                message = f'Dequeued value: "{dequeued_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'

    return render_template('queue_file.html', queue=list(queue), message=message)


@app.route('/input_restricted_deque', methods=['GET', 'POST'])
def input_restricted_deque_operations():
    message = None

    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()

        if action == 'enqueue_at_end':
            if value:
                inputrestricted.enqueue_at_end(value)
                message = f'"{value}" enqueued.'
            else:
                message = 'Please provide a value to enqueue.'
    
        elif action == 'deque_at_beginning':
            dequeued_head_value = inputrestricted.dequeue_at_beginning()
            if dequeued_head_value:
                message = f'Dequeued value: "{dequeued_head_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'

        elif action == 'deque_at_end':
            dequeued_tail_value = inputrestricted.dequeue_at_end()
            if dequeued_tail_value:
                message = f'Dequeued value: "{dequeued_tail_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'

    return render_template('input_restricted_deque.html', inputrestricted=list(inputrestricted), message=message)


@app.route('/output_restricted_deque', methods=['GET', 'POST'])
def output_restricted_deque_operations():
    message = None

    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '').strip()

        if action == 'enqueue_at_end':
            if value:
                outputrestricted.enqueue_at_end(value)
                message = f'"{value}" enqueued.'
            else:
                message = 'Please provide a value to enqueue.'

        elif action == 'enqueue_at_beginning':
            if value:
                outputrestricted.enqueue_at_beginning(value)
                message = f'"{value} enqueued.'
            else:
                message = 'Please provide a value to enqueue'

        elif action == 'dequeue_at_beginning':
            dequeued_head_value = outputrestricted.dequeue_at_beginning()
            if dequeued_head_value:
                message = f'Dequeued value: "{dequeued_head_value}".'
            else:
                message = 'Queue is empty. Nothing to dequeue.'            

    return render_template('output_restricted_deque.html', outputrestricted=list(outputrestricted), message=message)


if __name__ == '__main__':
    app.run(debug=True)
