from iInvest import app
import os

port = int(os.environ.get('PORT', 33508))
app.debug=True
app.run(host='0.0.0.0',port=port)
