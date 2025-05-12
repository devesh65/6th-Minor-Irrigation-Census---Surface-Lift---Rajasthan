import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\hp\\Desktop\\Python_Ca_2\\AgricultureDataset.csv")

#print(df.columns.tolist())



#1. Count number of schemes per village
top_villages = df['village_name'].value_counts().head(10)


top_villages.plot(kind='bar', color='skyblue', figsize=(10,5))
plt.title("Top 10 Villages by Number of Schemes")
plt.xlabel("Village Name")
plt.ylabel("Number of Schemes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#2. Count schemes per owner type
owner_counts = df['ref_scheme_owner_name'].value_counts()
owner_percent = (owner_counts / owner_counts.sum()) * 100


plt.figure(figsize=(6, 6))
colors = sns.color_palette('pastel')
plt.pie(owner_counts, labels=owner_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Schemes by Owner Type")
plt.axis('equal')
plt.show()



#3.
cols = [
    'pump_operating_days_kharif_season',
    'pump_operating_days_rabi_season',
    'pump_operating_days_perennial_season',
    'pump_operating_days_other_season'
]


avg_days = df[cols].mean()
avg_days.index = ['Kharif', 'Rabi', 'Perennial', 'Other']


sns.set(style="whitegrid")


avg_days.plot(kind='line', marker='o', color='orange', figsize=(8, 5), title='Average Pump Operating Days by Season')
plt.ylabel('Average Operating Days')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




#4.


cols = [
    'scheme_construction_cost',
    'scheme_machinery_cost',
    'scheme_maintainence_cost',
    'ipu_total',
    'ipc_total',
    'horse_power_of_lifting_device'
]


df_corr = df[cols].dropna()


corr_matrix = df_corr.corr()


plt.figure(figsize=(10, 6), facecolor='#f9f9f9')
sns.set(style="whitegrid")

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    linewidths=0.5,
    square=True,
    cbar_kws={'label': 'Correlation Coefficient'}
)


plt.title('Correlation Between Scheme Costs, Usage & Horsepower', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



#5.


df_filtered = df.dropna(subset=['ref_scheme_type_surface_flow_name', 'ref_scheme_type_surface_lift_name'])


villages_with_both = df_filtered['village_name'].nunique()


total_villages = df['village_name'].nunique()


villages_without_both = total_villages - villages_with_both


data = pd.DataFrame({
    'Village Type': ['Has Both', 'Does Not Have Both'],
    'Count': [villages_with_both, villages_without_both]
})


plt.figure(figsize=(6, 4), facecolor='#f5f7fa')
sns.set(style='whitegrid')

sns.barplot(data=data, x='Village Type', y='Count', hue='Village Type', legend=False)

plt.title('Villages with Both On-Stream and Off-Stream Schemes', fontsize=14)
plt.ylabel('Number of Villages')
plt.xlabel('')
plt.tight_layout()
plt.show()
plt.show()


