from excel_modify.edit_main_comment import EditMainComment
from excel_modify.edit_shared_comment import EditSharedComment


class ExcelMode:
    def __init__(self, file_path, cell_comment):
        self._main_comment = EditMainComment(file_path, cell_comment)
        self._shared_comment = EditSharedComment(file_path)

    def set_comment(self, cell, value):
        old_value = self._main_comment.get_value(cell).string
        self._shared_comment.set_comment_change(old_value=old_value, new_value=value)
        self._main_comment.set_comment_change(cell, value)

    def save(self):
        self._main_comment.save()
        self._shared_comment.save()
