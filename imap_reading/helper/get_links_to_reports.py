from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_links_to_report(html):

    """
    function that extract from html all links, that go to solarcloud reports

    Args:
        html (str): html from an email with potential inlcuding links to isloarcloud reports
        the links must contain the string "target=service=getPsReport" and the netloc must be "portal.isolarcloud.com"

    Returns:
        report_urls (list): List urls to the reports

    """

    link = None
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    report_urls = []
    for link in links:
        link_url = urlparse(link.get('href'))
        if "target=service=getPsReport" in link_url.fragment and link_url.netloc == "portal.isolarcloud.com":
            report_urls.append(link_url)
    return report_urls
