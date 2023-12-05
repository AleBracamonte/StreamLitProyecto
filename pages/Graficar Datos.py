import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    df = pd.read_csv(r"Data/DataResults.csv")
    st.set_page_config(page_title="Exploración de Datos", page_icon=":bar_chart:")
    st.title("Exploración de Datos")
    st.subheader("Tabla de Datos:")
    st.dataframe(df)
    st.subheader("Gráficas por Grupo:")
    grupos = df.groupby(['Signal', 'Parameter'])
    for nombre, grupo in grupos:
        st.write(f"Grupo: {nombre}")
        fig, ax = plt.subplots()
        sns.scatterplot(x='Objeto', y='Mean', data=grupo, ax=ax, label='Mean', color='blue')
        sns.scatterplot(x='Objeto', y='Max', data=grupo, ax=ax, label='Max', color='orange')
        sns.scatterplot(x='Objeto', y='Min', data=grupo, ax=ax, label='Min', color='green')
        ax.set_title(f"Grupo: {nombre}")
        ax.set_ylabel("Valor")
        ax.legend()
        st.pyplot(fig)
