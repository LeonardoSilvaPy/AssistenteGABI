# Guia de Contribuição para AssistenteGABI

Obrigado por seu interesse em contribuir para o projeto **AssistenteGABI**! Este guia descreve o processo para contribuir de maneira organizada e eficiente. Por favor, leia atentamente e siga as instruções abaixo.

## Como Começar

### 1. **Fork do Repositório**
   Antes de começar a trabalhar no projeto, faça um **fork** do repositório no GitHub. Isso cria uma cópia pessoal do projeto em sua conta.

### 2. **Clonar o Repositório**
   Após fazer o fork, clone o repositório em sua máquina local:
   ```bash
   git clone https://github.com/SEU-USUARIO/AssistenteGABI.git

3. Configuração do Git
Se você ainda não configurou seu Git, defina seu nome e e-mail:

git config --global user.name "SeuNomeDeUsuario"
git config --global user.email "seuemail@example.com"

4. Instalar Dependências
Se o projeto tiver dependências, instale-as conforme as instruções no README ou em um arquivo de configuração como requirements.txt (para Python):

pip install -r requirements.txt

Estrutura de Branches:

Adote a seguinte estrutura para nomear suas branches:
Funcionalidade nova: feature/nome-da-funcionalidade
Correção de bug: fix/nome-do-bug
Refatoração de código: refactor/nome-da-mudanca
Documentação: docs/nome-da-documentacao
Exemplo:
Se você for adicionar uma funcionalidade de chat:

git checkout -b feature/chat

Fluxo de Trabalho
Crie uma nova branch para a tarefa que você está fazendo:

git checkout -b tipo/nome-da-branch

Fazer Modificações no Código:
Realize as alterações necessárias no código ou documentação.
Adicionar Arquivos Modificados ao Commit:
Após fazer as alterações, adicione os arquivos modificados:

git add .

Fazer Commit das Alterações:
Comite suas alterações com uma mensagem clara e descritiva:

git commit -m "Adiciona funcionalidade de chat"

Envie sua branch para o repositório no GitHub:

git push origin nome-da-branch

Criar um Pull Request:

Abra um Pull Request (PR) no GitHub. Selecione a branch de origem e a branch de destino (geralmente main).
Descreva as mudanças que você fez no PR. Explique o que foi alterado e por que.
Revisão de Código
Após abrir o Pull Request, outros membros da equipe irão revisar suas mudanças. Certifique-se de que:

O código está bem escrito e documentado.
A funcionalidade foi testada.
O código segue as diretrizes de estilo do projeto.
Se houver algum feedback ou sugestões de melhoria, faça os ajustes necessários e atualize o PR.

Sincronizar com o Repositório Principal
Para evitar conflitos e garantir que seu código esteja atualizado, é importante sincronizar sua branch com a branch main do repositório principal antes de enviar suas alterações:

git fetch upstream
git checkout main
git merge upstream/main
Se houverem conflitos, resolva-os antes de fazer o commit.

Boas Práticas de Código
Escreva mensagens de commit claras: Use descrições claras e concisas nas mensagens de commit. Por exemplo: "Corrige erro de chat inicial".
Mantenha o código limpo: Evite código redundante e escreva funções/métodos curtos e claros.
Comente o código quando necessário: Explique o que partes complexas do código estão fazendo, mas evite comentários excessivos.

Licenciamento
Este projeto está licenciado sob a Licença MIT. Certifique-se de entender e seguir a licença antes de contribuir.

Código de Conduta
Por favor, leia e siga o nosso Código de Conduta. Queremos manter um ambiente respeitoso e profissional para todos os contribuidores.

Perguntas e Suporte
Se você tiver dúvidas ou problemas ao contribuir, abra uma nova Issue ou entre em contato com um dos mantenedores do projeto. A comunidade está aqui para ajudar!

Obrigado por contribuir para o AssistenteGABI!
