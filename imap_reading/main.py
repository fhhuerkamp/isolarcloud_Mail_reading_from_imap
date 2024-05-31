#
#
#
from imap_reading.services.read_mails.read_mails import read_mails_from_mailserver
from imap_reading.services.read_mails.get_links_to_reports import get_links_to_report
from imap_reading.helper.get_env import get_env



if __name__ == "__main__":
    host=get_env("IMAPHOST")
    user=get_env("IMAPUSER")
    password=get_env("IMAPPASSWORD")
    sender=get_env("SENDER")
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
