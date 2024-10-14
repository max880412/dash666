from flask import Flask, render_template

app = Flask(__name__)

# Datos simulados de criptomonedas
balances = {
    "BTC": 0.5,
    "EOS": 120.75,
    "USDT": 300.00,
    "Solana": 50.25,
    "Cardano": 1000.00
}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', balances=balances)

if __name__ == '__main__':
    app.run(debug=True)
