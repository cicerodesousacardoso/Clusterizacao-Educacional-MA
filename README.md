# 📊 Clusterização Hierárquica - Dados Educacionais do Maranhão

![Banner do Projeto](output/Flag_map_of_Maranhao.png)

## 📌 Sobre o Projeto
Análise completa do rendimento escolar por tipo de escola no Maranhão utilizando:

- **Clusterização hierárquica** (método Ward)
- **Dashboard interativo** com filtros por ano e fase escolar
- **Processamento automatizado** de dados do QEDU
- **Visualização** através de dendrogramas comparativos

## 🛠️ Tecnologias Utilizadas

### 🔍 Backend & Análise
```python
pandas      # Manipulação de dados
scipy       # Clusterização hierárquica
sklearn     # Pré-processamento
matplotlib  # Geração de dendrogramas
```

### 💻 Frontend & Visualização
```html
HTML5/CSS3  # Estrutura responsiva
JavaScript  # Carregamento dinâmico de dados
Font Awesome # Ícones modernos
```

## 📂 Estrutura do Projeto
```
.
├── dados/
│   ├── Taxa_de_Rendimento/
│   │   ├── json/               # Dados processados (JSON)
│   │   └── arquivos_originais/ # Dados brutos (XLSX)
│
├── output/                    # Resultados visuais
│   ├── Anos_Iniciais.png      # Dendrograma 1
│   ├── Anos_Finais.png        # Dendrograma 2
│   └── Total.png              # Visão consolidada
│
├── src/
│   ├── main.py                # Análise principal
│   └── converter_xlsx_para_json.py # Conversor de dados
│
├── index.html                 # Dashboard web
├── README.md                  # Documentação
└── .hintrc                    # Validação de código
```

## 🚀 Como Executar

1. **Pré-requisitos**:
```bash
Python 3.8+
pip install pandas scipy scikit-learn matplotlib
```

2. **Processamento dos dados**:
```bash
python src/converter_xlsx_para_json.py
python src/main.py
```

3. **Visualização**:
```bash
python -m http.server 8000
```
Acesse: http://localhost:8000

## 📊 Principais Funcionalidades

- Filtragem por fase escolar (Anos Iniciais/Finais)
- Seleção de ano (2018-2023)
- Visualização de dendrogramas interativos
- Tabela dinâmica com indicadores educacionais

## 👨💻 Autor
[Cícero Gabriel de Sousa Cardoso](https://github.com/cicerodesousacardoso)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cicero-gabriel-de-sousa-cardoso-3a86b02b0/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cicerodesousacardoso)

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
