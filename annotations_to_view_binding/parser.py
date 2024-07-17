import re

import_string_re= "^import org\.androidannotations\.annotations$"
layout_annotation_re= "^@EActivity\((.+)\)$"
view_by_id_annoration_re="@ViewById\s+"
variable_under_annotation_re= "(.+)\s(.+)" #group 1 type group 2 var name