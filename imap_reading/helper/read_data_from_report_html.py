from bs4 import BeautifulSoup
import pandas as pd

def get_cell_text(list_td_tag):
    """
        find a div-tag with CSS-class "cell" and return  the content as text
        limitations: returns only the first occurrence in each tag

        Args:
            list_td_tag: a list of bs4 tags.
    """
    rc = []
    for td_tag in list_td_tag:
        cell = td_tag.find("div",class_="cell")
        if cell:
            rc.append(cell.text)
    return rc

def read_data_from_report_html(html):

    """
        parses a html string containing the report of isolarcloud

        Args:
            html:   html-code after requesting a page with the selenium model.
                    it must contain a table with a TH tag and a list of TD tags
        returns:
            title:  title of the report found in DIV tag with class "report-title"
            df:     a dataframe with column headers from the TH tags and the values
                    in the TD tags.
    """

    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find("div",class_="report-title")
    rc = []
    column_header = get_cell_text(soup.find_all('th'))[1:]   # First column is not relevant
    # rc.append(column_header)
    for column_names in  ['el-table_1_column_'+str(i) for i in range(2,10)]:
        rc.append(get_cell_text(soup.find_all('td',class_=column_names)))
    print(rc)
    df = pd.DataFrame(rc).T
    df.columns=column_header
    print (df)
    return title_tag.text,df

if __name__ == "__main__":
    """
        only for testing purposes. Run the function with test data from "output.html"
    """

    with open("Output.html") as f:
        html = f.read()

    read_data_from_report_html(html)
