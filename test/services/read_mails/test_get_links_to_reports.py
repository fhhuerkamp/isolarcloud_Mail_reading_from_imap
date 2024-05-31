import pytest
from imap_reading.services.read_mails.get_links_to_reports import get_links_to_report

"""
    test of Class MailContent

"""


testmailbody = """

Sehr geehrte/r Benutzer/in huerkamp@huerkamp.de, <br/> <br/>

der von Benutzer/die Benutzerin [efbwkqspik] konfigurierte Tagesbericht wurde erstellt. Sie können den folgenden Link in den Browser kopieren oder auf den Link klicken, um den Bericht anzuzeigen. <br/> <br/>

<a href="https://portal.isolarcloud.com/#/reportOutlink?target=service=getPsReport%26lang=_de_DE%26param=ThEePJsgkvXPWPCpdXwHpcx21P2M2VeHJYc7FZnW14jKEOQ8tbC3Tm8SDwj61oyloKlYKchtZL-v-ZswpEVOX22VHWCSl_40gAs1fELZ3IZKvdR1PWoXqBmNp4mpw2GJ31iL9S5H-iNl0oOdtfkvRh-1aZs8HyFGu5WGnZCI3zQ">https://portal.isolarcloud.com/#/reportOutlink?target=service=getPsReport%26lang=_de_DE%26param=ThEePJsgkvXPWPCpdXwHpcx21P2M2VeHJYc7FZnW14jKEOQ8tbC3Tm8SDwj61oyloKlYKchtZL-v-ZswpEVOX22VHWCSl_40gAs1fELZ3IZKvdR1PWoXqBmNp4mpw2GJ31iL9S5H-iNl0oOdtfkvRh-1aZs8HyFGu5WGnZCI3zQ</a> <br/> <br/>

Bitte antworten Sie nicht auf diese System-E-Mail. Wenn Sie Fragen haben, senden Sie bitte eine E-Mail an feedback@sungrowpower.com.<br/> <br/>

iSolarCloud<br/> <br/>

Wenn Sie E-Mails wie diese nicht mehr erhalten möchten, klicken Sie bitte auf <a href="https://portal.isolarcloud.com/#/reportOutlink?target=service=cancelDeliverMail%26lang=_de_DE%26cloud_id=3%26param=YXvd-QBYxlJCjFExg-nCtVsfsE0iBcPT7XpfW7mACp8CChr9bIdP8RltDYovrS_ycHQtPeNGTnn_ixqZuV2za355-mQ_D2OsInySvWl7bdhOzkLAfrBbGfhgtEl2H84vHPC_wpfX1Kaw9DlZpkrLVyFV_Irul1Gmd0FySNNIxVs"><strong>ablehnen</strong></a>.

"""

def test_get_links_to_report():
    links = get_links_to_report(testmailbody)
    # import ipdb; ipdb.set_trace()
    assert len(links) == 1
    assert "portal.isolarcloud.com" in links[0]
    return
