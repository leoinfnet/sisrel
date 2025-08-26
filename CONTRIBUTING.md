# Guia de Contribuição – sisrel

Obrigado por considerar contribuir com este projeto!  
Antes de enviar mudanças, siga estas orientações para mantermos um repositório limpo e organizado.

---

## 📌 Commits

Este projeto usa o padrão **Conventional Commits**.  
Formato:

```
<tipo>(<escopo opcional>): <descrição curta no imperativo>
```

### Tipos aceitos
- feat: nova funcionalidade
- fix: correção de bug
- docs: mudanças na documentação (README, CHANGELOG, etc.)
- style: formatação sem alterar comportamento
- refactor: alteração interna sem mudança de comportamento externo
- perf: otimização de desempenho
- test: adição ou ajuste de testes
- build: mudanças em build/dependências
- ci: mudanças em integração contínua (GitHub Actions, etc.)
- chore: manutenção e tarefas auxiliares
- revert: reverte commit anterior

### Exemplos
```
feat(auth): adiciona login por token JWT
fix(api): corrige erro 500 no cadastro de usuário
docs(readme): adiciona seção de Roadmap
chore: adiciona .gitignore (template Python)
test: cria teste de sanidade em tests/test_sisrel_basico.py
```

---

## 📂 Estrutura recomendada de pastas
- `src/` → código principal
- `tests/` → testes automatizados
- `docs/` → documentação
- `.github/` → templates e metadados do GitHub

---

## 📝 Atualização do CHANGELOG
- Sempre que a mudança impactar usuários ou documentação, atualize o `CHANGELOG.md` na seção **[Unreleased]** com a categoria correspondente (Added, Changed, Fixed, Removed).

---

## 🗺️ Roadmap
Confira o [ROADMAP.md](ROADMAP.md) antes de propor mudanças para alinhar com o que está planejado.

---

## 🤝 Como contribuir
1. Faça fork do projeto ou crie uma branch (quando aplicável).
2. Adicione sua mudança com commits no padrão.
3. Atualize documentação e CHANGELOG se necessário.
4. Abra uma Issue ou Pull Request quando esse fluxo for habilitado.

Obrigado por ajudar a melhorar o **sisrel** 🚀
