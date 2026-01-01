# Deploy no itch.io - Guia Completo

## ✅ O jogo está pronto para itch.io!

O jogo funciona perfeitamente em:
- 💻 **Computador** (Windows, Mac, Linux) - Teclado
- 📱 **Celular/Tablet** (iOS, Android) - Controles touch
- 🌐 **Navegadores modernos** (Chrome, Firefox, Safari, Edge)

## 📦 Como fazer o deploy

### 1. Preparar os arquivos

O jogo já está pronto! Você só precisa do conteúdo da pasta `web_build/`:

```
web_build/
  └── index.html  ← Este é o único arquivo necessário!
```

### 2. Criar conta no itch.io

1. Acesse: https://itch.io
2. Crie uma conta (gratuita)
3. Vá em "Create new project"

### 3. Configurar o projeto

**Informações básicas:**
- **Título:** Space Mission – Land Safely! / ŰRMISSZIÓ
- **URL:** `space-mission-land-safely` (ou o que preferir)
- **Categoria:** Games → Educational
- **Tags:** educational, space, lander, physics, kids, browser, html5

**Descrição sugerida:**
```
🚀 Educational Space Lander Game for Kids!

Land safely on different planets! Learn about gravity, physics, and fuel management.

Features:
• 9 progressive levels (Moon, Mars, Earth)
• Kid-friendly controls (one button + arrows)
• Educational gameplay
• Beautiful graphics and effects
• Works on mobile and desktop!

Controls:
• ↑/SPACE = Thrust up
• ←/→ = Move sideways
• Touch controls on mobile

Languages: English / Magyar (Hungarian)
```

### 4. Upload do jogo

1. Na seção **"Uploads"**, escolha:
   - **Kind:** HTML
   - **Embed options:** Fullscreen

2. Faça upload do arquivo `web_build/index.html`

   ⚠️ **IMPORTANTE:** 
   - O arquivo DEVE se chamar `index.html`
   - É o único arquivo necessário (tudo está embutido)

3. Marque como **"This file will be played in the browser"**

### 5. Configurações adicionais

**Embedding:**
- ✅ Enable embedding
- Width: `960`
- Height: `540`

**Screenshots:**
- Tire screenshots do menu, gameplay e tela de vitória
- Recomendado: 1280x720 ou maior

**Pricing:**
- Gratuito: "Download for free"
- Ou coloque um preço se quiser

### 6. Publicar

1. Clique em **"Save & view page"**
2. Teste o jogo no navegador
3. Se tudo estiver OK, clique em **"Public"**

## 🎮 Testando antes de publicar

### No computador:
1. Abra `web_build/index.html` no navegador
2. Teste com teclado (SPACE, setas)
3. Verifique se funciona em tela cheia

### No celular:
1. Coloque o arquivo em um servidor (ou use GitHub Pages)
2. Acesse pelo celular
3. Teste os controles touch
4. Verifique se o canvas escala corretamente

## 📱 Compatibilidade

✅ **Funciona em:**
- Chrome/Edge (desktop e mobile)
- Firefox (desktop e mobile)
- Safari (iOS e macOS)
- Navegadores modernos com suporte a HTML5 Canvas

⚠️ **Requisitos:**
- JavaScript habilitado
- Canvas API suportado
- Web Audio API (opcional, para sons)

## 🔧 Troubleshooting

**Problema:** O jogo não carrega
- ✅ Verifique se o arquivo se chama `index.html`
- ✅ Certifique-se que está marcado como "HTML" no itch.io

**Problema:** Controles não funcionam no mobile
- ✅ O jogo detecta automaticamente touch
- ✅ Botões aparecem automaticamente em dispositivos móveis

**Problema:** Canvas muito pequeno/grande
- ✅ O canvas escala automaticamente
- ✅ Mantém proporção 16:9 (960x540)

## 📊 Estatísticas do jogo

- **Tamanho:** ~60KB (um único arquivo HTML)
- **Resolução:** 960x540 (escala automaticamente)
- **Tempo de jogo:** 2-5 minutos por nível
- **Idiomas:** Inglês e Húngaro

## 🎯 Dicas para sucesso no itch.io

1. **Screenshots atrativos** - Mostre o menu, gameplay e vitória
2. **Descrição clara** - Explique que é educativo e para crianças
3. **Tags relevantes** - Use: educational, space, physics, kids
4. **Atualizações** - Mantenha o jogo atualizado
5. **Feedback** - Responda comentários dos jogadores

## 🚀 Alternativa: GitHub Pages (Gratuito)

Se quiser hospedar gratuitamente também:

1. Crie um repositório no GitHub
2. Faça upload de `web_build/index.html` (renomeie para `index.html` na raiz)
3. Vá em Settings → Pages
4. Escolha a branch `main`
5. Acesse: `https://seu-usuario.github.io/nome-repo`

---

**Pronto!** Seu jogo está 100% compatível com itch.io e funcionará perfeitamente em celular e computador! 🎉

