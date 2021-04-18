import os
import shutil
from io import BytesIO
from zipfile import ZipFile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings

local_storage = FileSystemStorage()


class ZipResponseMixin:
    def response(self, request, files: list, folder_name: str) -> HttpResponse:
        """Zip Response

        Generate a zip file from given file list and return Http response (Force download)

        :param request: request Object
        :param files: list of file like objects saved in models
        :param folder_name: desired folder name
        :return:
        """
        folder_abs_path = f"{settings.MEDIA_ROOT}/temp-dl/{str(request.user.first_name)}/{folder_name}"
        if os.path.exists(folder_abs_path):
            shutil.rmtree(folder_abs_path)
        os.makedirs(folder_abs_path)
        file_names = list()
        for file in files:
            self._temp_save(file, file_names, folder_abs_path)
        buffer = BytesIO()
        zf = ZipFile(buffer, "w")
        for name in file_names:
            file_abs_path = folder_abs_path + "/" + name
            zf.write(file_abs_path, name)
        zf.close()
        response = HttpResponse(buffer.getvalue(), content_type="application/zip")
        response["Content-Disposition"] = f"attachment; filename={folder_name}.zip"
        return response

    def _temp_save(self, file, file_names, folder_abs_path):
        if file is not None:
            file_name = os.path.basename(file.name)
            file_abs_path = folder_abs_path + "/" + file_name
            local_storage.save(file_abs_path, file)
            file_names.append(file_name)
