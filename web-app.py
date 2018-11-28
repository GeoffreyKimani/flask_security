from flask import Flask
from werkzeug.security import generate_password_hash

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


""" we use generate_password_hash() function to generate a hashed value for the password. 
NB: the hash uses a sha256 encryption algorithm + a salt. The salt ensures a different hash is produced even for the 
same password value and therefore our final binary value should reflect this changes accordingly, by also changing
as we refresh the browser page."""


@app.route('/<password>')
def password(password):
    # generate a hashed value using sha256 encryption algorithm. Hashes also include a salt.
    hashed_value = generate_password_hash(password)
    print(hashed_value)

    # convert each letter of the hash to the equivalent binary value
    return ' '.join(format(ord(x), 'b') for x in hashed_value)


if __name__ == '__main__':
    app.run(debug=True)
