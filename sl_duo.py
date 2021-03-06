import streamlit as sl
from datetime import datetime, date


duo_dict = {
	"2021-11": 24,
	"2021-12": 22,
	"2022-01": 24,
	"2022-02": 24,
	"2022-03": 24,
	"2022-04": 22,
	"2022-05": 24,
	"2022-06": 24,
	"2022-07": 22,
	"2022-08": 24,
	"2022-09": 23,
	"2022-10": 24,
	"2022-11": 24,
	"2022-12": 22
}

def current_d(now):
	return now.strftime("%d")

def current_m_and_y(now):
	return now.strftime("%Y-%m")

def next_dict(month_and_year):
	global duo_dict
	temp = list(duo_dict)
	try:
		res = temp[temp.index(month_and_year) + 1]
	except (ValueError, IndexError):
		res = None
	return res

def get_dif(now, next_duo):
	year, month, day, hour = int(now.strftime("%Y")), int(now.strftime("%m")), int(now.strftime("%d")), int(now.strftime("%H"))
	f_date = datetime(year, month, day, hour)

	# 22-2021-12
	# print(next_duo[0:2])
	n_year, n_month, n_day = int(next_duo[3:7]), int(next_duo[8:10]), int(next_duo[0:2])
	l_date = datetime(n_year, n_month, n_day, 10)
	delta = l_date - f_date
	# next_duo = next_duo.strftime("%Y-%m-%d")
	# current_date = now.strftime("%Y-%m-%d")
	return delta

def main():
	global duo_dict
	now = datetime.now()
	day = current_d(now)
	month_and_year = current_m_and_y(now)
	
	# print(duo_dict[month_and_year])

	if int(day) >= duo_dict[month_and_year]:
		next_duo = (f"{duo_dict[next_dict(month_and_year)]}-{next_dict(month_and_year)}")
	else:
		next_duo = (f"{duo_dict[month_and_year]}-{month_and_year}")
	
	header = sl.container()
	data = sl.container()

	with header:
		dif = str(get_dif(now, next_duo))
		dif_dagen = dif.split(" ")[0]
		dif_uur = dif.split(" ")[2]
		dif_uur = dif_uur.split(":")[0]

		sl.title(f"Nog {dif_dagen} dagen en ongeveer {dif_uur} uur.")
			
	# print("dat is nog ")

main()

# header = sl.container()

# with header:
# 	sl.title("dagen tot ome duo!")

