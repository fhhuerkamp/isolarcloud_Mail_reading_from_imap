from imap_reading.services.read_report.read_url_with_selenium import read_url_with_selenium
import os
from dotenv import load_dotenv


def test_read_url_with_selenium():
    load_dotenv(override=False)
    url=os.environ.get("EXAMPLE_REPORT_URL")
    html = read_url_with_selenium(url,['report-table','el-table_1_column_9'],"test_output.html")
    assert len(html) > 0
    matches = ['23:00','report-table', 'el-table_1_column_9']
    for teststring in matches:
        assert teststring in html


if __name__ == "__main__":
    test_read_url_with_selenium()
