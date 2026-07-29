from werkzeug.utils import secure_filename
from flask import current_app
import os


class UploadService:

    @staticmethod
    def save_file(file):

        filename = secure_filename(file.filename)

        upload_path = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(upload_path)

        return filename, upload_path