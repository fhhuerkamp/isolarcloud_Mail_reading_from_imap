from imap_reading.services.read_mails.read_mails import read_mails_from_mailserver
from imap_reading.helper.get_env import get_env
from imap_reading.services.read_mails.read_mails import read_mails_from_mailserver, read_mails_from_file
from datetime import date, timedelta


def test_read_mails():
    host=get_env("TEST_IMAPHOST")
    user=get_env("TEST_IMAPUSER")
    password=get_env("TEST_IMAPPASSWORD")
    sender=get_env("TEST_SENDER")
    mails = read_mails_from_mailserver(host, user, password, sender)
    assert len(mails) > 0
    for mail in mails:
        assert sender in mail.m_from

def test_read_mails_with_daybacks():
    host=get_env("TEST_IMAPHOST")
    user=get_env("TEST_IMAPUSER")
    password=get_env("TEST_IMAPPASSWORD")
    sender=get_env("TEST_SENDER")
    daysback = 2
    mails = read_mails_from_mailserver(host, user, password, sender, daysback=daysback)
    date_check = date.today() - timedelta(days=daysback)

    assert len(mails) > 0
    for mail in mails:
        # import ipdb; ipdb.set_trace()
        assert sender in mail.m_from
        assert date_check <= mail.m_date.date()


def test_read_mails_from_file():
    mail_in_file=get_env("TEST_RAW_MAIL_IN_FILE")
    sender=get_env("TEST_SENDER")

    mailcontent = read_mails_from_file(mail_file=mail_in_file)
    # import ipdb; ipdb.set_trace()
    assert sender in mailcontent.m_from
