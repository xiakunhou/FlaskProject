from iInvest import app
import os

#app=app
port = int(os.environ.get('PORT', 33508))
app.debug=True
#if __name__=='__main__':
app.run(host='0.0.0.0',port=port)
