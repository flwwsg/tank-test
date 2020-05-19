import re
re_email=re.compile(r'(\d{9})@qq.com')
re_email.match('965972450@qq.com').groups()
re_gmail=re.compile(r'(^\w*?)@gmail.c   om')