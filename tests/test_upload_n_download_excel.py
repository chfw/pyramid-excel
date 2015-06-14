import pyexcel as pe
from _compact import BytesIO

FILE_TYPE_MIME_TABLE = {
    "csv": "text/csv",
    "tsv": "text/tab-separated-values",
    "csvz": "application/zip",
    "tsvz": "application/zip",
    "ods": "application/vnd.oasis.opendocument.spreadsheet",
    "xls": "application/vnd.ms-excel",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "xlsm": "application/vnd.ms-excel.sheet.macroenabled.12"
}


class TestExcelResponse:
    def setUp(self):
        from myproject import main
        from webtest import TestApp
        self.raw_app = main({})
        self.app = TestApp(self.raw_app)
        self.data = [
            [1, 2, 3],
            [4, 5, 6]
        ]

    def test_download(self):
        for upload_file_type in FILE_TYPE_MIME_TABLE.keys():
            file_name = 'test.%s' % upload_file_type
            for download_file_type in ['tsv']:#FILE_TYPE_MIME_TABLE.keys():
                print("Uploading %s Downloading %s" % (upload_file_type, download_file_type))
                io = BytesIO()
                sheet = pe.Sheet(self.data)
                sheet.save_to_memory(upload_file_type, io)
                io.seek(0)
                response = self.app.post('/switch/%s' % download_file_type,
                                         upload_files = [('file', file_name, io.getvalue())],
                                         )
                assert response.content_type == FILE_TYPE_MIME_TABLE[download_file_type]
                sheet = pe.get_sheet(file_type=download_file_type, file_content=response.body)
                sheet.format(int)
                array = sheet.to_array()
                assert array == self.data

