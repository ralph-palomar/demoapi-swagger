import connexion
import config
from flask_cors import CORS
from waitress import serve
from paste.translogger import TransLogger

app = connexion.App(__name__, specification_dir='openapi/')
app.add_api('openapi.yaml')
api = app.app
CORS(api)

if __name__ == '__main__':
    try:
        serve(TransLogger(api, logger=config.logger), host='0.0.0.0', threads=16)
    except Exception as ex:
        config.logger.exception(ex)
