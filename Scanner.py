import sys, re

## IDK if we needs comments or not the rubric says we need them but we've never needed them before so ig I do them just to be safe
def er(): #exits if invalid input

    print("NOT PROPER CIDR NOTATION!?!?")
    exit()
def checkermecker():
    if len(sys.argv) < 1: ##Checks if the input is empty and exits if it is
        print("No ip address provided, what the funk?.")
        exit()
    parameter = sys.argv[1]
    sp = re.split(r'[./]', parameter)
    if len(sp) != 5: #Make sure it has 5 'arguements'
        er()
    for x in sp: #make sure only number
        try: int(x)
        except ValueError:
            er()
    if int(sp[4]) > 32 or int(sp[4]) < 0: #make sure subnet mask is between 0-32
        er()
    subnet = sp[4]
    i1 = sp[0]
    i2 = sp[1]
    i3 = sp[2]
    i4 = sp[3]
    del sp[4]
    for x in sp: #Make sure all other number are good
        if int(x) > 255 or int(x) < 0:
            er()
    del sp
    lp = re.sub(f"[^{re.escape(".")}{re.escape("/")}]","",parameter)   # get only / and period
    if len(lp) != 4: er # Make sure right number of dots and dashes
    if lp[0] != "." or lp[1] != "." or lp[2] != "." or lp[3] != "/": #make sure stuff is in the right spot
        er()
    return subnet, i1, i2, i3, i4 

ip = sys.argv[1]
subnet, i1, i2, i3, i4 = checkermecker()