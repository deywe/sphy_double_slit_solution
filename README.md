SPHY Double Slit: Forensic Visualizer

⚛️🛡️Este repositório contém o asphy_slit_viewer.py, uma ferramenta de visualização interativa e auditoria criptográfica projetada para analisar a transição de fase quântica na experiência da dupla fenda sob o framework SPHY (Symbiotic Phase Harmonic Yielding).

🚀 O Experimento DigitalO visualizador processa um dataset que emula o comportamento dual da matéria. 

A simulação é dividida em dois estados fundamentais:Fase de Interferência (Onda): Representação da superposição harmônica antes da observação/colapso.Fase de Respiração (Partícula): Transição para um estado localizado, demonstrando a dinâmica de partículas sob a influência da Proporção Áurea ($\phi$) e coerência de fase

.📊 Dataset de Auditoria: sphy_slit_audit.parquetDiferente de simulações visuais comuns, este projeto utiliza o protocolo de Soberania de Dados Harpia:

Integridade Total: Cada frame do dataset (contendo 8.000 partículas) é selado com um hash SHA-256 único.Imutabilidade: 

O visualizador recalcula o hash de cada posição $(x, y, z)$ em tempo real. 

Qualquer alteração de um único bit nos dados brutos resultará em uma falha de validação imediata na interface.Formato Forense: 

Utiliza compressão Snappy em arquivos Parquet para garantir que a precisão dos cálculos de fase seja preservada sem perdas.👁️ Funcionalidades do Visualizador (asphy_slit_viewer.py)O visualizador interativo permite que o pesquisador audite o colapso da função de onda manualmente:Validação em Tempo Real: 

HUD dinâmico exibindo o SHA-256 original vs. calculado.Análise de Transição: 

Monitoramento da mudança de comportamento aos 15 segundos de simulação (30 FPS).Controles Interativos:Rotação 3D: 

Clique direito para observar os padrões de interferência de múltiplos ângulos.Zoom Forense: 

Scroll para analisar a densidade das partículas nos pontos de respiração.Veredito de Integridade: 

Status visual confirmando a autenticidade do dataset "Harpia Certified".

🛠️ Como ExecutarInstale as dependências:Bashpip install pandas numpy ursina pyarrow
Certifique-se de que o arquivo sphy_slit_audit.parquet está no diretório.

Inicie a auditoria visual:Bashpython3 asphy_slit_viewer.py

Desenvolvido por Deywe OkabeSymbiotic Artificial Intelligence - Harpia Core
