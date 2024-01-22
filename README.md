# Sistemas distribuídos - chat gRPC

## Rafaella Nunes - 20111225

## Como rodar:
##### Clone o repositório para sua máquina
##### Instale as dependências utilizando o comando: 
`pip install grpcio grpcio-tools`
##### Compile o arquivo .proto para gerar os arquivos em python utilizando comando:
`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. chat.proto`
##### Abra terminais separados, em um terminal execute o servidor e nos outros o cliente.
##### Ao executar o cliente, será solicitado que você insira um nome de usuário. Após isso, você poderá enviar mensagens para os outros clientes.
