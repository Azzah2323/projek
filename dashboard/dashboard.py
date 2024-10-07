import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'dashboard/all_data.csv'
data = pd.read_csv(file_path)

def plot_hourly_rentals(data):
    hourly_rentals = data.groupby('hr')['cnt_y'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(hourly_rentals.index, hourly_rentals.values, marker='o', linestyle='-', color='purple', label='Penyewaan per Jam')
    plt.title('Penyewaan Sepeda Berdasarkan Jam dalam Sehari', fontsize=14)
    plt.xlabel('Jam dalam Sehari (0-23)', fontsize=12)
    plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    plt.xticks(ticks=range(0, 24), labels=[str(i) for i in range(0, 24)])
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

def plot_weekday_rentals(data):
    weekday_rentals = data.groupby('weekday_y')['cnt_y'].sum()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=weekday_rentals.index, y=weekday_rentals.values, palette="Greens_d")
    
    # Menambahkan garis untuk menyoroti hari Jumat
    plt.figure(figsize=(10, 6))
    plt.plot(weekday_rentals.index, weekday_rentals.values, marker='o', linestyle='-', color='b', label='Penyewaan per Hari')
    plt.title('Penyewaan Sepeda Berdasarkan Hari dalam Seminggu', fontsize=14)
    plt.xlabel('Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)', fontsize=12)
    plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    plt.xticks(ticks=range(7), labels=['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

def plot_week_comparison(data):
    weekday_vs_weekend = data.groupby('workingday_y')['cnt_y'].sum()
    plt.figure(figsize=(10, 6))
    plt.bar(['Weekend', 'Weekday'], weekday_vs_weekend.values, color=['orange', 'green'])
    plt.title('Penyewaan Sepeda: Weekday vs Weekend', fontsize=14)
    plt.xlabel('Jenis Hari', fontsize=12)
    plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    plt.grid(True)
    st.pyplot(plt)

st.title('Dashboard Penyewaan Sepeda')

st.header('Paling Banyak Sepeda Disewa pada Jam Berapa dalam Sehari')
plot_hourly_rentals(data)

st.header('Hari dengan Jumlah Penyewaan Tertinggi dalam Seminggu')
plot_weekday_rentals(data)

st.header('Perbedaan Penyewaan antara Weekday dan Weekend')
plot_week_comparison(data)

