toggle = True
while toggle:
    dict = {
        'CU':'see you',
        ':-)':"I'm happy",
        ':-(':"I'm unhappy",
        ';-)':'wink',
        ':-P':'stick out my tongue',
        '(~.~)':'sleepy',
        'TA':'totally awesome',
        'CCC':'Canadian Computing Competition',
        'CUZ':'because',
        'TY':'thank-you',
        'YW':"you're welcome",
        'TTYL':'talk to you later'
    }
    short = input()
    if short == 'TTYL':
        long = dict.get(short)
        print(long)
        toggle = False
    elif short in dict:
        long = dict.get(short)
        print(long)
    else:
        print(short)