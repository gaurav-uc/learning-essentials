import re
CA_LA1_CASE_NUMBER_PREFIX_REGEX_STRING = r'\d+(?P<prefix>[a-zA-Z]+)(?P<raw_case_number>\d+)'
FL_PICC_CASE_NUMBER_PREFIX_REGEX_STRING = r'\d*-\d*-(?P<suffix>[A-Z]{2})'

# SELECT case_number FROM courtcase c
# INNER JOIN party p ON p.case_id=c.id
# WHERE p.fname='NONE';
# sudo mysql -u codaxtr_user codaxtr -pc0d@xtr -e "SELECT case_number FROM courtcase c INNER JOIN party p ON p.case_id=c.id WHERE p.fname=\'NONE\';" > case_numbers.txt

case_prefix_list = []

la_case_prefix_regex = re.compile(FL_PICC_CASE_NUMBER_PREFIX_REGEX_STRING, flags=re.I)
case_numbers_file = open("case_numbers.txt", "r")

for case_numbers in case_numbers_file:
	la_case_prefix = re.search(la_case_prefix_regex, case_number).group('prefix')
	case_prefix_list.append(la_case_prefix)

for unique_prefixes in set(case_prefix_list):
	print unique_prefixes,


