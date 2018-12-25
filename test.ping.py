import subprocess


def check_ping(name):
    hostname = name
    sub_p = subprocess.Popen(["ping", "-W", "500", "-c", "1", hostname], stdout=subprocess.PIPE)
    sub_p.wait()
    response = sub_p.poll()
    # and then check the response...
    if response == 0 :
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

if __name__ == "__main__":
    isConn = check_ping('192.168.0.20')
    print('isConn1 : ' + isConn)
    isConn2 = check_ping('192.168.0.9')
    print('isConn2 : ' + isConn2)
    