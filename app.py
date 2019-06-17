
import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
  amount = 500

  stripe.Charge.create(
    amount=amount,
    currency='usd',
    card=request.form['stripeToken'],
    description='Stripe Flask'
  )

  return render_template('charge.html', amount=amount)

if __name__ == '__main__':
  app.run(debug=True)