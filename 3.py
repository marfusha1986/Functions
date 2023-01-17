sh = input('Enter hours: ')
sr = input('Enter rate: ')
fh = float(sh)
fr = float(sr)
def computepay(fh, fr):
    return 42.37
xp= computepay(10, 20)
if fh < 40:
   # print('Regular')
    xp = fh * fr
    print('Pay ', xp)
else:
    #print('Overtime')
    reg = fh * fr
    otp = (fh-40)*(fr*0.5)
    xp = reg + otp
    print('Pay ', xp)