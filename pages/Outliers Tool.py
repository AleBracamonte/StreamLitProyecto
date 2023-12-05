import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    file_path = "Data/DataResults.csv"
    df = pd.read_csv(file_path)
    grupos = df.groupby(['Signal', 'Parameter'])
    st.set_page_config(page_title="Identificación de Outliers", page_icon=":chart_with_upwards_trend:")
    st.title("Identificación de Outliers")
    resultados_outliers = []
    for nombre, grupo in grupos:
        st.subheader(f"Grupo: {nombre}")

        columnas_outliers = grupo[['Mean', 'Max', 'Min']]

        q1 = columnas_outliers.quantile(0.25)
        q3 = columnas_outliers.quantile(0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        grupo['Status'] = grupo.apply(
            lambda row: 0 if (row['Mean'] < limite_inferior['Mean'] or row['Mean'] > limite_superior['Mean'] or
                              row['Max'] < limite_inferior['Max'] or row['Max'] > limite_superior['Max'] or
                              row['Min'] < limite_inferior['Min'] or row['Min'] > limite_superior['Min']) else 1, axis=1)

        resultados_outliers.append(grupo)

        st.subheader("Resultados de Identificación de Outliers:")
        st.dataframe(grupo)

        fig_outliers = plt.figure()
        sns.scatterplot(x='Mean', y='Max', hue='Status', data=grupo, palette={0: 'red', 1: 'blue'})
        plt.title(f"Grupo: {nombre}")
        plt.xlabel("Mean")
        plt.ylabel("Max")
        st.pyplot(fig_outliers)

    df_resultados_outliers = pd.concat(resultados_outliers)
    st.subheader("Tabla de Resultados Completa:")
    st.dataframe(df_resultados_outliers)