from flask import Flask, jsonify, request, render_template
import mongoengine as db
import json

# Create Flask application object
app = Flask(__name__)

# Create connection to MongoDB database
client = db.connect('AnimeHub', username='', password='')

supported_regions = ["Asia", "Europe", "NorthAmerica"]
ANNIVERSARY_COMIC = "1"
COMIC_BOOK = "2"
ANNIVERSARY_ANIME = "3"
DELUXE = "4"
MYSTERY = "5"

# Data class for accessing Anime Hub Orders
class Order(db.Document) :
  customerName = db.StringField()
  customerAddress = db.StringField()
  customerRegion = db.StringField()
  customerEmail = db.StringField()
  customerPhone = db.StringField()
  
  packageNo = db.IntField()
  totalPrice = db.IntField()

  meta = {'collection': 'Order', 'allow_inheritance': False}

# A route that directs user to main page
# http://localhost:5000/
@app.route('/', methods=['GET'])
def get_index() :
  return render_template('index.html')


# A route that allows user to place order
# http://localhost:5000/order/new
@app.route('/order/new', methods=['POST', 'GET'])
def place_order() :

  if (request.method == 'GET'):
    return render_template('order_form.html')

  customer_name = request.form.get('customerName')
  customer_address = request.form.get('customerAddress')
  customer_region = request.form.get('customerRegion')
  customer_email= request.form.get('customerEmail')
  customer_phone = request.form.get('customerPhone')
  package_number = request.form.get('packageNumber')

  # Calculate total price
  total_price = 0

  # Calculate Region
  # If region is Asia
  if (customer_region == supported_regions[0]) :
    total_price += 100

  # If region is Europe
  elif (customer_region == supported_regions[1]) :
    total_price += 200

  # If region is North America  
  elif (customer_region == supported_regions[2]) :
    total_price += 150

  # Calculate Package
  # If Anniversary Comic Book selected
  if(package_number == ANNIVERSARY_COMIC):
    total_price +=  400 
  print("total price here", total_price)
  # If Comic Book selected
  if(package_number == COMIC_BOOK):
    total_price +=  800

  # If Anniversary Anime selected
  if(package_number == ANNIVERSARY_ANIME):
    total_price +=  1500

  # If Deluxe selected
  if(package_number == DELUXE):
    total_price +=  3000

  # If Mystery selected
  if(package_number == MYSTERY):
    total_price +=  1000

  newOrder = Order(customerName = customer_name, customerAddress = customer_address, 
  customerRegion = customer_region, customerEmail = customer_email, customerPhone = customer_phone,
  packageNo = package_number, totalPrice = total_price)

  newOrder.save()

  return "Order has been submitted. The total cost is $" + str(total_price)


if __name__ == '__main__':
 app.run(debug=True)
