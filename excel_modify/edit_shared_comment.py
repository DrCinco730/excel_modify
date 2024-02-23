from excel_modify.edit_excel import EditExcel


class EditSharedComment(EditExcel):
    def __init__(self, file_path):
        super().__init__(file_path, r"xl/sharedStrings.xml")

    def set_comment_change(self, old_value: str, new_value):
        t = self._path_content.find("t", string=old_value)
        if t:
            si = t.parent
            sst = si.parent
            si.extract()
            new_tag_si = self._path_content.new_tag("si")
            new_tag_t = self._path_content.new_tag("t")
            new_tag_t.string = new_value
            new_tag_si.append(new_tag_t)
            sst.append(new_tag_si)
