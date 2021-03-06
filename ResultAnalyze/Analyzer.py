import os

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Analyzer():

    def __init__(self):
        pass

    def load_data(self, result_file_name):
        file_path = os.path.join('results', f'{result_file_name}.txt')
        return pd.read_csv(file_path, delimiter=',')
   
    def visualize_bees_results(self, file_name, optimum_type, title):
        df = self.load_data(file_name)

        sns.set() 
        #paired
        sns.set_palette("bright")

        fig, ax = plt.subplots(figsize=(15,7))  
        population_num = df['rozmiar populacji'].unique()
        trials=df['liczba prób'].unique()
        for j in range(len(population_num)):
            for k in range(len(trials)):                      
                filtered =  df[ (df['rozmiar populacji']==population_num[j])  & (df['liczba prób']==trials[k]) ]
                grouped = filtered.groupby(['rozmiar populacji', 'liczba iteracji', 'weight', 'iter'])
                x_data = np.arange(1, len(grouped)+1, 1)
                y_data = grouped[optimum_type].mean()
                plt.plot(x_data , y_data,  linewidth=1,  label='rozmiar populacji='+str(population_num[j])+', liczba prób='+ str(trials[k]))



        plt.axhline(y=df['optimum globalne'].iloc[0], color='r', linestyle='--', label='Optimum globalne')
        plt.xlabel ("Kroki iteracji")
        plt.ylabel('Wartośc optimum')
        plt.title(title)
        plt.legend()
       
        file_path = os.path.join('results', f'{file_name}+{optimum_type}.png')
        plt.savefig(file_path)

    def visualize_pso_results(self, file_name, optimum_type,  title):
        df = self.load_data(file_name)

        sns.set() 
        #paired
        sns.set_palette("bright")
        print(df.columns)
        fig, ax = plt.subplots(figsize=(15,7))  
        c1 = df['c1'].unique()
        c2 = df['c2'].unique()
        weight = df['weight'].unique()
        for j in range(len(c1)):
            for k in range(len(c2)):
                if(c1[j] == c2[k]):
                    for i in range(len(weight)):
                        filtered = df[ (df['c1']==c1[j]) & (df['c2']==c2[k]) & (df['weight']==weight[i]) ]
                        grouped = filtered.groupby(['c1', 'c2', 'weight', 'iter'])
                        x_data = np.arange(1, len(grouped)+1, 1)
                        y_data = grouped[optimum_type].mean()
                        plt.plot(x_data , y_data,  linewidth=1,  label='c1='+str(c1[j])+',  c2='+ str(c2[k]) + ', weight='+str(weight[i]))

        plt.axhline(y=df['optimum globalne'].iloc[0], color='r', linestyle='--', label='Optimum globalne')
        plt.xlabel ("Kroki iteracji")
        plt.ylabel('Wartośc optimum')
        plt.title(title)
        plt.legend(ncol=2)
       
        file_path = os.path.join('results', f'{file_name}+{optimum_type}.png')
        plt.savefig(file_path)


a = Analyzer()
# a.visualize_bees_results('bee50_2',  'najlepsze śledzone', 'Najlepsze znalezione optimum w danym kroku iteracji przez pszczołe zwiadowcę')
# a.visualize_bees_results('bee50_2', 'najlepsze znalezione', 'Najlepsze znalezione optimum w danym kroku iteracji przez pszczołe pracującą')
a.visualize_pso_results('particle50', 'najlepsze śledzone', 'Najlepsze znalezione optimum w danym kroku iteracji')
a.visualize_pso_results('particle50', 'najlepsze znalezione', 'Najlepsze znalezione dotychczas optimum w danym kroku iteracji')


