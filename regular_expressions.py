# Regular Expressions (RegEx) is a sequence of characters that forms a search pattern
# To work with RegEx a built-in package "import re" is used
# re module functions:
# 1) findall - returns a list containing all matches
# 2) search - returns a match object if there is a match anywhere in the string
# 3) split - returns a list where the string has been split at each match
# 4) sub - replaces one or many matches with a string

# Metacharacters:
# 1) [] - a set of characters ( [a-m], from a to m )
#       [arn], returns a match where one of the specified characters (a, r or n) is present
#       [a-n], returns a match for any lower case character alphabetically between a and n
#       [^arn], returns a match of any character except a, r or n
#       [0123], returns a match where one of the specified digits is present
#       [0-9], returns a match for any digits between 0 and 9
#       [0-5][0-9], returns a match for any two-digits number from 00 and 59
#       [a-zA-Z], returns a match for any character alphabetically between a and z , lower case or upper case
#       [+], In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means:
#           return a match for any + character in the string
# 2) \ - signals a special sequence (can also be used to escape special characters)
#       \d, find all digits;
#       \D, returns a match where the string does not contain any digits
#       \s, all spaces;
#       \S, returns a match where the string does not contain any spaces
#       \w, all letters;
#       \W, returns a match where the string does not contain any word character
#       \A, returns a match if the specified characters are at the beginning of the string '\AThe'
#       \b, returns a match where the specified characters are at the begin. or at the end of the word '\bain' 'ain\b'
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")
#   ! raw string treats backslash '\' as a literal character
#       \B, returns a match where the specified characters are present (BUT NOT at the begin/end) in the word
#           '\Bain' 'ain\B'
#       \Z, returns a match if the specified characters are at the end of the string 'Spain\Z'
# 3) . - any character (except newline character) ( he..o, Search for a sequence that starts with "he",
#       followed by two (any) characters, and an "o" )
# 4) ^ - starts with ( ^hello )
# 5) $ - ends with ( $llo )
# 6) * - zero or more occurrences ( he.*o, Search for a sequence that starts with "he",
#       followed by 0 or more  (any) characters, and an "o" )
# 7) + - one or more occurrences
# 8) ? - zero or one occurrences
# 9) {} - exactly the specified number of occurrences ( he.{2}o, Search for a sequence that starts with "he",
#       followed exactly 2 (any) characters, and an "o" )
# 10) | - either or ( falls|stays, Check if the string contains either "falls" or "stays" )
# 11) () - capture and group

import re

general_var = 'An Internet Protocol address (IP address) is a numerical label such as 192.168.1.254 that is connected ' \
              'to a computer network that uses the Internet Protocol for communication.[1][2] An IP address serves ' \
              'two main functions: network interface identification and location addressing. Internet Protocol ' \
              'version 4 (IPv4) defines an IP address as a 32-bit number.[2] However, because of the growth of the ' \
              'Internet and the depletion of available IPv4 addresses, a new version of IP (IPv6), using 128 bits for ' \
              'the IP address, was standardized in 1998.[3][4][5] IPv6 deployment has been ongoing since the mid-2000s.'

# 1
all_digits = re.findall('', general_var)
print(all_digits)
print('\n')

# 2
all_ips = re.findall('IPv4|IPv6', general_var)
print(all_ips)
print('\n')

# 3
mention_to_strip = '128 bits.*'
search_for_mention = re.search(mention_to_strip, general_var)
# re.MatchObject.group(<index of a group>) method returns the complete matched subgroup by default or
# a tuple of matched subgroups depending on the number of arguments
all_text_after_128bits = search_for_mention.group()
print(all_text_after_128bits)
print('\n')

# 4
# ip_address_pattern = '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
ip_address_pattern = '(\d+.){3}\d+'
search_for_ip_address = re.search(ip_address_pattern, general_var)
print(search_for_ip_address.group())
print('\n')

# 5
with open('regular_expressions.txt', 'w') as file:
    file.write(general_var)
with open('regular_expressions.txt', 'r') as file:
    read_file = file.read()
    updated_read_file = read_file
    ex5_pattern_to_delete = [ip_address_pattern, 'IPv4|IPv6', '\d']
    for i in ex5_pattern_to_delete:
        updated_read_file = re.sub(i, '', updated_read_file)
    print(updated_read_file)
