# Gerador de PDFs

Este projeto é um aplicativo GUI simples para converter arquivos Word (`.docx`) para PDF. Ele permite que os usuários selecionem uma pasta contendo arquivos `.docx` e converta todos esses arquivos em PDFs, salvando-os em uma pasta de saída.

## Funcionalidades

- Seleciona uma pasta contendo arquivos `.docx`
- Converte todos os arquivos `.docx` em PDFs
- Salva os PDFs em uma subpasta chamada "PDFs criados"

## Requisitos

- Python 3.6 ou superior

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/gerador-pdf.git
    cd gerador-pdf
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install python-docx reportlab
    ```

## Uso

1. Execute o script `geradorpdf.pyw`:
    ```sh
    python geradorpdf.pyw
    ```

2. Selecione a pasta contendo os arquivos `.docx` que você deseja converter.

3. Clique no botão "Gerar PDFs" para iniciar a conversão.

## Empacotamento com cx_Freeze

Se você deseja criar um executável para o seu script, siga estes passos:

1. Instale o `cx_Freeze`:
    ```sh
    pip install cx_Freeze
    ```

2. Execute o comando de build:
    ```sh
    python setup.py build
    ```

3. O executável será gerado na pasta `build`.

## Contribuição

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests. Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de mudar.


