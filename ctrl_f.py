# funciona como ctrl F para diretórios, nesse caso ele pega a string 'jpeg' e troca por 'doc'
# não tenho ctz mas acho q ele n vai nos sub diretórios

import os

def substituir_string_em_arquivos(diretorio_base):
    print(f"Buscando arquivos .c e .h no diretório: {os.path.abspath(diretorio_base)}")
    encontrou_ocorrencia = False
    
    # Percorre todos os arquivos no diretório atual e subdiretórios
    for root, _, arquivos in os.walk(diretorio_base):
        for nome_arquivo in arquivos:
            # Verifica se o arquivo tem a extensão .c ou .h
            if nome_arquivo.endswith(('.c', '.h')):
                caminho_completo = os.path.join(root, nome_arquivo)
                conteudo = ""
                
                # Tenta ler o arquivo com UTF-8, e se falhar, com Latin-1
                try:
                    with open(caminho_completo, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                except UnicodeDecodeError:
                    try:
                        with open(caminho_completo, 'r', encoding='latin-1') as f:
                            conteudo = f.read()
                    except Exception as e:
                        print(f"Erro de codificação ao processar {caminho_completo}: {e}")
                        continue # Pula para o próximo arquivo

                # Se o conteúdo foi lido, faz as substituições
                if conteudo:
                    novo_conteudo = conteudo.replace('jpeg', 'doc')
                    novo_conteudo = novo_conteudo.replace('JPEG', 'DOC')
                    novo_conteudo = novo_conteudo.replace('Jpg', 'Doc')

                    # Escreve o conteúdo modificado de volta no arquivo, se houver alteração
                    if conteudo != novo_conteudo:
                        print(f"Substituindo em: {caminho_completo}")
                        with open(caminho_completo, 'w', encoding='utf-8') as f:
                            f.write(novo_conteudo)
                        encontrou_ocorrencia = True
                    else:
                        print(f"Nenhuma ocorrência encontrada em: {caminho_completo}")

    if not encontrou_ocorrencia:
        print("\nSubstituição concluída. Nenhuma ocorrência de 'jpeg' foi encontrada em nenhum dos arquivos .c e .h.")


# Substitui no diretório atual e em seus subdiretórios
substituir_string_em_arquivos('.')