import streamlit as st
from contextlib import contextmanager
from database.session import get_db
from controllers.caixa_controller import create_caixa, get_caixas
from controllers.operadora_credito_controller import create_operadora_credito, get_operadoras_credito
from controllers.op_credito_controller import create_op_credito, get_op_creditos
from controllers.movimentos_controller import create_movimento, get_movimentos
from datetime import datetime

@contextmanager
def get_db_context():
  db = next(get_db())
  try:
      yield db
  finally:
      db.close()

def main():
  st.sidebar.title("Menu")
  menu = st.sidebar.selectbox("Selecione a Entidade", ["Caixa", "Operadora_Credito", "Op_Credito", "Movimentos"])
  crud_operation = st.sidebar.selectbox("Selecione a Operação", ["Create", "Update", "Delete", "List"])

  if menu == "Caixa":
      handle_caixa_operations(crud_operation)
  elif menu == "Operadora_Credito":
      handle_operadora_credito_operations(crud_operation)
  elif menu == "Op_Credito":
      handle_op_credito_operations(crud_operation)
  elif menu == "Movimentos":
      handle_movimentos_operations(crud_operation)

def handle_caixa_operations(crud_operation):
  if crud_operation == "Create":
      st.subheader("Create Caixa")
      caixa_aberto = st.text_input("Caixa Aberto")
      data = st.date_input("Data", value=datetime.now())
      saldo_inicial = st.text_input("Saldo Inicial", "0,00")
      valor_cartao_credito = st.text_input("Valor Cartão de Crédito", "0,00")
      valor_cartao_debito = st.text_input("Valor Cartão de Débito", "0,00")
      valor_ifood = st.text_input("Valor de Ifood", "0,00")
      valor_dinheiro = st.text_input("Valor em Dinheiro", "0,00")
      valor_fiado = st.text_input("Valor Fiado", "0,00")
      saidas_caixa = st.text_input("Saídas de Caixa", "0,00")
      valor_acrescimo = st.text_input("Valor de Acréscimo", "0,00")

      if st.button("Create Caixa"):
          with get_db_context() as db:
              create_caixa(db, {
                  "caixa_aberto": caixa_aberto,
                  "data": data,
                  "saldo_inicial": float(saldo_inicial.replace(",", ".")),
                  "valor_cartao_credito": float(valor_cartao_credito.replace(",", ".")),
                  "valor_cartao_debito": float(valor_cartao_debito.replace(",", ".")),
                  "valor_ifood": float(valor_ifood.replace(",", ".")),
                  "valor_dinheiro": float(valor_dinheiro.replace(",", ".")),
                  "valor_fiado": float(valor_fiado.replace(",", ".")),
                  "saidas_caixa": float(saidas_caixa.replace(",", ".")),
                  "valor_acrescimo": float(valor_acrescimo.replace(",", "."))
              })
          st.success("Caixa criado com sucesso!")

  elif crud_operation == "List":
      st.subheader("Lista de Caixas")
      with get_db_context() as db:
          caixas = get_caixas(db)
          if caixas:
              caixa_data = [{"Caixa Aberto": c.caixa_aberto, "Data": c.data, "Saldo Inicial": c.saldo_inicial} for c in caixas]
              st.write(caixa_data)
          else:
              st.write("Nenhum caixa encontrado.")

def handle_operadora_credito_operations(crud_operation):
  if crud_operation == "Create":
      st.subheader("Create Operadora de Crédito")
      nome_operadora = st.text_input("Nome da Operadora")
      
      if st.button("Create Operadora"):
          with get_db_context() as db:
              create_operadora_credito(db, nome_operadora)
          st.success("Operadora de Crédito criada com sucesso!")

  elif crud_operation == "List":
      st.subheader("Lista de Operadoras de Crédito")
      with get_db_context() as db:
          operadoras = get_operadoras_credito(db)
          if operadoras:
              operadora_data = [{"Nome da Operadora": o.nome_operadora} for o in operadoras]
              st.write(operadora_data)
          else:
              st.write("Nenhuma operadora encontrada.")

def handle_op_credito_operations(crud_operation):
  if crud_operation == "Create":
      st.subheader("Create Op Crédito")
      
      # Obter a lista de caixas e operadoras de crédito
      with get_db_context() as db:
          caixas = get_caixas(db)
          operadoras = get_operadoras_credito(db)
      
      # Criar listas de opções para os comboboxes
      caixa_options = [(c.id, c.caixa_aberto) for c in caixas]
      operadora_options = [(o.id, o.nome_operadora) for o in operadoras]
      
      # Usar comboboxes para selecionar caixa e operadora
      id_caixa = st.selectbox("Caixa", options=caixa_options, format_func=lambda x: x[1])
      id_operadora = st.selectbox("Operadora de Crédito", options=operadora_options, format_func=lambda x: x[1])
      
      data_extrato = st.date_input("Data do Extrato", value=datetime.now())
      total_credito = st.text_input("Total Crédito", "0,00")
      total_debito = st.text_input("Total Débito", "0,00")
      valor_pix = st.text_input("Valor de Pix", "0,00")
      valor_voucher = st.text_input("Valor de Voucher", "0,00")

      if st.button("Create Op Crédito"):
          with get_db_context() as db:
              create_op_credito(db, {
                  "id_caixa": id_caixa[0],  # Usar o ID selecionado
                  "id_operadora": id_operadora[0],  # Usar o ID selecionado
                  "data_extrato": data_extrato,
                  "total_credito": float(total_credito.replace(",", ".")),
                  "total_debito": float(total_debito.replace(",", ".")),
                  "valor_pix": float(valor_pix.replace(",", ".")),
                  "valor_voucher": float(valor_voucher.replace(",", "."))
              })
          st.success("Operação de Crédito criada com sucesso!")

  elif crud_operation == "List":
      st.subheader("Lista de Operações de Crédito")
      with get_db_context() as db:
          op_creditos = get_op_creditos(db)
          if op_creditos:
              op_credito_data = [{"ID Caixa": o.id_caixa, "Data Extrato": o.data_extrato, "Total Crédito": o.total_credito} for o in op_creditos]
              st.write(op_credito_data)
          else:
              st.write("Nenhuma operação de crédito encontrada.")

def handle_movimentos_operations(crud_operation):
  if crud_operation == "Create":
      st.subheader("Create Movimento")
      id_caixa = st.number_input("ID do Caixa", min_value=1, step=1)
      tipo_movimento = st.text_input("Tipo de Movimento")
      valor = st.text_input("Valor", "0,00")
      data_hora = st.date_input("Data e Hora", value=datetime.now())
      descricao = st.text_input("Descrição")

      if st.button("Create Movimento"):
          with get_db_context() as db:
              create_movimento(db, {
                  "id_caixa": id_caixa,
                  "tipo_movimento": tipo_movimento,
                  "valor": float(valor.replace(",", ".")),
                  "data_hora": data_hora,
                  "descricao": descricao
              })
          st.success("Movimento criado com sucesso!")

  elif crud_operation == "List":
      st.subheader("Lista de Movimentos")
      with get_db_context() as db:
          movimentos = get_movimentos(db)
          if movimentos:
              movimento_data = [{"ID Caixa": m.id_caixa, "Tipo": m.tipo_movimento, "Valor": m.valor} for m in movimentos]
              st.write(movimento_data)
          else:
              st.write("Nenhum movimento encontrado.")

if __name__ == "__main__":
  main()