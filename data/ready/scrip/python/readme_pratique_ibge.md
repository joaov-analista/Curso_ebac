Coleta de Dados - Banco Central (Pix)

Endpoint utilizado:
https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/EstatisticasFraudesPix(DataBase='202501')

Descrição dos dados:
Este endpoint fornece estatísticas de fraudes no Pix, incluindo informações agregadas sobre volume de transações fraudulentas, valores e possíveis recortes por instituição ou categoria.

Formato:
JSON (convertido para DataFrame com pandas)

Período:
Janeiro de 2025

Estrutura dos Dados

O DataFrame bcb_tabela.csv contém informações sobre fraudes no Pix, incluindo:

- Quantidade de transações fraudulentas
- Valores envolvidos
- Possíveis dimensões como instituição, tipo de fraude ou categoria

Esses dados serão utilizados para análise exploratória e identificação de padrões de fraude.

Tratamentos realizados

- Padronização dos nomes das colunas (lowercase)
- Conversão de colunas numéricas
- Remoção de valores nulos
- Remoção de registros duplicados

Validações

- Conferência dos tipos de dados
- Verificação de valores ausentes
- Verificação de duplicidades


Importância

O web scraping é uma técnica essencial para coleta automatizada de dados disponíveis na internet. No ambiente corporativo, ele permite:

- Monitorar concorrentes (preços, produtos, serviços)
- Coletar dados públicos para análise de mercado
- Alimentar modelos de dados e dashboards
- Automatizar tarefas repetitivas de coleta

Isso gera ganho de eficiência, escalabilidade e melhor tomada de decisão baseada em dados.

Riscos legais e éticos

Apesar de poderoso, o uso de web scraping envolve cuidados importantes:

- Termos de uso: muitos sites proíbem scraping automatizado
- Direitos autorais: conteúdos podem ser protegidos (textos, imagens, bases de dados)
- LGPD (Lei Geral de Proteção de Dados): coleta de dados pessoais sem base legal pode gerar sanções


Medidas práticas para mitigação

- Respeitar regras do site
- Verificar os termos de uso e o arquivo robots.txt
- Evitar sobrecarga (usar limites de requisição)
- Priorizar dados públicos e anonimizados
- Evitar coletar dados pessoais sensíveis
- Utilizar APIs oficiais sempre que disponíveis

API vs Web Scraping (sem API)
Requisição via API

- Estruturada e documentada
- Dados organizados (JSON, XML)
- Mais estável e confiável
- Autorizada pelo provedor

Requisição sem API (scraping direto)
Extrai dados do HTML de páginas

- Mais suscetível a quebras (mudanças no site)
- Pode violar termos de uso
- Exige parsing (ex: BeautifulSoup)

Qual abordagem é mais adequada?

A abordagem via API é a mais recomendada, pois:
- É legalmente mais segura
- Oferece dados estruturados e consistentes
- Reduz risco de falhas e manutenção
- Geralmente possui documentação oficial

O scraping direto deve ser utilizado apenas quando não houver API disponível e sempre com atenção às questões legais e éticas.
