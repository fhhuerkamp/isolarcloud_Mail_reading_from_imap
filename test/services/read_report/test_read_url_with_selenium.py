from imap_reading.services.read_report.read_url_with_selenium import read_url_with_selenium
from imap_reading.helper.get_env import get_env


def test_read_url_with_selenium():
    url=get_env("EXAMPLE_REPORT_URL")
    html = read_url_with_selenium(url,['report-table','el-table_1_column_9'],"test_output.html")
    assert html != None
    assert len(html) > 0
    matches = ['23:00','report-table', 'el-table_1_column_9']
    for teststring in matches:
        assert teststring in html
