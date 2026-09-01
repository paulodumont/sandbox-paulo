# sandbox-paulo

Servidor HTTP mínimo em Node.js, **sem nenhuma dependência externa** (não precisa de `npm install`).

## Requisitos

- Node.js 18 ou superior (`node --version` para conferir)

## Como rodar

```bash
git clone https://github.com/paulodumont/sandbox-paulo.git
cd sandbox-paulo
node server.js
```

O servidor sobe em `http://localhost:3000`. Para usar outra porta:

```bash
PORT=8080 node server.js
```

`npm start` também funciona, se preferir.

## Endpoints

| Rota      | Resposta                                              |
| --------- | ----------------------------------------------------- |
| `/`       | JSON com mensagem de boas-vindas e horário atual      |
| `/health` | JSON com `{"status":"ok"}` e uptime — use em monitoramento |
| outras    | JSON de erro 404                                      |

Teste rápido depois de subir:

```bash
curl http://localhost:3000/health
```

## Como implantar

### Opção 1 — Docker (recomendado)

```bash
docker build -t sandbox-paulo .
docker run -d -p 3000:3000 --restart unless-stopped --name sandbox-paulo sandbox-paulo
```

### Opção 2 — Direto num servidor com Node.js

Copie o repositório para o servidor e rode com um gerenciador de processos para manter o serviço no ar após quedas e reinicializações. Exemplo com [pm2](https://pm2.keymetrics.io/):

```bash
pm2 start server.js --name sandbox-paulo
pm2 save
```

### Opção 3 — Plataformas de nuvem (Render, Railway, Fly.io, Cloud Run…)

O projeto já está pronto para elas: todas detectam o `package.json` (comando `npm start`) ou o `Dockerfile` automaticamente, e injetam a variável `PORT`, que o servidor respeita.
