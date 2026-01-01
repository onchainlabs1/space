# Como Testar Localmente

## Passo a Passo

### 1. Abrir o Terminal
Abra o Terminal no macOS e navegue até a pasta do projeto:
```bash
cd /Users/fabio/Desktop/space
```

### 2. Criar Ambiente Virtual
```bash
python3 -m venv venv
```

### 3. Ativar o Ambiente Virtual
```bash
source venv/bin/activate
```
Você deve ver `(venv)` no início da linha do terminal.

### 4. Instalar Dependências
```bash
pip install -r requirements.txt
```

Isso vai instalar:
- `pygame-ce` (biblioteca de jogos)
- `pygbag` (para build web)

**Saída esperada:**
```
Collecting pygame-ce>=2.5.0
Collecting pygbag>=0.7.0
...
Successfully installed pygame-ce-X.X.X pygbag-X.X.X ...
```

### 5. Executar o Jogo
```bash
python src/main.py
```

Ou use o script de conveniência:
```bash
./run_local.sh
```

### 6. Jogar!
- Uma janela do jogo deve abrir
- Use as setas ↑↓ ou W/S para navegar no menu
- SPACE ou ENTER para selecionar
- No jogo: SPACE ou ↑ para empurrar para cima
- ESC para voltar ao menu

## Comandos Rápidos (Copy-Paste)

```bash
# 1. Ir para a pasta
cd /Users/fabio/Desktop/space

# 2. Criar e ativar venv
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar o jogo
python src/main.py
```

## Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'pygame'"
- Certifique-se de que o venv está ativado (veja `(venv)` no terminal)
- Execute: `pip install -r requirements.txt`

### Erro: "python3: command not found"
- Instale Python 3.9+ do site oficial ou via Homebrew
- Verifique: `python3 --version`

### A janela não abre
- Verifique se há erros no terminal
- Tente: `python3 src/main.py` em vez de `python src/main.py`

### Controles não funcionam
- Clique na janela do jogo para dar foco
- Tente tanto SPACE quanto a seta ↑

## Próximos Passos

Depois de testar localmente, você pode:
- Construir para web: `python -m pygbag --template index.html src/main.py`
- Modificar constantes em `src/constants.py`
- Ajustar física ou gráficos

