from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize a simple linked list as a global list for demonstration
linked_list_data = []


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


if __name__ == '__main__':
    app.run(debug=True)
