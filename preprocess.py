import streamlit as st
import numpy as np
import seaborn as sn
import pandas as pd
import re

def preprocess(data):
    def gettimeanddate(string):
        parts = string.split('-', 1)
        if len(parts) == 2:
            date, message = parts
            date_parts = date.split(',')
            if len(date_parts) == 2:
                date = date_parts[0].strip()
                time = date_parts[1].strip()
                user_message_parts = message.split(':', 1)
                if len(user_message_parts) == 2:
                    user = user_message_parts[0].strip()
                    message = user_message_parts[1].strip()
                    return date, time, user, message
        return None, None, None, None

    # Initialize empty lists to store extracted data
    dates = []
    times = []
    users = []
    messages = []

    for i in data:
        date, time, user, message = gettimeanddate(i)
        if date is not None:
            dates.append(date)
            times.append(time)
            users.append(user)
            messages.append(message)

    # Create a DataFrame
    data = {
        'Date': dates,
        'Time': times,
        'User': users,
        'Message': messages
    }

    df = pd.DataFrame(data)
    return df
