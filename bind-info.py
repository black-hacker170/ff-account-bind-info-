import requests
from os import system
import sys
import time

def convert(s):
    try:
        s = int(s)
        d, h = divmod(s, 86400)
        h, m = divmod(h, 3600)
        m, s = divmod(m, 60)
        return f"{d} Day {h} Hour {m} Min {s} Sec"
    except:
        return "0 Day 0 Hour 0 Min 0 Sec"

# অক্ষরর টইপ অ্যনমশনর জন্য ফশন
def animate_print(text, speed=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def is_success(rsp):
    """Check if the API response is truly successful without any nested errors"""
    if rsp.status_code != 200: 
        return False
    try:
        rj = rsp.json()
        if not rj.get("success"): 
            return False
            
        data = rj.get("data", {})
        if isinstance(data, dict):
            if data.get("error"): 
                return False
            g_resp = data.get("garena_response", {})
            if isinstance(g_resp, dict) and g_resp.get("error"):
                return False
                
        err_node = rj.get("error")
        if err_node: 
            return False
            
        return True
    except:
        return False

def show_res(rsp_json):
    """Formats the JSON to show only the pure error/success and globally fetched Credit"""
    try:
        error_msg = None
        err_node = rsp_json.get('error')
        data_node = rsp_json.get('data', {})

        # 1. Check if error is inside the 'error' dictionary
        if isinstance(err_node, dict):
            g_resp = err_node.get('garena_response', {})
            if isinstance(g_resp, dict) and g_resp.get('error'):
                error_msg = g_resp.get('error')
            elif err_node.get('error'):
                error_msg = err_node.get('error')
            elif err_node.get('message'):
                error_msg = err_node.get('message')
            else:
                error_msg = str(err_node)
        # 2. Check if error is a direct string
        elif isinstance(err_node, str):
            error_msg = err_node
            
        # 3. Check inside 'data' node if error still not found
        if not error_msg and isinstance(data_node, dict):
            if data_node.get('error'):
                error_msg = data_node.get('error')
            elif isinstance(data_node.get('garena_response'), dict) and data_node['garena_response'].get('error'):
                error_msg = data_node['garena_response']['error']
                
        # 4. Fallback (Direct Garena Response Error Check)
        if not error_msg:
            g_resp = rsp_json.get('garena_response', {})
            if isinstance(g_resp, dict) and g_resp.get('error'):
                error_msg = g_resp.get('error')

        # 5. Fallback Default
        if not error_msg and not rsp_json.get('success'):
            error_msg = rsp_json.get('message') or "Unknown Error"

        if error_msg:
            animate_print(f"- FaiLEd ! Error : {error_msg}")
        else:
            animate_print("- SuccEss !")
            
        # Displaying globally fetched API Credits
        animate_print(f"- DevELopEr : {GLOBAL_MAKER}")
        animate_print(f"- TeleGraM  : {GLOBAL_CHANNEL}\n")
    except:
        animate_print("- FaiLEd ! InvaLid ResPonsE\n")


GLOBAL_MAKER = "black"
GLOBAL_CHANNEL = "https://t.me/sakibblack" # পর্সনল টলগ্রম আইড লক সট কর হয়ছ

def fetch_api_credits():
    global GLOBAL_MAKER, GLOBAL_CHANNEL
    try:
        url = "https://chngeforgotcrownx72.vercel.app/otp"
        rsp = requests.get(url)
        data = rsp.json()
        
        credit = data.get("credit", {})
        if credit:
            GLOBAL_MAKER = "black"
            GLOBAL_CHANNEL = "https://t.me/sakibblack"
    except:
        pass 

# সুন্দর কলর কম্বনশন সহ ব্যনর ডসপ্ল ফশন
def display_banner(with_animation=False):
    G = '\033[92m'  # Neon Green
    R = '\033[91m'  # Blood Red
    W = '\033[97m'  # White
    C = '\033[96m'  # Cyan / Light Blue
    Y = '\033[93m'  # Yellow
    X = '\033[0m'   # Reset

    lines = [
        f"{G}==========================================================================",
        f"{C} _____   _          _       ____   _  __",
        f"{C}| __ )  | |        / \\     / ___| | |/ /",
        f"{G}|  _ \\  | |       / _ \\   | |     | ' / ",
        f"{G}| |_) | | |___   / ___ \\  | |___  | . \\ ",
        f"{C}|____/  |_____| /_/   \\_\\  \\____| |_|\\_\\  {R}[ WARNING: UNLEASHED ]",
        f"{G}==========================================================================",
        f"          {R}[ {W}DEVELOPER: {Y}{GLOBAL_MAKER} {R}| {W}TELEGRAM CONTACT: {C}{GLOBAL_CHANNEL} {R}]{G}",
        f"=========================================================================={X}"
    ]

    if with_animation:
        for line in lines:
            animate_print(line, speed=0.002)
    else:
        for line in lines:
            print(line)

def ChanGE_BinD_WiTh_Sec(access):
    email = input('\033[92m- EnTer NEw EmaiL : \033[0m')
    url = "https://chngemailcode48.vercel.app/send_otp"
    rsp = requests.get(url, params={'access_token': access, 'email': email})
    
    if is_success(rsp):
        show_res(rsp.json())
        otp = input('\033[92m- OtP => \033[0m')
        url_v = "https://chngemailcode48.vercel.app/verify_otp"
        rsp_v = requests.get(url_v, params={'access_token': access, 'email': email, 'otp': otp})
        
        if is_success(rsp_v):
            show_res(rsp_v.json())
            auth = rsp_v.json().get("verifier_token") or rsp_v.json().get("data", {}).get("verifier_token")

            sec = input('\033[92m- EnTer SecuriTy CodE : \033[0m')
            url_i = "https://chngemailcode48.vercel.app/verify_identity"
            rsp_i = requests.get(url_i, params={'access_token': access, 'code': sec})
            
            if is_success(rsp_i):
                show_res(rsp_i.json())
                iden = rsp_i.json().get("identity_token") or rsp_i.json().get("data", {}).get("identity_token")
                url_c = "https://chngemailcode48.vercel.app/create_rebind"
                rsp_c = requests.get(url_c, params={'access_token': access, 'email': email, 'identity_token': iden, 'verifier_token': auth})
                
                if is_success(rsp_c):
                    show_res(rsp_c.json())
                    animate_print(f'\033[92m- SuccesFuLy ChanGEd To : {email} !\033[0m')
                else:
                    show_res(rsp_c.json())
            else:
                show_res(rsp_i.json())
        else:
            show_res(rsp_v.json())
    else:
        try: show_res(rsp.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp.status_code}')

def ChanGE_BinD_No_Sec(access):
    cur_email = input('\033[92m- EnTer CurrenT EmaiL : \033[0m')
    url1 = "https://chngeforgotcrownx72.vercel.app/otp"
    rsp1 = requests.get(url1, params={'access_token': access, 'current_email': cur_email})
    
    if is_success(rsp1):
        show_res(rsp1.json())
        otp1 = input('\033[92m- OtP => \033[0m')
        url2 = "https://chngeforgotcrownx72.vercel.app/verify"
        rsp2 = requests.get(url2, params={'access_token': access, 'current_email': cur_email, 'otp': otp1})
        
        if is_success(rsp2):
            show_res(rsp2.json())
            iden = rsp2.json().get("identity_token") or rsp2.json().get("data", {}).get("identity_token")
            new_email = input('\033[92m- EnTer NEw EmaiL : \033[0m')
            url3 = "https://chngeforgotcrownx72.vercel.app/newotp"
            rsp3 = requests.get(url3, params={'access_token': access, 'new_email': new_email})
            
            if is_success(rsp3):
                show_res(rsp3.json())
                otp2 = input('\033[92m- OtP => \033[0m')
                url4 = "https://chngeforgotcrownx72.vercel.app/newverify"
                rsp4 = requests.get(url4, params={'access_token': access, 'new_email': new_email, 'otp': otp2})
                
                if is_success(rsp4):
                    show_res(rsp4.json())
                    auth = rsp4.json().get("verifier_token") or rsp4.json().get("data", {}).get("verifier_token")
                    url5 = "https://chngeforgotcrownx72.vercel.app/change"
                    rsp5 = requests.get(url5, params={'access_token': access, 'new_email': new_email, 'identity_token': iden, 'verifier_token': auth})
                    
                    if is_success(rsp5):
                        show_res(rsp5.json())
                        animate_print('\033[92m- SuccesFuLy ForGoT SecuriTy CodE !\033[0m')
                    else:
                        show_res(rsp5.json())
                else:
                    show_res(rsp4.json())
            else:
                show_res(rsp3.json())
        else:
            show_res(rsp2.json())
    else:
        try: show_res(rsp1.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp1.status_code}')

def Bind_Change_Flow(access):
    animate_print("\n\033[96m- Do you havE your currenT SecuriTy CodE ?\033[0m")
    animate_print("\033[96m- EnTer 'y' for YEs (ChanGE wiTh SecuriTy CodE)\033[0m")
    animate_print("\033[96m- EnTer 'n' for No  (ForGeT / REsET SecuriTy CodE)\033[0m")
    ch = input('\n\033[92m- ChoosE (y/n) : \033[0m').strip().lower()
    
    if ch == 'y':
        print()
        ChanGE_BinD_WiTh_Sec(access)
    elif ch == 'n':
        print()
        ChanGE_BinD_No_Sec(access)
    else:
        animate_print('\033[91m- InvaLid ChoicE !\033[0m')

def UnBinD_WiTh_Sec(access):
    sec = input('\033[92m- EnTer SecuriTy CodE : \033[0m')
    url = "https://crownxnewkey10010.vercel.app/securityunbind"
    rsp = requests.get(url, params={'access_token': access, 'security_code': sec})
    
    if is_success(rsp):
        show_res(rsp.json())
        animate_print('\033[92m- UnBinD REquEsT CrEaTEd SuccesFuLy! 15 Days Timer STrarTEd.\033[0m')
    else:
        try: show_res(rsp.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp.status_code}')

def UnBinD_No_Sec(access):
    cur_email = input('\033[92m- EnTer CurrenT EmaiL : \033[0m')
    url1 = "https://chngeforgotcrownx72.vercel.app/otp"
    rsp1 = requests.get(url1, params={'access_token': access, 'current_email': cur_email})
    
    if is_success(rsp1):
        show_res(rsp1.json())
        otp = input('\033[92m- OtP => \033[0m')
        url2 = "https://chngeforgotcrownx72.vercel.app/verify"
        rsp2 = requests.get(url2, params={'access_token': access, 'current_email': cur_email, 'otp': otp})
        
        if is_success(rsp2):
            show_res(rsp2.json())
            iden = rsp2.json().get("identity_token") or rsp2.json().get("data", {}).get("identity_token")
            
            url3 = "https://crownxforgotremove23.vercel.app/forgotunbind"
            rsp3 = requests.get(url3, params={'access_token': access, 'identity_token': iden})
            
            if is_success(rsp3):
                show_res(rsp3.json())
                animate_print('\033[92m- UnBinD REquEsT CrEaTEd SuccesFuLy! 15 Days Timer STrarTEd.\033[0m')
            else:
                show_res(rsp3.json())
        else:
            show_res(rsp2.json())
    else:
        try: show_res(rsp1.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp1.status_code}')

def Unbind_Flow(access):
    animate_print("\n\033[96m- Do you havE your currenT SecuriTy CodE ?\033[0m")
    animate_print("\033[96m- EnTer 'y' for YEs (UnBinD wiTh SecuriTy CodE)\033[0m")
    animate_print("\033[96m- EnTer 'n' for No  (ForGoT SecuriTy CodE / OTP)\033[0m")
    ch = input('\n\033[92m- ChoosE (y/n) : \033[0m').strip().lower()
    
    if ch == 'y':
        print()
        UnBinD_WiTh_Sec(access)
    elif ch == 'n':
        print()
        UnBinD_No_Sec(access)
    else:
        animate_print('\033[91m- InvaLid ChoicE !\033[0m')

def ChK(access):
    url = "https://bindinfocrownx612.vercel.app/check"
    rsp = requests.get(url, params={'access_token': access})
    if is_success(rsp):
        data = rsp.json()
        inner_data = data.get("data", {}) if data.get("data") else data
        
        print("")
        animate_print(f"- sTaTus : {inner_data.get('status', '')}")
        animate_print(f"- sTaTus_codE : {inner_data.get('status_code', '')}")
        animate_print(f"- summary : {inner_data.get('summary', '')}")
        animate_print(f"- counTdown_human : {inner_data.get('countdown_human', '')}")
        animate_print(f"- counTdown_sEconds : {inner_data.get('countdown_seconds', '')}")
        animate_print(f"- currenT_EmaiL : {inner_data.get('current_email', '')}")
        animate_print(f"- pEndinG_EmaiL : {inner_data.get('pending_email', '')}")
        animate_print(f"- EmaiL_To_bE : {inner_data.get('email_to_be', '')}")
        animate_print(f"- mobiLE : {inner_data.get('mobile', '')}")
        animate_print(f"- rEquEsT_ExEc_counTdown : {inner_data.get('request_exec_countdown', '')}")
        animate_print(f"- rEsuLT : {inner_data.get('result', '')}")
        animate_print(f"- EmaiL : {inner_data.get('email', '')}")
        animate_print(f"- mobiLE_To_bE : {inner_data.get('mobile_to_be', '')}")
        
        email = inner_data.get("email", "")
        email_to_be = inner_data.get("email_to_be", "")
        countdown = inner_data.get("request_exec_countdown", 0)
        
        print("")
        if email == "" and email_to_be != "":
            animate_print(f"- ConFirmEd in : {convert(countdown)}")
        elif email != "" and email_to_be == "":
            animate_print(f"- ConFirmEd : YEs Good !")
        elif email == "" and email_to_be == "":
            animate_print(f"- No IsTi3ada !")
            
        print("")
        animate_print(f"- DevELopEr : {GLOBAL_MAKER}")
        animate_print(f"- TeleGraM  : {GLOBAL_CHANNEL}")
    else:
        try: show_res(rsp.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp.status_code}')

def CancEL(access):
    url = "https://bindcnclcrownx34.vercel.app/cancelbind"
    rsp = requests.get(url, params={'access_token': access})
    if is_success(rsp):
        show_res(rsp.json())
        animate_print('\033[92m- SuccesFuLy CanceLEd BinD !\033[0m')
    else:
        try: show_res(rsp.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp.status_code}')

def BinD_NEw(email, access):
    url = "https://bindcnclcrownx34.vercel.app/bind"
    rsp = requests.get(url, params={'access_token': access, 'email': email})
    if is_success(rsp):
        show_res(rsp.json())
        otp = input('\033[92m- OtP => \033[0m')
        sec = input('\033[92m- EnTer SecuriTy CodE : \033[0m')
        url_c = "https://bindcnclcrownx34.vercel.app/confirmbind"
        rsp_c = requests.get(url_c, params={'access_token': access, 'email': email, 'otp': otp, 'security_code': sec})
        if is_success(rsp_c):
            show_res(rsp_c.json())
            animate_print(f'\033[92m- SuccesFuLy AddinG : {email} To AccounT !\033[0m')
        else:
            show_res(rsp_c.json())
    else:
        try: show_res(rsp.json())
        except: animate_print(f'- FaiLEd ! HTTP : {rsp.status_code}')

def GeT_PLaFTroms(t):
    r = requests.get("https://100067.connect.garena.com/bind/app/platform/info/get",
      params={'access_token': t},
      headers={'User-Agent':"GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)","Connection":"Keep-Alive","Accept-Encoding":"gzip","If-Modified-Since":"Sun, 18 May 2025 09:37:03 GMT"})
    if r.status_code not in[200,201]: 
        return animate_print("Failed to fetch.")
    j = r.json()
    m = {3:"Facebook", 8:"Gmail", 10:"iCloud", 5:"VK", 11:"Twitter", 7:"Huawei"}
    b, a = j.get("bounded_accounts",[]), j.get("available_platforms",[])
    animate_print("\033[97m> SEcondary LinKs : <\033[0m")
    l = False
    for x in b:
        try:
            p = x.get('platform')
            u = x.get('uid')
            uinfo = x.get('user_info', {})
            e = uinfo.get('email', '')
            n = uinfo.get('nickname', '')
            if p in m:
                animate_print(f"\n\033[92m=> {m[p]} !\033[0m")
                if e: animate_print(f"- Email : {e}")
                if n: animate_print(f"- Email NamE : {n}")
                print()
                l = True
        except: 
            continue
    if not l: 
        animate_print("\033[93m=> Secondary Links Not Found ! \033[0m")
        
    for k in m:
        if k not in a:
            animate_print(f"\n\033[96m> Main Platform => {m[k]} ! <\033[0m")
            break

def Revoke_Token(access):
    url = "https://crownxrevoker73.vercel.app/revoke"
    rsp = requests.get(url, params={'access_token': access})
    try:
        rj = rsp.json()
        
        if rj.get("success"):
            animate_print("\033[92m- SuccEsFuLy RevoKEd AccEss ToKeN !\033[0m")
        else:
            err = rj.get("error", {}).get("garena_response", {}).get("error", "Unknown")
            animate_print(f"\033[91m- FaiLEd To RevoKe ! Error : {err}\033[0m")
            
        animate_print(f"- DevELopEr : {GLOBAL_MAKER}")
        animate_print(f"- TeleGraM  : {GLOBAL_CHANNEL}\n")
    except:
        animate_print(f"\033[91m- FaiLEd ! HTTP : {rsp.status_code}\n\033[0m")

def MenU():
    fetch_api_credits()
    
    first_run = True
    
    while True:
        system('clear')
        
        G = '\033[92m'  # Neon Green
        R = '\033[91m'  # Blood Red
        W = '\033[97m'  # White
        Y = '\033[93m'  # Yellow
        X = '\033[0m'   # Reset
        
        if first_run:
            display_banner(with_animation=True)
            first_run = False
        else:
            display_banner(with_animation=False)
        
        # অপশন লস্ট
        print(f" {G}[1]{X} - Bind ChangE")
        print(f" {G}[2]{X} - UnBinD EmaiL")
        print(f" {G}[3]{X} - ChEcK BinD InFo")
        print(f" {G}[4]{X} - CanCeL MaiL BinD")
        print(f" {G}[5]{X} - BinD NEw EmaiL")
        print(f" {G}[6]{X} - ChEcK LinKs")
        print(f" {G}[7]{X} - RevoKe AccEss ToKeN")
        print(f" {R}[0]{X} - ExiT")
        print(f"{G}=========================================================================={X}")
        
        sH = input(f'\n{G}ChoosE : {X}').strip()
        
        if sH in ['1', '2', '3', '4', '6', '7']:
            system('clear')
            display_banner(with_animation=True)
            token = input(f'{G}- EnTer AccEss ToKeN : {X}')
            
            if sH == '1':
                Bind_Change_Flow(token)
            elif sH == '2':
                Unbind_Flow(token)
            elif sH == '3':
                ChK(token)
            elif sH == '4':
                CancEL(token)
            elif sH == '6':
                GeT_PLaFTroms(token)
            elif sH == '7':
                Revoke_Token(token)
                
        elif sH == '5':
            system('clear')
            display_banner(with_animation=True)
            new_mail = input(f'{G}- EnTer NeW EmaiL : {X}')
            token = input(f'{G}- EnTer AccEss ToKeN : {X}')
            BinD_NEw(new_mail, token)
            
        elif sH == '0':
            system('clear')
            exit(f'{R}- ExiTing !{X}')
        else:
            animate_print(f'{R}- No ChoosinG !{X}')
            
        input(f'\n{Y}- PrEss EnTer To REturn To Main MEnu...{X}')

if __name__ == "__main__":
    MenU()
