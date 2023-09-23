# import pandas as pd
# from datetime import datetime, timedelta
# from rest_framework.views import  APIView
# from rest_framework import status
# import logging
# from rest_framework.response import Response
# import supabase

# supabase_url = 'https://kdrmgmseudtaweqicows.supabase.co'
# supabase_key = ''

# supabase_client = supabase.Client(supabase_url, supabase_key)

# response, data = supabase_client.from_('store_statustimestampt').select('*').execute()
# response_store_status, data_store_status = supabase_client.from_('store_statustimestampt').select('*').execute()
# response_business_hours, data_business_hours = supabase_client.from_('store_businesshourstime').select('*').execute()

# if response_store_status.status_code == 200 and response_business_hours.status_code == 200:
#         # Convert data to Pandas DataFrames
#         store_status = pd.DataFrame(data_store_status)
#         business_hours = pd.DataFrame(data_business_hours)
# else:
#     print('Error fetching data from Supabase.')


# # Step 2: Calculate Business Hours
# def calculate_business_hours(df):
#     business_hours = {}
#     for _, row in df.iterrows():
#         store_id = row['store_id']
#         day_of_week = row['dayOfWeek']
#         start_time_local = datetime.strptime(row['start_time_local'], '%H:%M:%S').time()
#         end_time_local = datetime.strptime(row['end_time_local'], '%H:%M:%S').time()

#         if store_id not in business_hours:
#             business_hours[store_id] = {}
#         if day_of_week not in business_hours[store_id]:
#             business_hours[store_id][day_of_week] = {
#                 'start_time': start_time_local,
#                 'end_time': end_time_local
#             }
#         else:
#             # Update start and end times if needed
#             if start_time_local < business_hours[store_id][day_of_week]['start_time']:
#                 business_hours[store_id][day_of_week]['start_time'] = start_time_local
#             if end_time_local > business_hours[store_id][day_of_week]['end_time']:
#                 business_hours[store_id][day_of_week]['end_time'] = end_time_local


# calculate_business_hours(table2_df)


# # Step 3: Interpolate Uptime and Downtime
# def interpolate_status(store_id, day_of_week, df, business_hours):
#     # Initialize variables
#     start_time = business_hours[store_id][day_of_week]['start_time']
#     end_time = business_hours[store_id][day_of_week]['end_time']
#     interval = timedelta(minutes=1)  # Interval for interpolation
#     current_time = start_time
#     uptime_minutes = 0
#     downtime_minutes = 0

#     # Iterate through time intervals within business hours
#     while current_time <= end_time:
#         # Check if there is a status observation at the current time
#         matching_rows = df[(df['store_id'] == store_id) &
#                            (df['dayOfWeek'] == day_of_week) &
#                            (df['timestamp_utc'].dt.time == current_time)]

#         if not matching_rows.empty:
#             status = matching_rows.iloc[0]['status']
#             if status == 'up':
#                 uptime_minutes += 1
#             elif status == 'down':
#                 downtime_minutes += 1

#         current_time += interval

#     return uptime_minutes, downtime_minutes


# # Step 4: Aggregate Results
# def aggregate_results(df, business_hours):
#     result = pd.DataFrame(columns=[
#         'store_id',
#         'uptime_last_hour',
#         'uptime_last_day',
#         'uptime_last_week',
#         'downtime_last_hour',
#         'downtime_last_day',
#         'downtime_last_week'
#     ])

#     # Calculate current date and week start date
#     current_date = datetime.now().date()
#     week_start_date = current_date - timedelta(days=current_date.weekday())

#     # Iterate through each store and day of the week
#     for store_id in business_hours.keys():
#         for day_of_week in business_hours[store_id].keys():
#             # Interpolate uptime and downtime for the current day
#             uptime_hour, downtime_hour = interpolate_status(store_id, day_of_week, df, business_hours)

#             # Interpolate uptime and downtime for the last 24 hours
#             uptime_day, downtime_day = 0, 0
#             for i in range(24):
#                 day_ago = current_date - timedelta(days=1, hours=i)
#                 day_of_week_ago = day_ago.weekday()
#                 if day_of_week_ago == day_of_week:
#                     u, d = interpolate_status(store_id, day_of_week_ago, df, business_hours)
#                     uptime_day += u
#                     downtime_day += d

#             # Interpolate uptime and downtime for the last 7 days
#             uptime_week, downtime_week = 0, 0
#             for i in range(7):
#                 day_ago = week_start_date - timedelta(days=i)
#                 day_of_week_ago = day_ago.weekday()
#                 if day_of_week_ago == day_of_week:
#                     u, d = interpolate_status(store_id, day_of_week_ago, df, business_hours)
#                     uptime_week += u
#                     downtime_week += d

#             # Add results to the DataFrame
#             result = result.append({
#                 'store_id': store_id,
#                 'uptime_last_hour': uptime_hour,
#                 'uptime_last_day': uptime_day,
#                 'uptime_last_week': uptime_week,
#                 'downtime_last_hour': downtime_hour,
#                 'downtime_last_day': downtime_day,
#                 'downtime_last_week': downtime_week
#             }, ignore_index=True)

#     return result


# output_df = aggregate_results(store_status, business_hours)


# print(output_df)
