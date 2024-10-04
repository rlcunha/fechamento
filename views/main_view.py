pip import streamlit as st
from sqlalchemy.orm import Session
from database.session import get_db
from controllers.caixa_controller import create_caixa, get_caixas

def main():
  st.sidebar.title("Menu")
  menu = st.sidebar.selectbox("Selecione a Entidade", ["Caixa", "Operadora_Credito", "Op_Credito", "Movimentos"])
  crud_operation = st.sidebar.selectbox("Selecione a Operação", ["Create", "Update", "Delete", "List"])

  if menu == "Caixa":
      if crud_operation == "Create":
          st.subheader("Create Caixa")
          caixa_aberto = st.text_input("Caixa Aberto")
          data = st.date_input("Data")
          saldo_inicial = st.text_input("Saldo Inicial", "0,00")
          valor_cartao_credito = st.text_input("Valor Cartão de Crédito", "0,00")
          valor_cartao_debito = st.text_input("Valor Cartão de Débito", "0,00")
          valor_ifood = st.text_input("Valor de Ifood", "0,00")
          valor_dinheiro = st.text_input("Valor em Dinheiro", "0,00")
          valor_fiado = st.text_input("Valor Fiado", "0,00")
          saidas_caixa = st.text_input("Saídas de Caixa", "0,00")
          valor_acrescimo = st.text_input("Valor de Acréscimo", "0,00")

          if st.button("Create Caixa"):
              with get_db() as db:
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
          with get_db() as db:
              caixas = get_caixas(db)
          st.write(caixas)

if __name__ == "__main__":
  main()