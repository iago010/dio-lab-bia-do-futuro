import json
import pandas as pd
import requests
import streamlit as st

# ========= CARREGAR DADOS =============
praticas = json.load(open('./data/boas_praticas_seguranca.json'))
fraudes = json.load(open('./data/fraudes_comuns.json'))
faq = pd.read_csv('./data/faq_banco.csv')
transacoes = pd.read_csv('./data/transacoes_suspeitas.csv')
cliente = json.load(open('./data/cliente.json'))

# ========= CONFIGURAÇÕES OLLAMA ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "glm-5:cloud"

# ========= MONTAR CONTEXTO ============

contexto = f"""
=== DADOS DO CLIENTE ===
Nome: {cliente['nome']}
CPF: {cliente['cpf']}
Email: {cliente['email']}
Telefone: {cliente['telefone']}
Perfil de Risco: {cliente['perfil_risco']}

=== ENDEREÇO ===
Cidade: {cliente['endereco']['cidade']} - {cliente['endereco']['estado']}

=== CONTA BANCÁRIA ===
Banco: {cliente['conta_bancaria']['banco']}
Tipo de Conta: {cliente['conta_bancaria']['tipo_conta']}
Saldo Atual: R$ {cliente['conta_bancaria']['saldo_atual']}
Limite Pix Diário: R$ {cliente['conta_bancaria']['limite_pix_diario']}

=== SEGURANÇA ===
Autenticação 2FA Ativada: {cliente['seguranca']['autenticacao_dois_fatores']}
Último Login: {cliente['seguranca']['ultimo_login']}
Dispositivo Cadastrado: {cliente['seguranca']['dispositivo_cadastrado']}
IP Último Acesso: {cliente['seguranca']['ip_ultimo_acesso']}

=== HISTÓRICO DE ALERTAS ===
Total de Alertas: {len(cliente['historico_alertas'])}
Alertas Recentes:
{chr(10).join([f"- {a['data']} | {a['tipo']} | {a['descricao']}" for a in cliente['historico_alertas']])}
"""

# ========= SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o SegurAI, um agente inteligente especializado em segurança bancária e prevenção de fraudes digitais.
Seu objetivo é orientar o usuário a identificar, prevenir e reagir a golpes, transações suspeitas e tentativas de fraude, sempre de forma educativa e segura.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos na base de conhecimento do SegurAI (fraudes comuns, boas práticas, FAQ, transações suspeitas).
2. Nunca invente informações financeiras ou sobre clientes.
3. Se não souber algo, admita e direcione o usuário para canais oficiais do banco.
4. Sempre explique o motivo de uma transação ser suspeita ou de um alerta de segurança.
5. Use linguagem acessível, clara e paciente, mesmo ao explicar conceitos técnicos.
6. Evite causar pânico, priorize orientação e prevenção.
7. Quando possível, sugira ações concretas: bloquear cartão, contatar banco, alterar senha, ativar autenticação de dois fatores.
8. Para perguntas fora do escopo de fraude bancária, informe que seu foco é segurança financeira.
9. Utilize exemplos da base de conhecimento para contextualizar respostas (Few-Shot Prompting).
"""


# ========= CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ========= INTERFACE ============
st.title("SegurAI, Assistente de Segurança Bancária")

if pergunta := st.text_input("Faça sua pergunta sobre segurança bancária:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Processando..."):
        st.chat_message("assistant").write(perguntar(pergunta))