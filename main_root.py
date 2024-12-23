from api import *
from log import log
import json
from datetime import datetime

def main():
    processos_encontrados = procurar_pagamentos()
    docs = processos_encontrados.get("docs", [])
    
    if not docs:
        log.error("Nenhum processo encontrado na lista de 'docs'.")
        return
     
    for doc in docs:  
        process_id = doc.get("process_id")
        if not process_id:
            log.error("ID do processo não encontrado no documento.")
            continue  
        
        print("ID do processo encontrado:", process_id)
    
    # Definir dados do processo
    dados_processo = [
        {"id": "a709d0a0-5e35-11ee-a079-1f098f945990", "value": "241219.134819.87"},
        {"id": "a2621a80-5e35-11ee-a079-1f098f945990", "value": "65a57321778210009d3aff8f"},
        {"id": "8b3e8060-5e39-11ee-8459-ab06c4a21f7f", "value": "64a4060258f25700a09f830d"},
        {"id": "9f339a10-5e39-11ee-8459-ab06c4a21f7f", "value": str(datetime.now().date())}
    ]
    
    # Criar novo processo
    novo_processo_id = criar_processo(dados_processo)
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
         
            
            for prop in props:
               key = prop.get("key")
               value = prop.get("value")
               
               if key == "3a1aff10-ae4c-11ef-b1fc-a5a6a8166bca" and "nome_do_cliente" not in item_data:
                item_data["nome_do_cliente"] = value
               elif key == "1440e290-b3d4-11ef-b692-b3bb4e8edf2e" and "codigo" not in item_data:
                   item_data["codigo"] = value
               elif key == "d38cbeb0-ae5e-11ef-b6f7-cd21e09e8d3f" and "pagar" not in item_data:
                   item_data["pagar"] = value
               elif key == "d8bcb7a0-ae5e-11ef-b6f7-cd21e09e8d3f" and "receber" not in item_data:
                   item_data["receber"] = value
               elif key == "db647f10-ae5e-11ef-b6f7-cd21e09e8d3f" and "saldo_doc" not in item_data:
                   item_data["saldo_doc"] = value
               elif key == "12ad9c00-ae7c-11ef-99fd-ad2c33fd4964" and "taxa_transferencia" not in item_data:
                   item_data["taxa_transferencia"] = value
            
               elif key == "1fa01fa0-ae7c-11ef-99fd-ad2c33fd4964" and "taxa_placa" not in item_data:
                   item_data["taxa_placa"] = value
               elif key == "d1246a10-ae86-11ef-8926-d1fd16c367c2" and "taxas_extras" not in item_data:
                   item_data["taxas_extras"] = value
               elif key == "bd933fb0-b3d3-11ef-b692-b3bb4e8edf2e" and "responsavel_atual" not in item_data:
                   item_data["responsavel_atual"] = value
               elif key == "e3c86ed0-b95f-11ef-9661-fff35e180cdb" and "taxas_detran" not in item_data:
                   item_data["taxas_detran"] = value
               elif key == "4eef7c40-ae4c-11ef-b1fc-a5a6a8166bca" and "cpf_cnpj" not in item_data:
                   item_data["cpf_cnpj"] = value
            

            if item_data:
                    try:
                        inserir_item_tabela(id_task, item_data)
                        log.info(f"Item inserido na tabela para a tarefa ID: {id_task} com dados: {item_data}")
                    except Exception as e:
                        log.error(f"Erro ao inserir item na tabela: {e}")
            else:
                    log.warning(f"Nenhum dado relevante encontrado no documento {processo.get('process_id')}.")

if __name__ == "__main__":
    main()