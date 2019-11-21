{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]\
\
prices = [30, 25, 40, 20, 20, 35, 50, 35]\
\
last_week = [2, 3, 5, 8, 4, 4, 6, 2]\
\
total_price = 0\
\
for price in prices:\
  total_price = total_price + price  \
average_price = total_price / len(prices)\
print("Average Haircut Price: " + str(average_price))\
\
new_prices = [price - 5 for price in prices]\
print(new_prices)\
\
total_revenue = 0\
\
for i in range(len(hairstyles)):\
  total_revenue += prices[i] * last_week[i]\
print(total_revenue)\
\
average_daily_revenue = total_revenue / 7\
print(average_daily_revenue)\
\
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]\
print(cuts_under_30)}