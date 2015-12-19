"""
This script runs the HotOpinion application using a development server.
"""

from HotOpinion import app, db
import config
# from database import init_db

if __name__ == '__main__':
    db.create_all()
    # app.run(HOST, PORT)
    app.run(host="0.0.0.0",
            debug=config.DEBUG)
