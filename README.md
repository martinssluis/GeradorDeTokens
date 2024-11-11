# GeradorDeTokens <img src="https://cdn-icons-png.flaticon.com/512/8654/8654265.png" width="50" style="vertical-align: middle;">

Um mini projeto em Python, simples e funcional, ideal para integrar em outros projetos! O Gerador de Tokens cria senhas aleatórias ou tokens de verificação com segurança, contribuindo para substituir aquelas senhas fracas, como 123senha, com uma alternativa mais robusta e difícil de prever. Esse projeto pode ser usado como um módulo auxiliar em diversas aplicações que precisam de uma camada extra de segurança na criação de tokens e senhas.

### Por que Usar o Gerador de Tokens? 🔒
Um gerador de tokens seguro é essencial em qualquer aplicação que precise de proteção contra acessos não autorizados. Com essa implementação, você pode gerar senhas complexas ou tokens únicos de maneira rápida e prática, reduzindo a exposição a ataques e a vulnerabilidade do sistema.

## Ferramentas Utilizadas ⚙️
- *Biblioteca string*: usada para gerar letras, números e caracteres aleatórios. Ela não permite gerar todos de uma vez, então precisei usar o método para cada um dos tipos e juntar em uma grande lista.
- *Biblioteca random*: usei para pegar partes aleatórias da lista gerada anteriormente
- *''.join*: une todos esses caracteres em uma lista, e retira o espaço entre ele, por isso as aspas vazias.
- *k=*:  determina quantos caracteres vão ser definidos (length que é o parametro)

### Exemplo de Output
```
Escolha o tamanho do seu token: 14
6tbMVb2wmWT*P^
```

### Referências📚 

- [Stack OverFlow](https://pt.stackoverflow.com/questions/541504/como-gerar-chave-aleatória-em-python#:~:text=Gerando%20tokens%20de%20autenticação%20seguros,não%20para%20segurança%20ou%20criptografia.&text=A%20função%20token_hex%20retorna%20uma,o%20seu%20caso%20de%20uso.&text=Em%20python%20existe%20uma%20biblioteca%20que%20nos%20permite%20fazer%20isso%2C%20random.) - 
- [Vídeo do Otávio Miranda](https://youtu.be/KNfWZUMSB6g?si=k8W6Aywt6r_5dPq9) 