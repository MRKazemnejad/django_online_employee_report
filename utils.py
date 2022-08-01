from kavenegar import *


def otp_code_send(phone,code):

    try:
        api = KavenegarAPI('574F5666776C4269576F6A316B306C352B4E64577A706A657171757452526F78554855676735693952594D3D')
        params = {
            'sender': '100047778',  # optional
            'receptor': '09101938600',  # multiple mobile number, split by comma
            'message': f'{code}کد تایید شما : ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
