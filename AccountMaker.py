a
    �N�`�  �                   @   s  d dl Z d dlZe�d�Ze�d�Zeej� ed�Zeejv rBne	�  ed�Z
e
dkr�e �d� e �d� e �d	� e �d
� e �e jdkr�dnd� ne �e jdkr�dnd� d dlZd dlZd dlZd dlmZ d dlmZ dZee� ed� dd� Ze�  dS )�    Nz!https://pastebin.com/raw/R6Cvh21Yz!https://pastebin.com/raw/XhuMr4EXz
[+]Pasword Bnwsa : z:
[1] Download lib & update
[2] pass

[+] Please Choice >> �1zpip install requestszpip install user_agentzpkg install requestszpkg install user_agent�nt�cls�clear)�sleep)�generate_user_agenta
  
       _                             __  __       _             
      | |                           |  \/  |     | |            
      | | _____   _____  _ __ ___   | \  / | __ _| | _____ _ __ 
  _   | |/ _ \ \ / / _ \| '_ ` _ \  | |\/| |/ _` | |/ / _ \ '__|
 | |__| |  __/\ V / (_) | | | | | | | |  | | (_| |   <  __/ |   
  \____/ \___| \_/ \___/|_| |_| |_| |_|  |_|\__,_|_|\_\___|_| IG  
                                                                                                                                
z$====================================c                  C   sN  d} t �� }t�d�d }d}td�}|dkr>td� t�  nd}td	�}|dkrbtd
� t�  n d}d}tdd�D ]}	t�	|�}
||
 }qttdd�D ]}t�	|�}|| }q�|}d|� �}d}d}d}d}ddt
� |dddddddd�}d�|�|||ddd| ddd�
}| |ddd �}|j|||d!�}|j|||d!�}d"|jv �rTtd
� t�  n@d#|jv �rptd$� t�  n$d%|jv �r�td&� ntd'� t�  td(�}d�|�|||ddd|| dd)d*�}|j|||d!�}d+|jv �r�td,� t�  nDd%|jv �r td-� n.d.|jv �rtd/� nt|j� td'� t�  d0�||||�}|�|� q d S )1NzX5uC6wALAAF-Lw3oSZE9kuY0mP_9�   �   Z#abcdefghijklmnopqrstuvwxyz123456789z[+] Enter Your Telegram ID : � z[!] Error Telegram IDz.1629685400:AAGVpctliNLHIVvIIhhAP_CSYy1TXoZlZDsz[+] Enter Your Phone Number : z[!] Error Phone Numberr   �   Zjev0mzBy @AhmadDevz;https://www.instagram.com/accounts/web_create_ajax/attempt/z=https://www.instagram.com/accounts/send_signup_sms_code_ajax/z3https://www.instagram.com/accounts/web_create_ajax/zwww.instagram.com�Truez*/*z!application/x-www-form-urlencodedZXMLHttpRequestZ936619743392459Zmissingzen-US,en;q=0.9)ZHOSTZ	KeepAlivez
user-agentZCookieZAcceptZContentTypezX-Requested-WithzX-IG-App-IDzX-Instagram-AJAXzX-CSRFTokenzAccept-Languagez&#PWD_INSTAGRAM_BROWSER:0:1589682409:{}r   Z1999Zfals)
�enc_password�phone_number�username�
first_name�month�day�year�	client_id�seamless_login_enabledZopt_into_one_tap)r   r   Zphone_idZbig_blue_token)Zheaders�dataz.Looks like your phone number may be incorrect.z/Please wait a few minutes before you try again.z[!] Please wait a few Minutes�truez&[-] The SMS has been sent successfullyz[!] Error ..z[+] Enter The Code : �row)r   r   r   r   r   r   r   Zsms_coder   r   Ztos_versionzThat code isn't valid.z[!] That code isn't validz[-] Done Created AccountZcheckpoint_requiredz[!] Done, checkpoint requiredu�   https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=⌯ Instagram Fake Account  
⌯ User : {}
⌯ Pass : {}
⌯ Ch : @Div0mz)�requestsZSession�secretsZ	token_hex�input�print�exit�range�randomZchoicer   �formatZpost�text�get)Zidd�r�cookie�charsZmyID�tokenZphoneZuserrZpasss�xZ
userr_char�iZ
passs_charZpaas�user�nameZurl1Zurl2Zurl3�headZdata1Zdata2Z	Make_Acc1Z	Make_Acc2�codeZdata3Z	Make_Acc3ZAccount� r-   �=C:\Users\AHMED\Desktop\New-folder(5)\InstagramAccountMaker.py�Make.   s�    




����
r/   )�osr   r"   �g�sr   r!   r   Zaskvr   �lib�systemr*   r   r   �timer   Z
user_agentr   Zbannerr/   r-   r-   r-   r.   �<module>   s6   







	m