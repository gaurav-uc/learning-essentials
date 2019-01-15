import re

case_prefix_list = []

la_case_prefix_regex = re.compile(CASE_NUMBER_PREFIX_REGEX_STRING, flags=re.I)
case_numbers_file = open("case_numbers.txt", "r")

for case_numbers in case_numbers_file:
	la_case_prefix = re.search(la_case_prefix_regex, case_number).group('prefix')
	case_prefix_list.append(la_case_prefix)

for unique_prefixes in set(case_prefix_list):
	print unique_prefixes,


