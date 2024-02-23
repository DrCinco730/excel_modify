from excel_modifier.edit_excel import EditExcel


class EditMainComment(EditExcel):
    def __init__(self, file_path):
        super().__init__(file_path, r"xl/comments1.xml")

    def get_value(self, cell):
        cell_number = "".join([x for x in cell if x.isnumeric()])
        comments = self._path_content.find_all('comment')
        for comment in comments:
            ref = comment['ref']
            if ref == "AR" + cell_number:
                return comment.find('t')

    def set_comment_change(self, cell: str, value):
        self.get_value(cell).string = value
