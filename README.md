# Esteganografia Binária com Tkinter

Projeto em Python com interface gráfica para ocultar qualquer arquivo (ex: imagens) dentro de um MP3.

## O que é Esteganografia?

Esteganografia é a arte de esconder informações dentro de outras.
Enquanto a criptografia embaralha a mensagem para que ninguém entenda, a esteganografia esconde a existência da mensagem. Ou seja, ninguém nem percebe que há algo escondido.


## Funcionalidades
- Oculta qualquer tipo de arquivo dentro de um áudio `.mp3`
- Permite extrair posteriormente o conteúdo escondido
- Interface simples usando Tkinter

## Exemplo simples:

Imagine que você quer mandar uma mensagem secreta para alguém, mas não quer que ninguém saiba que está enviando uma mensagem.

Você pode, por exemplo:

- Esconder um texto dentro de uma imagem;
- Esconder uma foto dentro de uma música;
- Esconder um arquivo dentro de outro arquivo.

## Como funciona na prática?

Uma imagem digital é feita de milhares de pixels, cada um com cores representadas por números (como 255, 128, 0). A esteganografia altera esses números de forma tão sutil que o olho humano nem percebe.
Por exemplo:

O pixel [255, 128, 0] pode virar [255, 128, 1] — e isso já carrega um pedaço da informação escondida, sem mudar a aparência da imagem.

## Resumo em uma frase:

Esteganografia é como esconder uma agulha no palheiro — mas fazendo o palheiro parecer completamente normal.


## Requisitos
- Python 3.x
- Interface Tkinter (já incluída no Python)

python main.py

<img width="1536" height="1024" alt="20250719_1645_Arte com Esteganografia_simple_compose_01k0j3bqpbezc8cee73ca8rstv" src="https://github.com/user-attachments/assets/11424354-481b-4548-a684-8a1e12fc2a9f" />
