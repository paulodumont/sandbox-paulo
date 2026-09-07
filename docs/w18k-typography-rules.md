# W18K · Regra de tipografia

Decisão: **SF Pro com números tabulares** em todo o sistema da W18K (app interno). Vale para toda tela nova e para toda tela existente que for tocada.

## Famílias

| Uso | Fonte | Reserva (Windows / Android) |
|---|---|---|
| Títulos, valores em destaque | SF Pro Display | Inter |
| Corpo, tabelas, campos, botões | SF Pro Text | Inter |
| SKU, número de pedido, certificado | SF Mono | JetBrains Mono |

`font-variant-numeric: tabular-nums` ligado no `body`. Nunca desligar em tabela, KPI, preço, peso, data ou campo.

## Escala (um tamanho por nível)

| Nível | Onde | Fonte | Peso | Tamanho |
|---|---|---|---|---|
| T1 · Módulo | Dashboard, Products, Customers, Orders, Inventory, Reports | SF Pro Display | 600 | 26 px |
| T2 · Página interna | Detalhe de produto, cliente, pedido; cadastro e edição | SF Pro Display | 600 | 20 px |
| T3 · Caixa ou seção | Recent orders, Specifications, Identity | SF Pro Text | 600 | 13 px |
| T4 · Rótulo em caixa alta | Cabeçalho de tabela, rótulo de KPI e de ficha | SF Pro Text | 600 | 10 px · +0,08 em |
| V · Valor em destaque | KPI, preço, total | SF Pro Display | 600 | 22 px |
| B · Corpo | Texto, tabela, campo, botão | SF Pro Text | 400 / 600 | 13 px |
| S · Sublinha | Breadcrumb, data, meta abaixo do título | SF Pro Text | 400 | 12 px |
| C · Código | SKU, pedido, certificado | SF Mono | 400 | 11 px |

## Posição do título

- O bloco do título começa sempre a 24 px da borda do conteúdo e 20 px abaixo da barra superior.
- Altura fixa: 32 px para o título, 18 px para a sublinha. Igual em toda página.
- Avatar, preço e ações ficam à direita e nunca empurram o título.
- Nada acima do título além da barra superior.

## Regras de HTML já vigentes

- `color-scheme: light only`.
- Nunca azul como cor de fonte.
- Sem texto explicativo em título de caixa ou embaixo de campo.

Arquivo de tokens pronto: `docs/w18k-apple-fonts/w18k-typography.css`.
