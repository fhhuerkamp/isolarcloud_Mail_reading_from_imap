from imap_reading.helper.read_mails import read_mails
import os
from dotenv import load_dotenv
from imap_reading.helper.read_mails import read_mails
from datetime import date,timedelta


def test_read_mails():
    load_dotenv(override=False)
    host=os.environ.get("TEST_IMAPHOST")
    user=os.environ.get("TEST_IMAPUSER")
    password=os.environ.get("TEST_IMAPPASSWORD")
    sender=os.environ.get("TEST_SENDER")
    mails = read_mails(host, user, password, sender)
    assert len(mails) > 0
    for mail in mails:
        assert sender in mail.m_from

def test_read_mails_with_daybacks():
    load_dotenv(override=False)
    host=os.environ.get("TEST_IMAPHOST")
    user=os.environ.get("TEST_IMAPUSER")
    password=os.environ.get("TEST_IMAPPASSWORD")
    sender=os.environ.get("TEST_SENDER")
    daysback = 2
    mails = read_mails(host, user, password, sender, daysback=daysback)
    date_check = date.today() - timedelta(days=daysback)

    assert len(mails) > 0
    for mail in mails:
        # import ipdb; ipdb.set_trace()
        assert sender in mail.m_from
        assert date_check <= mail.m_date.date()
