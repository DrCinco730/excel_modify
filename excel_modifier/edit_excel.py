import os
import zipfile
from io import BytesIO
from bs4 import BeautifulSoup


class EditExcel:
    def __init__(self, file_path, path_in_file):
        self.path = file_path
        self._validate_file_path()
        self._path_in_file = path_in_file
        self._path_content = self._get_path_content(self._path_in_file)
        self._path_info = self._get_info_path(self._path_in_file)

    def _validate_file_path(self):
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f"The file {self.path} was not found.")

    def _get_info_path(self, path_in_file):
        with zipfile.ZipFile(self.path) as zip_ref:
            return zip_ref.getinfo(path_in_file)

    def _get_path_content(self, path_in_file):
        with zipfile.ZipFile(self.path) as zip_ref:
            return BeautifulSoup(zip_ref.read(path_in_file), features="xml")

    def save(self):
        with BytesIO() as temp_zip_contents, zipfile.ZipFile(self.path) as zip_ref:
            with zipfile.ZipFile(temp_zip_contents, 'w', zipfile.ZIP_DEFLATED) as temp_zip:
                for item in zip_ref.infolist():
                    if item.filename != self._path_in_file:
                        temp_zip.writestr(item, zip_ref.read(item.filename))
                temp_zip.writestr(self._path_info, str(self._path_content))

            with open(self.path, 'wb') as file:
                file.write(temp_zip_contents.getvalue())
