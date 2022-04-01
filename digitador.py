import streamlit as st

st.set_page_config('Digitador', page_icon = ':memo:')
st.title(':memo: Digitador')
st.markdown('---')



if not 'observacao' in st.session_state: st.session_state.observacao = ''
st.session_state.obs_construida = []

cliente_reconhece = st.radio('Cliente reconhece a compra?', options = ['Não', 'Sim'])

if cliente_reconhece == 'Não':
    st.session_state.obs_construida.append["Cliente não reconhece a compra.", "Não autorizou o uso de seus dados por terceiros.", "Confirma nome completo e data de nascimento.", "Fraude confirmada."]

    
    
elif cliente_reconhece == 'Sim':
    st.markdown('---')
        
    tipo_pergunta = st.selectbox('Tipo pergunta', options = ['Aplicação', 'Bureau', 'Comportamento', 'Reversa'])

    l, r = st.columns(2)
    
    if tipo_pergunta == 'Aplicação':
        
        l.subheader('Endereço')
        fonte_endereco = l.radio('Fonte', options = ['Mercado', 'Histórico'])
        endereco_informado = l.radio('Informa endereço?', options=['Sim', 'Não'])
        
        if endereco_informado == 'Sim':
            st.session_state.obs_construida.append(f'Informa endereço confiável no {fonte_endereco.lower()}.')
        else:
            st.session_state.obs_construida.append(f'Não informa endereço confiável no {fonte_endereco.lower()}.')
        
            
            
            
        r.subheader('Telefone')
        data_nasc_cliente = r.radio('Informa telefone?', options = ['Sim', 'Não'])
        
        if data_nasc_cliente == 'Sim':
            resposta_telefone = r.radio('Resposta Cliente', options=['Respondeu corretamente', 'Respondeu incorretamente'])
            st.session_state.obs_construida.append(f'{resposta_telefone}.')
        

    elif tipo_pergunta == 'Bureau':
        end_cliente = l.checkbox('Identidade')

        if end_cliente:
            resposta_identidade = st.radio('Resposta Cliente ', options=['Respondeu corretamente', 'Respondeu corretamente'])
            st.session_state.obs_construida.append(f'{resposta_identidade}.')

    
st.markdown('---')



l, m = st.columns(2)
if l.button('Adicionar observação'):
    for i in st.session_state.obs_construida:
        if not i in st.session_state.observacao:
            st.session_state.observacao += f'{i}\n'


if m.button('Apagar'):
    del st.session_state.observacao 
    del st.session_state.obs_construida
    st.experimental_rerun()

st.session_state.observacao = st.text_area('Observação', height = 500, value = st.session_state.observacao)
