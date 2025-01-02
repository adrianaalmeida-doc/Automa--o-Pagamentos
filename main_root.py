from api import *
from log import log
import json
from datetime import datetime

def main():
    
    
    
# Configuração de diretórios
    pasta_destino = os.path.join(os.path.dirname(__file__), "documentos_baixados")
    os.makedirs(pasta_destino, exist_ok=True)
    log.info("Os documentos serão salvos em: {pasta_destino}")

    # Procurar pagamentos
    processos_encontrados = procurar_pagamentos()
    docs = processos_encontrados.get("docs", [])

    if not docs:
        log.error("Nenhum processo encontrado na lista de 'docs'.")
        return

    arquivos_baixados = []

    for doc in docs:
        process_id = doc.get("process_id")
        if not process_id:
            log.error("Processo não encontrado no documento.")
            continue

        log.info(f"ID do processo encontrado: {process_id}")
        documentos_processo = listar_documentos(process_id)

        ids_desejados = {
            "99122f90-c448-11ef-9ad2-53afbcd659f9",
            "b6141320-c6f9-11ef-9134-c9cc1df81ba6",
            "236c46d0-c449-11ef-9ad2-53afbcd659f9",
        }

        for documento in documentos_processo:
            id = documento.get("id")
            if id in ids_desejados:
                document_id = documento.get("document_id")
                file_name = documento.get("file_name", f"{id}.pdf")
                log.info(f"Baixando {id} com document ID: {document_id}")

                conteudo = baixar_documento_da_api(document_id, pasta_destino)
                if conteudo:
                    try:
                        caminho_arquivo = os.path.join(pasta_destino, file_name)
                        with open(caminho_arquivo, "wb") as arquivo:
                            arquivo.write(conteudo.read())
                        arquivos_baixados.append(caminho_arquivo)
                    except Exception as e:
                        log.error(f"Erro ao salvar o documento {id}: {e}")

    # Mesclar PDFs
    if arquivos_baixados:
        pdf_saida = os.path.join(pasta_destino, "PDF_Mesclado.pdf")
        if len(arquivos_baixados) > 1:
            log.info(f"Mesclando {len(arquivos_baixados)} PDFs: {arquivos_baixados}")
            arquivo_final = mesclar_pdfs(arquivos_baixados, pdf_saida)
            log.info(f"PDF mesclado salvo em: {arquivo_final}")
        else:
            log.info("Apenas um PDF encontrado. Não há necessidade de mesclagem.")
            arquivo_final = arquivos_baixados[0]

        if os.path.exists(pdf_saida):
            log.info(f"Arquivo PDF_Mesclado.pdf gerado em: {pdf_saida}")
        else:
            log.error("Arquivo PDF_Mesclado.pdf não foi gerado.")
            return
    else:
        log.warning("Nenhum arquivo PDF encontrado para mesclar.")
        return

    # Criar novo processo
    dados_processo = [
        {"id": "a709d0a0-5e35-11ee-a079-1f098f945990", "value": datetime.now().strftime("%y%m%d.%H%M%S.%f")[:20]},
        {"id": "a2621a80-5e35-11ee-a079-1f098f945990", "value": "65a57321778210009d3aff8f"},
        {"id": "8b3e8060-5e39-11ee-8459-ab06c4a21f7f", "value": "64a4060258f25700a09f830d"},
        {"id": "9f339a10-5e39-11ee-8459-ab06c4a21f7f", "value": str(datetime.now().date())},
    ]

    novo_processo_id = criar_processo(dados_processo, anexar_documento())
    if not novo_processo_id:
        log.error("Erro ao criar o novo processo.")
        return

    log.info(f"Processo criado com ID: {novo_processo_id}")
    
    id_task = consulta_tarefa(novo_processo_id)
    if not id_task:
        log.error("Erro ao consultar a tarefa associada ao processo.")
        return

    log.info(f"Tarefa associada ao processo: {id_task}")
    
        
    for processo in docs:
        item_data = {}
        log.info(f"Iniciando o preenchimento dos dados para o documento {processo.get('process_id')}")
        
        props = processo.get("props", [])
        if props:
           for prop in props:
               key = prop.get("key")
               value = prop.get("value")
               fluxo = processo.get("fluxo")
               if key and value and fluxo:
                    inserir_item_tabela(id_task, item_data )
                    log.info(f"Item {key} preenchido com sucesso.")
               else:
                    log.warning(f"Dados incompletos para preencher o item {key}.")
            
if __name__ == "__main__":
    main()