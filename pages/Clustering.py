import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    file_path = "Data/DataResults.csv"
    df = pd.read_csv(file_path)
    columns_for_clustering = ['Mean', 'Max', 'Min']
    grupos = df.groupby(['Signal', 'Parameter'])
    st.set_page_config(page_title="Clustering por K-Means", page_icon=":chart_with_upwards_trend:")
    st.title("Clustering por K-Means")
    resultados_clustering = []

    for nombre, grupo in grupos:
        st.subheader(f"Grupo: {nombre}")
        datos_clustering = grupo[columns_for_clustering].values
        scaler = StandardScaler()
        datos_escala = scaler.fit_transform(datos_clustering)
        n_clusters = 5
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        labels = kmeans.fit_predict(datos_escala)
        grupo['Cluster'] = labels
        resultados_clustering.append(grupo)
        st.subheader("Resultados del Clustering:")
        st.dataframe(grupo)
        fig_cluster = plt.figure()
        sns.scatterplot(x='Mean', y='Max', hue='Cluster', data=grupo, palette='viridis')
        plt.title(f"Grupo: {nombre}")
        plt.xlabel("Mean")
        plt.ylabel("Max")
        st.pyplot(fig_cluster)
    df_resultados_clustering = pd.concat(resultados_clustering)
    st.subheader("Tabla de Resultados Completa:")
    st.dataframe(df_resultados_clustering)
