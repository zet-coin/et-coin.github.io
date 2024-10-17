from flask import Flask, jsonify, request
import subprocess
app = Flask(__name__)

@app.route('/api/verify', methods=['GET'])
def verify():
    coin = request.args.get('coin')  # Extract the coin from the query parameter
    if not coin:
        return jsonify({"error": "coin parameter is missing"}), 400  # Return error if coin is missing

    # Use f-string to include the 'coin' variable in the command
    command = f"python zetcoin.py verify {coin}"

    # Run the subprocess and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    # Return the result as JSON
    return jsonify({"res": result.stdout.replace("\n", "")})

@app.route('/api/exchange', methods=['GET'])
def exchange():
    coin = request.args.get('coin')  # Extract the coin from the query parameter
    if not coin:
        return jsonify({"error": "coin parameter is missing"}), 400  # Return error if coin is missing

    # Use f-string to include the 'coin' variable in the command
    command = f"python zetcoin.py exchange {coin}"

    # Run the subprocess and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    # Return the result as JSON
    return jsonify({"res": result.stdout.replace("\n", "")})

if __name__ == '__main__':
    app.run(debug=True)
