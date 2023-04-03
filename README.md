# Iniciar o projeto Bussiness Inteligence

Frontend da aplicação: [Frontend](https://github.com/kaiofgl/data-analysis-frontend).


## Versões

pip >= 20.0.2 \
python >= 3.0

## Scripts disponíveis

Na raiz do diretório do projeto, execute:

#### `pip install -r requirements.txt`

O aplicativo irá instalar todos os pacotes presentes no `requirements.txt` e irá instalar em sua maquina para que seja possível executar o projeto.
#### `python3 app/__init__.py`

O aplicativo será executado na porta 3333.\
Abra [http://localhost:3333/health](http://localhost:3333/health) para confirmar se o servidor está funcional.

# Documentação de Rotas

## Verificar saúde do servidor
```http
  GET /health
```


## Arquivo
#### Upload de arquivo

```http
  POST /api/v1/file/get
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `FormData` | **Required**. Seu arquivo |

## Processamento

#### Pega estrutura de colunas do arquivo

```http
  POST /api/v1/processing/structure
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `filename`      | `string` | **Required**. Nome do arquivo sem extensão |

#### Processamento de coluna única

```http
  POST /api/v1/processing/single
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `filename`      | `string` | **Required**. Nome do arquivo sem extensão |
| `column`      | `string` | **Required**. Nome da coluna a ser processada |
| `normalize`      | `boolean` | **Required**. Retorno dos dados em porcentagem|

#### Processamento de coluna com agrupamento

```http
  POST /api/v1/processing/single
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `filename`      | `string` | **Required**. Nome do arquivo sem extensão |
| `first_column`      | `string` | **Required**. Nome da coluna a ser processada |
| `second_column`      | `string` | **Required**. Nome da coluna a ser agrupada|

