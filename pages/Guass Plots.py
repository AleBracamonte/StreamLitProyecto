import pandas as pd
import streamlit as st
# import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


if __name__ == '__main__':

    file_path = "Data/DataResults.csv"
    df = pd.read_csv(file_path)
    st.set_page_config(page_title="Visualización de Distribuciones Normales", page_icon=":chart_with_upwards_trend:")
    st.title("Distribuciones Normales ")
    for (signal, parameter), grupo in df.groupby(['Signal', 'Parameter']):
        st.subheader(f"Signal: {signal}, Parameter: {parameter}")
        fig, ax = plt.subplots(figsize=(8, 4))
        for objeto, objeto_df in grupo.groupby('Objeto'):
            media = objeto_df['Mean'].mean()
            desviacion_estandar = df['Mean'].std()
            x = np.linspace(media - 3 * desviacion_estandar, media + 3 * desviacion_estandar, 100)
            y = norm.pdf(x, media, desviacion_estandar)
            y = y / y.sum()
            ax.plot(x, y, label=objeto)

        ax.legend()
        ax.set_xlabel("Valor")
        ax.set_ylabel("Densidad de Probabilidad")
        st.pyplot(fig)
    plt.close()
