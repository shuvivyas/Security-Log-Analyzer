from collections import defaultdict
brute_count = 3
password_count = 3

def brute(all_logs):
    count = defaultdict(int)
    alert = []
    for logs in all_logs:
        if logs["event"] == "login failed":
            ip = logs["ip"]
            count[ip] += 1
    for key,value in count.items():
        if value >= brute_count:
            alert.append({"Alert Type" : "Brute Force Attack",
            "IP" : key, "Attempts": value})
    return alert


def passwords(all_logs):
    users = defaultdict(set)
    alert = []
    for logs in all_logs:
        if logs["event"] == "login failed":
            ip = logs["ip"] 
            users[ip].add(logs["user"])
    for ip,acc in users.items():
        if len(acc) >= password_count:
            alert.append({"Alert Type" : "Password Spraying Attack",
            "IP" : ip, "User Accounts": list(acc)})
    return alert

def detect(all_logs):
    alert = []
    alert.extend(brute(all_logs))
    alert.extend(passwords(all_logs))
    return alert
