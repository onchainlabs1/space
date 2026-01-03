# Como Atualizar o Jogo no itch.io

## Passo a Passo para Atualizar

### 1. Preparar os Arquivos
- O arquivo principal é `web_build/index.html`
- Este arquivo contém TODO o jogo (HTML + CSS + JavaScript)
- Não precisa de outros arquivos para funcionar

### 2. Acessar seu Projeto no itch.io
1. Vá para https://itch.io/dashboard
2. Encontre seu projeto "Space Mission" (ou o nome que você deu)
3. Clique em "Edit project"

### 3. Fazer Upload do Novo Arquivo
1. Na seção **"Uploads"** ou **"Files"**
2. Clique em **"Upload new file"** ou **"Replace file"**
3. Selecione o arquivo `web_build/index.html`
4. Aguarde o upload completar

### 4. Configurar o Arquivo Principal
1. Na seção **"Embed options"** ou **"Project settings"**
2. Certifique-se de que o **"Main file"** ou **"Index file"** está configurado como `index.html`
3. Se não estiver, selecione `index.html` como arquivo principal

### 5. Salvar e Publicar
1. Role até o final da página
2. Clique em **"Save"** ou **"Save & view page"**
3. Se estiver em modo Draft, você pode mudar para **"Public"** quando estiver pronto

## Novidades desta Versão

### 🎮 Melhorias de Gameplay
- **Progressão Gradual de Elementos**: Começa com poucos obstáculos e vai aumentando gradualmente
  - Moon 1: 2 asteroides (sem alienígenas)
  - Moon 2-3: Mistura de asteroides e alienígenas (10-20%)
  - Mars 1-3: Mais alienígenas (25-35%)
  - Earth 1-3: Muitos alienígenas (30-40%)
- **Naves Alienígenas**: Naves alienígenas roxas que perseguem a nave (velocidade aumenta gradualmente)
- **Pouso Facilitado**: Velocidade segura aumentada nos níveis difíceis (Mars 2-3, Earth 2-3)
- **Tela Final Especial**: Tela de conclusão especial quando completa TODAS as 9 fases na sequência
- **Escudo Melhorado**: Escudo protege contra asteroides, alienígenas e terreno com período de invulnerabilidade
- **Câmera Lenta Aprimorada**: Efeito visual mais forte e claro (reduz gravidade em 70%)
- **Controles de Menu Visíveis**: Botões de navegação sempre visíveis nos menus (↑↓✓✕) para facilitar navegação

### 🔊 Sistema de Áudio
- **Apenas Efeitos Sonoros**: Música removida, apenas efeitos sonoros durante o jogo
- **Controle de Volume**: Use a tecla **M** para mutar/desmutar efeitos sonoros
- Efeitos sonoros: thrust, crash, success, power-up, click

## Testes Recomendados

Antes de publicar, teste:
1. ✅ Efeitos sonoros funcionam corretamente
2. ✅ Tecla M muta/desmuta corretamente
3. ✅ Controles de menu visíveis funcionam (botões ↑↓✓✕)
4. ✅ Progressão gradual: Moon 1 tem apenas asteroides, Moon 2-3 têm alguns alienígenas
5. ✅ Naves alienígenas aparecem gradualmente conforme o jogo progride
6. ✅ Pouso está mais fácil nos níveis difíceis
7. ✅ Tela final especial aparece ao completar todas as fases (atalho F)

## Compatibilidade

- ✅ Funciona no itch.io (Web Audio API é suportado para efeitos sonoros)
- ✅ Funciona em desktop (Windows, Mac, Linux)
- ✅ Funciona em mobile (iOS, Android)
- ✅ Funciona offline (tudo está no index.html)

## Pronto!

Após fazer o upload e salvar, seu jogo estará atualizado com todas as melhorias! 🚀

### Resumo das Mudanças
- ✅ Música removida (apenas efeitos sonoros)
- ✅ **Progressão gradual de elementos** (começa simples, vai aumentando)
- ✅ **Controles de menu visíveis** (botões ↑↓✓✕ sempre visíveis)
- ✅ Naves alienígenas aparecem gradualmente (0% → 40%)
- ✅ Pouso facilitado nos níveis difíceis
- ✅ Tela final especial
- ✅ Escudo melhorado
- ✅ Câmera lenta aprimorada

