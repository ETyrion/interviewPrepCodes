ip_str = 'i.like.this.program.very.much'

ip_str_list = ip_str.split('.')
print(ip_str_list)

rev_str = ip_str_list[::-1]
print(rev_str)
print('.'.join(rev_str))