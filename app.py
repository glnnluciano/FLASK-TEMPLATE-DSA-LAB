from flask import Flask, render_template, request

app = Flask(__name__)


# Initialize a simple linked list as a global list for demonstration
linked_list_data = []

# Route for the home page


@app.route('/')
def home():
    return render_template('index.html')

# Route for the About page


@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Works page


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
# Route for the Linked List page, handling both GET and POST methods


@app.route('/linked_list', methods=['GET', 'POST'])
def linked_list():
    global linked_list_data  # Reference the global list

    if request.method == 'POST':
        # Get the selected action (insert or delete)
        action = request.form['action']
        value = request.form['value']  # Get the value input by the user

        if action == 'insert_beginning':
            # Insert at the beginning of the list
            linked_list_data.insert(0, value)
        elif action == 'insert_end':
            # Insert at the end of the list
            linked_list_data.append(value)
        elif action == 'delete_beginning' and linked_list_data:
            # Delete from the beginning of the list
            linked_list_data.pop(0)
        elif action == 'delete_end' and linked_list_data:
            # Delete from the end of the list
            linked_list_data.pop()

    # Render the linked list page, passing the updated linked list data
    return render_template('linked_list.html', linked_list=linked_list_data)


if __name__ == '__main__':
    app.run(debug=True)
