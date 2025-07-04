import os
import pandas as pd
import json

# Caminhos base
base_path = r"C:\Users\Cicero\Documents\Dados\Codigo\Clusterizacao-Educacional-MA\dados\Taxa de Rendimento"
fases = ["Anos Iniciais", "Anos Finais"]

output_dir = os.path.join(base_path, "json")
os.makedirs(output_dir, exist_ok=True)

for fase in fases:
    fase_path = os.path.join(base_path, fase)
    arquivos = [f for f in os.listdir(fase_path) if f.endswith(".xlsx")]

    dados_por_ano = {}

    for arquivo in arquivos:
        ano = ''.join(filter(str.isdigit, arquivo))  # extrai "2018", "2019", etc.
        caminho_arquivo = os.path.join(fase_path, arquivo)

        try:
            df = pd.read_excel(caminho_arquivo, sheet_name="estado")
        except Exception as e:
            print(f"Erro ao ler {arquivo}: {e}")
            continue

        df = df.dropna(how="all")  # Remove linhas totalmente vazias

        # Converte para dicionário
        dados_por_ano[ano] = df.to_dict(orient="records")

    # Salva como JSON único por fase
    output_file = os.path.join(output_dir, f"{fase.replace(' ', '_')}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dados_por_ano, f, ensure_ascii=False, indent=2)

    print(f"✔ Arquivo salvo: {output_file}")
