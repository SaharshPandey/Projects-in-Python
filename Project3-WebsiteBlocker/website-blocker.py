import datetime,os,time,difflib,stat


#os.chmod(path="/etc/hosts", mode =0o644)
system_type=os.uname().sysname.lower()

linux_path=r"/etc/hosts"
windows_path=r"C:\Windows\System32\drivers\etc\hosts"
possible_systems=["linux","linux2","windows-pro","windows-home","windows","mac-os","mac"]
block_sites=["www.facebook.com","www.instagram.com","www.pornhub.com"]
redirect_into_localhost="127.0.0.1"

if system_type == difflib.get_close_matches(system_type,possible_systems,1,0.6)[0]:
    #os.system('sudo chmod 777 "/etc/hosts"')
    with open(linux_path,'r') as hosts:
        file=hosts.read()
        print(file)
else:
        with open(windows_path,'r') as hosts:
            file=hosts.read()
            print(file)

while True:
    if(9<datetime.datetime.now().time().hour<23):
        print('Working Hours\n')
        with open(linux_path,"r+") as hosts:
            content=hosts.read()
            for websites in block_sites:
                if websites in content:
                    pass
                else:
                    hosts.write(redirect_into_localhost+" "+websites+"\n")
    else:
        with open(linux_path,'r+') as hosts:
            content =hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(websites in line for websites in block_sites):
                    hosts.write(line)
            hosts.truncate()
        print("Block Sites can be Accessed..\n")

    time.sleep(5)
