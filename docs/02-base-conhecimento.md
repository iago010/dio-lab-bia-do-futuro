# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `fraudes_comuns.json` | JSON | Lista de golpes conhecidos, como phishing, clonagem de cartão e links suspeitos |
| `boas_praticas_seguranca.json` | JSON | Orientações gerais de segurança para clientes bancários |
| `faq_banco.csv` | CSV | Perguntas frequentes e respostas de prevenção de fraudes |
| `transacoes_suspeitas.csv` | CSV | Exemplos de padrões de transações que podem indicar fraude |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças e segurança digital, desde que sejam adequados ao contexto do SegurAI.

---

## Adaptações nos Dados

- Incluímos **campos de severidade** e **categoria do golpe** nos arquivos JSON para orientar o agente sobre a gravidade de cada situação.  
- Expandimos exemplos de transações suspeitas com valores, datas e tipos de operação, simulando cenários reais.  
- Todos os dados foram **anonimizados e mockados**, sem informações reais de clientes.

---

## Estratégia de Integração

### Como os dados são carregados?
- Os arquivos JSON/CSV são carregados no início de cada sessão e mantidos em memória para consulta rápida.  
- Dados estáticos (ex: boas práticas de segurança, FAQ) são incorporados ao **system prompt**, garantindo que o SegurAI tenha referências confiáveis durante a interação.  

### Como os dados são usados no prompt?
- O SegurAI consulta dinamicamente exemplos de transações suspeitas para alertar o usuário.  
- FAQs e boas práticas são incluídas no prompt como **contexto de referência**, permitindo respostas precisas e educativas.  
- Em casos de dúvida, o agente sugere links de verificação oficiais, mantendo a segurança do usuário.

---

## Exemplo de Contexto Montado

