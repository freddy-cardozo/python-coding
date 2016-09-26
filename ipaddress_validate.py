import re
import traceback
ip='99.10.10.10'
choice='y'
while(choice == 'y'):
    ip = raw_input('Enter your IP address : ')
    try:
        if [0<=int(x)<256 for x in re.split('\.',re.match(r'^\d+\.\d+\.\d+\.\d+$',ip).group(0))].count(True)==4:
            print "\t\tVALID IP  ADDRESS {}".format(ip)
        else:
            print "\t\tINVALID IP ADDRESS {}".format(ip)
    except:
        print "INVALID IP ADDRESS {}".format(ip)
    emailAddr = raw_input('Enter your email address : ')
    try:
        matchObj = re.match("[-_a-z0-9]+@[-_a-z0-9]+\.[a-zA-Z]{3,3}$", emailAddr, re.I)
        if matchObj:
            print (matchObj.group())
            print "\t\t VALID EMAIL ADDRESS {}".format(emailAddr)
        else:
            print "\t\t INVALID EMAIL ADDRESS ::{}--".format(emailAddr)
    except:
        print "EXCEPTION"
        traceback.print_exc()
        print "\t\t INVALID EMAIL ADDRESS {}".format(emailAddr)
    choice = raw_input('Do you want to continue (y/n)')