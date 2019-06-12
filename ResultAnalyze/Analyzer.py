import os

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Analyzer():

    def __init__(self):
        self.colors = []

        for i in range(50):
            res = '#'+str('%06X' % randint(0, 0xFFFFFF))
            self.colors.append(res)  

    def load_data(self, result_file_name):
        file_path = os.path.join('results', f'{result_file_name}')
        #file_path = result_file_name
        return pd.read_csv(file_path, delimiter=',')
   
    def visualize_bees_results(self, file_name, optimum_type, title):
        df = self.load_data(file_name)
        sns.set() 
        sns.set_palette("bright")
        fig, ax = plt.subplots(figsize=(15,7))  
        population_num = df['rozmiar populacji'].unique()
        trials=df['liczba prób'].unique()
        global_optimum = df['optimum globalne'].iloc[0]
        for j in range(len(population_num)):
            for k in range(len(trials)):                      
                filtered =  df[ (df['rozmiar populacji']==population_num[j])  & (df['liczba prób']==trials[k]) ]
                grouped = filtered.groupby(['rozmiar populacji', 'liczba iteracji', 'weight', 'iter'])
                x_data = np.arange(1, len(grouped)+1, 1)
                y_data = grouped[optimum_type].mean()
                if(y_data.min() < global_optimum + 0.15):
                    plt.plot(x_data , y_data,  linewidth=1,  label='rozmiar populacji='+str(population_num[j])+', liczba prób='+ str(trials[k]))
        plt.axhline(y=global_optimum, color='r', linestyle='--', label='Optimum globalne')
        plt.xlabel ("Kroki iteracji")
        plt.ylabel('Wartośc optimum')
        plt.title(title)
        plt.legend(ncol=3)   
        file_path = os.path.join('results', f'{file_name}+{optimum_type}.png')
        plt.savefig(file_path)

    def visualize_pso_results(self, file_name, optimum_type,  title):
        df = self.load_data(file_name)
        sns.set() 
       # sns.set_palette("bright")
        fig, ax = plt.subplots(figsize=(15,7))  
        c1 = df['c1'].unique()
        c2 = df['c2'].unique()
        weight = df['weight'].unique()
        global_optimum = df['optimum globalne'].iloc[0]
        for j in range(len(c1)):
            for k in range(len(c2)):
                    for i in range(len(weight)):
                        filtered = df[ (df['c1']==c1[j]) & (df['c2']==c2[k]) & (df['weight']==weight[i]) ]
                        grouped = filtered.groupby(['c1', 'c2', 'weight', 'iter'])
                        x_data = np.arange(1, len(grouped)+1, 1)
                        y_data = grouped[optimum_type].mean()
                        if(y_data.min() < global_optimum + 0.15):
                            plt.plot(x_data , y_data,  linewidth=1,  label='c1='+str(round(c1[j], 2))+',  c2='+ str(round(c2[k], 2)) + ', weight='+str(round(weight[i], 2) ) )

        plt.axhline(y=global_optimum, color='r', linestyle='--', label='Optimum globalne')
        plt.xlabel ("Kroki iteracji")
        plt.ylabel('Wartośc optimum')
        plt.title(title)
        plt.legend(ncol=3)
        file_path = os.path.join('results', f'{file_name}+{optimum_type}.png')
        plt.savefig(file_path)


    def visualize_firefly_results(self, file_name, optimum_type,  title):
            df = self.load_data(file_name)
            sns.set() 
            sns.set_palette("bright")
            print(df.columns)
            fig, ax = plt.subplots(figsize=(15,7))  
            max_beta = df['max_beta'].unique()
            absorption_coefficient = df['absorption_coefficient'].unique()
            global_optimum = df['optimum globalne'].iloc[0]
            for j in range(len(max_beta)):
                for k in range(len(absorption_coefficient)):
                        filtered = df[ (df['max_beta']==max_beta[j]) & (df['absorption_coefficient']==absorption_coefficient[k]) ]
                        grouped = filtered.groupby(['max_beta', 'absorption_coefficient', 'iter'])
                        x_data = np.arange(1, len(grouped)+1, 1)
                        y_data = grouped[optimum_type].mean()
                        if(y_data.min() < global_optimum + 0.15):
                            plt.plot(x_data , y_data,  linewidth=1,  label='max_beta='+str(max_beta[j])+',  absorption_coefficient='+ str(absorption_coefficient[k]) )

            plt.axhline(y=df['optimum globalne'].iloc[0], color='r', linestyle='--', label='Optimum globalne')
            plt.xlabel ("Kroki iteracji")
            plt.ylabel('Wartośc optimum')
            plt.title(title)
            plt.legend(ncol=3)
            file_path = os.path.join('results', f'{file_name}+{optimum_type}.png')
            plt.savefig(file_path)

a = Analyzer()

function =['Ackley', 'Bukin6', 'Rastrigin', 'Sphere', 'Trid']

for i in range(len(function)):
    pso_name = 'pso_200_'+str(function[i])
    a.visualize_pso_results(pso_name, 'najlepsze śledzone', 'Najlepsze znalezione optimum w danym kroku iteracji')
    a.visualize_pso_results(pso_name, 'najlepsze znalezione', 'Najlepsze znalezione dotychczas optimum w danym kroku iteracji')

