import streamlit as st
import pandas as pd
from src.ingestion import DataIngestion
from src.profiling import DataProfiler
from src.agent.workflow import AnalysisAgentWorkflow
from src.utils.pdf_export import PDFReportGenerator
st.set_page_config(page_title='Autonomous Data Analysis Agent', layout='wide')
st.title('🤖 Autonomous Data Analysis Agent')
uploaded_file = st.sidebar.file_uploader('Upload CSV/Excel', type=['csv', 'xlsx'])
if uploaded_file:
    df = DataIngestion.load_data(uploaded_file, uploaded_file.name)
    schema = DataIngestion.inspect_schema(df)
    profile = DataProfiler.generate_profile(df)
    tab1, tab2 = st.tabs(['📊 Dataset Preview & Profile', '⚡ Autonomous Agent'])
    with tab1:
        st.dataframe(df.head())
        st.write('Summary Statistics:')
        st.dataframe(pd.DataFrame(profile['stats']))
    with tab2:
        query = st.text_input('Query:', 'Analyze revenue by category')
        if st.button('Run Analysis', type='primary'):
            wf = AnalysisAgentWorkflow()
            res = wf.run(df, schema, query)
            st.markdown(res['report'])
            for fig in res['figures']: st.pyplot(fig)
            pdf = PDFReportGenerator.create_pdf(res['report'])
            with open(pdf, 'rb') as f:
                st.download_button('📥 Download PDF', f, file_name='report.pdf')
else:
    st.info('Upload a CSV or Excel file to get started.')
