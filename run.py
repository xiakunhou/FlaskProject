from iInvest import app

port = int(os.environ.get('PORT', 5000))
app.debug=True
if __name__=='__main__':
	app.run(host='0.0.0.0',port=port)
