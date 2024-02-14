import streamlit as st

# Título de la página
st.title("Dashboard de Siniestros Viales en Buenos Aires Argentina")

# Widget para cargar archivos
file = st.file_uploader("siniestros_viales.pdf", type="pdf")

# Verifica si se ha cargado un archivo
if file is not None:
    # Muestra el nombre del archivo
    st.write("Nombre del archivo:", file.name)
    
    # Muestra el contenido del archivo
    st.write("Contenido del archivo:")
    st.write(file.read())

    # También puedes mostrar el archivo como un visor de PDF
    # st.write(file)

