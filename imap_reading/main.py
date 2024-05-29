#
#
#

from dotenv import load_dotenv
import os
from imap_reading.services.read_mails.read_mails import read_mails_from_mailserver
from imap_reading.services.read_mails.get_links_to_reports import get_links_to_report




if __name__ == "__main__":
    load_dotenv(override=False)
    host=os.environ.get("IMAPHOST")
    user=os.environ.get("IMAPUSER")
    password=os.environ.get("IMAPPASSWORD")
    sender=os.environ.get("SENDER")
    mails = read_mails_from_mailserver(host,user,password,sender, daysback=1)

    report_urls=[]
    for mail in mails:
        url = get_links_to_report(mail.body)
        mail_dict = {"message_id": mail.message_id,
                     "sent_date": mail.m_date,
                     "report_url": url}
        # import ipdb; ipdb.set_trace()
        report_urls.append(mail_dict)

    print (f"Urls of report: {report_urls}")
