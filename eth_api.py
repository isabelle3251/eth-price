from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/eth-price')
def eth_price():
    # ETH price that follows ETH price pattern
    real_eth_price = 2370 + random.randint(-75, 75)  # Mimics ETH fluctuations
    return jsonify({"eth": real_eth_price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)