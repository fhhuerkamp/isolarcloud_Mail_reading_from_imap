import quopri
from email.header import decode_header
import datetime
from dateutil import parser

class MailContent:

    """
    defines a class for a single mail

    """

    def __init__(self,mail=None):
        self.return_path = None
        self.subject = None
        self.m_from = None
        self.m_to = None
        self.m_date = None
        self.m_delivery_date = None
        self.message_id = None
        self.content_type = None
        self.content_transfer_encoding = None
        self.body = None
        content_started = False
        lines = mail.decode("utf-8").split("\r\n")
        # import ipdb; ipdb.set_trace()

        if lines:
            for line in lines:
                if content_started:
                    self.body = self.body + "\r\n" + line
                else:
                    if line.startswith('Return-path:'):
                        self.return_path = line[len('Return-path:'):].strip()
                    if line.startswith('Subject:'):
                        header_subject = decode_header(line[len('Subject:'):].strip())[0]
                        self.subject = header_subject[0].decode(header_subject[1]) if header_subject[1] else header_subject[0]
                    if line.startswith('From:'):
                        # import ipdb; ipdb.set_trace()
                        self.m_from = line[len('From:'):].strip()
                    if line.startswith('To:'):
                        self.m_to = line[len('To:'):].strip()
                    if line.startswith('Date:'):
                        # import ipdb; ipdb.set_trace()
                        self.m_date = parser.parse(line[len('Date:'):].strip())
                    if line.startswith('Delivery-date:'):
                        # import ipdb; ipdb.set_trace()
                        self.m_delivery_date = parser.parse(line[len('Delivery-date:'):].strip())
                    if line.startswith('Message-ID:'):
                        self.message_id = line[len('Message-ID:'):].strip()[1:-1]
                    if line.startswith('Content-Transfer-Encoding:'):
                        self.content_transfer_encoding = line[len('Content-Transfer-Encoding:'):].strip()
                    if line.startswith('Content-Type:'):
                        self.content_type = line[len('Content-Type:'):].strip()
                    if len(line) == 0:
                        content_started = True
                        self.body = ""
            if self.content_transfer_encoding == "quoted-printable":
                self.body = quopri.decodestring(self.body).decode("utf-8")


    def debug_print(self):
        print (f"From: {self.m_from}")
        print (f"To: {self.m_to}")
        print (f"Subject: {self.subject}")
