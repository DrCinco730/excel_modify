from excel_modify.edit_excel import EditExcel


class EditMainComment(EditExcel):
    def __init__(self, file_path, cell_comment):
        self.cell_comment = cell_comment
        super().__init__(file_path, r"xl/comments1.xml")

    def get_value(self, cell):
        cell_number = "".join([x for x in cell if x.isnumeric()])
        comments = self._path_content.find_all('comment')
        for comment in comments:
            ref = comment['ref']
            if ref == self.cell_comment + cell_number:
                return comment.find('t')

    def new_comment(self, cell, value):
        cell_number = "".join([x for x in cell if x.isnumeric()])
        comments_list = self._path_content.find("commentList")
        ref = comments_list.find("comment")["ref"]
        ref_alpha = "".join([x for x in ref if x.isalpha()])
        if ref_alpha == self.cell_comment:
            pass
        else:
            children = comments_list.children
            for x in children:
                x.extract()

        comment_tag = self._path_content.new_tag("comment", ref=self.cell_comment + cell_number, authorId="0", shapeId="0")

        text_tag = self._path_content.new_tag("text")
        r_tag = self._path_content.new_tag("r")

        rPr_tag = self._path_content.new_tag("rPr")
        sz_tag = self._path_content.new_tag("sz", val="9")
        color_tag = self._path_content.new_tag("color", indexed="81")
        rFont_tag = self._path_content.new_tag("rFont", val="Tahoma")
        family_tag = self._path_content.new_tag("family", val="2")

        # Building the hierarchy
        rPr_tag.append(sz_tag)
        rPr_tag.append(color_tag)
        rPr_tag.append(rFont_tag)
        rPr_tag.append(family_tag)

        t_tag = self._path_content.new_tag("t")
        t_tag.string = value

        r_tag.append(rPr_tag)
        r_tag.append(t_tag)

        text_tag.append(r_tag)

        comment_tag.append(text_tag)

        comments_list.append(comment_tag)

    def set_comment_change(self, cell: str, value):
        self.get_value(cell).string = value
