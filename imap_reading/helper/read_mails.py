"""
    helper read_mails
"""
from imaplib import IMAP4
from imap_reading.model.MailContent import MailContent


def read_mails(imaphost, imapuser, imappassword, sender='system@isolarcloud.com'):

    """
    read mails from IMAP-Server that are comming from sender.

    Args:
        imaphost (str): hostname of the imap-server
        imapuser (str): username of the imap-account
        imappassword (str): password of the imap-account
        sender(str): select only mails from sender. Content of the FROM-header-field

    Returns:
        mails (list): List of mails as instances of MailContent-Class

    """
    mails = []
    M = IMAP4(imaphost)
    M.login(imapuser, imappassword)
    M.select()
    typ, data = M.search(None, 'FROM',sender)
    for num in data[0].split():
        typ, mail = M.fetch(num, '(RFC822)')
        if typ == 'OK':
            for items in mail:
                for item in items:
                    if type(item) == bytes:
                        if len(item) > 50:
                            mailcontent = MailContent(item)
                            mails.append(mailcontent)
    M.close()
    M.logout()
    return mails
