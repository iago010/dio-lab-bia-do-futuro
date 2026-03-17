# Pitch

### 1. O Problema 

Hoje, milhares de pessoas são vítimas de golpes bancários todos os dias.  
Golpes como phishing, falso suporte bancário, clonagem de WhatsApp e transferências não reconhecidas geram prejuízos financeiros e emocionais.

Muitos clientes:
- Não sabem identificar uma tentativa de fraude;
- Só percebem o golpe depois que o dinheiro já foi perdido;
- Não sabem quais medidas tomar imediatamente.

Além disso, o atendimento humano pode ser demorado, e o tempo é crucial quando falamos de fraude bancária.

Foi pensando nisso que surgiu o **SegurAI**.

---

### 2. A Solução

O **SegurAI** é um assistente inteligente especializado exclusivamente em segurança bancária e prevenção de fraudes digitais.

Ele:

- Analisa o perfil do cliente (dados fictícios para simulação);
- Avalia histórico de alertas e configurações de segurança;
- Utiliza uma base estruturada com fraudes comuns, boas práticas e FAQ bancário;
- Fornece orientações claras, seguras e acionáveis.

O diferencial técnico do projeto é:

- Uso de modelo LLM rodando via Ollama (`glm-5:cloud`);
- Contextualização dinâmica com dados do cliente em JSON;
- Controle de alucinação com regras explícitas no system prompt;
- Respostas com foco em prevenção, não em pânico.

O agente nunca inventa informações e sempre orienta o usuário a procurar canais oficiais quando necessário.

---

### 3. Demonstração

Nesta parte do vídeo, será mostrado:

1. A interface construída em Streamlit;
2. Uma pergunta simulando phishing:
   - "Recebi um email pedindo para atualizar meus dados bancários, isso é seguro?"
3. O agente identificando o risco e sugerindo não clicar no link.
4. Uma simulação de transação suspeita:
   - "Foi feita uma transferência que eu não reconheço."
5. O SegurAI recomendando bloquear o cartão e contatar o banco.
6. Um teste fora do escopo:
   - "Qual a previsão do tempo?"
7. O agente respondendo corretamente que seu foco é segurança bancária.

Isso demonstra controle de escopo, segurança e assertividade.

---

### 4. Diferencial e Impacto

O grande diferencial do SegurAI é ser um agente especializado, não generalista.

Ele combina:
- Base estruturada de conhecimento sobre fraudes;
- Contexto personalizado do cliente;
- Regras claras contra alucinação;
- Orientação prática e educativa.

O impacto social é significativo:

- Redução de prejuízos financeiros;
- Educação digital para prevenção de golpes;
- Apoio imediato em situações de risco;
- Fortalecimento da cultura de segurança digital.

O SegurAI mostra como a Inteligência Artificial pode ser usada de forma responsável para proteger pessoas.

---


## Link do Vídeo

https://youtu.be/3JGk9GetdQc