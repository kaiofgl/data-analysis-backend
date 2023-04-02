
## Documentação de Rotas

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

