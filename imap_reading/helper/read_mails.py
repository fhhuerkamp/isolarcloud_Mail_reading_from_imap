"""
    helper read_mails
"""
from imaplib import IMAP4
from imap_reading.model.MailContent import MailContent
from datetime import date,timedelta


def store_mail_in_file (raw_mail, mailcontent):
    with open(mailcontent.message_id,mode='wb') as f:
        f.write(raw_mail)
    return mailcontent.message_id


def read_mails_from_mailserver(imaphost, imapuser, imappassword, sender='system@isolarcloud.com',daysback=5):

    """
    read mails from IMAP-Server that are comming from sender.

    Args:
        imaphost (str): hostname of the imap-server
        imapuser (str): username of the imap-account
        imappassword (str): password of the imap-account
        sender (str): select only mails from sender. Content of the FROM-header-field
        daysback (int): Only look for emails in the last <daysback> days

    Returns:
        mails (list): List of mails as instances of MailContent-Class

    """
    mails = []
    M = IMAP4(imaphost)
    M.login(imapuser, imappassword)
    M.select()
    since_date = date.today() - timedelta(days=daysback)
    criterion = f'FROM "{sender}" SINCE "{since_date.strftime("%d-%b-%Y")}"'
    typ, data = M.search(None, criterion)
    for num in data[0].split():
        typ, mail = M.fetch(num, '(RFC822)')
        if typ == 'OK':
            for items in mail:
                for item in items:
                    if type(item) == bytes:
                        if len(item) > 50:
                            mailcontent = MailContent(item)
                            mails.append(mailcontent)
                            store_mail_in_file(item,mailcontent)

    M.close()
    M.logout()
    return mails

def read_mails_from_file(mail_file):

    """
    read mail from file.

    Args:
        mail_file(str) name of the file with the raw mail content.

    Returns:
        mail  as instances of MailContent-Class

    """
    mailcontent = None
    with open(mail_file,  mode="rb") as f:
        item = f.read()

    if len(item) > 50:
        mailcontent = MailContent(item)
    return mailcontent
