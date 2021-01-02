from datetime import datetime

host_paths = 'C:\Windows\System32\drivers\etc\hosts'
redirect = "127.0.0.1"

website_lists = ["facebook.com","instagram.com"]

start_date = datetime(2021,1,2)
end_date = datetime(2021,2,2)
today_date = datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if start_date <= today_date < end_date:
        with open(host_paths, "r+") as file:
            content = file.read()
            for site in website_lists:
                if site in content:
                    pass
                else:
                    file.write(redirect+""+site+"\n") 
        print("all sites are blocked")
        break
    else:
        with open(host_paths,"r+") as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_lists):
                    file.write(line)
            file.truncate()
        print("all sites are blocked")

        break
