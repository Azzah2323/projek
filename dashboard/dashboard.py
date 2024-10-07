import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'all_data.csv'
data = pd.read_csv(file_path)

def plot_hourly_rentals(data):
    hourly_rentals = data.groupby('hr')['cnt_y'].sum()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=hourly_rentals.index, y=hourly_rentals.values, palette="Blues_d")
    
    # Menambahkan garis untuk menyoroti jam 17.00
    plt.axvline(x=17, color='red', linestyle='--', label='Puncak: Jam 17.00')
    plt.title('Paling Banyak Sepeda Disewa pada Jam Berapa dalam Sehari', fontsize=14)
    plt.xlabel('Jam dalam Sehari')
    plt.ylabel('Total Penyewaan')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)

def plot_weekday_rentals(data):
    weekday_rentals = data.groupby('weekday_y')['cnt_y'].sum()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=weekday_rentals.index, y=weekday_rentals.values, palette="Greens_d")
    
    # Menambahkan garis untuk menyoroti hari Jumat
    plt.axvline(x=4, color='red', linestyle='--', label='Puncak: Hari Jumat')
    plt.title('Hari dengan Jumlah Penyewaan Tertinggi dalam Seminggu', fontsize=14)
    plt.xlabel('Hari dalam Seminggu (0=Minggu, 6=Sabtu)')
    plt.ylabel('Total Penyewaan')
    plt.legend()
    st.pyplot(plt)

def plot_week_comparison(data):
    data['weekend'] = data['workingday_y'].apply(lambda x: 'Weekday' if x == 1 else 'Weekend')
    week_comparison = data.groupby('weekend')['cnt_y'].sum()
    plt.figure(figsize=(6, 6))
    sns.barplot(x=week_comparison.index, y=week_comparison.values, palette="Oranges_d")
    plt.title('Perbedaan Penyewaan antara Weekday dan Weekend', fontsize=14)
    plt.xlabel('Jenis Hari')
    plt.ylabel('Total Penyewaan')
    st.pyplot(plt)

st.title('Dashboard Penyewaan Sepeda')

st.header('Paling Banyak Sepeda Disewa pada Jam Berapa dalam Sehari')
plot_hourly_rentals(data)

st.header('Hari dengan Jumlah Penyewaan Tertinggi dalam Seminggu')
plot_weekday_rentals(data)

st.header('Perbedaan Penyewaan antara Weekday dan Weekend')
plot_week_comparison(data)

