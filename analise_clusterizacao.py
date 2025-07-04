import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Caminhos base
base_path = "C:/Users/Cicero/Documents/Dados/Taxa de Rendimento"
pastas = ["Anos Iniciais", "Anos Finais"]
output_dir = "C:/Users/Cicero/Documents/Dados/Codigo/Gerando Dendrograma"
os.makedirs(output_dir, exist_ok=True)

# Função para carregar e preparar os dados
def carregar_e_preparar_dados(pasta):
    dados = []
    caminho_pasta = os.path.join(base_path, pasta)

    if not os.path.exists(caminho_pasta):
        print(f"❌ Pasta não encontrada: {caminho_pasta}")
        return pd.DataFrame()

    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".xlsx"):
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            try:
                df = pd.read_excel(caminho_arquivo, sheet_name="estado")
                df["dependencia_id"] = pd.to_numeric(df["dependencia_id"], errors="coerce").fillna(-1).astype(int)
                df["localizacao_id"] = pd.to_numeric(df["localizacao_id"], errors="coerce").fillna(-1).astype(int)
                df = df[df["localizacao_id"] == 0]  # Localização urbana
                ano = int(arquivo.split(".")[0])
                df["ano"] = ano
                dados.append(df)
                print(f"📥 Lido: {arquivo} da pasta {pasta}")
            except Exception as e:
                print(f"⚠️ Erro ao ler {arquivo}: {e}")

    if not dados:
        return pd.DataFrame()

    df_conc = pd.concat(dados, ignore_index=True)
    df_conc['matriculas'] = pd.to_numeric(df_conc['matriculas'], errors='coerce').fillna(0).astype(int)
    for col in ['aprovados', 'reprovados', 'abandonos']:
        df_conc[col] = df_conc[col].astype(str).str.replace(',', '.').astype(float)

    df_filtrado = df_conc[(df_conc['dependencia_id'] != 0) & (df_conc['dependencia_id'] != 5)]
    return df_filtrado

# Função para gerar dendrograma
def criar_dendrograma(df_entrada, titulo):
    if df_entrada.empty:
        print(f"⚠️ Dados vazios para '{titulo}'")
        return

    tipos = {
        1: "Federal",
        2: "Estadual",
        3: "Municipal",
        4: "Privada",
    }

    df_entrada.index = df_entrada.index.map(tipos)
    print(f"\n📊 Dados para {titulo}:")
    print(df_entrada)

    scaler = StandardScaler()
    dados_norm = scaler.fit_transform(df_entrada)

    Z = linkage(dados_norm, method='ward')

    plt.figure(figsize=(10, 6))
    dendrogram(Z, labels=df_entrada.index.tolist(), leaf_rotation=45, leaf_font_size=10)
    plt.title(f"Clusterização por Tipo de Escola - Maranhão ({titulo})")
    plt.xlabel("Tipo de Escola")
    plt.ylabel("Distância Euclidiana")
    plt.tight_layout()

    nome_arquivo = os.path.join(output_dir, f"{titulo.replace(' ', '_')}.png")
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    print(f"✅ Dendrograma salvo: {nome_arquivo}")
    plt.show()

# --- FLUXO PRINCIPAL ---

print("🔹 Processando Anos Iniciais...")
df_iniciais = carregar_e_preparar_dados("Anos Iniciais")
if not df_iniciais.empty:
    df_iniciais_soma = df_iniciais.groupby('dependencia_id')[['matriculas', 'aprovados', 'reprovados', 'abandonos']].sum()
    df_iniciais_soma['matriculas'] = df_iniciais_soma['matriculas'].astype(int)
    criar_dendrograma(df_iniciais_soma, "Anos Iniciais")

print("\n🔹 Processando Anos Finais...")
df_finais = carregar_e_preparar_dados("Anos Finais")
if not df_finais.empty:
    df_finais_soma = df_finais.groupby('dependencia_id')[['matriculas', 'aprovados', 'reprovados', 'abandonos']].sum()
    df_finais_soma['matriculas'] = df_finais_soma['matriculas'].astype(int)
    criar_dendrograma(df_finais_soma, "Anos Finais")

print("\n🔹 Processando Total...")
df_total = pd.concat([df_iniciais, df_finais], ignore_index=True)
if not df_total.empty:
    df_total_soma = df_total.groupby('dependencia_id')[['matriculas', 'aprovados', 'reprovados', 'abandonos']].sum()
    df_total_soma['matriculas'] = df_total_soma['matriculas'].astype(int)
    criar_dendrograma(df_total_soma, "Total")

print("\n✅ Processamento concluído.")
