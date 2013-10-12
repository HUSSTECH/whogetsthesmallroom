from flask import Flask, render_template, redirect, request
import math

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET','POST'])
def result():
	if request.method == 'GET':
		return render_template('index.html', title='WGTSR?')
	else: #Method is Post

		app.normrooms = [] #area of each room as percent
		app.logscalerooms = [] #log of room areas
		app.lognormrooms = [] #log adjusted area of each room as percent
		app.price = [] #rent for each room based on all of this stuff
		app.rent = request.form["rent"]
		app.rooms = request.form.values()
		app.rooms.remove(app.rent)
		app.rooms.sort()
		app.rooms.reverse()

		app.rent = float(app.rent)
		app.rooms = [float(i) for i in app.rooms]

		app.nrooms = len(app.rooms) #number of rooms
		app.sumrooms = sum(app.rooms) #total area of rooms

		for x in app.rooms:
			app.normrooms.append(x/app.sumrooms)
		for x in app.normrooms:
			app.logscalerooms.append(math.log10(x*app.rent))
		for x in app.logscalerooms:
			app.lognormrooms.append(x/sum(app.logscalerooms))
		for x in app.lognormrooms:
			app.price.append(round(x*app.rent,2))

		app.price.sort()
		app.price.reverse()

		return render_template('index2.html', title='WGTSR?',rooms=app.rooms,rent=app.rent,price=app.price)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run()