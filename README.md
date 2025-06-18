# cadastro-de-senha-com-hash-no-banco
Este projeto grava em um Banco de Dados os cadastros inseridos pelo usuário, registrando um email e uma senha, gravando a senha através de um método de Hash, obedecendo os padrões de Segurança da Informação. As etapas deste código foram feitas a partir de funções:
Cadastrar email e senha - pega o Email e Senha inseridos pelo usuário através de um Input e faz a validação com os padrões exigidos pelo sistema.
Criptografar senha - faz a criptografia da Senha inserida antes pelo usuário através do método Hash.
Gravar no banco - faz uma verificação para ver se o Email inserido pelo usuário já existe no Banco de Dados, caso exista, ele não registra o cadastro inserido e notifica o usuário. Caso não exista, ele grava o cadastro no Banco normalmente.
Validar senha - pede para o usuário digitar o email e a senha novamente, e essa senha passa pela função de Criptografar senha, depois é comparada com a senha Criptografada que está no Banco de Dados referente ao Email. Retornando para o usuário se o cadastro existe ou não no Banco de Dados, se a senha está correta ou incorreta.
Pesquisar hash - faz a busca e retorna para o usuário a senha Hash que está cadastrada no Banco de Dados, referente ao Email que ele digitar no Input.
