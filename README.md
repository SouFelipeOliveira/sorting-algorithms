# Trabalho de Estrutura de dados I - Algoritmos de Ordenação

Este projeto é uma aplicação web que utiliza a biblioteca Dash para visualizar o desempenho de vários algoritmos de ordenação. Os algoritmos incluídos são Bubble Sort, Gnome Sort, Heap Sort, Insertion Sort, Merge Sort, Quick Sort e Selection Sort.

## Funcionalidades
- Geração de arrays com os seguintes tamanhos para teste dos algoritmos de ordenação: 10, 50, 100, 200, 500, 800, 1000, 1500, 2000, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10000
- Visualização do desempenho dos algoritmos de ordenação em diferentes tamanhos de array.
- Possibilidade de deletar os arrays gerados.

## Como usar

1. Clone o repositório para a sua máquina local usando o Git Bash ou o terminal do seu IDE:

    ```
     git clone https://github.com/SouFelipeOliveira/sorting-algorithms
     ```
3. Navegue até a pasta app dentro do repositório clonado:
   
    ```
    cd sorting-algorithms/app
    ```
4. Crie um ambiente virtual e ative:
   
   Windows:
   ```
   python -m venv env
   ```
   
   ```
   env/Scripts/activate
   ```
   Linux:

   ```
   python3 -m venv env
   ```

   ```
   source env/bin/activate
   ```
   
6. Instale as dependências do projeto usando o comando:
   
   ```
   pip install -r requirements.txt
   ```

7. Execute o arquivo app.py para iniciar a aplicação:
   
    ```
    python app/myindex.py
    ```


## Dependências
- Dash
- Dash Bootstrap Components
- Pandas
- Numpy
- Plotly
