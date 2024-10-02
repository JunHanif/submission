import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load cleaned data
data_df = pd.read_csv('dashboard/main_data.csv')

datetime_columns = ['dteday']
data_df.sort_values(by='dteday', inplace=True)
data_df.reset_index(inplace=True)

for column in datetime_columns:
    data_df[column] = pd.to_datetime(data_df[column])

# Filter data
min_date = data_df['dteday'].min()
max_date = data_df['dteday'].max()

with st.sidebar:
    # Add logo
    st.image('https://github.com/dicodingacademy/assets/raw/main/logo.png')

    # Add date input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = data_df[(data_df['dteday'] >= str(start_date)) & (data_df['dteday'] <= str(end_date))]


st.header('Bike Rental Dashboard')

st.subheader('Overview')

total_count = main_df.cnt.sum()
st.metric(label='Total:', value=total_count)

fig, ax = plt.subplots(figsize=(16, 8))

sns.lineplot(
    x='mnth',
    y='cnt',
    data=main_df,
    palette='Set1',
    marker='o',
    linewidth=2,
    hue=main_df['dteday'].dt.year
    )

plt.title('Jumlah Pengguna Sepeda Rental per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna')
plt.legend(title='Tahun')

st.pyplot(fig)


st.subheader('Pengaruh Cuaca')

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    y='weathersit',
    x='cnt',
    data=main_df,
    palette='Set1',
    )

plt.title('Jumlah Pengguna Sepeda Rental Berdasarkan Cuaca')
plt.xlabel('Jumlah Pengguna')
plt.ylabel('Cuaca')

st.pyplot(fig)


st.subheader('Pengaruh Musim')

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    y='season',
    x='cnt',
    data=main_df,
    palette='Set1',
    )

plt.title('Jumlah Pengguna Sepeda Rental Berdasarkan Season')
plt.xlabel('Jumlah Pengguna')
plt.ylabel('Season')

st.pyplot(fig)
