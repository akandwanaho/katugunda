from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/join')
def join():
    return render_template('join.html')

# Route to show the password prompt
@app.route('/donations')
def donations():
    return render_template('donations_password.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form.get('password')
    if password == "katugu12@":
        return render_template('donations.html')
    else:
        flash("Sorry, this information is restricted.")
        return redirect(url_for('home'))


@app.route('/delete_donations', methods=['POST'])
def delete_donations():
    print("Delete donations route accessed.")
    print(f"Request method: {request.method}")
    if request.method != 'POST':
        return jsonify({'status': 'error', 'message': 'Invalid request method'}), 405

    indexes_to_delete = request.json.get('indexes', [])
    print(f"Indexes received for deletion: {indexes_to_delete}")
    return jsonify({'status': 'success'})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5001 to any available port
