import uvicorn

from Importers.common_imports import *
from Config.fastapi import *
from Helpers.booking import *
from Services.admin_auth import *
from Services.auth import *
from Services.booking import *
from Services.room import *
from Services.reports import *

if __name__ == '__main__':
    uvicorn.run(app=app,host='localhost', port=8000, log_level='debug', root_path="/api/v1")