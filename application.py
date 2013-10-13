from flask import Flask, render_template, redirect, request
import math

application = Flask(__name__,static_url_path='/s') #static_url_pth added to workaround static path issue on eb
#application.debug = True

@application.route('/', methods=['GET','POST'])
def result():
	if request.method == 'GET':
		return render_template('index.html', title='WGTSR?')
	else: #Method is Post

		application.normrooms = [] #area of each room as percent
		application.logscalerooms = [] #log of room areas
		application.lognormrooms = [] #log adjusted area of each room as percent
		application.price = [] #rent for each room based on all of this stuff
		application.rent = request.form["rent"] #total rent
		application.rooms = request.form.values() #post request from the form
		application.rooms.remove(application.rent) #remove the rent from list
		application.rooms.sort() 
		application.rooms.reverse()

		application.rent = float(application.rent)
		application.rooms = [float(i) for i in application.rooms]

		application.nrooms = len(application.rooms) #number of rooms
		application.sumrooms = sum(application.rooms) #total area of rooms

		for x in application.rooms: #normalise room area
			application.normrooms.append(x/application.sumrooms)
		for x in application.normrooms: #log of the normalised room areas
			application.logscalerooms.append(math.log10(x*application.rent))
		for x in application.logscalerooms: #calc log scale factor for rooms
			application.lognormrooms.append(x/sum(application.logscalerooms))
		for x in application.lognormrooms: #do the scaling
			application.price.append(round(x*application.rent,2))

		application.price.sort()
		application.price.reverse()

		return render_template('index2.html', title='WGTSR?',rooms=application.rooms,rent=application.rent,price=application.price)

@application.route('/about')
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
    application.run(host='0.0.0.0') #host='0.0.0.0'