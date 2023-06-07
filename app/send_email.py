import smtplib
import ssl
from email.message import EmailMessage
from email.headerregistry import Address
# Define email sender and receiver
email_sender = 'donotreply.quickrecipe@gmail.com'
email_password = 'umkqoylygzlpurgo'
email_receiver = 'doumbiasoft@gmail.com'
sender_name='Quick Recipe'

# Set the subject and body of the email
subject = 'Send mail test'
body = """
 <table cellpadding="0" cellspacing="0" border="0"
        style="border-collapse:collapse;width:100%;background-color:#ffffff" width="100%" bgcolor="#ffffff">
        <tbody>
            <tr>
                <td style="font-size:0">&nbsp;</td>
                <td align="center" valign="top" style="padding-bottom:0px;width:600px;background-color:#ffffff"
                    width="600" bgcolor="#ffffff">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse">
                        <tbody>
                            <tr>
                                <td align="center" style="padding:0;font-size:0;line-height:0">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%"
                                        style="border-collapse:collapse;width:100%;max-width:600px;background-color:#ffffff"
                                        bgcolor="#ffffff">
                                        <tbody>
                                            <tr>
                                                <td  align="center"
                                                    style="padding:0;font-size:0;line-height:0;border:1px solid #d8d9da">
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%"
                                                        bgcolor="#ffffff"
                                                        style="background-color:#ffffff;background:#ffffff">
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding:24px 0" align="center">
                                                                    <a href="#">
                                                                        <img style="width:200px"
                                                                            src="http://192.168.0.116:5000/static/images/quick-recipe-logo.png"
                                                                            alt="Quick Recipe" width="160" border="0"
                                                                            >
                                                                    </a>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%"
                                                        bgcolor="#ffffff" style="border-collapse:collapse">
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding:0;font-size:0;line-height:0"
                                                                    align="center">
                                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                                        width="90%" style="border-collapse:collapse">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td style="padding:8px 0 0;font-size:0;line-height:0"
                                                                                    align="left">

                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%"
                                                        bgcolor="#ffffff" style="border-collapse:collapse">

                                                        <tbody>
                                                            <tr>
                                                                <td style="padding:0;font-size:0;line-height:0"
                                                                    align="center">
                                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                                        width="100%" style="border-collapse:collapse">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td style="padding:32px 0 8px;font-size:0;line-height:0"
                                                                                    align="center"
                                                                                    >
                                                                                    <img style="border:0;height:auto;outline:none;text-decoration:none;width:225px"
                                                                                    src="http://192.168.0.116:5000/static/images/activation.svg"
                                                                                    alt="Quick Recipe" width="225"
                                                                                    border="0"
                                                                                    >
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%"
                                                        bgcolor="#ffffff" style="border-collapse:collapse">
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding:32px 0;font-size:0;line-height:0"
                                                                    align="center">
                                                                    <table width="87%" border="0" cellspacing="0"
                                                                        cellpadding="0" 
                                                                        style="border-collapse:collapse">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td align="center" valign="top"
                                                                                    style="padding:0;font-size:0;line-height:0">
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0"
                                                                                        style="border-collapse:collapse">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td style="padding:0;font-family:Georgia,Times New Roman,serif;font-size:30px;line-height:52px;color:#000000;font-weight:normal;letter-spacing:0.25px;text-align:center"
                                                                                                    
                                                                                                    align="center">
                                                                                                    <span style="color:#000000;text-decoration:none">
                                                                                                
                                                                                                        Hi, Mouhamed
                                                                                                 </span>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                            <tr>
                                                                                <td align="center" valign="top"
                                                                                    style="padding:0;font-size:0;line-height:0">
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0"
                                                                                        style="border-collapse:collapse">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td style="padding:16px 0 0;font-family:Helvetica,Arial,sans-serif;font-size:18px;line-height:27px;color:#3d4045;font-weight:normal;letter-spacing:0.5px;text-align:center"
                                                                                                    align="center">
                                                                                                    To activate and get access to all feautures in Quick Recipe click on the button bellow.
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                            <tr>
                                                                                <td
                                                                                    style="padding:0;font-size:0px;line-height:0">
                                                                                    <table border="0" cellpadding="0"
                                                                                        cellspacing="0" width="100%"
                                                                                        style="border-collapse:collapse">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td align="center"
                                                                                                    style="padding:32px 0 0;font-size:0;line-height:0">
                                                                                                    <table width="100%"
                                                                                                        border="0"
                                                                                                        cellpadding="0"
                                                                                                        cellspacing="0"
                                                                                                        style="border-collapse:collapse">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center"
                                                                                                                    style="text-align:center">
                                                                                                                    <div>
                                                                                                                        <a style="background-color:#e59038;border-radius:2px;color:#ffffff;display:inline-block;font-family:Helvetica,Arial,sans-serif;font-size:14px;font-weight:700;line-height:45px;text-align:center;text-decoration:none;width:250px;text-transform:uppercase;letter-spacing:0.05em"
                                                                                                                            href="#"
                                                                                                                            target="_blank">ACTIVATE</a>
                                                                                                                    </div>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" width="100%"
                                                        bgcolor="#ffffff" style="border-collapse:collapse">
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding:16px 0;font-size:0;line-height:0"
                                                                    align="center">
                                                                    <table width="87%" border="0" cellspacing="0"
                                                                        cellpadding="0" class="m_7157640124949244281w91"
                                                                        style="border-collapse:collapse">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td align="center" valign="top"
                                                                                    style="padding:0;font-size:0;line-height:0">
                                                                                    <table width="100%" border="0"
                                                                                        cellspacing="0" cellpadding="0"
                                                                                        style="border-collapse:collapse">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td style="padding:0;font-family:Helvetica,Arial,sans-serif;font-size:14px;line-height:21px;color:#64666a;font-weight:normal;letter-spacing:0.5px;text-align:center"
                                                                                                    align="center">
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table align="center" cellpadding="0" cellspacing="0" border="0"
                                                        style="border-collapse:collapse;width:100%" bgcolor="#ffffff"
                                                        width="100%">
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding-top:16px"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table align="center" cellpadding="0" cellspacing="0" border="0"
                                                        style="border-collapse:collapse;width:100%" bgcolor="#ffffff"
                                                        width="100%">
                                                        <tbody>
                                                            <tr>
                                                                <td style="padding-top:16px"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" border="0" align="center"
                                                        width="100%" bgcolor="#ffffff"
                                                        style="border-collapse:collapse;padding:0px;margin:0px">
                                                        <tbody>
                                                            <tr>
                                                                <td align="center" valign="top"
                                                                    style="padding:0;font-size:0;line-height:0">
                                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                                        width="100%" bgcolor="#F5F5F5">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td style="padding:32px 0;font-size:0;line-height:0"
                                                                                    align="center">
                                                                                    <table border="0" cellpadding="0"
                                                                                        cellspacing="0" width="100%"
                                                                                        bgcolor="#F5F5F5">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td style="padding:0;font-size:0;line-height:0"
                                                                                                    align="center">
                                                                                                    <table width="87%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0"
                                                                                                        >
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center"
                                                                                                                    valign="top"
                                                                                                                    style="padding:0;font-size:1px;line-height:1px;vertical-align:top;border-top:1px solid #b1b3b5;width:100%;max-width:520px"
                                                                                                                    width="520">
                                                                                                                    &nbsp;
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" cellpadding="0"
                                                                                        cellspacing="0" width="100%"
                                                                                        bgcolor="#F5F5F5">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td style="padding:32px 0;font-size:0;line-height:0"
                                                                                                    align="center">
                                                                                                    <table width="140"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0">
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td style="vertical-align:top;padding:0 4px"
                                                                                                                    valign="top">
                                                                                                                    <a href="#"
                                                                                                                        title="LinkedIn"
                                                                                                                        target="_blank">

                                                                                                                        <img 
                                                                                                                            height="32"
                                                                                                                            src="http://192.168.0.116:5000/static/images/linkedin.png"
                                                                                                                            alt="LinkedIn"
                                                                                                                            title="LinkedIn"
                                                                                                                            style="border:none;display:block"
                                                                                                                            >
                                                                                                                    </a>
                                                                                                                </td>
                                                                                                                <td style="vertical-align:top;padding:0 4px"
                                                                                                                    valign="top">
                                                                                                                    <a href="#"
                                                                                                                        title="GitHub"
                                                                                                                        target="_blank">

                                                                                                                        <img 
                                                                                                                            height="32"
                                                                                                                            src="http://192.168.0.116:5000/static/images/github.png"
                                                                                                                            alt="GitHub"
                                                                                                                            title="GitHub"
                                                                                                                            style="border:none;display:block"
                                                                                                                            >
                                                                                                                    </a>
                                                                                                                </td>
                                                                                                        
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                    <table border="0" cellpadding="0"
                                                                                        cellspacing="0" width="100%"
                                                                                        bgcolor="#F5F5F5">
                                                                                        <tbody>
                                                                                            <tr>
                                                                                                <td style="padding:0;font-size:0;line-height:0"
                                                                                                    align="center">
                                                                                                    <table width="87%"
                                                                                                        border="0"
                                                                                                        cellspacing="0"
                                                                                                        cellpadding="0"
                                                                                                        >
                                                                                                        <tbody>
                                                                                                            <tr>
                                                                                                                <td align="center"
                                                                                                                    style="padding:0px 10px 0px;margin:0px;font-family:Helvetica,sans-serif;font-size:12px;line-height:18px;color:#64666a;font-weight:normal;letter-spacing:normal">
                                                                                                                    You got this  message because you signed up to 
                                                                                                                    <span
                                                                                                                        class="il">Quick Recipe</span>
                                                                                                                            <br><br>
                                                                                                                            <span class="il">Quick Recipe</span><sup>™</sup>
                                                                                                                </td>
                                                                                                            </tr>
                                                                                                        </tbody>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </tbody>
                                                                                    </table>
                                                                                </td>
                                                                            </tr>
                                                                        </tbody>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td style="font-size:0">&nbsp;</td>
            </tr>
        </tbody>
    </table>
"""

em = EmailMessage()
em['From'] =Address(display_name=sender_name, addr_spec= email_sender) 
em['To'] = email_receiver
em['Subject'] = subject
em.set_type('text/html')
em.add_alternative(body, subtype="html")
#em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()


# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())