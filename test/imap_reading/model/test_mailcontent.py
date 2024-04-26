import pytest
from imap_reading.model.MailContent import MailContent
import datetime
import pytz

"""
    test of Class MailContent

"""

def test_sample_mail():
    testmail = b'Return-path: <system@isolarcloud.com>\r\nDelivery-date: Thu, 14 Sep 2023 17:57:50 +0200\r\nReceived: from mi018.mc1.hosteurope.de ([80.237.138.237])\r\n\tby wp077.webpack.hosteurope.de running ExIM with esmtps (TLS1.2:ECDHE_RSA_AES_256_GCM_SHA384:256)\r\n\tid 1qgoj0-00030n-4A; Thu, 14 Sep 2023 17:57:50 +0200\r\nReceived: from out208-78.dm.aliyun.com ([140.205.208.78])\r\n\tby mx0.webpack.hosteurope.de (mi018) with esmtps  (TLSv1.2:ECDHE-RSA-AES256-GCM-SHA384:256)\r\n\t(Exim)\r\n\tid 1qgoix-0005Ee-Do\r\n\tfor fhh@huerkamp.de; Thu, 14 Sep 2023 17:57:50 +0200\r\nX-AliDM-RcptTo: ZmhoQGh1ZXJrYW1wLmRl\r\nFeedback-ID: default:system@isolarcloud.com:trigger:1164\r\nReceived: from chitu-hsf(mailfrom:system@isolarcloud.com fp:ma_600000036032420520)\r\n          by smtp.aliyun-inc.com(127.0.0.1);\r\n          Thu, 14 Sep 2023 23:57:43 +0800\r\nDate: Thu, 14 Sep 2023 23:57:43 +0800\r\nFrom: "iSolarCloud" <system@isolarcloud.com>\r\nTo:  <fhh@huerkamp.de>\r\nMessage-ID: <01cb93e0-7315-46af-8273-0ff7eb7e64fb@alibaba.com>\r\nSubject: =?UTF-8?B?U3RhdGlvbnNiYXUgZXJpbm5lcm4=?=\r\nX-Priority: 3\r\nX-Mailer: Alimail-Mailagent\r\nMIME-Version: 1.0\r\nX-EnvId: 600000036032420521\r\nX-Mailer: Alimail-Mailagent\r\nContent-Type: text/html; charset="UTF-8"\r\nContent-Transfer-Encoding: quoted-printable\r\nX-HE-Spam-Level: +\r\nX-HE-Spam-Score: 1.4\r\nX-HE-Spam-Report: Content analysis details:   (1.4 points)\r\n  pts rule name              description\r\n ---- ---------------------- --------------------------------------------------\r\n  0.0 PDS_OTHER_BAD_TLD      Untrustworthy TLDs\r\n                             [URI: sg8.top (top)]\r\n  0.7 MIME_HTML_ONLY         BODY: Message only has text/html MIME parts\r\n  0.1 HTML_MESSAGE           BODY: HTML included in message\r\n  0.0 MIME_QP_LONG_LINE      RAW: Quoted-printable line longer than 76\r\n                             chars\r\n  0.0 UNPARSEABLE_RELAY      Informational: message has unparseable relay\r\n                             lines\r\n  0.6 HTML_MIME_NO_HTML_TAG  HTML-only message, but there is no HTML\r\n                             tag\r\nX-HE-SPF: PASSED\r\nEnvelope-to: fhh@huerkamp.de\r\n\r\n<div>=0A=0A=0A  <p style=3D"font-size: 24px;color:#000;">Willkommen bei iSolar=\r\nCloud!</p>=0A=0A  <p style=3D"margin-bottom:15px;text-indent: 2em;">F=C3=BCr S=\r\nie wurde eine Anlage registriert. </p>=0A=0A  <p style=3D"text-indent: 2em;">=0A=\r\n=0A   Melden Sie sich bei unserem Service mit Ihrem Konto =0A=0A   <span style=\r\n=3D"font-size:20px;color:#ff7300;">fhh@huerkamp.de</span>=0A=0A   und Passwort=\r\n an=0A=0A   <span style=3D"font-size:20px;color:#ff7300;">7un3yu95</span>.=0A=0A=\r\n    Nach der ersten Anmeldung =C3=A4ndern Sie bitte sofort Ihr Passwort.=0A=0A=\r\n  </p>=0A=0A  <p style=3D"margin-bottom:15px;text-indent: 2em;">=0A=0A   iSola=\r\nrCloud ist f=C3=BCr Ihre Mobilger=C3=A4te verf=C3=BCgbar=0A=0A   <a href=3D"ht=\r\ntp://sg8.top/c">http://sg8.top/c</a>=0A=0A  </p>=0A=0A  <p style=3D"margin-bot=\r\ntom:15px;text-indent: 2em;">=0A=0A      Dies ist eine automatisch erstellte Na=\r\nchricht. =0A=0A  </p>=0A=0A  =0A=0A </div>\r\n\r\n'
    mailcontent = MailContent(testmail)
    print (f"Subject: {mailcontent.subject}, Delivery_date: {mailcontent.m_delivery_date}")
    assert mailcontent.m_to == "<fhh@huerkamp.de>"
    assert mailcontent.m_delivery_date == datetime.datetime(2023, 9, 14, 15, 57, 50, tzinfo=pytz.utc)
    assert mailcontent.m_date == datetime.datetime(2023, 9, 14, 15, 57, 43, tzinfo=pytz.utc)
    return