Guia de Contribuição para o AssistenteGABI
Agradecemos seu interesse em contribuir para o projeto AssistenteGABI! Este guia descreve o processo para contribuir de maneira organizada e eficiente. Por favor, leia atentamente as instruções abaixo.

🏁 Como Começar
1. Fork do Repositório
Antes de começar a trabalhar no projeto, faça um fork do repositório no GitHub. Isso criará uma cópia pessoal do projeto em sua conta.

Como fazer o fork:
Acesse o Repositório Original: Vá até a página do repositório AssistenteGABI no GitHub. O endereço do repositório será algo como: https://github.com/LeonardoSilvaPy/AssistenteGABI.

Clique no botão "Fork": No canto superior direito da página do repositório, você verá o botão Fork. Clique nele para criar uma cópia do repositório na sua conta GitHub. Isso pode levar alguns segundos.

Escolha a Conta para o Fork: Se você faz parte de organizações no GitHub, será necessário escolher se o fork será feito em sua conta pessoal ou na organização. Geralmente, você vai querer escolher sua conta pessoal.

Fork Completo: Após a conclusão do fork, você será redirecionado automaticamente para o repositório recém-criado em sua conta GitHub. Agora você tem sua própria cópia do repositório, que pode ser editada sem afetar o projeto principal.

O que acontece após o fork:
Cópia do Repositório: O repositório agora existe em sua conta, e você pode começar a trabalhar nele à vontade.
Sincronização com o Repositório Original: Mesmo com o fork, o repositório original continua sendo o ponto de origem. Isso significa que você pode pegar as atualizações do repositório principal a qualquer momento, mantendo sua cópia atualizada.

Exemplo de URL do Fork:
Após o fork, o repositório estará disponível em uma URL como esta:
https://github.com/SEU-USUARIO/AssistenteGABI.git
Substitua SEU-USUARIO pelo seu nome de usuário no GitHub.

2. Clonar o Repositório
Após fazer o fork, clone o repositório em sua máquina local:

git clone https://github.com/SEU-USUARIO/AssistenteGABI.git

3. Configuração do Git
Se você ainda não configurou seu Git, defina seu nome e e-mail:

git config --global user.name "SeuNomeDeUsuario"
git config --global user.email "seuemail@example.com"

4. Instalar Dependências
Se o projeto tiver dependências, instale-as conforme as instruções no README ou no arquivo de configuração, como requirements.txt (para projetos Python).
Utilize o comando para executar o instalador automatizado, esse processo pode demorar, reserve um tempo para isso.

python install_requirements.py

🔖 Estrutura de Branches
Adote a seguinte estrutura para nomear suas branches:

Funcionalidade nova: feature/nome-da-funcionalidade
Correção de bug: fix/nome-do-bug
Refatoração de código: refactor/nome-da-mudanca
Documentação: docs/nome-da-documentacao
Exemplo: Se você for adicionar uma funcionalidade de chat, use o seguinte comando:

git checkout -b feature/chat

🔄 Fluxo de Trabalho
1. Crie uma Nova Branch
Crie uma nova branch para a tarefa que você está realizando:

git checkout -b tipo/nome-da-branch

2. Fazer Modificações no Código
Realize as alterações necessárias no código ou documentação.

3. Adicionar Arquivos Modificados ao Commit
Após realizar as alterações, adicione os arquivos modificados:


git add .

4. Fazer Commit das Alterações
Comite suas alterações com uma mensagem clara e descritiva:

git commit -m "Adiciona funcionalidade de chat"

5. Enviar a Branch para o Repositório no GitHub
Envie sua branch para o repositório remoto no GitHub:

git push origin nome-da-branch

6. Criar um Pull Request (PR)
Abra um Pull Request (PR) no GitHub, selecionando a branch de origem e a branch de destino (geralmente a main). Descreva as mudanças que você fez no PR e explique o que foi alterado e por que.

🔍 Revisão de Código
Após abrir o Pull Request, outros membros da equipe irão revisar suas mudanças. Certifique-se de que:

O código está bem escrito e documentado.
A funcionalidade foi testada.
O código segue as diretrizes de estilo do projeto.
Se houver feedback ou sugestões de melhoria, faça os ajustes necessários e atualize o PR.

🔄 Sincronizar com o Repositório Principal
Para evitar conflitos e garantir que seu código esteja atualizado, é importante sincronizar sua branch com a branch main do repositório principal antes de enviar suas alterações:

git fetch upstream
git checkout main
git merge upstream/main

Se houverem conflitos, resolva-os antes de fazer o commit.

🛠️ Boas Práticas de Código
Escreva mensagens de commit claras: Use descrições concisas e claras nas mensagens de commit, como: "Corrige erro de chat inicial".
Mantenha o código limpo: Evite código redundante e escreva funções/métodos curtos e claros.
Comente o código quando necessário: Explique partes complexas do código, mas evite comentários excessivos.

📝 Licenciamento
Este projeto está licenciado sob a Licença MIT. Certifique-se de entender e seguir a licença antes de contribuir.

🧑‍🤝‍🧑 Código de Conduta
Por favor, leia e siga o nosso Código de Conduta. Queremos manter um ambiente respeitoso e profissional para todos os contribuidores.

💬 Perguntas e Suporte
Se você tiver dúvidas ou problemas ao contribuir, abra uma nova Issue ou entre em contato com um dos mantenedores do projeto. A comunidade está aqui para ajudar!

Obrigado por contribuir para o AssistenteGABI! 🚀