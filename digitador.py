import streamlit as st

st.set_page_config('Digitador', page_icon = ':memo:')
st.title(':memo: Digitador')
st.markdown('---')

if not 'observacao' in st.session_state: st.session_state.observacao = ''
obs_construida = ''

st.radio('Cliente reconhece a compra?', options = ['Sim', 'Não'])

tipo_pergunta = st.selectbox('Tipo pergunta', options = ['Aplicação', 'Bureau', 'Comportamento', 'Reversa'])
st.markdown('##')

if tipo_pergunta == 'Aplicação':
    end_aplicacao = st.checkbox('Endereço?')

    if st.checkbox('Endereço?'):
        st.radio('Fonte', options = ['mercado', 'histórico'])



    data_nasc_cliente = st.checkbox('Data de nascimento?')
    if data_nasc_cliente:
        obs_construida += st.radio('Resposta Cliente', options=['Respondeu corretamente', 'Respondeu corretamente'])
    

elif tipo_pergunta == 'Bureau':
    end_cliente = st.checkbox('Endereço?')

    if end_cliente:
        obs_construida += st.radio('Resposta Cliente', options=['Respondeu corretamente', 'Respondeu corretamente'])

st.markdown('---')
l, m, r = st.columns(3)
if l.button('Criar observação'):
    st.session_state.observacao = obs_construida

if m.button('Apagar'):
    del st.session_state.observacao 
    st.experimental_rerun()

st.session_state.observacao = st.text_area('Observação', height = 500, value = st.session_state.observacao)